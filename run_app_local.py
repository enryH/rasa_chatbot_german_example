from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.tracker_store import MongoTrackerStore

import yaml

with open("endpoints.yml", "r", encoding = "utf8") as f:
	config = yaml.load(f)

with open("config_cloud_services.yaml", "r", encoding = "utf8") as f:
	config_cloud = yaml.load(f)

SLACK_KEY = config_cloud["slack"]
HOST_DB = config["tracker_store"]["url"]
ACTIONSERVER = config["action_endpoint"]["url"]

_type = config["tracker_store"]["store_type"]
if _type == "mongod":
    from rasa_core.tracker_store import MongoTrackerStore
elif _type == "redis":
    from rasa_core.tracker_store import RedisTrackerStore
else:
    raise Exception("Unknown Database type: Please specify mongod or redis database in `endpoints.yml`.")



nlu_interpreter = RasaNLUInterpreter(model_directory = './models/nlu/default/versicherung_nlu')
action_endpoint = EndpointConfig(url=ACTIONSERVER)

domain          = Domain.load('domain.yml')

if _type == "mongod":
    db = MongoTrackerStore(domain,
						host=HOST_DB, 
						db='rasa', username = None, 
						password = None, collection = 'conversations', 
						event_broker = None
						)
elif _type == "redis":
    db = RedisTrackerStore(domain, host=HOST_DB,
                 port=6379, db=0, password=None, event_broker=None,
                 record_exp=None)

agent = Agent.load( path = './models/dialogue', interpreter = nlu_interpreter, 
                    # generator = None ,
                    tracker_store = db,  
                    action_endpoint = action_endpoint
                )

input_channel = SlackInput(SLACK_KEY) #bot user authentication token

print("bot started")
agent.handle_channels([input_channel], 8080, serve_forever=True)
print("bot stopped")
