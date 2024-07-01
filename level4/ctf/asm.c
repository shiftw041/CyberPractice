#include <stdio.h>

char input[100], check[100];
int v3, v5, v7, v6, v8;
int i;
LABEL_12 : scanf("%d");
int main()
{

    _puts("I poisoned the program... Can you reverse it?");
    _puts("Come on! Give me your flag:");
    scanf_s("%s", input);
    if (strlen((const char *)input) != 35)
        goto LABEL_12;
    v3 = 0;
    if (strlen((const char *)input) != 1)
    {
        do
        {
            input[v3] += input[v3 + 1];
            ++v3;
        } while (v3 < strlen((const char *)input) - 1);
    }
    for (i = 0; i < strlen((const char *)input); ++i)
        input[i] = __ROR1__(input[i], 4);
    v5 = 0;
    v6 = 0;
    do
    {
        v7 = v5;
        v8 = v6 + 1;
        ++v5;
        if (input[v7] != check[v7])
            v8 = v6;
        v6 = v8;
    } while (v5 < 35);
    if (v8 == 35)
        _puts("\nTTTTTTTTTTQQQQQQQQQQQQQLLLLLLLLLL!!!!");
}