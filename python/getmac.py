import paramiko as prmk
import time
import csv
from colors import colors

print('\n' * 2 + '#' * 50 + '\n' * 2)

ssh = prmk.SSHClient()

ssh.set_missing_host_key_policy(prmk.AutoAddPolicy())

with open('ipaddr.txt', 'r') as file:

    servers = [line.strip() for line in file]

for server in servers:

    print(colors.WHITE + f'Attempting to connect to { server }')

    try:

        ssh.connect(hostname = server, port = '22', look_for_keys = True)

        if(ssh.get_transport().is_active() == True):

            print(colors.GREEN + f'Connected to { server }')

            std_in, std_out, std_err = ssh.exec_command("ifconfig | grep -ioE '([0-9a-f]{2}:){5}[0-9a-f]{2}'\n")

            time.sleep(1)

            print(colors.YELLOW + 'MAC Address is:- ' + std_out.read().decode('utf-8'), end='')

            print(colors.CYAN + f'Closing session with { server }')

            ssh.close()

    except:

        print(colors.RED + f'Node { server } is unreachable') 

    print(colors.WHITE)
