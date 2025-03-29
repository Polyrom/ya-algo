/*
Merge sort.
Time: O(n log n). Space: O(n)
*/

#include <stdio.h>
#include <stdlib.h>

void print_array(int *array, int len, const char *msg_prefix);
void merge(int *array, int *workspace, size_t start, size_t end, size_t mid);
void merge_sort(int *array, int *workspace, size_t start, size_t end);

int main(void) {
    int arr[] = {-1, -8, 0, 44, 12, -41, 21, 14, 99, -909};
    size_t arr_len = sizeof(arr) / sizeof(int);
    print_array(arr, arr_len, "original array: ");
    int workspace[arr_len];
    merge_sort(arr, workspace, 0, arr_len);
    print_array(arr, arr_len, "sorted array: ");
    return 0;
}

void print_array(int *array, int len, const char *msg_prefix) {
    printf("%s", msg_prefix);
    for (int i = 0; i < len; i++) {
        printf("%d ", array[i]);
    }
    printf(" \n");
}

void merge_sort(int *array, int *workspace, size_t start, size_t end) {
    if (end - start <= 1) {
        return;
    }

    size_t mid = start + (end - start) / 2;
    merge_sort(array, workspace, start, mid);
    merge_sort(array, workspace, mid, end);

    merge(array, workspace, start, end, mid);
}

void merge(int *array, int *workspace, size_t start, size_t end, size_t mid) {
    size_t i = start, j = mid, k = 0;

    while (i < mid && j < end) {
        if (array[i] <= array[j]) {
            workspace[k++] = array[i++];
        } else {
            workspace[k++] = array[j++];
        }
    }
    while (i < mid) {
        workspace[k++] = array[i++];
    }
    while (j < end) {
        workspace[k++] = array[j++];
    }
    for (i = start, k = 0; i < end; i++, k++) {
        array[i] = workspace[k];
    }
}
