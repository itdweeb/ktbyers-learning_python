show_version = '*0        CISCO881-SEC-K9        FTX0000038X    '
strip_show_version = show_version.strip()
split_strip_show_version = strip_show_version.split()

print('Cisco'.lower() in split_strip_show_version[1].lower())
print('881' in split_strip_show_version[1])
print("{}{}{}".format(split_strip_show_version[1],'\n',split_strip_show_version[2]))