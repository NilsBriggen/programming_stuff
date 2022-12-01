numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbersc =  []
counter = 0
numbersstorage = []

def calculator():
    for i in range(10000, 99999):
        numbersc.append(i)
    
    print(numbersc, "\n\n\n\n\n")
    
    global counter, counter_2, counter_char, numbersstorage
    while counter > 100000:
        numbersstorage = [] 
        numberstemp = []
        numberstemp2 = [] 
        counter_char = 0
        counter_2 = 0
        final_number = 0
        for char in numbers:
            if char in numbersc[counter]:
                numberstemp.append(char)
                numberstemp
                while counter_char >= 5:
                    numberstemp2.append(numberstemp[counter_char]**5)
                    print(numberstemp2)
                    while counter_2 >= 5:
                        final_number += numberstemp2[counter_2]
                        print(final_number)
                        if final_number == numbersc[counter]:
                            numbersstorage.append(final_number)
                        counter_2 += 1
                    counter_char += 1
                counter += 1
                
calculator()
print (numbersstorage)
