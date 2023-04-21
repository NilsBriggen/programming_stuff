from rotor import Rotor
import os

rotor = Rotor()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

available_rotors = [1, 2, 3, 4, 5]
chosen_rotors = []

def checker(rotor_num):
    while rotor_num.isdigit():
        while int(rotor_num) in available_rotors:
            while int(rotor_num) not in chosen_rotors:
                return int(rotor_num)
            else:
                return False
        else:
            return False
    else:
        return False

def checker2(rotor_start):
    while rotor_start.isdigit():
        return int(rotor_start)
    else:
        return False

while True:
    cls()

    rotor1=input(f"Choose Rotor 1#\nYou can choose from{available_rotors}\n")
    rotor1 = checker(rotor1)
    while rotor1 == False:
        rotor1=input(f"Something went wrong! Please retry\nChoose Rotor 1#\nYou can choose from{available_rotors}\n")
        rotor1=checker(rotor1)
    
    chosen_rotors.append(rotor1)
    available_rotors.remove(rotor1)
    cls()

    rotor2=input(f"Choose Rotor 2#\nYou can choose from{available_rotors}\n")
    rotor2 = checker(rotor2)
    while rotor2 == False:
        rotor2=input("Something went wrong! Please retry\nChoose Rotor 2#\nYou can choose from{available_rotors}\n")
        rotor2=checker(rotor2)

    chosen_rotors.append(rotor2)
    available_rotors.remove(rotor2)
    cls()

    rotor3=input(f"Choose Rotor 3#\nYou can choose from{available_rotors}\n")
    rotor3 = checker(rotor3)
    while rotor3 == False:
        rotor3=input("Something went wrong! Please retry\nChoose Rotor 3#\nYou can choose from{available_rotors}\n")
        rotor3=checker(rotor3)

    chosen_rotors.append(rotor3)
    available_rotors.remove(rotor3)
    cls()

    print(f"You have chosen:{chosen_rotors}")
    
    rotor_start1 = input("Insert the starting position of your rotors as a number\n First Rotor: ")
    rotor_start1=checker(rotor_start1)
    while rotor_start1==False:
        rotor_start1 = input("Insert the starting position of your rotors\n First Rotor: ")
        rotor_start1=checker(rotor_start1)

    rotor_start2 = input("Insert the starting position of your rotors as a number\n First Rotor: ")
    rotor_start2=checker(rotor_start2)
    while rotor_start2==False:
        rotor_start2 = input("Insert the starting position of your rotors\n First Rotor: ")
        rotor_start2=checker(rotor_start2)

    rotor_start3 = input("Insert the starting position of your rotors as a number\n First Rotor: ")
    rotor_start3=checker(rotor_start3)
    while rotor_start3==False:
        rotor_start3 = input("Insert the starting position of your rotors\n First Rotor: ")
        rotor_start3=checker(rotor_start3)
    rotor_tuple = (rotor_start1, rotor_start2, rotor_start3)
    rotor.set_rotors(chosen_rotors, rotor_tuple)