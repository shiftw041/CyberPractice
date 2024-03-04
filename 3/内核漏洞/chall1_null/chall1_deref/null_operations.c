#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/ioctl.h>

int main(void)
{
	int ret = EXIT_FAILURE;
	int fd = open("/dev/null_act", O_WRONLY);
	if (fd == -1)
		perror("[-] open failed\n");
		
	ret = ioctl(fd, 0x40001);
	if (ret != 0)
		perror("[-] NULL_ACT_ALLOC failed\n");
	else printf("NULL_ACT_ALLOC success\n");
	
	ret = ioctl(fd, 0x40002);
	if (ret != 0)
		perror("[-] NULL_ACT_CALLBACK failed\n");
	else printf("NULL_ACT_CALLBACK success\n");
	
	ret = ioctl(fd, 0x40003);
	if (ret != 0)
		perror("[-] NULL_ACT_FREE failed\n");
	else printf("NULL_ACT_FREE success\n");
	
	ret = ioctl(fd, 0x40004);
	if (ret != 0)
		perror("[-] NULL_ACT_RESET failed\n");
	else printf("NULL_ACT_RESET success\n");
	
	return ret;
}

