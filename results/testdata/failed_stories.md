## story 1541602345
* greet
    - utter_greet
* inform{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - utter_ask
* inform{"case": "diebstahl"}
    - slot{"case": "diebstahl"}
    - slot{"case": "diebstahl"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "43450"}
    - slot{"policy_no": "43450"}
    - slot{"policy_no": "43450"}
    - utter_ask_birthday   <!-- predicted: action_listen -->
* inform{"birthdate": "3.1.1987"}
    - slot{"birthdate": "3.1.1987"}
    - slot{"birthdate": "3.1.1987"}
    - action_check_membership
    - slot{"policy_no": "43450"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* deny
    - utter_goodbye
    - action_restart


## story 1542965223
* greet
    - utter_greet
* inform{"object": "Fahrrad"}
    - slot{"object": "Fahrrad"}
    - slot{"object": "Fahrrad"}
    - utter_ask
* inform{"case": "diebstahl"}
    - slot{"case": "diebstahl"}
    - slot{"case": "diebstahl"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "44444"}
    - slot{"policy_no": "44444"}
    - slot{"policy_no": "44444"}
* confirm
* greet
    - action_listen   <!-- predicted: action_default_fallback -->
* inform{"policy_no": "49898"}
    - slot{"policy_no": "49898"}
    - slot{"policy_no": "49898"}
    - action_check_membership   <!-- predicted: action_listen -->
    - slot{"policy_no": "49898"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location   <!-- predicted: action_listen -->
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* deny
    - utter_goodbye
    - action_restart


## story handle-missing-location
* greet
    - utter_greet
* inform{"object": "fahrrad", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* deny
    - utter_ask_again
* inform{"policy_no": "55534"}
    - slot{"policy_no": "55534"}
    - slot{"policy_no": "55534"}
    - utter_ask_birthday
* inform{"birthdate": "01.01.1970"}
    - slot{"birthdate": "01.01.1970"}
    - slot{"birthdate": "01.01.1970"}
    - action_check_membership
    - slot{"policy_no": "55534"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform
    - utter_default   <!-- predicted: action_finalise -->
* inform
    - utter_skip   <!-- predicted: action_finalise -->
    - action_finalise   <!-- predicted: action_listen -->
* utter_ask
    - utter_selbstbeteiligung   <!-- predicted: utter_goodbye -->
* goodbye
    - utter_goodbye   <!-- predicted: action_restart -->
    - action_restart   <!-- predicted: action_listen -->


