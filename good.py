n=int(input())

for _ in range(n):
    x=input().strip()
    y=len(x)
    if x>10:
       print( x[0]+ str(y-2) + x[-1] )
    else:
       print(x)