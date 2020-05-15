import getpass
import telnetlib

# Set host parameters
host = 'CS1'
user = input('Enter your telnet username:')
password = getpass.getpass()

# Create variable for telnet host
tn = telnetlib.Telnet(host)

# Logon to network device
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b'\n')
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b'\n')

# Configure commands
tn.write(b'conf t\n')

# Use a for loop to create vlans
for v in range(2, 12):
	tn.write(b"vlan "+ str(v).encode('ascii') + b"\n")
	tn.write(b"name Python_vlan_" + str(v).encode('ascii') + b"\n")
tn.write(b"end\n")
output = tn.write(b"show vlan brief\n")
filename = 'vlan_brief.txt'
with open(filename, 'w') as file_object:
	file_object.write(str(output))
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))
