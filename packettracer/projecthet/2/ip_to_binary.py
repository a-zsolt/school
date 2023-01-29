#Andorko Zsolt

count = int(input("How many ip's do you want to convert to binary?: "))

# Get the ip from the user
ip = []
while count > 0:

    ip.append(input("Enter the ip you want to convert to binary: "))

    count -= 1

# Convert the ip to binary
for x in ip:
    print("--------------------------------------------")
    print(x + "\n")
    
    x = x.replace(".", "")

    ipbin = bin(int(x)).replace("0b", "")
    iphex = hex(int(x)).replace("0x", "").upper()

    print(ipbin + "\n")
    print(iphex)
