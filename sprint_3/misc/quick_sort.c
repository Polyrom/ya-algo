/*
Quick sort.
Time: O(n log n)* (worst case O(n**2)). Space: O(n)
*/

#include <stdio.h>
#include <stdlib.h>

void print_array(int *array, int len, const char *msg_prefix);
int select_pivot(int *array, size_t array_size);
void partition(int *array, size_t array_size, int pivot, int *left, int *mid,
               int *right, size_t *left_size, size_t *mid_size,
               size_t *right_size);
void quick_sort(int *array, size_t array_size);

int main(void) {
    int arr[] = {-1, -8, 0, 44, 12, -41, 21, 14, 99, -909};
    size_t arr_len = sizeof(arr) / sizeof(int);
    print_array(arr, arr_len, "original array: ");
    quick_sort(arr, arr_len);
    print_array(arr, arr_len, "sorted array: ");
    return 0;
}

int select_pivot(int *array, size_t array_size) {
    int first = array[0];
    int middle = array[array_size / 2];
    int last = array[array_size - 1];

    // Find the median of the three
    if ((first > middle) ^ (first > last))
        return first;
    else if ((middle > first) ^ (middle > last))
        return middle;
    else
        return last;
}

void partition(int *array, size_t array_size, int pivot, int *left, int *mid,
               int *right, size_t *left_size, size_t *mid_size,
               size_t *right_size) {
    *left_size = *mid_size = *right_size = 0;
    size_t i = 0;
    while (i < array_size) {
        if (array[i] == pivot) {
            mid[(*mid_size)++] = array[i++];
        } else if (array[i] < pivot) {
            left[(*left_size)++] = array[i++];
        } else {
            right[(*right_size)++] = array[i++];
        }
    }
}

void quick_sort(int *array, size_t array_size) {
    if (array_size < 2) {
        return;
    }
    int pivot = select_pivot(array, array_size);
    int *left = (int *)malloc(array_size * sizeof(int));
    int *mid = (int *)malloc(array_size * sizeof(int));
    int *right = (int *)malloc(array_size * sizeof(int));
    size_t left_size, right_size, mid_size;
    partition(array, array_size, pivot, left, mid, right, &left_size, &mid_size,
              &right_size);
    quick_sort(left, left_size);
    quick_sort(right, right_size);
    int k = 0;
    for (size_t i = 0; i < left_size; i++) {
        array[k++] = left[i];
    }
    for (size_t i = 0; i < mid_size; i++) {
        array[k++] = mid[i];
    }
    for (size_t i = 0; i < right_size; i++) {
        array[k++] = right[i];
    }
    free(left);
    free(mid);
    free(right);
}

void print_array(int *array, int len, const char *msg_prefix) {
    printf("%s", msg_prefix);
    for (int i = 0; i < len; i++) {
        printf("%d ", array[i]);
    }
    printf(" \n");
}
