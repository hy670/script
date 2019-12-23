

f = open("/Users/mac/Documents/page.log", 'r')
ipaddr = []
for line in f.readlines():
    if "professioninfo" in line:
        if "index.html" not in line:
            if line.split(" ")[0] not in ipaddr:
                ipaddr.append(line.split(" ")[0])
            print(line.strip())
for ip in ipaddr:
    print(ip)






