import subprocess           # To run cmd commands
import re                   # For regular expressions & patterns

# Accept the IP Addresses to be scanned from the user
first_ip = input("Enter the first IP Address: ")
last_ip = input("Enter the last IP Address: ")

# Function to separate network and host from the IP Address
def get_host(ip_address):
    dot_count = 0
    position = 0
    for j in ip_address:
        if j == '.':
            dot_count += 1
        if dot_count == 3:      # Host comes after the 3rd dot
            return ip_address[:position + 1], ip_address[position + 1:]
        position += 1


network, first_host = get_host(first_ip)
network, last_host = get_host(last_ip)

print("\nScanning IPs...\n")

# For loop to scan through each of the hosts between first and last IP addresses
for i in range(int(first_host), int(last_host) + 1):
    response = subprocess.getoutput("ping -n 1 " + network + str(i))    # Get the response of ping command in cmd
    pattern = re.compile(r"TTL=")
    match = pattern.search(response)            # Search for the pattern in response

    try:
        if match.group() == "TTL=":
            print("HOST " + network + str(i) + " is UP")
    except AttributeError:                      # If no matching string an exception is raised
        print("HOST " + network + str(i) + " is DOWN")

print("\nScanning is completed")
