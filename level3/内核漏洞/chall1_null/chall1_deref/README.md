# Linux kernel exploitation experiments

__Contents:__
  - __chall1_null_mod.c__ - a small Linux kernel module with vulnerability.
  - __null_exploit_min_addr.c__ - a basic null-ptr-deref exploit, which directly mmaps zero addr. The mmap_min_addr protection can be disabled by `CONFIG_DEFAULT_MMAP_MIN_ADDR=0`.
  - __bzImage__ - Linux kernel x86 boot executable bzImage compiled with 5.0.0-rc1
  - __config-5.0-rc1__ - the .config file of linux 5.0.0-rc1
  - __rootfs.cpio__ - the file system for qemu vm
  - __run.sh__ - the script to run a qemu vm
  - __fs.sh__ - the script to repack the rootfs.cpio
  - __flag__ - a test flag
  - __upload.py__ - the script to upload exploit to remote challenge 

Have fun!

## Preparation

### 1. Compile Linux Kernel

* If you do not want to compile kernel by yourself, just use the *`bzImage`* in attachments and pass this part.
* Preferably build on Ubuntu 20.04 or docker to reduce compile issues
```
wget https://mirrors.hust.edu.cn/git/linux.git/snapshot/linux-5.0-rc1.tar.gz
tar -xvf v5.0-rc1.tar.gz
cd linux-5.0-rc1
cp ../config-5.0-rc1 .config
make olddefconfig
make -j32 CC=gcc-8
```

Create soft link with the target Linux kernel in case you have multiple Linux kernel versions, then use the `bzImage` in `$PWD/linux/arch/x86/boot/bzImage`
```
ln -s linux-5.0-rc1 linux
```

*Note that linux-5.0-rc1 is vulnerable to [Null Pointer Dereference exploit][1]. When compiling linux-5.0-rc1 with gcc-9, it will report [error: ' mindirect branch' and ' fcf protection' are not compatible](https://mudongliang.github.io/2021/04/09/error-mindirect-branch-and-fcf-protection-are-not-compatible.html)*

### 2. Basic Knowledges For Busybox File System
- Create a new directory named `core`, 
  getinto it and **unpack** the file system by `cpio -idmv < ../rootfs.cpio`
- `init` script and `$challenge.ko` is at the root directory of `rootfs.cpio`
- `init` is equivalent to the boot script of the Linux kernel and will be started as root
- **Repack** the file system to **save changes**, just run `find . | cpio -o --format=newc > ../rootfs.cpio`
- For local debugging, modify the corresponding code in the `init` script can easily get a root shell. 
  ```
  - setsid /bin/cttyhack setuidgid 1000 /bin/sh
  + setsid /bin/cttyhack setuidgid 0 /bin/sh
  ```
  *But please remember that altering the `init` script to acquire root privileges goes against the primary objective of this experiment, so don't be clever here.*
- `fs.sh` is very useful script that can be used to automatically unpack and repack the rootfs.cpio

### 3. Compiling The Vulnerable Module

Make sure the `vulnerable module` is in the same directory as `linux`
```
make
```

*Note that if you have modified the vulnerable module(e.g, **patched** it), you need to copy the new compiled `$challenge.ko` into `rootfs.cpio`. Please refer to subsection 2 for specific experimental steps.*


### 4. Start QEMU VM
Make sure both `-kernel` and `-initrd` are configured correctly.

Run the qemu with `run.sh`.


### 5. Exploitation

**Supplement** the original `exploit` and achieve the purpose of privilege escalation by interacting with the `vulnerability module`.

**Compile** with `gcc -static exploit.c -o exp`. Or compress `exp` with `musl-gcc -static exploit.c -o exp`.

**Local exploitation:** copy the `exp` into `rootfs.cpio`. Please refer to subsection 2 for specific experimental steps.

**Remote exploitation:** upload the `exp` with `upload.py`, `python3 upload.py [exploit file] remote_ip remote_port`

### 6. Patch The Vulnerable Linux Kernel And Recompile
- Run the following commands to patch and recompile the kernel
```
cp -rf linux-5.0-rc1/ linux-5.0-rc1-patched
wget "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id=0a1d52994d440e21def1c2174932410b4f2a98a1" -O patch
cd linux-5.0-rc1-patched
patch -p1 < ../patch
make -j32 CC=gcc-8
cd ..
ln -vnsf linux-5.0-rc1-patched/ linux
cp linux/arch/x86/boot/bzImage .
```

- Redo the null pointer exploit and this exploit does not work any more

---

<!-- ## References -->

[1]: https://bugs.chromium.org/p/project-zero/issues/detail?id=1792&desc=2
[2]: https://github.com/google/syzkaller/blob/master/tools/create-image.sh