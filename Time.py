inpu=str(input())
format=inpu[-2:]
inp=inpu[:-2]
[h,m,s]=inp.split(':')
h=int(h)
if(inpu=="12:00:00AM"):
  print("00:00:00")
elif(format=="AM"):
  if(h==12):
    h=str('00')
    print(h,end=":")
    print(m,end=":")
    print(s)
  else:
    print(inp)
elif(format=="PM"):
  if(h<12):
    h=h+12
  elif(h==12):
    h=12
  print(h,end=":")
  print(m,end=":")
  print(s)