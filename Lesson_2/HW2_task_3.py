v=int(input("Enter the bike's speed:"))
# v = int(v)
t=input("Enter the time in a path:")
t=int(t)
p=0
if v>0:
   p=v*t
else:
# elif v<0:
    p=100+v*t
   # p=abs(100+v*t)
print("Stop Point of Vasya:",int(p),"km")
if p>100:
   print("Вася, тормози! Вали обратно!")
