fb1 = fb2 = 1
 
n = int(input())
 
if n < 2:
    quit()
 
print(fb1)
print(fb2)
for i in range(2, n):
    fb1, fb2 = fb2, fb1 + fb2
    print(fb2)
