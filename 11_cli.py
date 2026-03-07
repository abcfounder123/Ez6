
"""
CLI (35)

1. Water Intake Calculator

weight = float(input("Enter your weight in kg: "))
min = weight * 0.033
max = weight * 0.050
print(f"You should drink from {min:.2f} liters to {max:.2f} litres.")

################################################

2. Area of the circle ( pi.r**2 )

r = float(input("Enter radius: "))
area = 3.14159 * r ** 2
print("Area of the circle:", area)               

################################################

3.Area of triangle ( 1/2.b.h) (0.5.b.h)

base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("Area of triangle:", area)

################################################

4. Hypotenuse ( c**2 = a**2 + b**2 )  ( c**(2/1) = a**2 + b**2 ) ( c = (a**2 + b**2) ** (1/2) )

|\\
| \\ c
|b \\
|...\\
  a  

16 ** (1/2)
16 ** 0.5
4.0

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
h = (a ** 2 + b ** 2) ** (1/2)
print("Hypotenuse:", h)

################################################

5. Ohm’s Law (Voltage, Current, Resistance)( V = IR ) ( I = V/R ) ( R = V/I )

voltage = float(input("Enter voltage (V): "))     
resistance = float(input("Enter resistance (Ω): "))
current = voltage / resistance
print("Current:", current, "A")

################################################

6. Speed ( s = d / t )

3m + 3m + 3m + .. = 30m


30 m , 10 sec, 

speed = 3m/s
time = 10 seconds
distance = ? = 3m/s * 10s = 30m
d = s * t

10 sec, 30m, 
s = ?
1 sec   ?
30 / 10, d/t 

distance = float(input("Enter distance (m): "))
time = float(input("Enter time (s): "))
speed = distance / time
print("Speed:", speed, "m/s")

################################################

7. Force (Newton's Second Law) ( F = ma )

mass = float(input("Enter mass (kg): "))
acceleration = float(input("Enter acceleration (m/s²): "))
f = mass * acceleration
print("Force:", f, "N")

################################################

initial_amount = 600 g
half_life = 1000 years

3000 ? 
1000 ->  600 / 2  = 300 g
2000 ->  300 / 2  = 150 g
3000 ->  150 / 2  = 75  g  

initial_amount = 600 g
half_life = 1000 years
total = 3000 years
final_amount = ?

n = total / half_life = 3

=> 600 * 0.5 * 0.5 * 0.5
=> 600 * (0.5 ** 3) 
=> initial_amount * (0.5 ** (total / half_life)) 

8. Half-Life Calculator ( NO * 0.5 ** (time / half_life) )

initial_amount = float(input("Enter initial amount(g): "))
half_life = float(input("Enter half-life (years): "))  # 4.468e9 ( e9 = 1_000_000_000 )
time = float(input("Enter elapsed time (years): "))  # 4_000_000_000

n = time / half_life
ans = initial_amount * 0.5 ** n

print("Remaining amount:", ans)

################################################

9. Character to unicode( က )

char = input("Enter a character: ")
print("ASCII Code:", ord(char))

################################################

10. ASCII Code to Character

ascii_code = int(input("Enter an ASCII code: "))
print("Character:", chr(ascii_code))

################################################

11. decimal to bin, oct, hex

decimal = int(input("Enter a decimal number: "))
print("Binary:", bin(decimal))  
print("Octal:", oct(decimal))  # "0o12"
print("Hexadecimal:", hex(decimal))

################################################

12. bin, oct, hex  to decimal ( without code No )  "0011"

binary = input("Enter a binary number: ")
print("Decimal:", int(binary, 2))

oct = input("Enter a octal number: ")
print("Decimal:", int(oct, 8))

hex = input("Enter a hexadecimal number: ")
print("Decimal:", int(hex, 16))

################################################

13. bin, oct, hex  to decimal ( with code No )  

"10"
"0b10"    0b = 2
"0o10"    0o = 8
"0x10"    0x = 16

int("0b10", base=0)
int("0o10", base=0)
int("0x10", base=0)

code = input("Enter a code: ")
print("Decimal:", int(code, base=0))

binary = input("Enter a binary number: ")
print("Decimal:", int(binary, base=0))

oct = input("Enter a octal number: ")
print("Decimal:", int(oct, base=0))

hex = input("Enter a hexadecimal number: ")
print("Decimal:", int(hex, base=0))

################################################

code = "10"
int("10", base=2)   => 2
int("10", base=8)   => 8
int("10", base=16)  => 16

code = "0b10"
int(code, base=0)

################################################

14. Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
ans = f"{celsius} °C is equal to {fahrenheit} °F."
print(ans)

################################################

15. Fahrenheit to Celsius

fahrenheit = (celsius * 9/5) + 32
(celsius * 9/5) + 32 = fahrenheit
celsius * 9/5  = fahrenheit - 32
celsius  = (fahrenheit - 32) * 5/9

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius}°C")

################################################

16. Temperature Converter (Celsius to Kelvin) (F -> C -> K)

celsius = float(input("Enter temperature in Celsius: "))
kelvin = celsius + 273.15
print(f"{celsius}°C is equal to {kelvin:.2f}K")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
k = celsius + 273.15
print(k)

################################################

1km = 0.621371 miles
- miles = km * 0.621371
- km = miles / 0.621371

1 miles = 1.609 km
- km = miles * 1.609
- miles = km / 1.609

17. Kilometers to Miles       ( 1km = 0.621371 miles )   

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371  # 1km = 0.621371 miles
print(f"{km} km is equal to {miles} miles")

################################################

18. Miles to Kilometers    

miles = float(input("Enter distance in miles: "))
km = miles * 1.609  # 1miles = 1.609 km
print(f"{miles} miles is equal to {km} km")

################################################

19. Kilograms to Pounds   ( 1 kg = 2.20462 lb ) ( 1 lb = 0.454 kg )

kg = float(input("Enter weight in kilograms: "))
pounds = kg * 2.20462  # 1 kg = 2.20462 lb
print(f"{kg} kg is equal to {pounds} pounds")

################################################

20. Pounds to Kilograms

pounds = float(input("Enter weight in pounds: "))
kg = pounds * 0.454  # 1 lb = 0.454 kg
print(f"{pounds} pounds is equal to {kg} kg")

################################################

21. Meters to Feet     ( 1m = 3.28084 ft ) ( 1 ft = 0.305 m )

meters = float(input("Enter length in meters: "))
feet = meters * 3.28084
print(f"{meters} meters is equal to {feet} feet")

################################################

22. Feet to Meters

feet = float(input("Enter length in feet: "))
meters = feet * 0.305
print(f"{feet} feet is equal to {meters} meters")

################################################################################################

"""
