from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

# import pandas as pd  #if dummy DataFrame is needed

class ActionMembershipCheck(Action):
	"""
	Perform a Membership check using a given policy number and birthdate.

	ToDo:
	- Create artifical database consisting of birthdate and policy_no entries
	- parse given birthdate?
	- check use of new Form Actions, see https://rasa.com/docs/core/slotfilling/
	"""
	# def __init__(self):
	#     self.df = pd.DataFrame(
	#         { "policy_no": [12345, 12456, 93845, 45544, 34899],
	#           "birthdate": ["12-34-1988", "1.2.1976", "9.12.1986", "12.6.1988", "03-3-2000"]
	#          }
	#      )

	def name(self):
		return 'action_check_membership'

	def run(self, dispatcher, tracker, domain):
		try:
			id = tracker.get_slot('policy_no')
			id = int(id)
		except Exception:
			dispatcher.utter_message("Entschuldige, aber ich konnte leider deine Mitgliedsnummer "
									  "nicht einlesen. Hast du dich vertippt? "
									  "Sie besteht aus 5 Zahlen.")
			return [SlotSet('policy_no', None)]	
		try:
			birthdate = tracker.get_slot('birthdate')
		except Exception:
			dispatcher.utter_message("Kannst du mir bitte dein Geburtsdatum noch einmal nennen?")
			return
		# do something with this number
		if id < 20000 or id > 100000:
			dispatcher.utter_message("Ich konnte leider keine Mitgliedschaft unter dieser Nummer finden. Kannst du sie vielleicht noch einmal überprüfen?")
			return [SlotSet('policy_no', None)]	
		response = "Ich konnte ihre Police finden unter der ID {} finden".format(id)
		dispatcher.utter_message(response)
		return [ SlotSet('policy_no', str(id)), 
		         SlotSet('policy', 'Hausratsversicherung')
			   ]


class ActionSummarize(Action):
	"""
	Summarizes what bot has understood at the end of a conversation.
	"""

	def name(self):
		return 'action_finalise'
	
	def check_none(self, slot):
		if slot is None:
			slot = "???"
		return slot

	def run(self, dispatcher, tracker, domain):
		_id =  self.check_none(tracker.get_slot('policy_no'))
		_birthdate = self.check_none(tracker.get_slot('birthdate'))
		_location  = self.check_none(tracker.get_slot('location'))
	
		_case   = self.check_none(tracker.get_slot('case'))
		
		_object = self.check_none(tracker.get_slot('object'))
		
		print(_case)
		print(type(_case))
		print(_object)
		print(type(_object))

		msg = ( "Ich fasse zusammen: Es geht um einen {}. Es betrifft ihr {}. Es ist {} passiert. " 
				"Ihre Versicherungsnummer lautet {} und sie wurdem am {} geboren.\n"
				"Wir werden ihr Anliegen bearbeiten und uns dann per E-Mail oder Post bei Ihnen melden.\n\n"  
				"War das alles?").format(_case.capitalize(), _object.capitalize(), _location, _id, _birthdate)
		dispatcher.utter_message(msg)
		return 

# class ActionWeather(Action):
# 	def name(self):
# 		return 'action_weather'
		
# 	def run(self, dispatcher, tracker, domain):
# 		from apixu.client import ApixuClient
# 		api_key = '2d876df34f334252ad093411182009' #your apixu key from https://www.apixu.com/my/
# 		client = ApixuClient(api_key)
		
# 		loc = tracker.get_slot('location')
# 		current = client.getCurrentWeather(q=loc)
		
# 		country = current['location']['country']
# 		city = current['location']['name']
# 		condition = current['current']['condition']['text']
# 		temperature_c = current['current']['temp_c']
# 		humidity = current['current']['humidity']
# 		wind_mph = current['current']['wind_mph']

# 		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
# 		dispatcher.utter_message(response)
# 		return [SlotSet('location',loc)]


