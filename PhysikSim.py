from matplotlib import pyplot as plt

#Konstanten
G = 9.81 #Erdbeschleunigung
t = 0 #Zeit in Sekunden
x = 10**4 #Anfangsposition in m
v = 0 #Anfangsgeschwindigkeit in m/s
k = 0.35
DELTA_T = 0.001 #Zeitschritt in Sekunden
M=80

a = -G

x_results = [] #Liste für x-Werte
v_results = [] #Liste für v-Werte
counter = 0
for i in range(60*int((1/DELTA_T))):
    counter +=1
    if x <= 6000:
        k = 3
    t_new=t+1
    v_new = a*DELTA_T+v
    x_new = v*DELTA_T+x
    a_new = -G+(k/M)*v**2

    t=t_new
    v=v_new
    x=x_new
    a=a_new

    if x <= 0:
        x = 0
        print("Schlägt auf dem Boden auf nach",i*DELTA_T,"Sekunden mit einer Geschwindigkeit von",round(abs(v), 2),"m/s")
        x_results.append(x)
        v_results.append(0)
        break
    x_results.append(x)
    v_results.append(abs(v))
    
#make graph
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 6))

ax[0].plot(range(int(counter)), x_results, label='x(t)')
ax[1].plot(range(int(counter)), v_results, label='v(t)')
ax[0].set_xlabel('t in s')
ax[1].set_xlabel('t in s')
ax[0].set_ylabel('x in m')
ax[1].set_ylabel('v in m/s')
ax[0].grid()
ax[1].grid()
ax[0].legend()
ax[1].legend()

plt.show()