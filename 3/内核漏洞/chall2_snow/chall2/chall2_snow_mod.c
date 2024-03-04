/*
 * One Kernel Module for Kernel Exploitment Experiments
 */

#include <linux/module.h>
#include <linux/slab.h>
#include <linux/uaccess.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/cdev.h>
#include <linux/fs.h>
#include <linux/string.h>
#include <linux/miscdevice.h>

#define ACT_SIZE 5
#define SNOW_BUF_SIZE 0x400

enum snow_act_t {
	SNOW_ACT_NONE = 0x40000,
	SNOW_ACT_ALLOC = 0x40001,
	SNOW_ACT_CALLBACK = 0x40002,
	SNOW_ACT_FREE = 0x40003,
	SNOW_ACT_RESET = 0x40004
};

struct snow_t {
	struct snow_item_t *item;
};

struct snow_item_t {
	u32 foo;
	void (*callback)(void);
	char bar[1];
};

static struct snow_t snow; /* initialized by zeros */

static void snow_callback(void) {
	pr_notice("normal snow_callback %lx!\n", (unsigned long)snow_callback);
}

static long snow_act_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)
{
	ssize_t ret = 0;

	switch (cmd) {
	case SNOW_ACT_ALLOC:
		snow.item = kmalloc(SNOW_BUF_SIZE, GFP_KERNEL_ACCOUNT);
		if (snow.item == NULL) {
			pr_err("snow: not enough memory for item\n");
			ret = -ENOMEM;
			break;
		}

		pr_notice("snow: kmalloc'ed buf at %lx (size %d)\n",
				(unsigned long)snow.item, SNOW_BUF_SIZE);

		snow.item->callback = snow_callback;
		break;

	case SNOW_ACT_CALLBACK:
		if (snow.item->callback == NULL) {
			pr_err("snow: callback is NULL\n");
			ret = -EINVAL;
			break;
		}

		pr_notice("drill: exec callback %lx for item %lx\n",
					(unsigned long)snow.item->callback,
					(unsigned long)snow.item);
		snow.item->callback();
		break;

	case SNOW_ACT_FREE:
		pr_notice("snow: free buf at %lx\n",
					(unsigned long)snow.item);
		kfree(snow.item);
		break;

	case SNOW_ACT_RESET:
		snow.item = NULL;
		pr_notice("snow: set buf ptr to SNOW\n");
		break;

	default:
		pr_err("snow: invalid act %d\n", cmd);
		ret = -EINVAL;
		break;
	}

	return ret;
}

static const struct file_operations snow_act_fops = {
	.unlocked_ioctl = snow_act_ioctl,
};

static struct miscdevice misc = {
    .minor = MISC_DYNAMIC_MINOR,
    .name  = "snow",
    .fops = &snow_act_fops
};

int snow_init(void)
{
	printk(KERN_INFO "Welcome to kernel challenge2 snow\n");
	misc_register(&misc);
	return 0;
}

void snow_exit(void)
{
	printk(KERN_INFO "Goodbye hacker\n");
	misc_deregister(&misc);
}

module_init(snow_init)
module_exit(snow_exit)

MODULE_AUTHOR("Dongliang Mu <dzm91@hust.edu.cn>");
MODULE_DESCRIPTION("One Kernel Module for Kernel Exploitment Experiments");
MODULE_LICENSE("GPL v2");
