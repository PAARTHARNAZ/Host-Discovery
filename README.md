# Ping Prowler

This Python project provides a set of network scanning tools to perform various types of host discovery and ping scans using different protocols. The available scans include ARP Ping, ICMP Echo, UDP, TCP, and IP Protocol scans. The project leverages external tools like `nmap`, `hping3`, and `arping` to execute these scans.

## Features

- **ARP Ping Scan**
- **ICMP Ping Scans**
  - ICMP Echo Ping
  - ICMP Echo Ping Sweep
  - ICMP Timestamp Ping
  - ICMP Address Mask Ping
- **UDP Ping Scan**
- **TCP Ping Scans**
  - TCP SYN Scan
  - TCP ACK Scan
  - TCP Null Scan
  - TCP XMAS Scan
  - TCP FIN Scan
- **IP Protocol Ping Scan**

## Prerequisites

Make sure you have the following tools installed on your system:

- `nmap`
- `hping3`
- `arping`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/host-discovery.git
    ```

2. Change into the project directory:

    ```sh
    cd host-discovery
    ```

## Usage

1. Run the main script:

    ```sh
    python main.py
    ```

2. Follow the on-screen menu to choose the type of scan you want to perform.

## Menu Options

1. **ARP Ping Scan**: Perform an ARP ping scan.
2. **ICMP Ping Scan**: Access sub-menu to perform different types of ICMP ping scans.
3. **UDP Ping Scan**: Perform a UDP ping scan.
4. **TCP Ping Scan**: Access sub-menu to perform different types of TCP ping scans.
5. **IP Protocol Ping Scan**: Perform an IP protocol ping scan.
6. **Exit**: Exit the program.

### ICMP Ping Scan Sub-Menu

1. **ICMP Echo Ping**: Perform a standard ICMP echo ping scan.
2. **ICMP Echo Ping Sweep**: Perform an ICMP echo ping sweep over a subnet.
3. **ICMP Timestamp Ping**: Perform an ICMP timestamp ping scan.
4. **ICMP Address Mask Ping**: Perform an ICMP address mask ping scan.
5. **Back to main menu**: Return to the main menu.

### TCP Ping Scan Sub-Menu

1. **TCP SYN Scan**: Perform a TCP SYN scan.
2. **TCP ACK Scan**: Perform a TCP ACK scan.
3. **TCP Null Scan**: Perform a TCP Null scan.
4. **TCP XMAS Scan**: Perform a TCP XMAS scan.
5. **TCP FIN Scan**: Perform a TCP FIN scan.
6. **Back to main menu**: Return to the main menu.

## ASCII Art

The script includes ASCII art that displays "Host Discovery" upon startup.

```python
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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Authors

- **Your Name** - [Your GitHub Profile](https://github.com/yourusername)

Feel free to open issues or submit pull requests for any improvements or bug fixes.

Enjoy discovering hosts!
