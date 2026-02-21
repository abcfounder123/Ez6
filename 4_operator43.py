
"""

Day.6  

Operator 43

1. Operation, Operator, Operand


        1 + 2    <=   Additional Operation
          +      <=   Additional Operator
          1      <=   Left Operand
          2      <=   Right Operand

################################################

2. Types of operator 
   - unary operator    (right)
   - binary operator   (l, r)
   - ternary operator  (middle)

################################################

3. positive, negative, addition, subtraction

+1          <- pos
-1          <- neg
1 + 2       <- addition
1 - 2       <- subtraction

################################################

1 + 2  ->  add
1 - 2  ->  sub
-2     ->  neg
1 * 2  ->  multiplication, mul
1 / 2  ->  division, div

################################################

Precedence

add
1 + 2 * 3
    3 * 3
        9
        
mul
1 + 2 * 3
1 + 6
7

################################################

Associativity

1. Left sided bind
2. Right sided bind

Left
2 ** 2 ** 3
     4 ** 3
         64
         
Right
2 ** 2 ** 3
2 ** 8
256


1 + 2 * 3 // 4 - 5 % 6 + 1 ** 7

################################################

Exercise

1 + 2 * 3 // 4 - 5 % 6 + 1 ** 7

1. **
>> 1 + 2 * 3 // 4 - 5 % 6 + 1

3. * 
>> 1 + 6 // 4 - 5 % 6 + 1

3. //
>> 1 + 1 - 5 % 6 + 1

3. %
>> 1 + 1 - 5 + 1

4. +
>> 2 - 5 + 1
 
4. -
>> -3 + 1

4. +
>> -2


1. **
2. 
3. *, //, %
4. +, -, +

################################################

Arithmetic operators (9)(e u */ +-)

true division   =>   5 / 2    =>  2.5
floor division  =>   5 // 2   =>  2
modulus         =>   5 % 2    =>  1

################################################

1. e     exponent    **                                  R

2. u     unary operator   +1, -1 , ~                     R

3. *, /  .......          *, /, //, %                    L

4. +, -    add, sub       +, -                           L

################################################

e u */ +-

shift and or2

################################################

Bit => Binary digit => 0, 1

################################################

Bitwise operators(6)
1. left shift
2. right shift
3. Bitwise AND
4. Bitwise Exclusive OR (XOR)
5. Bitwise OR
6. Bitwise NOT

################################################
   
1. e 
2. u       positive, negative, ~
3. */ 
4. +-

5. shift     <<, >>
6. and       &
7. xor       ^
8. or        |

Bitwise

################################################

Bitwise operators(6)

1. left shift

    0000
    1111
    
    0000
   1111 
   
   1111 << 1      -->  1110
   
################################################

2. right shift

    0000
    1111
    
    0000
     1111 
   
    1111 >> 1      -->  0111
       
################################################   
       
3. Bitwise AND (both wires)

  0101
         AND    0001
  0011


  0101 & 0011  => 0001

################################################ 

4. Bitwise Exclusive OR (XOR)  (only one wire)

  0101
         XOR     0110
  0011

  0101 ^ 0011  =>  0110
  
################################################

5. Bitwise OR (any wire)

  0101
          OR     0110
  0011


  0101 | 0011  =>  0111
  
################################################

6. Bitwise NOT (opposite)

  0011 ---  NOT  --- 1100   

  ~ 0011  =>  1100

################################################

1111 << 1       =>  1110
1111 >> 1       =>  0111
0101 & 0011     =>  0001
0101 ^ 0011     =>  0110
0101 | 0011     =>  0111
     ~ 0011     =>  1100

################################################

I want apple and banana. 
I want apple or banana.  
I want apple xor banana.
I do not want apple.

################################################################################################

Daty.7

Comparison Operators(6) (compare values => True, False)
1. equal to (==) 
2. not equal to (!=) 
3. greater than (>)
4. less than (<)
5. greater than or equal to (>=)
6. less than or equal to (<=)

eg

################################################

Identity Operators(2) (compare ID)
1. is
2. is not

################################################

Mg Mg   123456
Mg Mg   143257

x == y    True
x is y    False

################################################

Membership Operators(2)
1. in
2. not in

################################################

Logical Operators(3) (Logical value, boolean value, True/False)
1. not
2. and
3. or

################################################

~ 1        =>   0             (bitwise not)  (precedence.2 )
not True   =>   False         (logical not)  (precedence.10)

1 & 1           =>   1        (bitwise and)
True and True   =>   True     (logical and)

0 | 1           =>   1        (bitwise and)
False or True   =>   True     (logical and)

################################################

Ternary Operator, Conditional Operator, if else Operator, Conditional Expression

left   middle   right

condition => True   => left
condition => False  => right


permit = "sell" if age > 18 else "not sell"
permit = "not sell"  age <= 18 "sell"

result = "pass" if mark >= 40 else "fail"
result = "fail" if mark < 40 else "pass"

################################################

14. Assignment Operator(13)

1. Assign (=)

2. Exponent and assign (**=)
3. Multiply and assign (*=)
4. Division and assign (/=)
5. Floor Division and assign (//=)
6. Modulus and assign (%=)
7. Add and assign (+=)
8. Substract and assign (-=)

9. left shift and assign (<<=)
10. Right shift and assign (>>=)
11. Bitwise AND and assign (&=)
12. Bitwise Exclusive OR and assign (^=)
13. Bitwise OR and assign (|=)

################################################

x = x + 1  
=>  x += 1
add and assign

################################################

15. Walrus operator ( := )
    - assign and use
    - assign in operation

################################################

Precedence of Operators

1. e 
2. u       positive, negative, ~
3. */ 
4. +-

5. shift     <<, >>
6. and       &
7. xor       ^
8. or        |

9. c          c.6, i.2, m.2     ==
10. not
11. and
12. or

13. t
14. assignment     (assign, - and assign)  
15. walrus

################################################

Types of Operators by usage

a. Unary Operator(4)
   1. positive       +1
   2. negative       -1
   3. ~              ~ 0011
   4. not            not True

b. Binary Operator(38)

c. Ternary Operator(1)

################################################

Groups of Operators

1. Arithmetic operators (9)
2. Bitwise operators(6)
3. Comparison Operators(6)
4. Identity Operators(2)
5. Membership Operators(2)
6. Logical Operators(3)
7. Assignment Operator(13)

################################################################################################


"""
