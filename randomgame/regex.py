# import re 

# pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8}$")
# string = "Mic@ael1"
# a = pattern.search(string)
# print(a)

import text_to_speech as speech

speech.speak("Γεια σας το όνομά μου είναι Μιχάλης","el")