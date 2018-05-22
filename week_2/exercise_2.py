ip_address_list = ['4.2.2.1','4.2.2.2','8.8.8.8','8.8.4.4','9.9.9.9']
ip_address_list.append('1.1.1.1')
ip_address_list.extend(['4.2.2.3','4.2.2.4'])
ip_address_list = ip_address_list + ['75.75.75.75','75.75.76.76']
print(ip_address_list)
print(ip_address_list[0])
print(ip_address_list[-1])
ip_address_list.pop(0)
ip_address_list.pop(-1)
print(ip_address_list)
ip_address_list[0] = '2.2.2.2'
print(ip_address_list[0])