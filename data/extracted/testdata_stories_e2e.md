## story 1542965223
* greet: Hoi
  - utter_greet
* inform: Gestern ist mein [Fahrrad](object:fahrrad) [geklaut](case:Diebstahl) worde
!!!
  - slot{"case": "Diebstahl"}
  - slot{"object": "fahrrad"}
  - utter_proceed
* confirm: ok
  - utter_ask_no
* deny: weiss ich nicht
  - utter_ask_again
* wait: moment
  - utter_affirm
* inform: also: [55534](policy_no:55534)
  - slot{"policy_no": "55534"}
  - utter_ask_birthday
* inform: [01.01.1970](birthdate:01.01.1970)
  - slot{"birthdate": "01.01.1970"}
  - action_check_membership
  - slot{"policy_no": "55534"}
  - slot{"policy": "Hausratsversicherung"}
  - utter_ask_location
* inform: [zuhause](location:zuhause)
  - slot{"location": "zuhause"}
  - action_finalise
* deny: ja danke
  - utter_goodbye
  - action_restart
  
## story 1542965224
* greet: Hey
  - utter_greet
* inform: mein schönes rotes [Fahrrad](object:fahrrad) wurde mir heute morgen [gestohlen](case:Diebstahl)!
  - slot{"case": "Diebstahl"}
  - slot{"object": "fahrrad"}
  - utter_proceed
* confirm: Das können wir gerne gemeinsam tun.
  - utter_ask_no
* inform: [68308](policy_no:68308)
  - slot{"policy_no": "68308"}
  - utter_ask_birthday
* inform: [3.5.1989](birthdate:3.5.1989)
  - slot{"birthdate": "3.5.1989"}
  - action_check_membership
  - slot{"policy_no": "68308"}
  - slot{"policy": "Hausratsversicherung"}
  - utter_ask_location
* inform: Bei mir [zuhause](location:zuhause)
  - slot{"location": "zuhause"}
  - action_finalise
* deny: vielen dank!
  - utter_goodbye
  - action_restart


## story 1542965223
* greet: Hey
  - utter_greet
* inform: Mein [Fahrrad](object:fahrrad) wurde [gestohlen](case:Diebstahl)
  - slot{"case": "Diebstahl"}
  - slot{"object": "fahrrad"}
  - utter_proceed
* confirm: gerne zusammen
  - utter_ask_no
* inform: [54548](policy_no:54548)
  - slot{"policy_no": "54548"}
  - utter_ask_birthday
* inform: [3.5.1877](birthdate:3.5.1877)
  - slot{"birthdate": "3.5.1877"}
  - action_check_membership
  - utter_ask_location
* inform: [zuhause](location:zuhause)
  - slot{"location": "zuhause"}
  - action_finalise
* question: Wie hoch wird meine [Selbstbeteiligung](policy_detail:selbstbeteiligung) ungefähr sein?
  - utter_selbstbeteiligung
* goodbye: vielen dank. Das war dann alles meinerseits. Ich warte dann auf ihre Rückmeldung. Tschüss.
  - utter_goodbye
  - action_restart

## story 1542965223
* greet: Hey
  - utter_greet
* inform: Mein [Fahrrad](object:fahrrad) wurde mir [geklaut](case:Diebstahl).
  - slot{"case": "Diebstahl"}
  - slot{"object": "fahrrad"}
  - utter_proceed
* confirm: gerne gemeinsam
  - utter_ask_no
* inform: [54928](policy_no:54928)
  - slot{"policy_no": "54928"}
  - utter_ask_birthday
* inform: [4.3.1988](birthdate:4.3.1988)
  - slot{"birthdate": "4.3.1988"}
  - action_check_membership
  - slot{"policy_no": "54928"}
  - slot{"policy": "Hausratsversicherung"}
  - utter_ask_location
* inform: [zuhause](location:zuhause)
  - slot{"location": "zuhause"}
  - action_finalise
* inform: danke, das wars!
  - utter_goodbye
  - action_restart


## story 1542965223
* greet: test
  - utter_greet
* mood_unhappy: Ich weiss nicht was das soll. Bin ich ein Versuchskaninchen?
  - utter_apology
  - utter_connect
  - utter_goodbye
  - action_restart


## story 1542965232 
* greet: Hey
  - utter_greet
* inform: Ich möchte einen [Fahrraddiebstahl](case:Diebstahl) melden
  - slot{"case": "Diebstahl"}
  - utter_ask_object
* inform: ein [Fahrrad](object:fahrrad)
  - slot{"object": "fahrrad"}
  - utter_proceed
* deny: lieber ein Mensch
  - utter_connect
  - utter_goodbye
  - action_restart

  
## story 1542965223
* greet: Hey
  - utter_greet
* inform: Mein [Fahrrad](object:fahrrad) wurde mir [gestohlen](case:Diebstahl).
  - slot{"case": "Diebstahl"}
  - slot{"object": "fahrrad"}
  - utter_proceed
* confirm: los gehts
  - utter_ask_no
* inform: [45839](policy_no:45839)
  - slot{"policy_no": "45839"}
  - utter_ask_birthday
* inform: [9.8.1999](birthdate:9.8.1999)
  - slot{"birthdate": "9.8.1999"}
  - action_check_membership
  - utter_ask_location
* inform: [zuhause](location:zuhause)
  - slot{"location": "zuhause"}
  - action_finalise
* deny: danke
  - utter_goodbye
  - action_restart

## story 1542965223
* greet: Hey
  - utter_greet
* inform: Mein [Fahrrad](object:fahrrad) wurde mir [gestohlen](case:Diebstahl)
  - slot{"case": "Diebstahl"}
  - slot{"object": "fahrrad"}
  - utter_proceed
* confirm: auf geht es
  - utter_ask_no
* inform: [43029](policy_no:43029)
  - slot{"policy_no": "43029"}
  - utter_ask_birthday
* inform: [10.8.1988](birthdate:10.8.1988)
  - slot{"birthdate": "10.8.1988"}
  - action_check_membership
  - utter_ask_location
* inform: [zuhause](location:zuhause)
  - slot{"location": "zuhause"}
  - action_finalise
* deny: Nein, das war alles
  - utter_goodbye
  - action_restart

