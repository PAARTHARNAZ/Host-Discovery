import os
import subprocess

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
ip = "192.168.199.136"

# ASCII art for "Ping Prowler"
ascii_art = """

\033[89m
██████╗ ██╗███╗   ██╗ ██████╗                              
██╔══██╗██║████╗  ██║██╔════╝                              
██████╔╝██║██╔██╗ ██║██║  ███╗                             
██╔═══╝ ██║██║╚██╗██║██║   ██║                             
██║     ██║██║ ╚████║╚██████╔╝                             
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝                              
                                                           
██████╗ ██████╗  ██████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██║    ██║██║     ██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║██║ █╗ ██║██║     █████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║██║███╗██║██║     ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝╚███╔███╔╝███████╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝ 
\033[0m

"""

# Function to perform ARP Ping Scan
def arp_ping_scan():
    clear_screen()
    print("\033[96mPerforming ARP Ping Scan...\033[0m")
    subprocess.call(["arping", "-c", "3", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform ICMP Echo Ping Scan
def icmp_echo_ping_scan():
    clear_screen()
    print("\033[96mPerforming ICMP Echo Ping Scan...\033[0m")
    subprocess.call(["ping", "-c", "3", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform ICMP Echo Ping Sweep
def icmp_echo_ping_sweep():
    clear_screen()
    print("\033[96mPerforming ICMP Echo Ping Sweep...\033[0m")
    subprocess.call(["nmap", "-PE", "-sn", "192.168.1.0/24"])  # Example subnet, change as needed
    input("\nPress Enter to continue...")

# Function to perform ICMP Timestamp Ping Scan
def icmp_timestamp_ping_scan():
    clear_screen()
    print("\033[96mPerforming ICMP Timestamp Ping Scan...\033[0m")
    subprocess.call(["hping3", "-1", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform ICMP Address Mask Ping Scan
def icmp_address_mask_ping_scan():
    clear_screen()
    print("\033[96mPerforming ICMP Address Mask Ping Scan...\033[0m")
    subprocess.call(["hping3", "--icmp-ts", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform UDP Ping Scan
def udp_ping_scan():
    clear_screen()
    print("\033[96mPerforming UDP Ping Scan...\033[0m")
    subprocess.call(["nmap", "-sU", "-p", "53", ip])  # Example IP and port, change as needed
    input("\nPress Enter to continue...")

# Function to perform TCP Ping Scan
def tcp_ping_scan():
    clear_screen()
    print("\033[96mPerforming TCP Ping Scan...\033[0m")
    subprocess.call(["nmap", "-sT", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform TCP SYN Scan
def tcp_syn_scan():
    clear_screen()
    print("\033[96mPerforming TCP SYN Scan...\033[0m")
    subprocess.call(["nmap", "-sS", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform TCP Ack Scan
def tcp_ack_scan():
    clear_screen()
    print("\033[96mPerforming TCP Ack Scan...\033[0m")
    subprocess.call(["nmap", "-sA", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform TCP Null Scan
def tcp_null_scan():
    clear_screen()
    print("\033[96mPerforming TCP Null Scan...\033[0m")
    subprocess.call(["nmap", "-sN", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform TCP XMAS Scan
def tcp_xmas_scan():
    clear_screen()
    print("\033[96mPerforming TCP XMAS Scan...\033[0m")
    subprocess.call(["nmap", "-sX", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform TCP FIN Scan
def tcp_fin_scan():
    clear_screen()
    print("\033[96mPerforming TCP FIN Scan...\033[0m")
    subprocess.call(["nmap", "-sF", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Function to perform IP Protocol Ping Scan
def ip_protocol_ping_scan():
    clear_screen()
    print("\033[96mPerforming IP Protocol Ping Scan...\033[0m")
    subprocess.call(["nmap", "-sO", ip])  # Example IP, change as needed
    input("\nPress Enter to continue...")

# Main function to display menu and handle user input
def main():
    while True:
        clear_screen()
        print(ascii_art)
        print("1. \033[94mARP Ping Scan\033[0m")
        print("2. \033[94mICMP Ping Scan\033[0m")
        print("3. \033[94mUDP Ping Scan\033[0m")
        print("4. \033[94mTCP Ping Scan\033[0m")
        print("5. \033[94mIP Protocol Ping Scan\033[0m")
        print("6. \033[91mExit\033[0m")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            arp_ping_scan()
        elif choice == '2':
            while True:
                clear_screen()
                print("\033[95mICMP Ping Scan Options:\033[0m")
                print("1. \033[94mICMP Echo Ping\033[0m")
                print("2. \033[94mICMP Echo Ping Sweep\033[0m")
                print("3. \033[94mICMP Timestamp Ping\033[0m")
                print("4. \033[94mICMP Address Mask Ping\033[0m")
                print("5. \033[91mBack to main menu\033[0m")

                icmp_choice = input("\nEnter your choice: ")

                if icmp_choice == '1':
                    icmp_echo_ping_scan()
                elif icmp_choice == '2':
                    icmp_echo_ping_sweep()
                elif icmp_choice == '3':
                    icmp_timestamp_ping_scan()
                elif icmp_choice == '4':
                    icmp_address_mask_ping_scan()
                elif icmp_choice == '5':
                    break
                else:
                    input("\nInvalid choice! Press Enter to continue...")
        elif choice == '3':
            udp_ping_scan()
        elif choice == '4':
            while True:
                clear_screen()
                print("\033[95mTCP Ping Scan Options:\033[0m")
                print("1. \033[94mTCP SYN Scan\033[0m")
                print("2. \033[94mTCP Ack Scan\033[0m")
                print("3. \033[94mTCP Null Scan\033[0m")
                print("4. \033[94mTCP XMAS Scan\033[0m")
                print("5. \033[94mTCP FIN Scan\033[0m")
                print("6. \033[91mBack to main menu\033[0m")

                tcp_choice = input("\nEnter your choice: ")

                if tcp_choice == '1':
                    tcp_syn_scan()
                elif tcp_choice == '2':
                    tcp_ack_scan()
                elif tcp_choice == '3':
                    tcp_null_scan()
                elif tcp_choice == '4':
                    tcp_xmas_scan()
                elif tcp_choice == '5':
                    tcp_fin_scan()
                elif tcp_choice == '6':
                    break
                else:
                    input("\nInvalid choice! Press Enter to continue...")
        elif choice == '5':
            ip_protocol_ping_scan()
        elif choice == '6':
            clear_screen()
            print("\033[91mExiting...\033[0m")
            break
        else:
            input("\nInvalid choice! Press Enter to continue...")

if __name__ == "__main__":
    main()
