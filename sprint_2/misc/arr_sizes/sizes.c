#include <stdio.h>
#include <unistd.h>

int main() {
  int arr[4] = {42, 12, 2, 99};
  size_t len = sizeof(arr) / sizeof(arr[0]);
  printf("int array of %lu elements size = %lu bytes\n", len, sizeof(arr));
  execlp("python", "python", "./sizes.py", NULL);
  return 0;
}
