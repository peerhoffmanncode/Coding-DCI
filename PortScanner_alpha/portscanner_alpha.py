# This should be a simple and easy port scanner
# -- STRUCTURE --
# read a input >IP address<
# read a input >max port for range<
# open a socket to the IP address + port
# scan the >IP address with corresponding port <
# gather information
# print out result

#######################
### code start here ###
#######################

import os  # OS stuff
import socket  # for connecting
from ping3 import ping
from colorama import init, Fore  # for styling consol output
import time

# set some colors for colorama
init()
GREEN = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET

# input function to check correct input


def userinput(message_to_user, shouldbe_text, shouldbe_number):
    while True:
        print(" " * (80-len(message_to_user)))
        print("\r", end="")
        user_input = input("\033[F"+str(message_to_user))
        print("\r", end="")
        if shouldbe_text:
            if user_input.isalpha():
                return user_input
            else:
                print(
                    "\033[FWrong input, should be alphabetical               ", end="\r")
                time.sleep(1)

        if shouldbe_number:
            if user_input.isnumeric():
                return user_input
            else:
                print(
                    "\033[FWrong input, should be numerical                  ", end="\r")
                print("", end="\r")
                time.sleep(1)

# function to ping/ check if a host is alive


def ping_a_host(host):

    return ping(host, timeout=1)

# function to open and probe a tcp port


def is_port_open_tcp(host_ip_address, port_num):

    # creates a new socket, set timeout to 0.20 seconds
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # use TCP port

    s.settimeout(0.20)  # set timeout value

    try:
        # try to connect to host using port
        s.connect((host_ip_address, port_num))
        return "open"

    except ConnectionRefusedError:
        # cannot connect
        s.close()
        return "closed"

    except socket.timeout:
        # cannot connect
        s.close()
        return "filter"

# function to open and probe a udp port


def is_port_open_upd(host_ip_address, port_num):

    # creates a new socket, set timeout to 0.20 seconds
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # use UDP port

    s.settimeout(0.20)  # set timeout value

    try:
        # try to connect to host using port
        bytesToSend = str.encode("udp_dummy_msg")

        # s.connect((host_ip_address, port_num))
        # send dummy data to probe UDP
        s.sendto(bytesToSend, (host_ip_address, port_num))
        data, address = s.recvfrom(1024)
        print(data)
        time.sleep(1)
        s.close()
        if data != None:
            return "open"
        else:
            return False

    except ConnectionRefusedError:
        # cannot connect
        s.close()
        return "closed"

    except socket.timeout:
        # cannot connect
        s.close()
        return "filter"

#################
### MAIN CODE ###
#################


if __name__ == "__main__":

    # clear terminal
    os.system('clear')

    # get the host IP from the user
    host_ip_address = input("Enter the hostname or IP address: ")

    # get the min port number from the user
    first_port = int(userinput(message_to_user="Enter the first port to probe   : ",
                     shouldbe_text=False, shouldbe_number=True))
    if first_port < 1:
        first_port = 1

    # get the max port number from the user
    last_port = int(userinput(message_to_user="Enter the last port to probe    : ",
                    shouldbe_text=False, shouldbe_number=True))
    if last_port < first_port:
        last_port = first_port + 1

    # probe if hostname is alive
    pingtime = ping_a_host(host_ip_address)

    if pingtime:  # is not False:

        print(
            f"{GRAY}[{host_ip_address}] seems alive and responded after [{pingtime:.4f}] seconds")

        # iterate over given ports
        open_tcp_ports_found = 0
        open_udp_ports_found = 0

        for port_num in range(first_port, last_port+1):

            if is_port_open_tcp(host_ip_address, port_num) == "open":
                open_tcp_ports_found = open_tcp_ports_found + 1
                print(
                    f"{GREEN}[+] {host_ip_address}:{port_num} TCP is open                 {RESET}")
            elif is_port_open_tcp(host_ip_address, port_num) == "filter":
                print(
                    f"{YELLOW}[+] {host_ip_address}:{port_num} TCP is filtered            {RESET}")
            else:
                print(
                    f"{GRAY}[!] {host_ip_address}:{port_num} TCP is closed                {RESET}", end="\r")

            if is_port_open_upd(host_ip_address, port_num) == "open":
                open_udp_ports_found = open_udp_ports_found + 1
                print(
                    f"{GREEN}[+] {host_ip_address}:{port_num} UDP is open                 {RESET}")
            # elif is_port_open_upd(host_ip_address, port_num) == "filter":
            #    print(f"{YELLOW}[+] {host_ip_address}:{port_num} UDP is filtered            {RESET}")
            else:
                print(
                    f"{GRAY}[!] {host_ip_address}:{port_num} UDP is closed/filtered       {RESET}", end="\r")

        # print out summary
        print(f"[Open ports found: {open_tcp_ports_found} TCP port(s) and {open_udp_ports_found} UDP port(s) out of {(last_port+1)-first_port} port(s) [{first_port} to {last_port}] on host [{host_ip_address}] \n")

    else:
        # abort, host is not alive!
        print(
            f"{RED}[{host_ip_address}] is DEAD, or not responding to ICMP ping ! \n")
