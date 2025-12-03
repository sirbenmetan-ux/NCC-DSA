#problem 1
n =int(input(print("Enter n: ")))
if n%2==0:
    print("even")
else:
    print("odd")

#problem 2
a=int(input(print("Enter a: ")))
b=int(input(print("Enter b: ")))
if a>b:
    print(a-b)
else:
    print(a+b)

#problem 3
x=int(input(print("Enter x: ")))
y=int(input(print("Enter y: ")))
z=int(input(print("Enter z: ")))
if x>0:
    k=x*y
else:
    k=x-y
print(k)
if z%2==0:
    print(k+z)
else:
    print(z-k)

#problem 4
t=int(input(print("Enter t: ")))
t=abs(t)
print(t)