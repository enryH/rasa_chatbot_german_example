from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.tracker_store import RedisTrackerStore
from rasa_core.tracker_store import MongoTrackerStore

import yaml
from pprint import pprint

config = yaml.open(
              open("endpoints.yml", "r")
              )
pprint(config)


NLUMODELPATH = './models/nlu/default/versicherung_nlu'
COREMODEL    = './models/dialogue'
ACTIONSERVER = config.get('action_endpoint').get('url')
DBHOST       = 'mongodb://localhost:27017'
SLACKTOKEN   = 'xoxb-443057380438-441520048564-716FIJUsElz1Kx6PJocO3JkW'
PORT         = 5004

nlu_interpreter = RasaNLUInterpreter(model_directory= NLUMODELPATH)
action_endpoint = EndpointConfig(url= ACTIONSERVER)

domain          = Domain.load('domain.yml')

db 			    = MongoTrackerStore(domain,
								host= DBHOST, 
								db='rasa', collection = 'conversations', 
                                # username = None, 
								# password = None, 
								# event_broker = None
							)

agent = Agent.load( path = COREMODEL, interpreter = nlu_interpreter, 
                    # generator = None ,
                    tracker_store = db,  
                    action_endpoint = action_endpoint
                )

input_channel = SlackInput(SLACKTOKEN) #bot user authentication token

print("bot started on port {}".format(PORT))
agent.handle_channels([input_channel], PORT, serve_forever=True)
print("bot stopped")
