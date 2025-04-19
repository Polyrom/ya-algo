#include <gtest/gtest.h>
#include "../bst.h"


// Helper function to count nodes in BST
int count_nodes(BTNode* root) {
    if (root == NULL) return 0;
    return 1 + count_nodes(root->left) + count_nodes(root->right);
}

// Test cases
TEST(BSTDeleteTest, DeleteFromEmptyTree) {
    BTNode* root = NULL;
    root = bst_delete(root, 10);
    EXPECT_EQ(root, nullptr);
}

TEST(BSTDeleteTest, DeleteNonExistentValue) {
    int values[] = {50, 30, 70};
    BTNode* root = bst_create_from_array(values, 3);
    BTNode* original_root = root;
    
    root = bst_delete(root, 99);
    EXPECT_EQ(root, original_root);
    EXPECT_EQ(count_nodes(root), 3);
    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));
    
    bst_destroy(root);
}

TEST(BSTDeleteTest, DeleteLeafNode) {
    int values[] = {50, 30, 70, 20, 40, 60, 80};
    BTNode* root = bst_create_from_array(values, 7);

    root = bst_delete(root, 20);
    EXPECT_EQ(bst_find(root, 20), nullptr);
    EXPECT_EQ(count_nodes(root), 6);
    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));

    bst_destroy(root);
}

TEST(BSTDeleteTest, DeleteNodeWithOneChild) {
    int values[] = {50, 30, 70, 20, 40, 60, 80, 10};
    BTNode* root = bst_create_from_array(values, 8);

    root = bst_delete(root, 20);
    EXPECT_EQ(count_nodes(root), 7);
    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));
    EXPECT_EQ(bst_find(root, 20), nullptr);
    BTNode * found = bst_find(root, 10);
    EXPECT_EQ(found->value, 10);

    bst_destroy(root);
}

TEST(BSTDeleteTest, DeleteNodeWithTwoChildren) {
    int values[] = {50, 30, 70, 20, 40, 60, 80, 35, 45};
    BTNode* root = bst_create_from_array(values, 9);

    root = bst_delete(root, 30);
    EXPECT_EQ(count_nodes(root), 8);
    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));
    EXPECT_EQ(bst_find(root, 30), nullptr);
    // Verify the replacement node's value is now in the tree
    BTNode * found = bst_find(root, 20);
    EXPECT_EQ(found->value, 20);
    found = bst_find(root, 40);
    EXPECT_EQ(found->value, 40);

    bst_destroy(root);
}

TEST(BSTDeleteTest, DeleteRootNode) {
    int values[] = {50, 30, 70, 20, 40, 60, 80};
    BTNode* root = bst_create_from_array(values, 7);

    root = bst_delete(root, 50);
    EXPECT_EQ(count_nodes(root), 6);
    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));
    EXPECT_EQ(bst_find(root, 50), nullptr);
    // Verify the new root is valid
    EXPECT_TRUE(root != NULL);

    bst_destroy(root);
}

TEST(BSTDeleteTest, DeleteAllNodes) {
    int values[] = {50, 30, 70, 20, 40, 60, 80};
    BTNode* root = bst_create_from_array(values, 7);

    for (int i = 0; i < 7; i++) {
        root = bst_delete(root, values[i]);
        EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));
    }

    EXPECT_EQ(root, nullptr);
}
