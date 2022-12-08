import random
import matplotlib.pyplot as plt

check_list1 = 0
check_list2 = 0
check_list3 = 0
check_list4 = 0
check_list5 = 0
check_list6 = 0
check_list7 = 0
check_list8 = 0
check_list9 = 0
check_list0 = 0

def main(iterations):
    global check_list0, check_list1, check_list2, check_list3, check_list4, check_list5, check_list6, check_list7, check_list8, check_list9
    for i in range(iterations):
        number = random.randint(0, 9)
        if number == 1:
            check_list1 += 1
        elif number == 2:
            check_list2 += 1
        elif number == 3:
            check_list3 += 1
        elif number == 4:
            check_list4 += 1
        elif number == 5:
            check_list5 += 1
        elif number == 6:
            check_list6 += 1
        elif number == 7:
            check_list7 += 1
        elif number == 8:
            check_list8 += 1
        elif number == 9:
            check_list9 += 1
        elif number == 0:
            check_list0 += 1
        check_list = [check_list0, check_list1, check_list2, check_list3, check_list4, check_list5, check_list6, check_list7, check_list8, check_list9]
    
        # creating the bar plot
        counter = 0
        for item in check_list:
            counter +=1
            plt.bar(counter, item, color ='maroon', width = 0.4)
            plt.draw()

plt.ion()
fig = plt.figure(figsize = (10, 5))
plt.xlabel("Number")
plt.ylabel("Amount")
plt.title("Random")

main(200)
        