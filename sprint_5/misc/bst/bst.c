#include <stdint.h>
#include <stdlib.h>

#include "bst.h"

BTNode *bst_create_node(int32_t value) {
  BTNode *node = (BTNode *)malloc(sizeof(BTNode));
  node->value = value;
  return node;
}

BTNode *bst_create_from_array(int32_t *array, int32_t len) {
  BTNode *root = NULL;
  for (int i = 0; i < len; i++) {
    root = bst_push(root, array[i]);
  }
  return root;
}

void bst_destroy(BTNode *root) {
  if (root->left) {
    bst_destroy(root->left);
  }
  if (root->right) {
    bst_destroy(root->right);
  }
  free(root);
}

int is_bst(BTNode *node, int min, int max) {
  if (node == NULL)
    return 1;
  if (node->value < min || node->value > max)
    return 0;
  return is_bst(node->left, min, node->value - 1) &&
         is_bst(node->right, node->value + 1, max);
}

BTNode *bst_find(BTNode *root, int32_t value) {
  if (root == NULL) {
    return NULL;
  }
  if (root->value < value) {
    return bst_find(root->right, value);
  }
  if (root->value > value) {
    return bst_find(root->left, value);
  }
  return root;
}

int bst_find_node_with_parent(BTNode *root, BTNode **found,
                              BTNode **found_parent, int value) {
  *found = root;
  *found_parent = NULL;
  while (*found != NULL) {
    if ((*found)->value == value) {
      return 1;
    }
    *found_parent = *found;
    if (value > (*found)->value) {
      *found = (*found)->right;
    } else {
      *found = (*found)->left;
    }
  }
  return 0;
}

BTNode *bst_push(BTNode *root, int32_t value) {
  if (root == NULL) {
    BTNode *node = bst_create_node(value);
    return node;
  }
  if (value < root->value) {
    root->left = bst_push(root->left, value);
  } else if (value >= root->value) {
    root->right = bst_push(root->right, value);
  }
  return root;
}

BTNode *bst_delete(BTNode *root, int32_t value) {
  if (root == NULL) {
    return NULL;
  }
  BTNode *node_to_delete, *node_to_delete_parent;
  int is_found = bst_find_node_with_parent(root, &node_to_delete,
                                           &node_to_delete_parent, value);
  if (is_found == 0) {
    return root;
  }
  // node to delete has only one or no children
  if (node_to_delete->left == NULL || node_to_delete->right == NULL) {
    BTNode *tmp =
        node_to_delete->left ? node_to_delete->left : node_to_delete->right;
    // node to delete is the root
    if (node_to_delete_parent == NULL) {
      free(node_to_delete);
      return tmp;
    }
    if (node_to_delete == node_to_delete_parent->left) {
      node_to_delete_parent->left = tmp;
    } else {
      node_to_delete_parent->right = tmp;
    }
    free(node_to_delete);
  } else { // node has both children
    BTNode *replacer_parent = node_to_delete;
    BTNode *replacer = node_to_delete->left;
    while (replacer->right != NULL) {
      replacer_parent = replacer;
      replacer = replacer->right;
    }
    node_to_delete->value = replacer->value;

    if (replacer_parent == node_to_delete) {
      replacer_parent->left = replacer->left;
    } else {
      replacer_parent->right = replacer->left;
    }
    free(replacer);
  }
  return root;
}
