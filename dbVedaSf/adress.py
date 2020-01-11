import socket
import os
import time
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
def ping():
    Connectpath = path+"/connectParameters.json"
    # local_ip_address = "127.0.0.1"
    # response = os.system("ping -c 1 " + local_ip_address)
    # if(response==0):
    #     Connectpath = path+"/connectParameters.json"
    # else:
    #     Connectpath = path+"/connectParameters1.json"

    return Connectpath

# def ping():
#     Connectpath = path+"/connectParameters.json"
#     # local_ip_address = "127.0.0.1"
#     # response = os.system("ping -c 1 " + local_ip_address)
#     # if(response==0):
#     #     Connectpath = path+"/connectParameters.json"
#     # else:
#     #     Connectpath = path+"/connectParameters1.json"

#     return Connectpath