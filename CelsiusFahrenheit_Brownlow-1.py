#CONVERTING FAHRENHEIT TO CELSIUS

Fahrenheit = float(input("Enter in the temp in Fahrenheit: "))

FToC = (Fahrenheit - 32) * 5/9 #FORMULA TO CONVERT F TO C

#PRINTS OUT CONVERTED TEMP IN CELSIUS
print(Fahrenheit,"fahrenheit to celsius is: ",FToC)

Celsius = float(input("Enter in the temp in Celsius: "))
CToF = Celsius * 9/5 + 32 #FORMULA TO CONVERT C TO F 

#PRINTS OUT CONVERTED TEMP IN FAHRENHEIT 
print(Celsius, "celsius to fahrenheit is: ", CToF)


