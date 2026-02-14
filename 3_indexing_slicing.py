
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

Day.5

Slicing

- value
- index
- start, stop, step

- f5 (start to 4)
  - stop = 5
- l5 (-5 to end)
  - start = -5
  
- reverse = [::-1]
- left to right  =>  step = +
- right to left  =>  step = -
- richest to poorest = reverse

Extra
- half => [:m], [m:], even(equal), odd(r+1)
- 3    => [:p1], [p1:p2], [p2:]
- 4    => [:p1], [p1:p2], [p2:p3], [p3:]
- 5    =>  p1 to p4 (p1 = t//5, p4 = p1 * 4)
- 75%  =>  3/4 = stop_point = t//4 * 3
- 25%  =>  [stop_point:]
- 80%  =>  4/5, stop_point = t//5 * 4
- 20%  =>  [stop_point:]

Knowledge
1. Reverse engineering
2. Real world example
3. range of collections
4. 1D, 2D, 3D

#################################################
 
Machine learning

input data = x , result = y

x =  1, 2, 3, 4, 5, 6              
y =  2, 4, 6, 8, 10, 12             

Train data  
x =  1, 3, 4, 6             
y =  2, 6, 8, 12
      
model = 2x        

Test data
x = 2, 5
y = 4, 10

test(x) by using our model = 2, 5
predict output from our model = 4, 10

If test data of y (real output) is equal to predict output from our model, our model will be true.
y = 4, 10
predict = 4, 10

#################################################

1 -> 100000
2 -> 150000
3 -> 200000
function -> bed * 50000 + 50000

#################################################

x1 = bed
x2 = bath

1, 1 -> 120000
2, 1 -> 170000
3, 2 -> 240000
4, 2 -> 290000

function => (bed * 50000) + (bath * 20000) + 50000
function => (x1 * 50000) + (x2 * 20000) + 50000

#################################################

x3 = bad review   (1 or 0)

1, 1, 1 -> 70000
2, 1, 0 -> 170000
3, 2, 1 -> 190000
4, 2, 0 -> 290000

function => (bed * 50000) + (bath * 20000) - (bad_review * 50000) + 50000
function => (x1 * 50000) + (x2 * 20000) - (x3 * 50000) + 50000

################################################################################################## 

1. Reverse engineering

richest[-10:][::-1]  -->  true poorest 10             <---

[-10:] <-- last 10
[::-1] <-- reverse
true poorest 10

richest[:10]         -->  richest 10, first 10
richest[-10:]        -->  poorest10,  last 10
richest[::-1]        -->  richest list to poorest list

################################################# 

richest[-1:-29:-1]   -->  poorest 28       <--- complex
rf10 = [9::-1]                             <--- complex

richest[-28:][::-1]  -->  poorest 28       <--- easy
f10r = [:10][::-1]                         <--- easy

################################################# 

1/4

p1 = t * 1/4 = t // 4 * 1 = 4
p2 = t * 2/4 = t // 4 * 2 = 8
p3 = t * 3/4 = t // 4 * 3 = 12

abcdefghijklmnop     = 16

abcd    efgh     ijkl      mnop  
[:p1]   [p1:p2]  [p2:p3]   [p3:]

################################################# 

2. Real world

last 50 = [-50:]
f 50    = [:50]

f15 to l10 = [14:-10]
l10 to f15 = f15 to l10 reverse = [14:-10] [::-1]
l10 to f15 = [-10:13:-1]        <--- right to left is complex

#################################################

right to left is complex 

1 2 3 4 5 6 7 8 9 10  11 12 13 14 15 16 17 18 19 20  21 22 23 24 25 26 27 28 29 30

      15 16 17 18 19 20  21

13    14 15 16 17 18 19  20
-17  -16-15-14-13-12-11 -10

################################################# 

3. range of collections

total = 10
range => -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9   => -t to t-1

total = 100
range => -100 to 99
 

#################################################

out of range error

IndexError: list index out of range
IndexError: string index out of range
IndexError: tuple index out of range

################################################# 

4. 1D, 2D, 3D

1D  ( collection of data )

x = [1, 2, 3, 4, 5]

################################################# 

2D  (collection of collection)
   c0    c1   c2   c3  c4
[  
   [1,   2,   3,   4,  5],          row0
   [1.1, 2.2, 3.3       ],          row1
   [1,   1.1, 2.1, 3    ]           row2
      
]


2D = row x col
1 = 0, 0
3.3 = 1, 2 



x = [1, 2, 3, 4, 5]
y = [1.1, 2.2, 3.3]
z = [1, 1.1, 2.1, 3, "apple"]
d2 = [x, y, z]

print(x[0])                  <--- 1D
print(d2[1][2])              <--- 2D
print(d2[2][-1][-1])         <--- 3D

################################################# 

3D by cubic example
4D by expanding sponge example

  _________
 /        /|
/________/ |  1cm
|        | |
|        | /    
|________|/ 1cm
   1cm


1 sec
width, length, x =  1 cm
height       , y =  1 cm
thick        , z =  1 cm

2 sec
width, length, x =  1.1 cm
height       , y =  1.1 cm
thick        , z =  1.1 cm

3 sec
width, length, x =  1.2 cm
height       , y =  1.2 cm
thick        , z =  1.2 cm

...
...

10s
width, length, x =  2 cm
height       , y =  2 cm
thick        , z =  2 cm

x + y + z + time = 4D

################################################# 

photo + time     -> video

################################################################################################## 

"""
