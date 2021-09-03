#Exec For Test
def replc(strng, old, new):
  for i in range(len(old)):
    strng = strng.replace(old[i], new[i])
  return(strng)
#
#
f = open("programmet/a.py", "r")
p = f.read()
f.close()
p = replc(p, ["os.getcwd()", "/notsus.py"], ['"test/test.py"', "test/notsus.py"])
#
#
#
#
#
#
#
f = open("test/test.py", "w")
f.write(p)
f.close()
exec(p)