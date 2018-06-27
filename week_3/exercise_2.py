arp_list = []
jumpout = 0
with open("show_arp.txt") as f:
    arp_info = f.read()

for line in arp_info.splitlines():
    fields = line.split()
    ip_addr = fields[1]
    mac_addr = fields[3]
    if '10.220.88.1' in line:
        print('Default Gateway IP/MAC: ', ip_addr , mac_addr)
        jumpout += 1
    if '10.220.88.30' in line:
        print('Arista3 IP/Mac is: ', ip_addr, mac_addr)
        jumpout += 1
    if jumpout >=2:
        break
    arp_list.append((ip_addr, mac_addr))
