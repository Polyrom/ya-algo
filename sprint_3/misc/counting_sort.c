/*
Counting sort.
Time: O(n). Space: O(n).
Suitable only for arrays with known elements range.
(This example is for arrays, whose elements <= 12).
*/

#include <stdbool.h>
#include <stdio.h>

#define MONTHS_NUM 12

void print_array(int *array, size_t len, const char *msg_prefix);

void counting_sort(int *array, size_t len) {
    int met_count[MONTHS_NUM] = {0};
    for (size_t i = 0; i < len; i++) {
        met_count[array[i] - 1]++;
    }
    print_array(met_count, 12, "met_count: ");
    int k = 0;
    for (size_t i = 0; i < MONTHS_NUM; i++) {
        for (int j = 0; j < met_count[i]; j++) {
            array[k++] = i + 1;
        }
    }
}

void print_array(int *array, size_t len, const char *msg_prefix) {
    printf("%s", msg_prefix);
    for (size_t i = 0; i < len; i++) {
        printf("%d ", array[i]);
    }
    printf(" \n");
}

bool is_arrs_equal(int *arr1, int *arr2, size_t arr1_len, size_t arr2_len) {
    if (arr1_len != arr2_len) {
        return false;
    }
    for (size_t i = 0; i < arr1_len; i++) {
        if (arr1[i] != arr2[i]) {
            return false;
        }
    }
    return true;
}

int main(void) {
    int arr[] = {12, 11, 8, 11, 4, 2, 3, 3, 3, 3, 9, 1, 6};
    size_t arr_len = sizeof(arr) / sizeof(int);
    print_array(arr, arr_len, "array before: ");
    counting_sort(arr, arr_len);
    print_array(arr, arr_len, "array sorted: ");
    int arr_expected[] = {1, 2, 3, 3, 3, 3, 4, 6, 8, 9, 11, 11, 12};
    print_array(arr_expected, arr_len, "array expected: ");
    bool is_equal = is_arrs_equal(arr, arr_expected, arr_len, arr_len);
    if (is_equal) {
        puts("test passed!");
    } else {
        puts("test failed!");
    }
    return 0;
}
