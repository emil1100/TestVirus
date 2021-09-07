osredo = 0
i = input("Programname: ")+".py"

if i == "Test.py":
  i = "ExecForTest.py"
  osredo = 1

f = open(i, "r")
exec(f.read())
f.close()

if osredo == 1:
  import os
  print("\n\n\n")
  if input('Vill du tömma "Test/"(ja/nej)? ') == "ja":
    for i in os.listdir("Test"):
      os.remove("Test/" + i)