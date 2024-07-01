directive_table = " \
*************\
*************\
*-@**********\
*-***-**-****\
*-*****-*****\
*-***#**-****\
*--**----****\
**-*****-****\
**-****--****\
**---**-*****\
**-*-----****\
**-------****";
static int is_valid_directive(char *directive)
{
    char *p = directive, *q = directive_table + 28;
    while (*p != '\0'&&*q!='*'){
        switch (*p++){
        case 'w': 
            q -= 13;
            break;
        case 's': 
            q += 13;
            break;
        case 'd': 
            q++;
            break;
        case 'a': 
            q--;
            break;
        default: 
            return 0;}}
    return *q == '#';
}

