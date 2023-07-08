#Вариант1
x=input("Enter the nuber:")
x=int(x)
for i in range(x):
    print("*",end="")
print()

#Вариант2
x=input("Enter the nuber:")
x=int(x)
i = 0
s = ""
while x>i:
    s += "*"
    i += 1
print(s)

#Вариант3
x=input("Enter the nuber:")
x=int(x)
print("*"*x)
