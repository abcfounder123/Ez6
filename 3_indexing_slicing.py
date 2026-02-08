
"""

1. Collection, element
2. print()
3. Standard output file
4. len()
5. absolute value  +1, -1, 1  =>  1
6. Division
   - True Division       2.5
   - Floor Division      2
   - Modulus             1

#################################################

"abcdefg"

 a  b  c  d  e  f  g          7
 0  1  2  3  4  5  6          positive index
-7 -6 -5 -4 -3 -2 -1          negative index 

#################################################

Indexing
- positive index  
- negative index 
- hard = total - abs(easy)
- f1, f5, f10
- l1, l5, l10
- middle index 
  - odd, m = total // 2
  - even, rm = total // 2, lm = rm - 1

#################################################

Slicing
- value
- index
- start, stop, step
- f5 (start to 4)
  - stop = 5
- l5 (-5 to end)
  - start = -5

#################################################

1. value => bcde
2. index => 1 2 3 4, -6 -5 -4 -3 
3. start, stop, step

#################################################

bcde

1 2 3 4
start = 1
stop  = 5
step  = 1
[1:5:1]

-6 -5 -4 -3 
start = -6
stop  = -2
step  = 1
[-6:-2:1]

x = "abcdefg"
print(x[1:5:1])
print(x[-6:-2:1])

#################################################

1. value => edcb
2. index => 4 3 2 1, -3 -4 -5 -6
3. start, stop, step

#################################################

edcb

4 3 2 1
start = 4
stop  = 0
step  = -1
[4:0:-1]

-3 -4 -5 -6
start = -3
stop  = -7
step  = -1
[-3:-7:-1]

#################################################

f5 
abcde 
01234 

start = 0
stop  = 5
step  = 1

print(x[0:5:1])
print(x[0:5])
print(x[:5])     # [start:5]  => 01234

#################################################

f5
stop = 5

f10
stop = 10

#################################################

l5

 c  d  e  f  g
-5 -4 -3 -2 -1

start = -5
stop  = end 
step  = 1

print(x[-5::1])
print(x[-5:])      # from -5 to the end   => -5 -4 -3 -2 -1

#################################################

l5
start = -5

l10
start = -10

##################################################################################################

"""
