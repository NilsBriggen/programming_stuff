import prime_gen, time, matplotlib.pyplot as plt, os, numpy as np
from sympy import factorint

#Change these settings to customize the test
BATCHSIZE = 100
STARTSIZE = 99
ACCURACY = 2

#Clear Terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#Alternativ for Phi function
def factors(n):
        print(n)
        factor = factorint(n)
        result = n
        for number, multiplicator in factor:
            print(number, "\n", multiplicator)
            final_factor = number*multiplicator
            result = result * (1-final_factor**-1)
        return result

#Public key generator
def pub_key_gen(x):
    global p, q
    p, q = prime_gen.main(x), prime_gen.main(x)
    n = p*q
    e = prime_gen.main(x)
    phi_n = factors(n)
    while e > phi_n:
        e = prime_gen.main(x)

#Private key generator
def priv_key_gen():
    pass

#Text encryption
def encrypt():
    pass

#Text decryption
def decrypt():
    pass

#calculates the average
def average():
    for item in range(0, (BATCHSIZE+1)-STARTSIZE):
        temp_eval = []
        for lists in range(0, len(time_plot_lib)):
            temp_eval.append(time_plot_lib[lists][item])
        average_line.append(np.mean(temp_eval))

time_plot_lib = []

x = 0

#Runs the stuff
def run():
    global x
    cls()
    print(f"The test started at {start_time}\nRun{str(x+1)}: Started!")
    time_plot = []
    for key_length in range(STARTSIZE, BATCHSIZE+1):
        start = time.perf_counter()
        pub_key_gen(key_length)
        stop = time.perf_counter()
        time_plot.append(stop-start)
    x += 1
    time_plot_lib.append(time_plot)

#timing all of it
t = time.localtime()
start_time = time.strftime("%H:%M:%S", t)
start_full = time.perf_counter()
for a in range(0, ACCURACY):
    run()
stop_full = time.perf_counter()

cls()
print("All done!\nThe calculation took", round(stop_full-start_full, 2), "seconds to complete.\nThe graph will be opened in a new window.")
timing = np.arange(STARTSIZE, BATCHSIZE+1, 1.0)

decision = input("\nWant to run more?\n Enter a number: ")

while decision != "":
    for a in range(0, int(decision)):
        run()
    decision = input("\nWant to run more?\n Enter a number: ")

indexer = len(time_plot_lib)
average_line = []

average()
counter = 0

#plotting it to the graph
fig, ax = plt.subplots()
for x in time_plot_lib:
    if counter == 0:
        name = "Testing runs"
        label_line, = ax.plot(timing, x, color='blue', label = name, alpha = 0.5)
    else:
        name = "Run "+str(counter)
        ax.plot(timing, x, color='blue', label = name)
    counter += 1

avg_line, = ax.plot(timing, average_line, color = "red", marker = "o", label = "Calculated Average")

ax.set(xlabel='key size', ylabel='time (s)',
       title='Duration of Pub_key_gen()')
ax.grid()
ax.legend([label_line, avg_line], ["Testing runs", "Calculated Average"])

plt.show()



# Write to a file and make a general plotter
# Can run multiple times and will be like a personal BOINC where I can contribute to submit data until it's fairly accurat
# Every run gets directly written to file incase of brake down

#Find out what the fuck is wrong with "alpha = 0.5"