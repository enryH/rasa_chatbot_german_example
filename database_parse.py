from rasa_core.domain import Domain
from rasa_core.tracker_store import MongoTrackerStore
from utils_database import story_from_dialog
import time

from pprint import pprint
from rasa_nlu.training_data import load_data


FNAMESTORIES = "stories_slack_{}.md".format(round(time.time()))
FNAMENLU     = "nlu_slack_{}.md".format(round(time.time()))

# https://www.coursera.org/learn/introduction-mongodb
domain  = Domain.load('domain.yml')
db 		= MongoTrackerStore(domain,
						host='mongodb://Henry:CourseraCourse@clusterdialogs-shard-00-00-6gpzg.gcp.mongodb.net:27017,clusterdialogs-shard-00-01-6gpzg.gcp.mongodb.net:27017,clusterdialogs-shard-00-02-6gpzg.gcp.mongodb.net:27017/test?ssl=true&replicaSet=ClusterDialogs-shard-0&authSource=admin', 
						db='rasa', 
                        username = "Henry", 
                        password = "CourseraCourse", 
                        collection = 'conversations', 
						event_broker = None
					)

collection = db.db.client.rasa.conversations
pipeline = [
    {
        '$project': {"sender_id" :1 }
    }
]

list_sender_ids = [obj["sender_id"] for obj in list(collection.aggregate(pipeline))]

for sender_id in list_sender_ids:
    dialog = db.retrieve(sender_id).as_dialogue()
    md_story, md_nlu, logs, md_story_e2e = story_from_dialog(dialog, user = sender_id, do_print= True)

    RELPATH  = "data/extracted/"
    FNAMESTORIES = RELPATH + "stories_{}.md".format(sender_id)
    FNAMENLU     = RELPATH + "nlu_{}.md".format(sender_id)
    FNAMENLUJSON = RELPATH + "nlu_{}.json".format(sender_id)
    FNAMELOG     = RELPATH + "log_{}.txt".format(sender_id)
    FNAMEE2E     = RELPATH + "stories_e2e_{}.md".format(sender_id)

    # print("\n\nStories from Slack: saved to %s:"%FNAMESTORIES)
    # print(md_story)

    with open(FNAMESTORIES, "w", encoding = "utf8") as f:
        f.write(md_story)

    # print("\n\nNLU from Slack: saved to %s:"%FNAMENLU)
    # print(md_nlu)

    with open(FNAMENLU, "w", encoding = "utf8") as f:
        f.write(md_nlu)
    
    with open(FNAMENLUJSON, "w") as f:
        _json = load_data(FNAMENLU, language="de").as_json()
        print("\nNLU from Slack as JSON: saved to {}".format(FNAMENLUJSON))
        pprint(_json)
        f.write(_json) 

    print("\n\nLogs from Slack: saved to %s:"%FNAMELOG)
    print(logs)

    with open(FNAMELOG, "w", encoding = "utf8") as f:
        f.write(logs)

    print(("\n\nStories for evaluation in end-to-end (e2e) format\n"
          "combining RASA NLU and CORE, saved to {}").format(FNAMEE2E))
    print(md_story_e2e)

    with open(FNAMEE2E, "w", encoding = "utf8") as f:
        f.write(md_story_e2e)

"""
to add:
    restore tracker object with help of conversation.
"""
