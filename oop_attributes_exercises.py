
"""

Step.1   --->   Write

Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)

Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။  (size, pressure=0) ( pump(p) )
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။  (fuel_type, state="off") 
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

#################################################

Step.2   --->   Divide

class   --->   Car
data    --->   VIN, tires, engine
method  --->

class   --->  Tires
data    --->  size, pressure = 0
method  --->  pump(p)

class   --->  Engine
data    --->  fuel_type, state = off
method  --->  on(), off()

#################################################

Naming rules

1. lower snake case, lower case     =>   all (data, fun, file, module, ... )
2. Upper cameal case                =>   class name
3. Upper case                       =>   Constant data

#################################################

Knowledges

1. Name
   - UpperCamealCase

2. Data
   - external 
   - prefix

3. Method
   - external 
   - prefix
   
4. init
   - initialzation ( first stage of somthing. )
   - constructor
   - self, other


5. class    =>  design for house (paper)

6. object   =>  real house (RAM)

7. label    =>  house address (Mandalay)

#################################################

class Tires:
    def __init__(self, size):
        self.size = size        <--- external data
        self.pressure = 0       <--- prefix data
        
#################################################              
        
def pump():
    print("pump to 0 psi.")        <--- function with prefix data


def pump(x):
    print(f"pump to {x} psi.")     <--- function with external data
 
################################################################################################## 
   
Step.3   --->   Draw design


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        print(f"ON ({self.fuel_type})")

    def off(self):
        print("OFF")
        

##################################################################################################

Step.4   --->   controlling data by fun ( pressure by pump(), state by on() and off() )

self.pressure = x

#################################################

Step.5   --->   controlling function by data ( on() and off() by state )

if off: on
if on: off

#################################################

Step.6   --->   Auto create serial number

n = 0

Car.n += 1
self.VIN = f"BMW-{Car.n:0>4}"

#################################################


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, x):
        print(f"pump to {x} psi.")
        self.pressure = x


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print(f"ON ({self.fuel_type})")
            self.state = "on"
        else:
            print("Already on.")

    def off(self):
        if self.state == "on":
            print("OFF")
            self.state = "off"
        else:
            print("Already off.")
            

class Car:
    n = 0
    def __init__(self, tires, engine):
        Car.n += 1
        self.VIN = f"BMW-{Car.n:0>4}"
        self.tires = tires
        self.engine = engine


car1 = Car(Tires(15), Engine("Gas"))
car2 = Car(Tires(15), Engine("Gas"))
car3 = Car(Tires(15), Engine("Gas"))
car4 = Car(Tires(15), Engine("Gas"))

print(car4.__dict__)

##################################################################################################

"""
