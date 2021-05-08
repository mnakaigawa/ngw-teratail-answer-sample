#include <stdio.h>

int main(void)
{
    int i, n = 0;
    char a[][5] = {"LISP", "C", "Ada"};
    char *p[]   = {"PAUL", "X", "MAC"};

    for (i = 0; a[i][0] != '\0'; i++) {
        n++;
    }
    /*n = sizeof(a) / sizeof(a[0]);
    printf("sizeof a= %d, sizeof a[0] = %d\n", sizeof(a), sizeof(a[0]));
    printf("sizeof p= %d, sizeof p[0] = %d\n", sizeof(p), sizeof(p[0]));
    */

    for (i = 0; i < n; i++) {
        printf("p[%d] = \"%s\"\n", i, p[i]);
    }

    for (i = 0; i < n; i++) {
        printf("a[%d] = \"%s\"\n", i, a[i]);
    }

    return 0;
}
