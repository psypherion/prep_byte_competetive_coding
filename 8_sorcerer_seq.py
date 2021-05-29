ip_1 = int(input())
for i in range (0,ip_1):
  ip = int(input())
  ar = []
  ar.append(str(ip))
  while ip>1:
    if ip%2 == 0:
      ip = int((ip)**(0.5))
      ar.append(str(ip))
    elif ip%2 != 0:
      ip = int((ip)**(1.5))
      ar.append(str(ip))
  s = " ".join(ar)
  print(s)
