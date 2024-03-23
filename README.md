## Network Packet Sniffer Tool

The Ethical Packet Sniffer Tool is a powerful Python script designed for educational purposes. It enables users to capture and analyze network packets, providing insights into network traffic through IP addresses, protocols, and payload data. This tool is built with a focus on ethical use and user-friendliness.

## Features

- **Real-time Network Packet Capture**:    Seamlessly capture packets over specified network interfaces.
- **Comprehensive Packet Analysis**:       Analyze packets with options to view details like IP addresses, protocols, and payload data.
- **Interactive User Interface**:          A straightforward menu-driven interface for easy operation.
- **Ethical Usage Reminder**:              Includes prompts to ensure users are reminded of ethical considerations.

## Installation

Before you begin, ensure you have Python 3.x installed on your system. Additionally, this tool requires the Scapy library.

### Install Python

Python 3.x is required to run this tool. Download and install it from [Python's official website](https://www.python.org/downloads/).

### Install Scapy

Scapy is a powerful Python library used for packet manipulation. Install it using pip:
pip install scapy

## Usage

Follow these steps to start capturing and analyzing network packets with the Ethical Packet Sniffer Tool.

### Starting the Tool

To launch the tool, navigate to the directory containing the script and run:
python packet_sniffer.py

### Capturing Network Packets

1. From the main menu, choose `1` to start the packet capture process.
2. When prompted, enter the network interface you wish to monitor (e.g., `eth0`, `wlan0`).

### Analyzing Network Packets

1. To analyze the captured packets, select `2` from the main menu.
2. Choose your desired level of detail for packet analysis:
   - `1` for IP Addresses only
   - `2` for Protocol types
   - `3` for Payload data
   - `4` for All above details

### Exiting the Tool

When you're finished, select `3` from the main menu to exit the tool.

## Ethical Considerations

This tool is intended for educational purposes and ethical use only. Users are strongly encouraged to capture and analyze packets only on networks for which they have explicit permission. Unauthorized use may violate privacy laws and ethical standards.

## Contributing

Contributions to improve the Ethical Packet Sniffer Tool are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. For more information, please refer to the LICENSE file in the repository.

---
