
''' Temperature conversion scale form Celcuis to Fahrenheit ,kelvin to Fahrenheit ,Celcius to Kelvin and viceverso
 develped by M Sathya Kumar 14-10-2022

'''
class Temperature_Scale:
    def __init__(self):
        self.Celcius = 0.0
        self.Fahrenheit = 0
        self.Kelvin = 0
        pass
    def Celcius_to_Fahrenheit(self,Celcius):
        self.Celcius = Celcius
        fahrenheit = (9/5)*self.Celcius+32
        return fahrenheit
    def Fahrenheit_to_Celcius(self,Fahrenheit):
        self.Fahrenheit = Fahrenheit
        celcius = (self.Fahrenheit-32)*(5/9)
        return celcius
    def Celcius_To_Kelvin(self,Celcius):
        self.Celcius = Celcius
        kelvin = self.Celcius+273
        return kelvin
    def Kelvin_To_Celcius(self,Kelvin):
        self.Kelvin = Kelvin
        celcius = self.Kelvin -273
        return celcius
    def Kelvin_To_Fahrenheit(self,Kelvin):
        self.Kelvin = Kelvin
        fah = (9/5)*(self.Kelvin-273)+32
        return fah
    def Fahrenheit_To_Kelvin(self,fahrenheit):
        self.fahrenheit = fahrenheit
        kelvin = (5/9)*(self.fahrenheit-32)+(273)
        return kelvin
    def __str__(self):
        return "Sathya"


if(__name__=="__main__"):
    temp = Temperature_Scale()
    print("Please Select Options for conversion: ")
    print("a. C to Fah \nb. Fah to C \nc. C to Kel \nd. Kel to C \ne. K to Fah\nf. Fah to K ")
    
    option = input("Please Enter input to proceed :")
    ''' Developed  by M Sathya Kumar '''
    # conversion Celcuis to Fahrenheit
    
    if((option).lower() =="a"):
        print("Please enter Celcius to Convert to Fahrenheit")
        cel = float(input(""))
        fahrenheit = temp.Celcius_to_Fahrenheit(cel)
        print("The Conversion from %d degree Celcius to Fahrenheit is"%(cel),fahrenheit)

    # conversion Fahrenheit to Celcuis
    elif((option).lower() =="b"):
        print("Please enter Fahrenheit to Convert")
        fah = float(input(""))
        cel = temp.Fahrenheit_to_Celcius(fah)
        print("The Conversion from %d Fahrenheit to Celcius  is"%(fah),cel)

    # conversion Fahrenheit to Celcuis    
    elif((option).lower() =="c"):
        print("Please enter Celcius to Convert to Kelvin")
        cel = float(input(""))
        kel = temp.Celcius_To_Kelvin(cel)
        print("The Conversion from %d Celcius to Kelvin is"%(cel),kel)
        
    # Conversion From Kelvin to Celcius
    elif((option).lower() =="d"):
        print("Please enter Kelvin to Convert to Celcius")
        kel = float(input(""))
        cel = temp.Kelvin_To_Celcius(kel)
        print("The Conversion from %d kelvin to celcius is"%(kel),cel)

    # Conversion From Kelvin To Fahrenheit
    
    elif((option).lower() =="e"):
        print("Please enter Kelvin to Convert to Fahrenheit")
        kel = float(input(""))
        fah = temp.Kelvin_To_Fahrenheit(kel)
        print("The Conversion from %d Kelvin to Fahrenheit is"%(kel),fah)

    #Conversion From Fahrenheit to Kelvin 
        
    elif((option).lower() =="f"):
        print("Please enter Fahrenheit to Convert to Kelvin")
        fah = float(input(""))
        kel = temp.Fahrenheit_To_Kelvin(fah)
        print("The Conversion from %d Fahrenheit to kelvin is"%(fah),kel)
        
        
        
        
        
""""
>>> 
= RESTART: C:/STUDY/Python_Practice_Projects/Temperature_Conversin_Scale.py =
Please Select Options for conversion: 
 a. C to Fah 
b. Fah to C 
c. C to Kel 
d. Kel to C 
e. K to Fah
f. Fah to K 
a
Please enter Celcius to Convert
0
The Conversion from 0 Celcius to Fahrenheit is 32.0
----------------------------------------------------------------------------------
>>> 
= RESTART: C:/STUDY/Python_Practice_Projects/Temperature_Conversin_Scale.py =
Please Select Options for conversion: 
 a. C to Fah 
b. Fah to C 
c. C to Kel 
d. Kel to C 
e. K to Fah
f. Fah to K 
a
Please enter Celcius to Convert
57
The Conversion from 57 Celcius to Fahrenheit is 134.60000000000002
-----------------------------------------------------------------------------------
>>> 
= RESTART: C:/STUDY/Python_Practice_Projects/Temperature_Conversin_Scale.py =
Please Select Options for conversion: 
a. C to Fah 
b. Fah to C 
c. C to Kel 
d. Kel to C 
e. K to Fah
f. Fah to K 
b
Please enter Fahrenheit to Convert
100
The Conversion from 100 Fahrenheit to Celcius  is 37.77777777777778
----------------------------------------------------------------------------------
>>> 
= RESTART: C:/STUDY/Python_Practice_Projects/Temperature_Conversin_Scale.py =
Please Select Options for conversion: 
a. C to Fah 
b. Fah to C 
c. C to Kel 
d. Kel to C 
e. K to Fah
f. Fah to K 
c
Please enter Celcius to Convert to Kelvin
0
The Conversion from 0 Celcius to Kelvin is 273.0
----------------------------------------------------------------------------------
= RESTART: C:/STUDY/Python_Practice_Projects/Temperature_Conversin_Scale.py =
Please Select Options for conversion: 
a. C to Fah 
b. Fah to C 
c. C to Kel 
d. Kel to C 
e. K to Fah
f. Fah to K 
d
Please enter Kelvin to Convert to Celcius
273
The Conversion from 273 Celcius to Fahrenheit is 241.0
----------------------------------------------------------------------------------
>>> 
= RESTART: C:/STUDY/Python_Practice_Projects/Temperature_Conversin_Scale.py =
Please Select Options for conversion: 
a. C to Fah 
b. Fah to C 
c. C to Kel 
d. Kel to C 
e. K to Fah
f. Fah to K 
d
Please enter Kelvin to Convert to Celcius
273
The Conversion from 273 kelvin to celcius is 0.0
----------------------------------------------------------------------------------
>>> 
= RESTART: C:/STUDY/Python_Practice_Projects/Temperature_Conversin_Scale.py =
Please Select Options for conversion: 
a. C to Fah 
b. Fah to C 
c. C to Kel 
d. Kel to C 
e. K to Fah
f. Fah to K 
e
Please enter Kelvin to Convert
273
The Conversion from 273 Kelvin to Fahrenheit is 32.0
----------------------------------------------------------------------------------
>>> 
= RESTART: C:/STUDY/Python_Practice_Projects/Temperature_Conversin_Scale.py =
Please Select Options for conversion: 
a. C to Fah 
b. Fah to C 
c. C to Kel 
d. Kel to C 
e. K to Fah
f. Fah to K 
f
Please enter Fahrenheit to Convert to Kelvin
32
The Conversion from 32 Fahrenheit to kelvin is 273.0
----------------------------------------------------------------------------------
>>> 
= RESTART: C:/STUDY/Python_Practice_Projects/Temperature_Conversin_Scale.py =
Please Select Options for conversion: 
a. C to Fah 
b. Fah to C 
c. C to Kel 
d. Kel to C 
e. K to Fah
f. Fah to K 
Please Enter input to proceed :a
Please enter Celcius to Convert to Fahrenheit
100
The Conversion from 100 degree Celcius to Fahrenheit is 212.0

"""
