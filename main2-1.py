name = input("Your name:")
num = input("number:")
n = int(num)
c = list(reversed(name))
b = ''.join(c)
print("My name is:", b)
print(num)

for i in range(n):
    print(str(i) + ":" + name)
