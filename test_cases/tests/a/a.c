#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isSubsetSum(int set[], int n, int sum, int set2[], int sum2, int cnt){
    if (sum == 0 && sum2==0)
        return true;
    if (n == cnt || (sum < 0 || sum2 < 0))
        return false;
        
    if ((set[cnt] > sum) || (set2[cnt] > sum2))
        return isSubsetSum(set, n, sum, set2, sum2, cnt+1);

    return isSubsetSum(set, n, sum, set2, sum2, cnt+1) || isSubsetSum(set, n, sum-set[cnt], set2, sum2-set2[cnt], cnt+1);
}

#define BUF_SIZE 1024

int main(){
    char buffer[BUF_SIZE];
    size_t contentSize = 1; // includes NULL
    /* Preallocate space.  We could just allocate one char here, 
    but that wouldn't be efficient. */
    char *content = malloc(sizeof(char) * BUF_SIZE);
    if(content == NULL)
    {
        perror("Failed to allocate content");
        exit(1);
    }
    content[0] = '\0'; // make null-terminated
    while(fgets(buffer, BUF_SIZE, stdin))
    {
        char *old = content;
        contentSize += strlen(buffer);
        content = realloc(content, contentSize);
        if(content == NULL)
        {
            perror("Failed to reallocate content");
            free(old);
            exit(2);
        }
        strcat(content, buffer);
    }
    char l0 = content[0];
    printf("%c", l0+1);

    if(ferror(stdin))
    {
        free(content);
        perror("Error reading from stdin.");
        exit(3);
    }

    char * token = strtok(&content[0], " ");
    printf( " %s\n", token+1 ); //printing the token
    /*
    lines = []
    for line in sys.stdin:
        if line == '': # If empty string is read then stop the loop
            break
        lines.append(line.rstrip('\n'))

    l = lines[0].split(" ");
    int nb_products = int(l[0]);
    int money = int(l[1]);
    int kcal = int(l[2]);

    p = []
    s_m = []
    s_k = []

    for(i=1; i<l_length; i++){
        l = l.split(" ")
        s_m.append(int(l[0]))
        s_k.append(int(l[1]))
    }
        
    if(isSubsetSum(s_m, nb_products, money, s_k, kcal, 0)){
        printf("Yes");
    }
    else {
        printf("No");
    }
    */
   return 0;
}
