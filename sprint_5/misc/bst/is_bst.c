#include <limits.h>
#include <stdbool.h>
#include <stdio.h>

#define MAX_NODES 20

typedef struct BTNode {
  int value;
  struct BTNode *left;
  struct BTNode *right;
} BTNode;

// TODO: implement visualisation
void print_binary_tree(BTNode *root);

// Time: O(n) Space: O(h). Best for simple trees.
bool is_BST_recursive(BTNode *root, int low, int high) {
  if (root == NULL)
    return true;
  if (root->value <= low || root->value >= high)
    return false;
  return is_BST_recursive(root->left, low, root->value) &&
         is_BST_recursive(root->right, root->value, high);
}

typedef struct {
  BTNode *node;
  int low;
  int high;
} BTNodeComparator;

// Time: O(n) Space: O(h). Best for deeper trees.
bool is_BST_iterative(BTNode *root) {
  if (root == NULL)
    return true;
  int i = 0;
  BTNodeComparator stack[MAX_NODES];
  stack[i++] =
      (BTNodeComparator){.node = root, .low = INT_MIN, .high = INT_MAX};
  while (i > 0) {
    BTNodeComparator current = stack[--i];
    BTNode *node = current.node;
    if (node->value <= current.low || node->value >= current.high) {
      return false;
    };
    if (node->left != NULL) {
      BTNodeComparator ndc_left = {
          .node = node->left, .low = current.low, .high = node->value};
      stack[i++] = ndc_left;
    }
    if (node->right != NULL) {
      BTNodeComparator ndc_right = {
          .node = node->right, .low = node->value, .high = current.high};
      stack[i++] = ndc_right;
    }
  }
  return true;
}

// Time: O(n) Space: O(h). Generally better approach.
bool is_BST_inorder(BTNode *root) {
  if (root == NULL)
    return true;
  int i = 0;
  int prev = INT_MIN;
  BTNode *stack[MAX_NODES];
  while (root != NULL || i > 0) {
    while (root != NULL) {
      stack[i++] = root;
      root = root->left;
    }
    BTNode *current = stack[--i];
    if (current->value <= prev) {
      return false;
    }
    prev = current->value;
    root = current->right;
  }
  return true;
}
void confirm_result(bool got, bool expected, const char *test_num) {
  if (got == expected) {
    printf("test %s passed!\n", test_num);
  } else {
    printf("test %s failed!\n", test_num);
  }
}

int main(void) {
  // Define valid BST here
  BTNode node7 = {.value = 20, .left = NULL, .right = NULL};
  BTNode node6 = {.value = 15, .left = NULL, .right = NULL};
  BTNode node5 = {.value = 16, .left = &node6, .right = NULL};
  BTNode node4 = {.value = 9, .left = NULL, .right = NULL};
  BTNode node3 = {.value = 4, .left = NULL, .right = NULL};
  BTNode node2 = {.value = 18, .left = &node5, .right = &node7};
  BTNode node1 = {.value = 8, .left = &node3, .right = &node4};
  BTNode root = {.value = 12, .left = &node1, .right = &node2};

  // Test recursive implementation
  bool validated_bst = is_BST_recursive(&root, INT_MIN, INT_MAX);
  confirm_result(validated_bst, true, "is BST recursive positive");
  node4.value = 148;
  validated_bst = is_BST_recursive(&root, INT_MIN, INT_MAX);
  confirm_result(validated_bst, false, "is BST recursive negative");
  node4.value = 9;

  // Test iterative implementation
  validated_bst = is_BST_iterative(&root);
  confirm_result(validated_bst, true, "is BST iterative positive");
  node4.value = 148;
  validated_bst = is_BST_iterative(&root);
  confirm_result(validated_bst, false, "is BST iterative negative");
  node4.value = 9;

  // Test inorder implementation
  validated_bst = is_BST_inorder(&root);
  confirm_result(validated_bst, true, "is BST iterative positive");
  node4.value = 148;
  validated_bst = is_BST_inorder(&root);
  confirm_result(validated_bst, false, "is BST iterative negative");
  node4.value = 9;
  return 0;
}
