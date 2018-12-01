from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
# from rasa_core.tracker_store import RedisTrackerStore
from rasa_core.tracker_store import MongoTrackerStore



with open("config_cloud_services.yaml", "r", encoding = "utf8") as f:
	config_cloud = yaml.load(f)


SLACK_KEY = config_cloud["slack"]
HOST_DB = config_cloud["tracker_store"]["url"]
USERNAME = config_cloud["tracker_store"]["username"]
PASSWORD = config_cloud["tracker_store"]["password"]
ACTIONSERVER = config_cloud["action_endpoint"]["url"]





nlu_interpreter = RasaNLUInterpreter(model_directory = './models/nlu/default/versicherung_nlu')



action_endpoint = EndpointConfig(url=ACTIONSERVER)



domain          = Domain.load('domain.yml')

db 			= MongoTrackerStore(domain,
								host=HOST_DB, 
								db='rasa', username = USERNAME, 
								password = PASSWORD, collection = 'conversations', 
								event_broker = None
							)

agent = Agent.load( path = './models/dialogue', interpreter = nlu_interpreter, 
                    # generator = None ,
                    tracker_store = db,  
                    action_endpoint = action_endpoint
                )

input_channel = SlackInput(SLACK_KEY) #bot user authentication token

print("bot started")
agent.handle_channels([input_channel], 8080, serve_forever=True)
print("bot stopped")
