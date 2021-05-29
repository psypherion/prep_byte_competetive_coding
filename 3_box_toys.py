ip = int(input())
count = 0
for i in range (0,ip):
  t, c = input().split()
  s = int(c)-int(t)
  if s > 1:
    count = count +1
print(count)
