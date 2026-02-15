
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

"""
