import subprocess
import matplotlib.pyplot as plt
from plyer import notification

latency = []; down = []; up = []; reference = []
NUM = 50

def speedtest_org(subprocess, ref):
    global latency, down, up, reference
    debug = ""
    subprocess = subprocess.Popen("./speedtest.exe", shell=False, stdout=subprocess.PIPE)
    subprocess_return = str(subprocess.stdout.read())

    latency_pos = subprocess_return.find("Latency:")
    down_pos = subprocess_return.find("Download:")
    up_pos = subprocess_return.find("Upload:")        
    latency.append(float(subprocess_return[latency_pos+9:latency_pos+18].strip()))
    down.append(float(subprocess_return[down_pos+10:down_pos+19].strip()))
    up.append(float(subprocess_return[up_pos+8:up_pos+17].strip()))
    reference.append(ref-1)
    if latency_pos == -1:
        latency.pop()
        latency.append(0)
        debug = str(subprocess_return[subprocess_return.find("Result URL:"):subprocess_return.find("Result URL:")+75])
        notify(notification, 0, ref, debug)
    if down_pos == -1:
        down.pop()
        down.append(0)
        debug = str(subprocess_return[subprocess_return.find("Result URL:"):subprocess_return.find("Result URL:")+75])
        notify(notification, 0, ref, debug)
    if up_pos == -1:
        up.pop()
        up.append(0)
        debug = str(subprocess_return[subprocess_return.find("Result URL:"):subprocess_return.find("Result URL:")+75])
        notify(notification, 0, ref, debug)
    print(f"Test {ref}:\nPing: {latency[-1]}ms\nDownload: {down[-1]} Mbps\nUpload: {up[-1]} Mbps\n{debug}\n")

def main():
    for i in range(NUM):
        speedtest_org(subprocess, i+1)
            
    plt.plot(reference, latency, color = 'red', label = 'Latency', marker = 'o')
    plt.plot(reference, down, color = 'blue', label = 'Download', marker = 'o')
    plt.plot(reference, up, color = 'green', label = 'Upload', marker = 'o')
    plt.legend()
    plt.title("Results")
    plt.grid(visible=True, axis='both')
    notify(notification, 1, "0", "Test finished")
    print(f"Average Values:\nPing: {round(sum(latency)/len(latency), 2)}\nDownload: {round(sum(down)/len(down), 2)}\nUpload: {round(sum(up)/len(up), 2)}")
    plt.show()

def notify(notification, version, ref, msg):
    if version == 0:
        notification.notify(title = f"Speedtest nr.{ref}", message = f"An error occured. Check it out with the link below\n{msg}", timeout = 30)
    elif version == 1:
        notification.notify(title = msg, message = "", timeout = 30)

main()