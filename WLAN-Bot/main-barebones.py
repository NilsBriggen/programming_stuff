from subprocess import PIPE, Popen

latency = 0
down = 0
up = 0

subprocess_return = str(
    Popen("./speedtest.exe", shell=False, stdout=PIPE).stdout.read()
)

latency_pos = subprocess_return.find("Latency:")
down_pos = subprocess_return.find("Download:")
up_pos = subprocess_return.find("Upload:")
latency = float(subprocess_return[latency_pos + 9 : latency_pos + 18].strip())
down = float(subprocess_return[down_pos + 10 : down_pos + 19].strip())
up = float(subprocess_return[up_pos + 8 : up_pos + 17].strip())
if latency_pos == -1:
    latency = 0
if down_pos == -1:
    down = 0
if up_pos == -1:
    up = 0
print(f"Ping: {latency}ms\nDownload: {down} Mbps\nUpload: {up} Mbps\n\n")
