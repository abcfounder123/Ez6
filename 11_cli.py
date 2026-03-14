
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

                90350 sec
                  
            1505 min           50 sec
            
        25 h        5min
     
    1 day   1 h   
    

23. Seconds to Minutes or Hours

seconds = int(input("Enter time in seconds: "))
minutes = seconds / 60
hours = seconds / 3600
print(f"{seconds} seconds is equal to {minutes:.2f} minutes or {hours:.2f} hours")

################################################

24. Seconds to Seconds, Minutes and Hours   ( 350, 3950)

            3950 sec
            
            
       1 hour        350 sec
       
                  5 min    50 sec
                  
seconds = int(input("Enter time in seconds: "))
h = seconds // 3600               # 1 hour
m = (seconds % 3600) // 60        # 350 sec // 60 => 5 min
s = (seconds % 3600) % 60         # 50 sec
print(f"{h}:{m}:{s}")

################################################

25. Seconds to Seconds, Minutes, Hours and days ( 90350 )
25  --> 1 + 1

seconds = int(input("Enter time in seconds: "))
h = seconds // 3600
m = (seconds % 3600) // 60
s = (seconds % 3600) % 60
d = h // 24
nh = h % 24
print(f"{d} days and {nh}:{m}:{s}")

################################################################################################

* rate

1$ = 5000 Kysts
10$ = ?
Kysts =  10 / 1  * 5000  = 50000


26. Currency Converter (USD to MMK)

usd = float(input("Enter amount in USD: "))
exchange_rate = 5000
mmk = usd * exchange_rate                      
print(f"{usd} USD is equal to {mmk} MMK.")

dollar = float(input("Dollar : "))
kyats = dollar * 5000
print(f"{dollar} $ is equal to {kyats:.0f} kyats.")

################################################

27. Currency Converter (Custom Rate)

1 $        -> 5000 kyats
1 kyats    -> 0.0002 $

1 $ -> 40 B
1 B -> 0.025 $

5%  to rate
=> 100   ....   5
=> 1     ....   =  1/100  * 5  = 5 / 100 = 0.05

rate of 5% = 5/100 = 0.05
rate of 10% = 10/100 = 0.1
rate of 20% = 20/100 = 0.2
rate of 25% = 25/100 = 0.25
rate of 110% = 110/100 = 1.1
rate of 107% = 1.07
rate of 112.5% = 1.125
rate of 200% = 2

################################################

amount = float(input("Enter amount: "))
rate = float(input("Enter exchange rate: "))
converted = amount * rate
print(f"Converted amount: {converted}")

################################################

Enter amount: 10000
Enter exchange rate: 0.0002
Converted amount: 2.0

Enter amount: 2
Enter exchange rate: 5000
Converted amount: 10000.0

################################################

28. Step-to-Calorie Converter

1 Step -> 0.04 kilo calorie
1 kcal -> 25 steps

steps = int(input("Enter number of steps taken: "))
calories_burned = steps * 0.04  # Approximation for an average person
print(f"Calories burned: {calories_burned:.0f} kcal")

calories_burned = int(input("Calories burned: "))
steps = calories_burned * 25
print(f"Number of steps : {steps:.0f} steps")

################################################

29. Storage Converter (GB to MB & KB)

    60     60
sec => min => hour

 1000
b -> k -> m -> g

 1024
b -> k -> m -> g


10    = 10 ** 1
100   = 10 ** 2
1000  = 10 ** 3

2 ** 1  = 2
2 ** 2  = 4
2 ** 3  = 8
2 ** 4  = 16
2 ** 5  = 32
2 ** 6  = 64
2 ** 7  = 128
2 ** 8  = 256
2 ** 9  = 512
2 ** 10 = 1024
2 ** 11 = 2048

1kg = 1000 g
1km = 1000 m

1kb = 1000 bytes
1kb = 1024 bytes

gb = float(input("Enter storage in GB: "))
mb = gb * 1000
kb = gb * 1000 * 1000
print(f"{gb} GB is equal to {mb} MB or {kb} KB")

gb = float(input("Enter storage in GB: "))
mb = gb * 1024  # 2 ** 10  Vs  10 ** 3
kb = gb * 1024 * 1024
print(f"{gb} GB is equal to {mb} MB or {kb} KB")

################################################

30. Bytes to GB + MB + KB + B

                    34_567_891_234 bytes

                  34_567_891 kb      234 b
                  
                 34_567 M     891 kb
                  
              34 G    567 M
                                                                        
################################################

31. 

bytes = int(input("Enter size in bytes: ")) # 34_567_891_234 bytes
e = 1000

kb = bytes // e # 34_567_891 KB
b = bytes % e   # 234 B

mb = kb // e # 34_567 MB
kb2 = kb % e # 891 KB

gb = mb // e # 34 GB
mb2 = mb % e # 567 MB

print(f"{bytes} bytes = {gb} GB {mb2} MB {kb2} KB {b} B")


34567891234 bytes = 34 GB 567 MB 891 KB 234 B
34567891234 bytes = 32 GB 198 MB 522 KB 290 B

################################################

bytes_size = int(input("Enter size in bytes: ")) # 34_567_891_234 bytes

e = 1024

kb = bytes_size // e 
b = bytes_size % e 

mb = kb // e 
kb2 = kb % e

gb = mb // e
mb2 = mb % e 

print(f"{bytes_size} bytes = {gb} GB {mb2} MB {kb2} KB {b} B")


Enter size in bytes: 34_567_891_234
34567891234 bytes = 32 GB 198 MB 522 KB 290 B

################################################

32.

         12_345_678_900       bytes
         
      12 GB     345_678_900 bytes
         
              345 MB      678_900   bytes
              
                      678 KB     900  bytes


bytes_size = int(input("Enter size in bytes: ")) # 12_345_678_900       bytes

gb = bytes_size // 1e9                       # 12 GB
mb = (bytes_size % 1e9) // 1e6               # 345 MB
kb = ((bytes_size % 1e9) % 1e6) // 1e3       # 678 KB
b = ((bytes_size % 1e9) % 1e6) % 1e3         # 900  bytes

print(f"{gb} GB {mb} MB {kb} KB and {b} bytes")

################################################

bytes_size = int(input("Enter size in bytes: ")) # 12_345_678_900       bytes

gb = bytes_size // (1024 ** 3)                               # 11 GB
mb = (bytes_size % (1024 ** 3)) // (1024 ** 2)               # 509 MB
kb = ((bytes_size % (1024 ** 3)) % (1024 ** 2)) // 1024       # 775 KB
b = ((bytes_size % (1024 ** 3)) % (1024 ** 2)) % 1024         # 52 bytes

print(f"{gb} GB {mb} MB {kb} KB and {b} bytes")

################################################

                  90350 sec
                  
            1505 min           50 sec        60
            
        25 h        5min                     60
     
     1 day 1 h                               24
         
################################################
    
                            90350 sec

    86400              1 day         3950 sec
    
    3600                           1 h       350 sec
    
    60                                     5 min  50 sec

n = 60 * 60 * 24 = 86400

sec = int(input("Seconds = "))
d = sec // 86400
h = (sec % 86400) // 3600
m = ((sec % 86400) % 3600) // 60
s = ((sec % 86400) % 3600) % 60
print(f"{d} day {h} : {m} : {s}")
        
################################################################################################

platform
1. system()
2. version()
3. architecture()[0] 

sys
1. version

psutil (process and system utilities )
1. virtual_memory() -> RAM 
   - total = 8GB
   - available = 3GB 
   
2. cpu_count(logical=False) # man = 2
   cpu_count(logical=True)  # work = 4
   
3. disk_usage('/')
   - total = 256GB
   - free = 156GB 
   
4. cpu_percent(interval=1)     

5. sensors_battery()
   - power_plugged
   - percent

################################################

1. Check Operating System


import platform

print("Operating System:", platform.system()) # mac OS and IOS based on Darwin OS

################################################

2. Check OS Version

import platform
print("OS Version:", platform.version())

################################################

3. Check Machine Type (32-bit or 64-bit)

import platform
print("Machine Type:", platform.architecture()[0])

################################################

4. Check Python Version

import sys
print("Python Version:", sys.version)

################################################

5. Check Total RAM / Available RAM (Memory)

import psutil

ram = psutil.virtual_memory()
total = ram.total / ( 1024 ** 3 )
available = ram.available / ( 1024 ** 3 )
print(f"Total RAM:", total, "GB")
print(f"Available RAM:", available, "GB")

################################################

6. Check CPU Information

Physical CPU count = 2
Logical CPU count = 4

2   =>  4
2   =>  2

i5 U      => 4, 4 
i5 H, HQ  => 4, 8 

i3, i5, i7     (boy, man)

i7 U      8, 8
i5 H      4, 8

i7 12 generation    
m1                 

1 km   => 6 min, 6 min
1 km   => 10 min, 6 min
1 km   => 15 min, 6 min
          31 min, 18 min

import psutil
print("CPU Cores:", psutil.cpu_count(logical=False))        
print("Logical CPUs:", psutil.cpu_count(logical=True))     

################################################

7. Check Disk Usage (Total and Free Space)

import psutil
disk = psutil.disk_usage('/')
t = disk.total / ( 1024 ** 3 )
f = disk.free / ( 1024 ** 3 )
print(f"Total Disk Space: {t:.0f} GB")
print(f"Free Disk Space: {f:.0f} GB")

################################################

8. Check CPU Usage

import psutil
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage:", cpu, "%")

################################################

9. Check Battery Status

import psutil

battery = psutil.sensors_battery()
percent = battery.percent
charging = battery.power_plugged

print(f"Battery Status: {percent}%")
print("Charging:", charging)

################################################################################################

10. BMI (Body Mass Index) Calculator  (kg per m**2)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")


weight = float(input("Enter weight in lb: ")) * 0.454
height = float(input("Enter height in ft: ")) * 0.3048
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")


# 1lb = 0.454 kg  ( lb * 0.454 )
# 1kg = 2.2lb     ( lb / 2.2 )

# 1ft = 0.3048m   ( ft * 0.3048 )
# 1m = 3.28 ft    ( ft / 3.28 )

weight2 = float(input("Enter weight in lb: ")) * 0.454
height_f = float(input("Enter height in ft: ")) * 0.3048
height_i = float(input("Enter height in inches: ")) * 0.0254
height2 = height_f + height_i

bmi2 = weight2 / (height2 ** 2)
print(f"Your BMI is: {bmi2}")

################################################

11. Heart Rate Zones Calculator

age = int(input("Enter your age: "))
max_heart_rate = 220 - age

print(f"Maximum Heart Rate: {max_heart_rate} bpm")
print(f"Fat Burn Zone (50-70%): {max_heart_rate * 0.5} - {max_heart_rate * 0.7} bpm")
print(f"Cardio Zone (70-85%): {max_heart_rate * 0.7} - {max_heart_rate * 0.85} bpm")
print(f"Peak Zone (85-100%): {max_heart_rate * 0.85} - {max_heart_rate} bpm")

################################################

12. Moles to Mass Converter

molar_mass = float(input("Enter molar mass (g/mol): "))
moles = float(input("Enter number of moles: "))
print("Mass:", molar_mass * moles, "g")

################################################

13. Mass to Moles Converter

mass = float(input("Enter mass (g): "))
molar_mass = float(input("Enter molar mass (g/mol): "))
print("Moles:", mass / molar_mass)

################################################

14. Concentration (Molarity) Calculator

moles = float(input("Enter moles of solute: "))
volume = float(input("Enter volume of solution (L): "))
print("Molarity:", moles / volume, "M")

################################################

15. Dilution Calculator (M1V1 = M2V2)

M1V1 = M2V2
M2V2 = M1V1
M2 = M1V1/V2

M1 = float(input("Enter initial molarity (M): "))
V1 = float(input("Enter initial volume (L): "))
M2 = float(input("Enter final molarity (M): "))
print("Final volume:", (M1 * V1) / M2, "L")

################################################

16. Work Done

force = float(input("Enter force (N): "))
distance = float(input("Enter distance (m): "))
print("Work Done:", force * distance, "J")

################################################

17. Gravitational Force

G = 6.674 * (10**-11)
m1 = float(input("Enter mass of first object (kg): "))
m2 = float(input("Enter mass of second object (kg): "))
r = float(input("Enter distance between objects (m): "))
print("Gravitational Force:", G * m1 * m2 / (r ** 2), "N")

################################################

18. Kinetic Energy ( 1/2.m.v**2 )  ( 0.5 * m * v ** 2 )

mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
print("Kinetic Energy:", 0.5 * mass * velocity ** 2, "J")

################################################

19. Potential Energy (mgh) ( m * g * h )

mass = float(input("Enter mass (kg): "))
height = float(input("Enter height (m): "))
g = 9.81
ans = mass * g * height
print("Potential Energy:", ans, "J")

################################################

20. Power Calculation (Electrical Power) ( P = VI ) ( V * I )

voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))

print("Power:", voltage * current, "W")

################################################

21. Frequency and Wavelength (Wave Equation) (Frequency = speed / wavelength)

Frequency = speed / wavelength

wavelength = 3m
speed = 12 m sec
Frequency = 12 / 3 = 4

speed = float(input("Enter wave speed (m/s): "))
wavelength = float(input("Enter wavelength (m): "))
print("Frequency:", speed / wavelength, "Hz")

################################################

22. Momentum

mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
print("Momentum:", mass * velocity, "kg·m/s")

################################################

23. Ideal Gas Law Calculator (PV = nRT) (P = nRT/V) (P = n * R * T / V)

V = float(input("Enter volume (L): "))
n = float(input("Enter number of moles: "))
R = 0.0821  # Gas constant (L·atm/mol·K)
T = float(input("Enter temperature (K): "))
print("Pressure:", n * R * T / V, "atm")

################################################

24. Percentage Composition

element_mass = float(input("Enter mass of the element (g): "))             # oxygen = 10
compound_mass = float(input("Enter total mass of the compound (g): "))     # H2O = 20 + 20 + 10 = 50
print("Percentage composition:", (element_mass/compound_mass) * 100, "%")

################################################

25. Heat Energy Calculation (q = mcΔT) (mass * specific_heat * temp_change)

mass = float(input("Enter mass (g): "))
specific_heat = float(input("Enter specific heat capacity (J/g·°C): "))
temp_change = float(input("Enter temperature change (°C): "))
print("Heat energy:", mass * specific_heat * temp_change, "J")

################################################

26. Avogadro’s Law Calculator (V1/n1 = V2/n2) (v2 = (V1/n1) * n2 )

20/10 = 40/20

V1 = float(input("Enter initial volume (L): "))
n1 = float(input("Enter initial moles: "))
n2 = float(input("Enter final moles: "))
print("Final volume:", (V1/n1) * n2, "L")

################################################

27. Running Pace Calculator

5km   60 min
1km   ? 
=> 1 / 5 * 60  = 60/5

distance = float(input("Enter distance in kilometers: "))
time_minutes = float(input("Enter time taken in minutes: "))

pace = time_minutes / distance
print(f"Your running pace is {pace:.2f} minutes per km.")

################################################

28. Fuel Efficiency Converter (L/100km to MPG) (miles per gallon)

mpg = 235.215 / liters_per_100km
mpg * liters_per_100km = 235.215  
liters_per_100km = 235.215 / mpg  

liters_per_100km = float(input("Enter fuel efficiency in L/100km: "))
mpg = 235.215 / liters_per_100km
print(mpg, "MPG")

mpg = float(input("Enter fuel efficiency in mpg: "))
liters_per_100km = 235.215 / mpg
print(liters_per_100km, "l per 100km.")

################################################

29. Square Root Calculator

                16
                
            4        4
            
          
            
            4 ** (2/1)  = 16
            16 ** (1/2) = 4

number = float(input("Enter a number: "))
sqrt = number ** (1/2)
print(f"The square root of {number} is {sqrt}")

# Cube Root Calculator
number = float(input("Enter a number: "))
print(f"The cube root of {number} is {number ** (1/3):.0f}")


################################################

30. Simple Interest  (p * r * t)

100_000
1 year = 100_000 * 0.1 = 10_000
5 years = 10_000 * 5

100    10
1      ?  0.1

% to rate  =>  % / 100
=> 1/100 * 10 = 10/100 = 0.1

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate (%): ")) / 100  # 0.1
t = float(input("Enter time (years): "))
print("Simple Interest:", p * r * t)

################################################

31. Compound Interest

p = 100_000
1 year => 100_000 + 10_000 =>  110_000 
2 year => 110_000 + 11_000 =>  121_000
3 year => 121_000 + 12_100 =>  133_100

################################################

p = 100_000
r = 0.1

i = p * r # 10_000
p = p + i # 110_000
print(p)

################################################

p = 100_000
r = 0.1

i = p * r
p = p + i

i = p * r
p = p + i

i = p * r
p = p + i

i = p * r
p = p + i

i = p * r
p = p + i

print(f"5 year = {p}")

################################################

p = 100_000
r = 0.1

for _ in range(5):
    i = p * r
    p = p + i

print(f"5 year = {p}")

################################################

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate (%): ")) / 100 
t = int(input("Enter time (years): ")) 

for _ in range(t):
    i = p * r
    p = p + i

print(f"{t} year = {p}")

################################################################################################

32. nested loop

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
2 * 11 = 22
2 * 12 = 24

print(f"2 * 1 = ?")
print(f"2 * 2 = ?")
print(f"2 * 3 = ?")
print(f"2 * 4 = ?")
print(f"2 * 5 = ?")
print(f"2 * 6 = ?")
print(f"2 * 7 = ?")
print(f"2 * 8 = ?")
print(f"2 * 9 = ?")
print(f"2 * 10 = ?")
print(f"2 * 11 = ?")
print(f"2 * 12 = ?")
       
################################################

for l in range(2, 11, 1):
    print(l)

for r in range(1, 13, 1):
    print(f"2 * {r} = {2 * r}")

print("-" * 42)

for r in range(1, 13, 1):
    print(f"3 * {r} = {3 * r}")

print("-" * 42)

for r in range(1, 13, 1):
    print(f"4 * {r} = {4 * r}")

print("-" * 42)

for r in range(1, 13, 1):
    print(f"5 * {r} = {5 * r}")

print("-" * 42)

################################################

for l in range(2, 17, 1): 
    for r in range(1, 13, 1):
        print(f"{l} * {r} = {l * r}")
    print("-" * 42)

################################################

for l in range(2, 37, 1):
    for r in range(12, 0, -1): 
        print(f"{l} * {r} = {l * r}")
    print("-" * 42)

################################################################################################

"""
