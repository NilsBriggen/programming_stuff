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

Pi = input('Brauchst du Pi in deiner Formel? Tippe hier "Y" ein und es wird dir Pi ausgeben damit du es in deiner Formel brauchen kannst. ')

Pi = Pi.lower()

if Pi == "y" or Pi == "yes":
    print(math.pi)

Hoch = input("Geben sie ein ob sie Hoch rechnen möchten. Y or N\n")
Wurzel = input("Geben sie ein ob sie Wurzel rechnen möchten. Y or N\n")

Zahl1 = float(input("geben sie hier die erste Zahl ein: "))

Zahl2 = float(input("geben sie hier die zweite Zahl ein: "))

print ("Die Summe der Zahlen ist: ", add(Zahl1, Zahl2))
print ("Die Differenz der Zahlen ist: ", subtract(Zahl1, Zahl2))
print ("Das Produkt der Zahlen ist: ",multiply(Zahl1, Zahl2))
print ("Der Quotientwert ist: ", divide(Zahl1, Zahl2))

Wurzel = Wurzel.lower()

if Wurzel == "y" or Wurzel == "yes": 
    print ("Die Wurzel aus der ersten Zahl ist: ", math.sqrt(Zahl1))   
    print ("Die Wurzel aus der zweiten Zahl ist: ", math.sqrt(Zahl2))

Hoch = Hoch.lower()

if Hoch == "y" or Hoch == "yes":
    if Zahl1 > 9999999:
        print("Die Zahl die du angegeben hast war zu gross. Du hast das Limit dieses Programms erreicht.")


    elif Zahl2 > 50:
        print("Die 2.Zahl die du angegeben hast war zu gross um sie als Potenz zu gebrauchen. Du hast das Limit dieses Programms erreicht.")

    else:
        print ("Die erste Zahl hoch die zweite Zahl ist: ", power(Zahl1, Zahl2))

print ("Thanks for using this tool. Have a great day!")