## greet
* greet
    - utter_greet
> checkpoint_greet

## goodbye
> checkpoint_goodbye
* goodbye
   - utter_goodbye
   - action_restart

## body_000
> checkpoint_greet
* inform{"case": "Diebstahl", "object": "fahrrad"}
    - slot{"case": "Diebstahl", "object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no" : "45896"}
    - slot{"policy_no" : "69852"}
    - utter_ask_birthday
* inform{"birthdate": "10.08.1980"}
    - slot{"birthdate": "10.08.1980"}
    - action_check_membership
    - slot{"policy_no" : "45896"}
    - slot{"policy" : "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "home"}
    - slot{"location": "home"}
    - action_finalise
> checkpoint_goodbye

## Generated Story 2334022597340090022
* other
    - utter_greet
* inform{"case": "diebstahl", "object": "Fahrrad"}
    - slot{"case": "diebstahl"}
    - slot{"object": "Fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "45898"}
    - slot{"policy_no": "45898"}
    - utter_ask_birthday
* inform{"birthdate": "14.4.1970"}
    - slot{"birthdate": "14.4.1970"}
    - action_check_membership
    - slot{"policy_no": "45898"}
    - slot{"policy" : "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* confirm
    - utter_goodbye
    - action_restart


## story_001-01
> checkpoint_greet
* inform
    - utter_ask
* inform{"case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - utter_ask_object
* inform{"object": "Fahrrad"}
    - slot{"object": "Fahrrad"}
    - utter_proceed
* deny
    - utter_connect
    - utter_goodbye
    - action_restart

## Generated Story -4054165050561420963
* greet
    - utter_greet
* inform
    - utter_ask
* inform{"object": "fahrrad", "location": "direkt vor der haust\u00fcr", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"location": "direkt vor der haust\u00fcr"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* deny
    - utter_connect
    - utter_goodbye
* goodbye
     - action_restart   

## Generated Story 7390413998049535240
* greet
    - utter_greet
* inform{"case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - utter_ask_object
* inform{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* deny
    - utter_connect
    - utter_goodbye
* goodbye
    - action_restart

## Generated Story -1161949728620048101
* greet
    - utter_greet
* inform{"object": "fahrrad", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* deny
    - utter_connect
    - utter_goodbye


## story_001-02
> checkpoint_greet
* inform
    - utter_ask
* inform{"case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - utter_ask_object
* inform{"object": "Fahrrad"}
    - slot{"object": "Fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no" : "13424"}
    - slot{"policy_no" : "13424"}
    - utter_ask_birthday
* inform{"birthdate" : "10.10.1906"}
    - slot{"birthdate" : "10.10.1906"}
    - action_check_membership
    - slot{"policy" : "Hausratsversicherung"}
    - slot{"policy_no" : "13424"}
    - utter_ask_location
* inform{"location":"zuhause"}
   - slot{"location":"zuhause"}
   - action_finalise
> checkpoint_goodbye

## story_002
> checkpoint_greet
* inform{"location": "zuhause", "case": "Diebstahl"}
   - slot{"location":"zuhause", "case": "Diebstahl"}
   - utter_proceed
* confirm
   - utter_ask_no
* inform{"policy_no":"44556"}
   - slot{"policy_no":"44556"}
   - utter_ask_birthday
* inform{"birthdate":"2.1.1955"}
   - slot{"birthdate":"2.1.1955"}
   - action_check_membership
   - slot{"policy_no": null}
* inform{"policy_no": "45321", "birthdate": "10.10.1960"}
    - slot{"policy_no": "45321", "birthdate": "10.10.1960"}
    - action_check_membership
    - slot{"policy" : "Hausratsversicherung"}
    - slot{"policy_no": "45321"}
    - utter_ask_location
* inform{"location":"zuhause"}
   - slot{"location":"zuhause"}
   - action_finalise
> checkpoint_goodbye

## Generated Story -3408620161030825341
* greet
    - utter_greet
* inform{"object": "fahrrad", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "13232"}
    - slot{"policy_no": "13232"}
    - utter_ask_birthday
* inform{"birthdate": "3.4.1904"}
    - slot{"birthdate": "3.4.1904"}
    - action_check_membership
    - slot{"policy_no": null}
* inform{"policy_no": "30987"}
    - slot{"policy_no": "30987"}
    - action_check_membership
    - slot{"policy_no": "30987"}
    - slot{"policy" : "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "direkt bei mir zuhause"}
    - slot{"location": "direkt bei mir zuhause"}
    - action_finalise
* confirm
    - utter_goodbye
    - action_restart

## story_003
> checkpoint_greet
* inform{"case": "Diebstahl", "object": "fahrrad", "location": "zuhause"}
   - slot{"case": "Diebstahl", "object": "fahrrad", "location": "zuhause"}
   - utter_proceed
* confirm 
    - utter_ask_no
* deny 
   - utter_ask_again
* inform{"policy_no": "34221"}
   - slot{"policy_no": "34221"}
   - utter_ask_birthday
* inform{"birthdate":"2.1.1950"}
   - slot{"birthdate":"2.1.1950"}
   - action_check_membership
   - slot{"policy_no": "34221"}
   - slot{"policy" : "Hausratsversicherung"}
   - utter_ask_location
* inform{"location" : "zuhause"}
    - slot{"location" : "zuhause"}
   - action_finalise
> checkpoint_goodbye

## story_004
> checkpoint_greet
* other
   - utter_ask
* inform{"case": "Diebstahl"}
   - slot{"case": "Diebstahl"}
   - utter_ask_object
* inform{"object": "Fahrrad"}
    - slot{"object": "Fahrrad"}
    - utter_proceed
* confirm
   - utter_ask_no
* inform{"policy_no":"13456"}
   - slot{"policy_no":"13456"}
   - utter_ask_birthday
* inform{"birthdate":"13.3.1983"}
    - slot{"birthdate":"13.3.1983"}
    - action_check_membership
    - slot{"policy_no":"13456"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location" : "zuhause"}
   - action_finalise
> checkpoint_goodbye


## Generated Story 6244745167850923221
* greet
    - utter_greet
* other
    - utter_chitchat
* confirm
    - utter_ask
* inform{"object": "fahrrad", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "48932"}
    - slot{"policy_no": "48932"}
    - utter_ask_birthday
* inform{"birthdate": "13.3.1988"}
    - slot{"birthdate": "13.3.1988"}
    - action_check_membership
    - slot{"policy_no": "48932"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "vor meiner haust\u00fcr"}
    - slot{"location": "vor meiner haust\u00fcr"}
    - action_finalise
* confirm
    - utter_goodbye
    - action_restart

## story_005
> checkpoint_greet
* inform{"case": "Diebstahl", "object": "fahrrad"}
   - slot{"case": "Diebstahl", "object": "fahrrad"}
   - utter_proceed
* confirm 
    - utter_ask_no
* deny 
   - utter_ask_again
* deny
   - utter_connect
   - utter_goodbye
   - action_restart

## story_006
* greet
    - utter_greet
* inform{"object":"Fahrrad", "location": "vor der Haustür"}
    - slot{"object":"Fahrrad"}
    - utter_ask
* inform{"case":"Diebstahl"}
    - slot{"case":"Diebstahl"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "13452"}
    - slot{"policy_no": "13452"}
* inform{"birthdate": "13.3.1988"}
    - slot{"birthdate": "13.3.1988"}
    - action_check_membership
    - slot{"policy_no": "13452"}
    - slot{"policy": "Hausratsversicherung"}
    - action_finalise
* confirm
    - utter_goodbye
* goodbye
    - action_restart

## Generated Story -2076655036165244257
* greet
    - utter_greet
* inform{"case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - utter_ask_object
* inform{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* greet{"policy_no": "12345"}
    - slot{"policy_no": "12345"}
    - utter_ask_birthday
* inform{"birthdate": "1 . januar 2020"}
    - slot{"birthdate": "1 . januar 2020"}
    - action_check_membership
    - slot{"policy_no": null}
* inform
    - action_check_membership
    - slot{"policy_no": null}
* inform{"policy_no": "23341"}
    - slot{"policy_no": "23341"}
    - action_check_membership
    - slot{"policy_no": "23341"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - action_finalise
* confirm
    - utter_goodbye

## Generated Story -2483060758026041198
* greet
    - utter_greet
* mood_unhappy
    - utter_apology
    - utter_connect
    - utter_goodbye
* goodbye
    - action_restart

## Generated Story -5331721088502025691
* greet
    - utter_greet
* inform
    - utter_ask
* inform{"object": "fahrrad", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* greet
    - utter_ask_again
* inform{"policy_no": "12345"}
    - slot{"policy_no": "12345"}
    - utter_ask_birthday
* inform{"birthdate": "21 . juli 1994"}
    - slot{"birthdate": "21 . juli 1994"}
    - action_check_membership
    - slot{"policy_no": null}
* deny
    - utter_apology
    - utter_connect
    - utter_goodbye
    - action_restart


## Generated Story 2946630211805984047
* greet
    - utter_greet
* inform{"object": "fahrrad", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "05512245"}
    - slot{"policy_no": "05512245"}
    - utter_ask_birthday
* inform
    - action_default_fallback
* inform{"birthdate": "3.5.1999"}
    - slot{"birthdate": "3.5.1999"}
    - action_check_membership
    - slot{"policy_no": "5512245"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "bei mir vor der haust\u00fcr"}
    - slot{"location": "bei mir vor der haust\u00fcr"}
    - action_finalise
* question{"policy_detail": "selbstbeteiligung"}
    - slot{"policy_detail": "selbstbeteiligung"}
    - utter_selbstbeteiligung
* confirm
    - utter_goodbye
* goodbye
    - action_restart

## Generated Story -6996456960021452071
* greet
    - utter_greet
* inform{"object": "fahrrad", "case": "diebstahl"}
    - slot{"case": "diebstahl"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "000000"}
    - slot{"policy_no": "000000"}
    - utter_ask_birthday
* inform
    - action_check_membership
    - slot{"policy_no": null}
* inform{"policy_no": "34987"}
    - slot{"policy_no": "34987"}
    - action_check_membership
    - slot{"policy_no": "34987"}
    - slot{"policy": "Hausratsversicherung"}
    - slot{"policy_detail": "500"}
    - utter_ask_location
* inform
    - action_default_fallback
* inform{"location": "direkt bei mir zuhause"}
    - slot{"location": "direkt bei mir zuhause"}
    - action_finalise
* question{"policy_detail": "selbstbeteiligung"}
    - slot{"policy_detail": "selbstbeteiligung"}
    - utter_selbstbeteiligung
* confirm
    - utter_goodbye
* goodbye
    - action_restart


## Generated Story 821031437007498937
* greet
    - utter_greet
* inform{"case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - utter_ask_object
* inform{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "45739"}
    - slot{"policy_no": "45739"}
    - utter_ask_birthday
* inform
    - action_check_membership
    - slot{"policy_no": "45739"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform
    - action_default_fallback
* inform
    - action_default_fallback
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* confirm
    - utter_goodbye
    - action_restart

## Generated Story -2593694690125172727
* greet
    - utter_greet
* inform{"case": "diebstahl"}
    - slot{"case": "diebstahl"}
    - utter_ask_object
* inform{"object": "fahrrad"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "45398"}
    - slot{"policy_no": "45398"}
    - utter_ask_birthday
* inform{"birthdate": "4.3.1988"}
    - slot{"birthdate": "4.3.1988"}
    - action_check_membership
    - slot{"policy_no": "45398"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* confirm
    - utter_goodbye
    - action_restart

## Generated Story 4463818590526241149
* greet
    - utter_greet
* inform{"object": "farrad", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "farrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* other
    - utter_ask_again
* inform{"policy_no": "12345"}
    - slot{"policy_no": "12345"}
    - utter_ask_birthday
* inform{"birthdate": "10/18/2000"}
    - slot{"birthdate": "10/18/2000"}
    - action_check_membership
    - slot{"policy_no": null}
* inform{"policy_no": "23453"}
    - slot{"policy_no": "23453"}
    - action_check_membership
    - slot{"policy_no": "23453"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* goodbye
    - utter_goodbye

## Generated Story 798092631695803599
* greet
    - utter_greet
* inform{"object": "fahrrad", "case": "Diebstahl"}
    - slot{"case": "Diebstahl"}
    - slot{"object": "fahrrad"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "12345"}
    - slot{"policy_no": "12345"}
    - utter_ask_birthday
* inform{"birthdate": "4.5.45"}
    - slot{"birthdate": "4.5.45"}
    - action_check_membership
    - slot{"policy_no": null}
* inform{"policy_no": "45674"}
    - slot{"policy_no": "45674"}
    - action_check_membership
    - slot{"policy_no": "45674"}
    - slot{"policy": "Hausratsversicherung"}
    - slot{"policy_detail": "500"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story 1186712233144775508
* greet
    - utter_greet
* other
    - action_default_fallback
    - rewind
* inform{"case": "diebstahlm", "object": "velos"}
    - slot{"case": "diebstahl"}
    - slot{"object": "velo"}
    - utter_proceed
* confirm
    - utter_ask_no
* inform{"policy_no": "48379"}
    - slot{"policy_no": "48379"}
    - utter_ask_birthday
* inform{"birthdate": "3.4.1988"}
    - slot{"birthdate": "3.4.1988"}
    - action_check_membership
    - slot{"policy_no": "48379"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* question{"policy_detail": "Selbstbeteiligung"}
    - slot{"policy_detail": "Selbstbeteiligung"}
    - utter_selbstbeteiligung
* confirm
    - utter_goodbye
    - action_restart

## Generated Story 5539305647933277241
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
* inform{"policy_no": "49839"}
    - slot{"policy_no": "49839"}
    - utter_ask_birthday
* inform{"birthdate": "6.9.1999"}
    - slot{"birthdate": "6.9.1999"}
    - action_check_membership
    - slot{"policy_no": "49839"}
    - slot{"policy": "Hausratsversicherung"}
    - utter_ask_location
* inform{"location": "zuhause"}
    - slot{"location": "zuhause"}
    - action_finalise
* question{"policy_detail": "Selbstbeteiligung"}
    - slot{"policy_detail": "Selbstbeteiligung"}
    - utter_selbstbeteiligung
* goodbye
    - utter_goodbye
    - action_restart

