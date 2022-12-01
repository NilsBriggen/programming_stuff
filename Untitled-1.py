import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

Zahl1 = float(input("geben sie hier die erste Zahl ein: "))

Zahl2 = float(input("geben sie hier die zweite Zahl ein: "))

print ("Die Summe der Zahlen ist: ", add(Zahl1, Zahl2))
print ("Die Differenz der Zahlen ist: ", subtract(Zahl1, Zahl2))
print ("Das Produkt der Zahlen ist: ",multiply(Zahl1, Zahl2))
print ("Der Quotiontenwert ist: ", divide(Zahl1, Zahl2))
print ("Die Wurzel aus der ersten Zahl ist: ", math.sqrt(Zahl1))
print ("Die Wurzel aus der zweiten Zahl ist: ", math.sqrt(Zahl2))
print ("Die erste Zahl hoch die zweite Zahl ist: ", power(Zahl1, Zahl2))
print ("Thanks for using this tool, have a great day!")