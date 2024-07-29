# Malicious Attack Tool

Malicious Attack is a command-line tool designed for beginners in the field of cybersecurity. It allows users to execute basic attacks on Wi-Fi networks, providing an educational and practical experience without the need for writing complex commands.

## Features

- **Select Wireless Interface**: Scans and lists available wireless interfaces for user selection.
- **Simple Menu**: Provides a clear and easy-to-use menu with options for different operations.
- **Enable Monitor Mode**: Automatically enables monitor mode on the selected wireless interface.
- **Scan Wireless Networks**: Scans nearby Wi-Fi networks and displays their BSSID, channel, and ESSID.
- **Deauthentication Attack**: Allows users to execute a deauthentication attack on a selected Wi-Fi network.
- **Run Wifite**: Runs the Wifite tool to scan networks and attempt to obtain Wi-Fi passwords and WPS pins.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/malicious-attack.git
    ```
2. Change into the directory:
    ```bash
    cd malicious-attack
    ```
3. Ensure you have the necessary tools installed (e.g., `airmon-ng`, `airodump-ng`, `aireplay-ng`, `wifite`).

## Usage

Run the tool with:
```bash
python3 malicious_attack.py

You will be presented with a menu to select from the following options:


                             Menu
[1] Scanner Wifi (Airodump-ng).
[2] Get password Wifi and WPS pin (Wifite).
[3] Deauth Attack in wifi (Aireplay-ng).
[4] Exit


Follow the prompts to select your desired operation.

Code Structure


malicious_attack.py: Main script that runs the tool.
data.json: File to store persistent data.
Example
Selecting a Wireless Interface
The tool scans for available wireless interfaces and allows you to select one:


Select your Interface:
[0]- wlan0
[1]- wlan1
[+] 0
Wireless selected is: wlan0



Enabling Monitor Mode and Scanning

The tool enables monitor mode and starts scanning for Wi-Fi networks:

Monitor mode enabled successfully.
Scanner Started...


Deauthentication Attack
The tool allows you to execute a deauthentication attack on a selected Wi-Fi network:

Select your Wi-Fi:
+----+-------------------+---------+------------+
| ID | BSSID             | Channel | ESSID      |
+----+-------------------+---------+------------+
| 0  | 00:14:6C:7E:40:80 | 6       | ExampleNet |
+----+-------------------+---------+------------+
Entry ID: 0
Attack Deauth start

Disclaimer

This tool is intended for educational purposes only. Unauthorized use of this tool to attack networks without permission is illegal and unethical. Use responsibly and always ensure you have permission to test any network you do not own.



This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to fork, contribute, or open issues for any bugs or feature requests!


