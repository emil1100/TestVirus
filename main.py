i = input("Programname: ")+".py"
if i == "test.py":
  i = "test/ExecForTest.py"
f = open(i, "r")
exec(f.read())