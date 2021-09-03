#Exec For Test
def replc(strng, old, new):
  for i in range(len(old)):
    strng = strng.replace(old[i], new[i])
  return(strng)
#
#
f = open("programmet.py", "r")
p = f.read()
f.close()
p = replc(p, ["os.getcwd()", "/notsus.py", "not done yet", "good location"], ['"Test/test.py"', "Test/notsus.py", '"Test/control.py"', '"Test/ask.py"'])
#
#
#
#
#
#
#
f = open("Test/test.py", "w")
f.write(p)
f.close()
exec(p)