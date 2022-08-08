#!/user/bin/env python3

import subprocess
import optparse
import re


# RETURNS INTERFACE AND NEW MAC ADDRESS FROM COMMANDLINE INPUT
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change MAC address for")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address (eg, 00:11:22:33:44:55)")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info")
    return options


# CHANGE THE MAC ADDRESS
def change_mac(interface, new_mac):
    print("\n[+] Changing MAC address for " + interface + " from " + get_current_mac(interface) + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# RETURNS THE CURRENT MAC ADDRESS FOR A GIVEN INTERFACE
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if search_mac:
        return search_mac.group(0)
    else:
        print("\n[-] Could not read MAC address")
        exit()


# OBTAIN COMMANDLINE ARGUMENTS
options = get_arguments()

# OBTAIN CURRENT MAC ADDRESS
current_mac = get_current_mac(options.interface)

# CHANGES THE MAC ADDRESS
change_mac(options.interface, options.new_mac)

# OBTAIN CURRENT MAC ADDRESS
current_mac = get_current_mac(options.interface)

# CHECKS IF THE MAC WAS CHANGED
if current_mac == options.new_mac:
    print("\n[+] MAC address was successfully changed to " + current_mac)
else:
    print("\n[-] Error, MAC address did not get changed")
