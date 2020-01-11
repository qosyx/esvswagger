import socket
import os
import time
def ping():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))
    s.setblocking(False)
    local_ip_address = s.getsockname()[0]
    response = os.system("ping -c 1 " + local_ip_address)
    return local_ip_address

if __name__ == "__main__":
    start_time = time.time()
    while (start_time>=0):
        if (start_time-time.time())==25:
            ping.ping()
            start_time=time.time()


