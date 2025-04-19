#include <stdint.h>

typedef struct BTNode {
  int32_t value;
  struct BTNode *left;
  struct BTNode *right;
} BTNode;

BTNode *create_node(int32_t value);
BTNode *create_bst_from_array(int32_t *array, int32_t len);
void free_tree(BTNode *root);

BTNode *bst_find(BTNode *root, int32_t value);
int bst_find_node_with_parent(BTNode *root, BTNode **found,
                              BTNode **found_parent, int value);
BTNode *bst_push(BTNode *root, int32_t value);
BTNode *bst_delete(BTNode *root, int32_t value);
