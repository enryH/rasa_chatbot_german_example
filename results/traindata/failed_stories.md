## Generated Story 6244745167850923221
* greet
    - utter_greet
* other
    - utter_chitchat   <!-- predicted: utter_ask -->
* confirm
    - utter_ask
* inform{"object": "fahrrad", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "48932"}
    - slot{"policy_no": "48932"}
    - slot{"policy_no": "48932"}
    - utter_ask_birthday
* inform{"birthdate": "13.3.1988"}
    - slot{"birthdate": "13.3.1988"}
    - slot{"birthdate": "13.3.1988"}
    - action_check_membership
    - slot{"policy_no": "48932"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "vor meiner haust\u00fcr"}
    - slot{"location": "vor meiner haust\u00fcr"}
    - slot{"location": "vor meiner haust\u00fcr"}
    - action_finalise
* confirm
    - utter_goodbye
    - action_restart


## Generated Story -2076655036165244257
* greet
    - utter_greet
* inform{"case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - utter_ask_object
* inform{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* greet{"policy_no": "12345"}
    - slot{"policy_no": "12345"}
    - slot{"policy_no": "12345"}
    - utter_ask_birthday
* inform{"birthdate": "1 . januar 2020"}
    - slot{"birthdate": "1 . januar 2020"}
    - slot{"birthdate": "1 . januar 2020"}
    - action_check_membership
    - slot{"policy_no": null}
* inform
    - action_check_membership
    - slot{"policy_no": null}
* inform{"policy_no": "23341"}
    - slot{"policy_no": "23341"}
    - slot{"policy_no": "23341"}
    - action_check_membership
    - slot{"policy_no": "23341"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* confirm
    - utter_goodbye
    - action_listen   <!-- predicted: action_restart -->


## Generated Story -2593694690125172727
* greet
    - utter_greet
* inform{"case": "diebstahl"}
    - slot{"case": "diebstahl"}
    - slot{"case": "diebstahl"}
    - utter_ask_object
* inform{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "45398"}
    - slot{"policy_no": "45398"}
    - slot{"policy_no": "45398"}
    - utter_ask_birthday
* inform{"birthdate": "4.3.1988"}
    - slot{"birthdate": "4.3.1988"}
    - slot{"birthdate": "4.3.1988"}
    - action_check_membership
    - slot{"policy_no": "45398"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* confirm
    - utter_goodbye
    - action_listen   <!-- predicted: action_restart -->


## Generated Story 7390413998049535240
* greet
    - utter_greet
* inform{"case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - utter_ask_object
* inform{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* deny
    - utter_connect
    - utter_goodbye
    - action_listen   <!-- predicted: action_restart -->
* goodbye
    - action_restart


## Generated Story 2946630211805984047
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
* inform{"policy_no": "05512245"}
    - slot{"policy_no": "05512245"}
    - slot{"policy_no": "05512245"}
    - utter_ask_birthday
* inform
    - action_default_fallback   <!-- predicted: action_check_membership -->
* inform{"birthdate": "3.5.1999"}
    - slot{"birthdate": "3.5.1999"}
    - slot{"birthdate": "3.5.1999"}
    - action_check_membership
    - slot{"policy_no": "5512245"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "bei mir vor der haust\u00fcr"}
    - slot{"location": "bei mir vor der haust\u00fcr"}
    - slot{"location": "bei mir vor der haust\u00fcr"}
    - action_finalise
* question{"policy_detail": "selbstbeteiligung"}
    - slot{"policy_detail": "selbstbeteiligung"}
    - slot{"policy_detail": "selbstbeteiligung"}
    - utter_selbstbeteiligung
* confirm
    - utter_goodbye
* goodbye
    - action_restart


