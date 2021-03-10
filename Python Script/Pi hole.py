import paramiko
user_name = "pi"
passwd = "password"
ip = "192.168.0.188"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=ip, username=user_name, password=passwd)

stdin, stdout, stderr = ssh.exec_command('''sudo apt-get update
                                         sudo apt-get upgrade
                                         ''')
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    print (line)


ssh.close()
