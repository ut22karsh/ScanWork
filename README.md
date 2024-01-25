# Scanwork - Network Mapping Tool

## Overview

Scanwork is a Python-based network mapping tool designed for discovering devices on a network. It utilizes ARP scanning to identify IP and MAC addresses of connected devices, providing a quick and efficient way to conduct network reconnaissance.

## Features

- **ARP Scanning:** Utilizes Address Resolution Protocol (ARP) requests to map IP and MAC addresses on the network.
- **Python and Scapy:** Developed in Python, leveraging the Scapy library for crafting and sending network packets.
- **Command Line Interface (CLI):** User-friendly CLI for easy operation and customization.
- **Network Security:** Provides a tool for network administrators and security professionals to perform quick and reliable device mapping.

### Installation

Ensure that Python and the Scapy library are installed on your system.

```bash
pip install scapy
```

### Running Scanwork

Run the tool from the command line, specifying the target IP address or IP range.

```bash
python scanwork.py -t 192.168.1.1/24
```

Replace `192.168.1.1/24` with the desired target IP address or range.

### Output

Scanwork will display a list of discovered devices, including their IP and MAC addresses.

```
IP Address       MAC Address
-----------------------------------------
192.168.1.1      00:1a:2b:3c:4d:5e
192.168.1.2      00:2a:3b:4c:5d:6e
...

```

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Author
- Utkarsh Pandey
- linkedin.com/in/ut22karsh
