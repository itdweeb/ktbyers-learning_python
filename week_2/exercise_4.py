with open("show_ip_int_brief.txt") as file:
    ip_status = file.readlines()
interface = ip_status[5]
interface = interface.split()
interface_tuple = (interface[0],interface[1])
print(interface_tuple)