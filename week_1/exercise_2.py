ip_addr = input("Please enter an IP address: ")
print("\n")
ip_addr_split = ip_addr.split(".")
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1","Octet2","Octet3","Octet4"))
print("-" * 80)
print("{:^15}{:^15}{:^15}{:^15}".format(ip_addr_split[0],ip_addr_split[1],ip_addr_split[2],ip_addr_split[3]))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(ip_addr_split[0],10)),bin(int(ip_addr_split[1],10)),bin(int(ip_addr_split[2],10)),bin(int(ip_addr_split[3],10))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(ip_addr_split[0],10)),hex(int(ip_addr_split[1],10)),hex(int(ip_addr_split[2],10)),hex(int(ip_addr_split[3],10))))
print("-" * 80)
