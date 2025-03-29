#include <stdio.h>
#include <stdlib.h>

#define ARR_LEN 10

int *slice(const int *arr, int start, int end) {
    int len = end - start;
    int *result = (int *)malloc((len) * sizeof(int));
    for (int i = 0; i < len; i++) {
        result[i] = arr[start + i];
    }
    return result;
}

void print_array(int *array, int len, const char *msg_prefix) {
    printf("%s: ", msg_prefix);
    for (int i = 0; i < len; i++) {
        printf("%d ", array[i]);
    }
    printf(" \n");
}

int main(void) {
    int arr[ARR_LEN] = {-1, -8, 0, 44, 12, -41, 21, 14, 99, -909};
    print_array(arr, ARR_LEN, "original array");
    int start = 0, end = 8;
    int *arr_new = slice(arr, start, end);
    char prefix_msg[100];
    sprintf(prefix_msg, "sliced array [%d:%d]", start, end);
    print_array(arr_new, end - start, prefix_msg);
    free(arr_new);
    return 0;
}
