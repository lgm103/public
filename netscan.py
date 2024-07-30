#a simple network scanner using scapy

from scapy.all import ARP, Ether, srp


#ip for ARP
target_ip = "10.0.2.1/24" 

#create ARP packet
arp = ARP(pdst=target_ip)

#create broadcast packet

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether/arp

result = srp(packet, timeout=3)[0]

#create a list of clients
clients = []

for sent, received in result:
	#for each response, append IP and MAC to 'clients' list
	clients.append({'ip': received.psrc, 'mac': received.hwsrc})

#print clients
print("Available devices on the network:")
print("IP" + " " *18+"MAC")

for client in clients:
	print("{:16}    {}".format(client['ip'], client['mac']))


