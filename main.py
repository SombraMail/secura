import subprocess

ip = str(input("Enter the IP address you want to scan "))

# 192.168.1.172


def scan(ip, cmd):
    rep = open('report.txt', 'a')
    subprocess.call(f'nmap {cmd} {ip}', stdout=rep)


resp = input("""\nPlease enter the type of scan you want to run
                1)General ports scan
                2)Specific ports scan \n""")
print("You have selected option: ", resp)
if resp == '1':
    file = open('report.txt', 'a')
    file.write('<<<<<<<<<<<<<<<<<<<<<<PORTS REPORT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

    cmd = "-T4 -A"
    scan(ip, cmd)

    cmd = "--reason"
    scan(ip, cmd)

    cmd = "-sU"
    scan(ip, cmd)

    cmd = "-p-"
    scan(ip, cmd)

if resp == '2':
    port = str(input("Enter port(s) you want to scan "))
    cmd = f"-sS -p T:{port}"
    scan(ip, cmd)
    cmd = f"-sU -p U:{port}"
    scan(ip, cmd)
