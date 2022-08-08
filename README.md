# Description
Basic Python script to change the MAC address on Linux machines.

# Usage
mac_changer.py [options]

Options:
  -h, --help            show this help message and exit        
  -i INTERFACE, --interface=INTERFACE
                        interface to change MAC address for    
  -m NEW_MAC, --mac=NEW_MAC
                        new MAC address (eg, 00:11:22:33:44:55)
# Examples
mac_changer.py -i eth0 -m 00:11:22:33:44:55

mac_changer.py --interface wlan0 --mac 00:11:22:33:44:55
