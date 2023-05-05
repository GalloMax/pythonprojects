#include <stdio.h>
#include <stdlib.h>

long long part2(int array[], int len){
    long long* possibilities = (long long*)calloc(len, sizeof(long long));
    possibilities[0] = 1;
    possibilities[1] = 1;
    if(array[1] - array[0] < 4){
        possibilities[2] = possibilities[0] + possibilities[1];
    }

    for (int i = 3; i < len; i++){
        possibilities[i] = possibilities[i - 1];
        if(array[i] - array[i - 2] < 4){
            possibilities[i] += possibilities[i - 2];
            if(array[i] - array[i - 3] == 3){
                possibilities[i] += possibilities[i - 3];
            }
        }
    }
    return possibilities[len - 1];
}


int main(int argc, char const *argv[])
{
    int input[] = {0,1,2,3,4,7,10,13,16,19,20,21,24,27,28,29,30,31,34,37,38,39,40,41,44,45,46,47,48,51,54,57,58,59,60,61,64,67,68,69,70,73,74,75,76,77,80,83,84,87,90,91,92,93,94,97,100,101,102,103,104,107,108,109,110,111,114,115,116,117,118,121,122,123,126,127,128,129,132,135,136,137,138,139,142,145,146,147,150,151,152,155,156,157,160,161,162,163,164};
    int len_input = 99;
    long long* possibilities = part2(input, len_input);
    printf("Part 2: %llu", possibilities);
    free(possibilities);
    return 0;
}