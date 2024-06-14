KPATH := ${PWD}/linux/

obj-m := chall2_snow_mod.o

all:
	make -C $(KPATH) M=$(PWD) modules

clean:
	make -C $(KPATH) M=$(PWD) clean
	