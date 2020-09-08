## happy path 1 (C:\Users\Infogen\AppData\Local\Temp\tmpcnr5z732\95ba545448a34514a716169676349603_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->


## happy path 2 (C:\Users\Infogen\AppData\Local\Temp\tmpcnr5z732\95ba545448a34514a716169676349603_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (C:\Users\Infogen\AppData\Local\Temp\tmpcnr5z732\95ba545448a34514a716169676349603_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_deny -->
    - utter_did_that_help
* affirm: yes
    - utter_happy


## sad path 2 (C:\Users\Infogen\AppData\Local\Temp\tmpcnr5z732\95ba545448a34514a716169676349603_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_deny -->
    - utter_did_that_help
* deny: not really
    - utter_goodbye


## sad path 3 (C:\Users\Infogen\AppData\Local\Temp\tmpcnr5z732\95ba545448a34514a716169676349603_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: food-related: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_deny -->
    - utter_did_that_help
* deny: no
    - utter_goodbye


