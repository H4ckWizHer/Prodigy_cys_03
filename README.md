A network packet sniffer/analyzer tool

Ethical Packet Sniffer Tool

Overview:
The Ethical Packet Sniffer Tool is a Python-based utility designed for educational purposes to capture and analyze network packets. It leverages the powerful Scapy library to decode packets and provide insights into network traffic. This tool is intended for use in controlled environments where the user has explicit permission to capture and analyze network traffic, promoting ethical hacking practices.

Features:

Capture Network Packets:      Listens on a specified network interface and captures packets transmitted over the network.
Analyze Packets:              Provides options to analyze captured packets, offering details such as IP addresses, protocols, and payload data.
User-Friendly Interface:      Easy-to-navigate command-line interface for capturing and analyzing packets.
Ethical Use Reminder:         Emphasizes the importance of using the tool responsibly in permitted network environments.

Installation:
Prerequisites:
. Python 3.x
. Scapy
Before you begin, ensure you have Python installed on your system. This tool also requires the Scapy library, which can be installed using pip:
pip install scapy

Dependencies:
The tool relies on the Scapy library, a powerful packet manipulation tool. It's used for packet crafting and sniffing in this project.
from scapy.all import *

Setup:
Clone this repository to your local machine:
git clone https://github.com/H4ckWizHer/ethical-packet-sniffer.git
cd ethical-packet-sniffer

Usage:
Run the tool from the command line:
python packet_sniffer.py

Follow the on-screen prompts to either capture packets or analyze previously captured packets. When capturing packets, you will need to specify the network interface (e.g., eth0, wlan0) on which the tool should listen

How It Works:
The tool operates in two main modes:

. Capture Mode:     Sniffs packets on a specified network interface, leveraging the Scapy library's sniff function. Captured packets are stored in a global list for later analysis.

. Analysis Mode:    Allows the user to analyze the captured packets. Users can choose to view IP addresses, protocols, payload data, or all available information about each packet.

Contributing:
Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or add new features.

License:
This project is licensed under the MIT License - see the LICENSE file for details.


