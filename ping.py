"""
Ping Internet Program 
---------------------
2023-11-07
"""
import os
import socket
import urllib.request

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
public_ip = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
package_send = 500
file_name = "temp_ping_data.dat"


def default_geteway():
    
    # one time run
    if os.path.exists(file_name):
        pass
    else:
        os.system(f"ipconfig /all >>{file_name}")

    with open(f"{file_name}", mode="rb") as file:
        data = file.readlines()

        for i in data:
            if i.strip().startswith(b"DHCP Server", ):
                #print(i)
                ip = i[-13:-2]
    return ip.decode("ASCII")


def delete_file():
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        pass

if __name__ == "__main__":
    print(f"""
                ************
        Your Computer Name: {host_name}
        Private Ip Address: {ip_address}
        Public Ip Address: {public_ip}
                ************

          Welcome To My Ping Program
                -------------
          1. Ping Network Default Gateway
          2. Ping Google
          3. Manual Package
          4. Crt + C (Exit Program)
                
""")

    user = int(input("Enter option: "))
    if user == 1:
        os.system(f"ping -t -l {package_send} {default_geteway()}")
        delete_file()
    if user == 2:
        os.system(f"ping -t -l {package_send} www.google.com")
    elif user == 3:
        amount = int(input("Enter package(eg.500):"))
        package_send = amount
        os.system(f"ping -t -l {package_send} {default_geteway()}")
        delete_file()
    else:
        exit(0)
