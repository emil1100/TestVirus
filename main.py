i = input("Programname: ")+".py"
if i == "Test.py":
  i = "Test/ExecForTest.py"
f = open(i, "r")
exec(f.read())