import paramiko
import time

SSH_HOST = "atlas.picoctf.net"
SSH_PORT = 53043
SSH_USER = "ctf-player"
SSH_PASSWORD = "1db87a14"

MIN_NUM, MAX_NUM = 1, 1000
ATTEMPTS = 10

def connect_ssh():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    client.connect(SSH_HOST, 
                   port=SSH_PORT, 
                   username=SSH_USER, 
                   password=SSH_PASSWORD
                )

    channel = client.invoke_shell()
    time.sleep(1)  
    
    return client, channel

def play_game(channel):
    min_num, max_num = MIN_NUM, MAX_NUM

    output = channel.recv(4096).decode()
    print(output.strip())  

    for _ in range(ATTEMPTS):
        guess = (min_num + max_num) // 2
        print(f"sending: {guess}")
        channel.send(f"{guess}\n")  

        time.sleep(1)
        output = channel.recv(4096).decode().strip()
        print(output)

        if "Lower! Try again." in output:
            max_num = guess - 1
        elif "Higher! Try again." in output:
            min_num = guess + 1
        else:
            print(f"{guess}.")
            time.sleep(1)   
            output = channel.recv(4096).decode().strip()
            return

    print("Number Not Found")

def main():
    client, channel = connect_ssh()
    try:
        play_game(channel)
    finally:
        client.close() 

if __name__ == "__main__":
    main()
