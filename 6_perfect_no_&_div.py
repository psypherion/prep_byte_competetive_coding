ip = int(input())
for i in range (0,ip):
  ip_1 = int(input())
  sum = 0
  for j in range (1,ip_1):
    if (ip_1%j == 0) :
      sum = sum+j
  if (sum == ip_1) :
    print("true")
  else :
    print("false")
