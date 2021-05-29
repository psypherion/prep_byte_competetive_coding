ar=[]
t=int(input())
for i in range(0,t):
  ip = int(input())
  ar.append(ip)
  if ar[i]%400 == 0:
    print("Yes")
  elif ar[i]%100 != 0 and ar[i]%4 == 0 :
    print("Yes")
  else :
    print("No")
