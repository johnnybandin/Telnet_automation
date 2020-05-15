import getpass
import telnetlib

host = 'localhost'
user = input("Enter your username here:")
password = getpass.getpass()

f = open ('myswitches')

for IP in f:
	IP=IP.strip()
	print('Configuring Swtich ' + (IP))
	host = IP 
	tl = telnetlib.Telnet(host)
	tl.read_until(b"Username: ")
	tl.write(user.encode('ascii') + b'\n')
	if password:
		tl.read_until(b"Password: ")
		tl.write(password.encode("ascii") + b"\n")
	tl.write(b"conf t\n")
	for v in range(2,20):
		tl.write(b'vlan ' + str(v).encode('ascii') + b'\n')
		tl.write(b'name Python_vlan_' + str(v).encode('ascii') + b'\n')
	tl.write(b'end\n')
	tl.write(b'exit\n')
my_list = ['CS1', 'CS2', 'AS1']
for device in my_list:
	print('Verifying VLANs on' + (device))
	host = device
	tn = telnetlib.Telnet(host)
	tn.read_until(b'Username:')
	tn.write(user.encode('ascii') + b'\n')
	if password:
		tn.read_until(b'Password:')
		tn.write(password.encode('ascii') + b'\n')
	filename = 'vlan_verify.txt'
	output = tn.write(b"show vlan brief\n")
	with open(filename, 'w') as file_object:
		file_object.write(b'show vlan brief\n')
	tn.write(b'exit\n')

print(tl.read_all().decode('ascii'))