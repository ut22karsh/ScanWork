import scapy.all as scapy
import argparse
from termcolor import colored,cprint

logo = '''
  _________                    __      __             __    
 /   _____/ ____ _____    ____/  \    /  \___________|  | __
 \_____  \_/ ___\\__  \  /    \   \/\/   /  _ \_  __ \  |/ /
 /        \  \___ / __ \|   |  \        (  <_> )  | \/    < 
/_______  /\___  >____  /___|  /\__/\  / \____/|__|  |__|_ \.
        \/     \/     \/     \/      \/                   \/
                  
                  '''

cprint(logo,'blue',attrs=['bold'])

cprint('\n{}*** Programmed by Utkarsh Pandey ***','green',attrs=['bold'])


def get_arguments():
    parser = argparse.ArgumentParser(description="Network Mapper Tool")
    parser.add_argument("-t", "--target", dest="target", help="Target IP address or IP range")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target IP address or IP range. Use --help for more information.")
    return options

def scan(ip):
    # Create an ARP request packet
    arp_request = scapy.ARP(pdst=ip)

    # Create an Ethernet frame to encapsulate the ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine the Ethernet frame and ARP request
    arp_request_broadcast = broadcast/arp_request

    # Send the packet and receive the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # List to store the results
    clients_list = []

    # Process the response
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list

def print_result(results_list):
    print("IP Address\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

def main():
    options = get_arguments()
    target_ip = options.target
    scan_result = scan(target_ip)
    print_result(scan_result)

if __name__ == "__main__":
    main()
