#!/usr/bin/env python3
from pwn import *
from sys import argv
import os

if len(sys.argv) <= 3:
        print("Usage: python3 upload.py [exploit file] ip port")
        exit(0)
else:
        ip = sys.argv[2]
        port = sys.argv[3]
# This file is used to upload exploit to remote and execute it
context.log_level = 'debug'

# Remember to replace `ip` and `port` of your docker container
io = remote(ip, port)

def exec_cmd(cmd):
        io.sendline(cmd)
        io.recvuntil(b"$ ")

def upload(file, remote_path):
        if os.path.exists(file) == False:
                log.info(f"[-]Error: File {file} not found")
                exit(0) 
        
        p = log.progress("Upload")

        # config filename
        local_gzip_f = "./exp.gz"
        remote_base_f = remote_path + "/base_exp"
        remote_gzip_f = remote_path + "/exp.gz"
        remote_rexp_f = remote_path + "/exp"
        
        os.system(f'strip {file}')
        os.system(f'gzip -c {file} > {local_gzip_f}')
        with open(local_gzip_f, "rb") as f:
                data = f.read()
        encoded = base64.b64encode(data)
        io.recvuntil(b"$ ")

        for i in range(0, len(encoded), 600):
                p.status("%d / %d" % (i, len(encoded)))
                exec_cmd(f"echo \"%s\" >> {remote_base_f}" % (encoded[i:i+600].decode()))

        exec_cmd(f"cat {remote_base_f} | base64 -d > {remote_gzip_f}")
        exec_cmd(f'gunzip -c {remote_gzip_f} > {remote_rexp_f}')
        exec_cmd(f"chmod +x {remote_rexp_f}")

        # trigger remote exploit
        io.sendline(f"{remote_rexp_f}")

upload(argv[1], "/home/ctf")
context.log_level = 'debug'
io.interactive()
