with open("show_ip_bgp_summ.txt") as file:
    bgp = file.readlines()
bgp_1 = bgp[0]
bgp_2 = bgp[-1]
bgp_1 = bgp_1.split()
bgp_2 = bgp_2.split()
as_number = bgp_1[-1]
ip_address = bgp_2[0]
print(as_number,ip_address)