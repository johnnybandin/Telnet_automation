import getpass
import telnetlib

# Set host parameters
host = 'R1'
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
tn.write(b'no int loop 0\n')
tn.write(b'int loop 0\n')
tn.write(b'ip address 1.1.1.1 255.255.255.0\n')
tn.write(b'end\n')
tn.write(b'exit\n')

print(tn.read_all().decode('ascii'))