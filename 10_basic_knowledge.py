
"""
1. CLI
2. character code, encode, ecode
3. single line string, preformatted string, multiline string, documentation string
4. square root ( exponent 1/2 ), cube root ( exponent 1/3 ) 
5. unicode, uppercase to lowercase  ( A to a )
6. Algorithms, pseudo code

################################################

CLI ( Command Line Interface )

GUI

800 * 600 = 480_000

2000 * 1000 = 2_000_000

500 50
. . . . .       X
. . . . .
. . . . .
. . . . .
. . . . .  5, 5

Y

500

x
      .             .
        .         .
           .   .
             .
          .    .
        .        .
      .            .
                                     
                                                    
################################################

1. Basic input & output (str)
   - input -> prompt letter
   - print -> comma

################################################

b = int(input("Enter bith year:"))

age = 2026 - b
ans = f"Your age is {age} years old."

print(ans)

################################################

x = 1
y = 2
z = 1.5
a = "apple"

print(x, y, z, a)

################################################

b = int(input("Enter bith year:"))

b           identifier, label
=           assignment operator
int()       creating integer by name, type casting
input()     receive input string

"Enter bith year:"  creating str by symbol, prompt letter

################################################

2. format(f)

f"Name = {name:fatr}."

################################################

3. character code (u0041, u000a, u0009)
   - 'the new line' character = 10, u000a, n
   - select the new line = \n
   - select the tab = t  (4 space)   =  9, u0009, t
   

A
	B
		C

A  =>  65   =>  u0041
B  =>  66   =>  u0042
C  =>  67   =>  u0043

"tab"      => 9  => u0009	
"new line" => 10 => u000a

print("\u0041\u000a\u0009\u0042\u000a\u0009\u0009\u0043")

print("A\n\tB\n\t\tC")

################################################

encode
ABC  => \u0041\u0042\u0043

decode
\u0041\u0042\u0043 => ABC

################################################

4. single line string 
   - single quotes, double quotes
   - can not encode "new line chr"  
   - single quotes can not encode '  
   - double quotes can not encode "   
 
39   0x27  single quote
34   0x22  double quote
  
################################################
     
Single line stringcan not encode "new line chr".
              
'I am a student.
I go to school.'

unterminated str 

################################################ 

I am a student.
I go to school.

=> "I am a student.\u000aI go to school."
=> "I am a student.\nI go to school."

################################################

single quotes can not encode '

I'm a student.
=> 'I\u0027m a student.'
=> 'I\'m a student.'
=> "I'm a student."

################################################

doublele quotes can not encode " 

Title = "My Self"
=> "Title = \u0022My Self\u0022"
=> "Title = \"My Self\""
=> 'Title = "My Self"'

################################################

y = "\nAge = 20\n\tName = Mg Mg\n\t\tMarks = 100\n\t\t\tRoll No = 1"
print(y)  

################################################

'''
Age = 20
    Name = Mg Mg
        Marks = 100
            Roll No = 1
'''

################################################

Triple quotes can encode "new line character".

5. multiline string
6. preformatted string   
7. documentation string
   
################################################

8. square root ( exponent 1/2 )   

4 ** 2 
4 * 4 
16


16 ** (1/2)
4

square root of 16 = 4
square root of 9 = 3
square root of 25 = 5


################################################

9. cube root ( exponent 1/3 ) 

4 ** 3
4 * 4 * 4
64

64 ** (1/3)
4

cube root of 64 = 4

################################################

10. Sequence

Ohm’s Law (Voltage, Current, Resistance)( V = IR )

V = I * R
I = V / R
R = V / I

################################################

i = float(input("Current = "))
r = float(input("Resistance = "))
v = i * r

print(f"Voltage = {v}")

################################################

print(f"Voltage = {float(input("Current = ")) * float(input("Resistance = "))}")

################################################

1. input("Current = ")
2. float()
3. input("Resistance = ") 
4. float()
5. mul()
6. format() 
7. print() 

################################################

1. input
2. float
3. assign
4. input
5. float
6. assign
7. mul
8. assign
9. format
10. print

################################################

11. unicode

65       A
97       a
4096     က

################################################

12. character to unicode number (ord(က) -> 4096)
    - ordinal unicode number of a character (ord)

13. unicode number to character (chr(4096) -> က)
    - unicode character (chr) 

################################################

14. uppercase to lowercase  ( A to a )

- unicode of A          65
- unicode of A + 32     97
- unicode number of 'a' to character

"A"  ->  65  + 32  ->  97  ->  "a"

u = input("Uppercase Character = ")
l = chr(ord(u) + 32)
print(f"Lowercase Character = {l}")

l = input("Lowercase Character = ")
u = chr(ord(l) - 32)
print(f"Uppercase Character = {u}")

################################################

15. Algorithms 

Algorithm for uppercase to lowercase 
- add 32

Algorithm for lowercase to uppercase
- substract 32

################################################

16. pseudo code

1. unicode of uppercase   
2. unicode of uppercase + 32    
3. unicode number of lowercase to character

################################################

uppercase = ord(input("uppercase = ")) # A   ->  65
lowercase = chr(uppercase + 32)        # 97  ->  a
print("lowercase =", lowercase)

################################################

Algorithm for lowercase to uppercase ( -32 )

pseudo code for lowercase to uppercase
- unicode of lowercase   
- unicode of lowercase - 32    
- unicode number of uppercase to character

Python code for lowercase to uppercase

lowercase = ord(input("lowercase = ")) # a   ->  97
uppercase = chr(lowercase - 32)        # 65  ->  A
print("uppercase =", uppercase)

################################################

Algorithm for A to  က ( + 4031 )

################################################################################################


"""

