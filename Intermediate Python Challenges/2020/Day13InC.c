#include <stdio.h>
#include <stdlib.h>

long long part2(int array[], int len){
    int not_done = 1;
    int not_loop_done = 1;
    int max = 467;
    int max_index = 33;
    long long time = max;
    long long check = 100;
    while(not_done){
        //printf(" Time: %llu\n", time);
        not_done = 0;
        not_loop_done = 1;
        for (int i = 0; i < len && not_loop_done; i++)
        {
            //printf(" array[i]: %i\n", array[i]);
            if (array[i] && ((time - (max_index - i)) % array[i])){
                not_done = 1;
                not_loop_done = 0;
            }
        }
        time += max;
        if (time > check){
            printf("Check: %llu\n", check);
            check = check * (long long) 10;
        }
    }

    return time - max - max_index;
}


int main(int argc, char const *argv[])
{
    int input[] = {29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,37,0,0,0,0,0,467,0,0,0,0,0,0,0,23,0,0,0,0,13,0,0,0,17,0,19,0,0,0,0,0,0,0,0,0,0,0,443,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41};
    int len_input = 113;
    long long time = part2(input, len_input);
    printf("Part 2: %llu", time);
    return 0;
}