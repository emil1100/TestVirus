l = ["control.py", "notsus.py"]
for i in l:
  f = open("Test/"+i, "r")
  exec(f.read())
  f.close()