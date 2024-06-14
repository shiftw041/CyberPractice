# Linux kernel exploitation experiments

__Contents:__
  - __chall2_snow_mod.c__ - a small Linux kernel module with vulnerability.
  - __snow_exploit_uaf.c__ - a basic use-after-free exploit
  - __bzImage__ - Linux kernel x86 boot executable bzImage compiled with 5.10.202
  - __config-5.10.202__ - the .config file of linux 5.10.202
  - __rootfs.cpio__ - the file system for qemu vm
  - __run.sh__ - the script to run a qemu vm
  - __fs.sh__ - the script to repack the rootfs.cpio
  - __flag__ - a test flag
  - __upload.py__ - the script to upload exploit to remote challenge 

Have fun!

## Preparation

1. Compile Linux Kernel


* If you do not want to compile kernel by yourself, just use the *`bzImage`* in attachments and pass this part.
* Preferably build on Ubuntu 20.04 or docker to reduce compile issues
```
wget https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.10.202.tar.xz
tar -xvf linux-5.10.202.tar.xz
cd linux-5.10.202
cp ../config-5.10.202 .config
make olddefconfig
make -j32 CC=gcc-8
```
Create soft link with the target Linux kernel in case you have multiple Linux kernel versions, then use the `bzImage` in `$PWD/linux/arch/x86/boot/bzImage`
```
ln -s linux-5.10.202 linux
```

### 2. Exploitation

Achieve privilege escalation through `use-after-free` exploit strategies. 

#### Mitigation Enable
- `CONFIG_SLUB_DEBUG=y`
- `CONFIG_SLUB=y`
- `CONFIG_SLAB_MERGE_DEFAULT=y`
- `CONFIG_SLUB_CPU_PARTIAL=y`
- `CONFIG_RANDOMIZE_BASE=y`
- `CONFIG_X86_SMAP=y`
- `CONFIG_PAGE_TABLE_ISOLATION=y`

#### Mitigation Disable
- `CONFIG_SLAB is not set`
- `CONFIG_SLAB_FREELIST_RANDOM is not set`
- `CONFIG_SLAB_FREELIST_HARDENED is not set`
- `CONFIG_MEMCG is not set`
- `CONFIG_DEBUG_LIST is not set`


### 3. Patch The Vulnerable Module And Recompile
- Patch the vulnerability in `vulnerability module`. 
- Recompile it and repack into `rootfs.cpio`.
- Redo the `use-after-free` exploit and this exploit does not work any more

---
