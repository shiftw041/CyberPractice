import os
import socket
from multiprocessing import Process
from Crypto.Cipher import AES
auth_key = os.urandom(16)


def getFlag():
    try:
        with open("/flag","r") as f:
            flag = f.read()
        f.close
    except Exception:
        return "error"
    return flag


MENU = """
Enter your choice:
1) Create HUSTCTFer Account
2) Create Admin Account
3) Login
4) Exit
"""

def read_line(s):
    body = b""
    while True:
        ch = s.recv(1)
        if ch == b"\n":
            break
        body = body + ch
    return body

def go(s):
    try:
        s.send("Only admin can get the flag ! \n".encode())
        while True:
            s.send(MENU.encode())
            line = read_line(s)
            if line == b"1":
                token = b'HUSTCTFer!______'
                user_key = os.urandom(16)
                cipher = AES.new(auth_key, AES.MODE_CBC, user_key)
                code = cipher.encrypt(token)
                s.send(f'here is your token: {user_key.hex() + code.hex()} \n'.encode())
            elif line == b"2":
                s.send('Not Admin !!!!!!'.encode())
            elif line == b"3":
                s.send("Enter your token > \n".encode())
                try:
                    authcode = read_line(s).decode()
                    user_key = bytes.fromhex(authcode)[:16]
                    code = bytes.fromhex(authcode)[16:]
                    cipher = AES.new(auth_key, AES.MODE_CBC, user_key)
                    token = cipher.decrypt(code)
                except Exception as e:
                    s.send("Decrypt error\n".encode())
                    break
                if token == b'AdminAdmin!_____':
                    s.send("Hello Admin! Here is your FLAG: ".encode())
                    flag = getFlag()
                    s.send(flag.encode())
                    break
                elif token == b'HUSTCTFer!______':
                    s.send('Have fun!!\n'.encode())
                    break
                else:
                    s.send('Who are you?\n'.encode())
                    break
            elif line == b"4":
                s.send('ByeBye\n'.encode())
                break
            else:
                s.send('WTF\n'.encode())
        s.close()
    except socket.timeout:
        print("Exit for timeout!")
    finally:
        s.close()


if __name__ == '__main__':
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 7000))
    s.listen(10)
    while True:
        client, addr = s.accept()
        print(f"Got connect from {addr}")
        p = Process(target=go, args=(client,))
        p.daemon = True
        p.start()
        client.close()