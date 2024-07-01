from multiprocessing import Process
import os
import random
import socket
from ecdsa import ecdsa as ec 
from datetime import datetime
RNG = random.Random()
import hashlib

g = ec.generator_192
N = g.order()
secret = RNG.randrange(1, N)
PUBKEY = ec.Public_key(g, g * secret)
PRIVKEY = ec.Private_key(PUBKEY, secret)

BANNER = """
Welcome to Hust Signer. 
What do you want to do?
1) Make signature
2) Get the flag 
>"""

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
        s.send(BANNER.encode())
        line = read_line(s)
        if line == b"1":
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            random_data = f"{RNG.getrandbits(512):x}"
            hash = int(hashlib.md5(f"{time}:{random_data}".encode()).hexdigest(), 16)
            nonce = RNG.randrange(1, N)
            signature = PRIVKEY.sign(hash, nonce)
            s.send(f"{signature.r}, {signature.s}, {hash}\n".encode())
        elif line == b"2":
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            to_check = int(hashlib.md5(f"{time}:get_flag".encode()).hexdigest(), 16)
            s.send(f"Get signature for md5(\"{time}:get_flag\")\n".encode())
            try: 
                sig_line = read_line(s).decode().split(",")
            except ValueError:
                s.send("Error!".encode())
            sig = ec.Signature(int(sig_line[0]), int(sig_line[1]))
            if PUBKEY.verifies( to_check, sig ):
                s.send(b"Congratulation! Here is your flag:")
                f = open("/flag", "r")
                flag = f.read()
                f.close()
                s.send(flag.encode())
            else:
                s.send(b"Failed!\n")
        else:
            s.send(b"What?")
    except socket.timeout:
        print("Exit via timeout!")
    finally:
        s.close()
    
if __name__ == '__main__':
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 8000))
    s.listen(10)
    while True:
        client, addr = s.accept()
        print(f"Got connect from {addr}")
        p = Process(target=go, args=(client,))
        p.daemon = True
        p.start()
        client.close()