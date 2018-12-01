## Generated Story 8893157412145707837
* greet
    - utter_greet
* other
    - action_default_fallback
    - rewind
* inform{"case": "diebstahlm", "object": "velos"}
    - slot{"case": "diebstahlm"}
    - slot{"object": "velos"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "45698"}
    - slot{"policy_no": "45698"}
    - utter_ask_birthday
* inform{"birthdate": "14.4.1995"}
    - slot{"birthdate": "14.4.1995"}
    - action_check_membership
    - slot{"policy_no": "45698"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "Hauptbahnhof, Z\u00fcrich"}
    - slot{"location": "Hauptbahnhof, Z\u00fcrich"}
    - action_finalise
* question{"policy_detail": "Selbstbeteiligung"}
    - slot{"policy_detail": "Selbstbeteiligung"}
    - utter_selbstbeteiligung
* confirm
    - utter_goodbye
    - action_restart

