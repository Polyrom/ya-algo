/*
Insertion sort.
Time: O(n**2). Space: O(1)
*/

#include <stdio.h>

#define ARR_LEN 5

void selection_sort(int *array, size_t len)
{
    for (int i = 0; i < len; i++)
    {
        int elem_to_insert = array[i];
        int j = i;
        while (j > 0 && array[j] < array[j - 1])
        {
            array[j] = array[j - 1];
            j--;
        }
        array[j] = elem_to_insert;
    }
}

void print_array(int *array, int len)
{
    for (int i = 0; i < len; i++)
    {
        printf("%d ", array[i]);
    }
    printf(" \n");
}

int main()
{
    int arr[ARR_LEN] = {-1, -8, 0, 44, 12};
    puts("array before:");
    print_array(arr, ARR_LEN);
    selection_sort(arr, ARR_LEN);
    puts("array after:");
    print_array(arr, ARR_LEN);
    return 0;
}