ip = int(input())
for i in range (0,ip):
  x,y = input().split()
  if float(x) <= 100.0:
    print(float(x)*float(y))
  else :
    print(float(x)*(float(y)-float(y)*(0.2)))
