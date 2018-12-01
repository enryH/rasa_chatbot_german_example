 
## story 1542965223
* greet: Hey
  - utter_greet
* inform: Mein [Fahrrad](object:fahrrad) wurde [geklaut](case:Diebstahl)
  - slot{"object": "fahrrad"}
  - slot{"case":"Diebstahl"}
  - utter_proceed
* confirm: gerne gemeinsam
  - utter_ask_no
* inform: [45938](policy_no:45938)
  - slot{"policy_no": "45938"}
  - utter_ask_birthday
* greet: [3.4.1967](birthdate:3.4.1967)
  - slot{"birthdate": "3.4.1967"}
  - action_check_membership
  - slot{"policy_no": "45938"}
  - slot{"policy": "Hausratsversicherung"}
  - utter_ask_location
* inform: In der [Wiesenstr. 10A, 8952 Schlieren](location:Wiesenstr. 10A, 8952 Schlieren) <!-- breaks code: not recognized by NLU-->
  - action_finalise
* deny: danke, das wärs!
  - utter_goodbye
  - action_restart


## story 1394872  
* greet: Hey
  - utter_greet
* inform: Ich möchte den [Diebstahl](case:diebstahl) meines [Fahrrads](object:Fahrrad) melden
  - slot{"case": "diebstahl"}
  - slot{"object": "Fahrrad"}
  - utter_proceed
* confirm: los geht es
  - utter_ask_no
* inform: [48298](policy_no:48298)
  - slot{"policy_no": "48298"}
  - utter_ask_birthday
* greet: [4.4.1977](birthdate:4.4.1977)
  - slot{"birthdate": "4.4.1977"}
  - action_check_membership
  - utter_ask_location
* inform: Das war auf der [Langstrasse in Zürich](location:Langstrasse in Zürich) <!-- breaks code: not recognized by NLU-->
  - action_finalise
* question: Wie viel muss ich wohl [selber zahlen](policy_detail:Selbstbeteiligung)?
  - utter_selbstbeteiligung
* confirm: Vielen Dank. Dann ist dann alles. Bis dann
  - utter_goodbye
  - action_restart

