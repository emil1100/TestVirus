try:
  f = open('Test/notsus.py', 'r')
  f.close()
except:
  f = open('Test/notsus.py', 'w')
  f.write('')