from pprint import pprint

with open("show_arp.txt") as file:
    arp = file.readlines()
arp = arp[1:]
pprint(arp)
arp.sort()

arp_2 = arp[0:3]
print(arp_2)
arp_2 = "\n".join(arp_2)
print(arp_2)

with open("arp_entries.txt", mode="w") as file_2:
    file_2.write(arp_2)
    file_2.flush()
