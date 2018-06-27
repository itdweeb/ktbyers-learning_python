from pprint import pprint

vlan_list = []
with open("show_vlan.txt") as f:
    vlan_info = f.read()

for line in vlan_info.splitlines():
    if 'VLAN' in line or '---' in line or line.startswith('  '):
        continue
    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan_id, vlan_name))

print()
pprint(vlan_list)
print()