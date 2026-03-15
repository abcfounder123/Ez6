
"""

English-like language

Example.1
if mark is greater than or equal to 40, exam pass.
if mark is less than 40, exam fail.

Example.2
if mark is greater than or equal to 40, exam pass.
if not mark is greater than or equal to 40, exam fail.

Example.3
if mark is greater than or equal to 40, exam pass.
else, exam fail.

Example.4
if mark is less than 40, exam fail.
else, exam pass. 

################################################

Example.1

if mark is greater than or equal to 40, exam pass.
if mark >= 40: print("Exam pass.")

if mark is less than 40, exam fail.
if mark < 40: print("Exam fail.")

################################################

mark = int(input("Enter your marks : "))

if mark >= 40: print("Exam pass.")
if mark < 40: print("Exam fail.")

################################################

1. input()        "80"
2. int()           80
3. assign()
4. if
5. ge() 
6. print("Exam pass.")
7. if
8. lt()

1. input()        "30"
2. int()           30
3. assign()
4. if
5. ge() 
6. if
7. lt()
8. print("Exam fail.")

################################################

mark = int(input("Enter your marks : "))
exam_pass = mark >= 40
exam_fail = mark >= 40

if exam_pass: print("Exam pass.")
if exam_fail: print("Exam fail.")

################################################

1. input
2. int
3. assign
4. ge
5. assign
6. lt
7. assign
8. if
9. print("Exam pass.")
10. if

################################################

Example.2

if mark is greater than or equal to 40, exam pass.
if not mark is greater than or equal to 40, exam fail.

mark = int(input("Enter your marks : "))
exam_pass = mark >= 40

if exam_pass: print("Exam pass.")
if not exam_pass: print("Exam fail.")

################################################

30
1. input
2. int
3. assign
4. ge
5. assign
6. if
7. if
8. not
9. print("Exam fail.")

################################################

Example.3

if mark is greater than or equal to 40, exam pass.
else, exam fail.

################################################

mark = int(input("Enter your marks : "))

if mark >= 40: print("Exam pass.")
else: print("Exam fail.")

################################################

80
1. input
2. int
3. assign
4. if
5. ge
6. print("Exam pass.")

30
1. input
2. int
3. assign
4. if
5. ge
6. print("Exam fail.")

################################################

Example.4

if mark is less than 40, exam fail.
else, exam pass. 

################################################

mark = int(input("Enter your marks : "))

if mark < 40: print("Exam fail.")
else: print("Exam pass.")

################################################

if int(input("Enter your marks : ")) < 40: print("Exam fail.")
else: print("Exam pass.")

################################################

1. if
2. input
3. int
4. lt
5. print("Exam pass.")

################################################################################################

Selection

1. Normal Statement (semi-colon, end of line)
   - motor on
   - motor off
   - pass
   - fail

2. Conditional Statement
   - If water level is low, motor on.  
   - If water level is high, motor off. 
   - if exam pass, show "pass".
   - if exam fail, show "fail".

3. Conditional if Statement
   - boolean data type
   - True

4. Conditional else Statement
   - boolean data type
   - False
   
################################################

if c1: program.1

program.1 => Conditional Statement, Conditional if Statement, if Statement
c1        => first condition
if        => Conditional if, if
:         => creating code block 

code block
conditional code block
conditional if code block 
if block

################################################

1. Conditional if, if
2. Code block
3. Conditional code block
4. Conditional if code block, if code block, if block 
5. Conditional else code block, else code block, else block  
6. Condition
7. Boolean value (empty - False)
8. program flow
9. control flow
10. : (creating code block)
11. pass (keyword name for pass)
12. nested if (step.4)
13. Normally open Vs Normally close
14. Opposite condition ( not )
16. all from all, one from one ( if )
17. one from two ( if + else )
15. one from all (if + elif + else)

################################################

12. nested if (step.4)

Step.1 (condition => output?) (flow)

- 110 => a c 
- 111 => a c
- 011 => b e
- 001 => b e
- 1111 => a c
- 1011 => a d g
- 1010 => a d h

################################################

c1 = 1
c2 = 0
c3 = 1
c4 = 0

if c1:
    print("a")
    if c2:
        print("c")
    else:
        print("d")
        if c4:
            print("g")
        else:
            print("h")
    
else:
    print("b")
    if c3:
        print("e")
    else:
        print("f")

################################################

Step.2 (output => condition?) (control)

- a d h =>  1 0 - 0
- a d g =>  1 0 - 1
- b e g =>  0 _ 1 1
- b e h =>  0 _ 1 0

################################################

c1 = 0
c2 = 0
c3 = 1
c4 = 0

if c1:
    print("a")
    if c2:
        print("c")
    else:
        print("d")
        if c4:
            print("g")
        else:
            print("h")
    
else:
    print("b")
    if c3:
        print("e")
        if c4:
            print("g")
        else:
            print("h")
    else:
        print("f")

################################################

Step.3 (condition => new code)
- 1100 => print("new1")
- 1111 => print("new2")
- 0-01 => print("new3")
- 0-00 => print("new4")
- 10-0 => print("new5")

c4 = False

if c4:
    pass
else:
    print("new")
        
if not c4:
    print("new")
        
################################################

c1 = 1
c2 = 0
c3 = 1
c4 = 0

if c1:
    if c2:
        if c3:
            if c4:
                print("new2")
        else:
            if c4:
                pass
            else:
                print("new1")
    else:
        if c4:
            print("g")
        else:
            print("new5")
    
else:
    if c3:
        print("e")
        if c4:
            print("g")
        else:
            print("h")
    else:
        if c4:
            print("new3")
        else:
            print("new4")

################################################################################################

"""
