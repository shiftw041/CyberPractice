#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/ioctl.h>

int main(void)
{
	int ret = EXIT_FAILURE;

	/* Fill all the operations in the kernel module */
	/* Fill your code here */
	int fd = open("/dev/snow", O_WRONLY);
	if (fd == -1)
		perror("[-] open failed\n");

	ret = ioctl(fd, 0x40001);
	if (ret != 0)
		perror("[-] SNOW_ACT_ALLOC failed\n");
	else
		printf("SNOW_ACT_ALLOC success\n");

	ret = ioctl(fd, 0x40002);
	if (ret != 0)
		perror("[-] SNOW_ACT_CALLBACK failed\n");
	else
		printf("SNOW_ACT_CALLBACK success\n");

	ret = ioctl(fd, 0x40003);
	if (ret != 0)
		perror("[-] SNOW_ACT_FREE failed\n");
	else
		printf("SNOW_ACT_FREE success\n");

	ret = ioctl(fd, 0x40004);
	if (ret != 0)
		perror("[-] SNOW_ACT_RESET failed\n");
	else
		printf("SNOW_ACT_RESET success\n");
	return ret;
}
