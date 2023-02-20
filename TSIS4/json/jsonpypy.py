import json

with open("example_of_dictionary.json", "r") as json_file:
    file = json.load(json_file)


sta = 0
for i in range(len(file['imdata'])):
    if sta == 0:
        print("Interface Status\n================================================================================")
        print("""DN                                                 Description           Speed    MTU
-------------------------------------------------- --------------------  ------  ------""")
        sta += 1
    x = len("                            ")
    z = len("topology/pod-1/node-201/sys/phys-[eth1/33]")
    y = len(file["imdata"][i]["l1PhysIf"]["attributes"]['dn'])
    print(file["imdata"][i]["l1PhysIf"]["attributes"]['dn'], 
        ' '*(x - ( y - z)), file["imdata"][i]["l1PhysIf"]["attributes"]['speed'], ' '*1, file["imdata"][i]["l1PhysIf"]["attributes"]['mtu'])