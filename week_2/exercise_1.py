file = open("show_version.txt")
show_version = file.read()
file.close()
print(type(show_version))
print(show_version)

with open("show_version.txt") as file_2:
    show_version_2 = file_2.readlines()
print(type(show_version_2))
print(show_version_2)