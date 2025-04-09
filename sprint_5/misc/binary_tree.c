#include <limits.h>
#include <stdio.h>

#define MAX_NODES 10

typedef struct Node {
  int value;
  struct Node *left;
  struct Node *right;
} Node;

int find_max(Node *root) {
  int i = 0, max = INT_MIN;
  Node *s[MAX_NODES];
  while (root != NULL || i > 0) {
    while (root != NULL) {
      if (root->value > max) {
        max = root->value;
      }
      s[i++] = root;
      root = root->left;
    }
    if (i > 0) {
      root = s[--i];
      root = root->right;
    }
  }
  return max;
}

int main() {
  Node node13 = {9, NULL, NULL};
  Node node12 = {0, NULL, NULL};
  Node node11 = {14, NULL, NULL};
  Node node10 = {12, NULL, NULL};
  Node node9 = {-9, NULL, NULL};
  Node node8 = {4, NULL, &node13};
  Node node7 = {7, &node12, NULL};
  Node node6 = {10, &node10, &node11};
  Node node5 = {2, &node8, &node9};
  Node node4 = {16, &node7, &node8};
  Node node3 = {6, &node9, &node10};
  Node node2 = {17, &node3, &node4};
  Node node1 = {-2, &node5, &node6};
  Node root = {10, &node1, &node2};
  int res = find_max(&root);
  printf("max value = %d, expected = 17", res);
  return 0;
}
