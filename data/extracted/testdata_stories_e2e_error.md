## story 1542965223
* greet: Hoi
  - utter_greet
* inform: Gestern ist mein [Fahrrad](object) [geklaut](case) worde!!!
  - utter_proceed
* confirm: ok
  - utter_ask_no
* deny: weiss ich nicht
  - utter_ask_again
* inform: moment
  - utter_affirm
* inform: also [55534](policy_no)
  - utter_ask_birthday
* inform: [01.01.1970](birthdate)
    - action_check_membership
  - utter_ask_location
* inform: Ganz in der Nähe. Hier im Ghetto [Schlieren](location) <!-- "zuhause" funktioniert-->
  - action_finalise
* deny: ja danke
  - utter_goodbye
  - action_restart

