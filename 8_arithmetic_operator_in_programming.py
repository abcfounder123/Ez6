
"""
Arithmetic operators in programming 

f = (c * 9 / 5) + 32
c = (f - 32) * 5 / 9
f = x ** 2 - (2 * x * y) + y ** 2

################################################

floordiv and modulus

          350 sec
      
      5 min    50 sec

350 // 60 = 5 min
350 % 60 = 50 sec
 
################################################

                  90350 sec
                  
            1505 min           50 sec
            
        25 h        5 min
     
    1 day   1 h   
        
        
90350 sec = 1 days, 1 hours, 5 minutes, 50 seconds

################################################

t = int(input("Enter seconds:"))

min = t // 60   # 1505 min
sec = t % 60    # 50 sec

h = min // 60       # 25 h
min2 = min % 60     # 5 min

d = h // 24         # 1 day
h2 = h % 24         # 1 h

ans = f"{d} days, {h2} hours, {min2} minutes, {sec} seconds"

print(ans)

################################################

d = int(input("Enter days:"))
h = int(input("Enter hours:"))
m = int(input("Enter minutes:"))
s = int(input("Enter seconds:"))

ds = d * 24 * 60 * 60
hs = h * 60 * 60
ms = m * 60

t = ds + hs + ms + s
print(t)

################################################################################################

"""
