from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import rasa_core

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

def load_bot(nlu_model, 
             core_model = './models/dialogue',
             url_actionserver = "http://localhost:5055/webhook",
             serve_forever=True, 
             db = None):
	nlu_interpreter = RasaNLUInterpreter(nlu_model)
	action_endpoint = EndpointConfig(url = url_actionserver)
	agent = Agent.load( path = core_model, 
                        interpreter = nlu_interpreter, 
                        generator = None ,
                        tracker_store = db,  
                        action_endpoint = action_endpoint
                    )
	# rasa_core.serve_application(agent , channel='cmdline')		
	return agent

if __name__ == '__main__':
    from rasa_core.domain import Domain
    domain = Domain.load('domain.yml')
    
    # Select either Redis or MongoDB as Trackerstore

    from rasa_core.tracker_store import RedisTrackerStore
    db  = RedisTrackerStore( domain, 
                            host='127.0.0.1',  # 127.0.0.1 = localhost
                            port=6379, 
                            db=0, 
                            password=None, 
                            event_broker=None
                        )

    from rasa_core.tracker_store import MongoTrackerStore
    db	= MongoTrackerStore(domain,
                            host='mongodb://localhost:27017', 
                            db='rasa', 
                            collection = 'conversations', 
                            username = None, 
                            password = None, 
                            event_broker = None
                            )

    agent = load_bot(nlu_model = './models/nlu/default/versicherung_nlu',
                     core_model = './models/dialogue',
                     db = db )

    from rasa_core import run
    run.serve_application(agent , channel='cmdline')
