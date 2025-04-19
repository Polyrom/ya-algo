#include <gtest/gtest.h>
#include "../bst.h"


// Helper function to count nodes in BST
int count_nodes(BTNode* root) {
    if (root == NULL) return 0;
    return 1 + count_nodes(root->left) + count_nodes(root->right);
}

// Helper function to verify BST property
int is_bst(BTNode* node, int min, int max) {
    if (node == NULL) return 1;
    if (node->value < min || node->value > max) return 0;
    return is_bst(node->left, min, node->value - 1) && 
           is_bst(node->right, node->value + 1, max);
}

// Test cases
TEST(BSTDeleteTest, DeleteFromEmptyTree) {
    BTNode* root = NULL;
    root = bst_delete(root, 10);
    EXPECT_EQ(root, nullptr);
}

TEST(BSTDeleteTest, DeleteNonExistentValue) {
    int values[] = {50, 30, 70};
    BTNode* root = create_bst_from_array(values, 3);
    BTNode* original_root = root;
    
    root = bst_delete(root, 99);
    EXPECT_EQ(root, original_root);
    EXPECT_EQ(count_nodes(root), 3);
    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));
    
    free_tree(root);
}

/*TEST(BSTDeleteTest, DeleteLeafNode) {*/
/*    int values[] = {50, 30, 70, 20, 40, 60, 80};*/
/*    BTNode* root = create_bst_from_array(values, 7);*/
/**/
/*    root = bst_delete(root, 20);*/
/*    EXPECT_EQ(count_nodes(root), 6);*/
/*    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));*/
/*    EXPECT_EQ(bst_find(root, 20), 0);*/
/**/
/*    free_tree(root);*/
/*}*/
/**/
/*TEST(BSTDeleteTest, DeleteNodeWithOneChild) {*/
/*    int values[] = {50, 30, 70, 20, 40, 60, 80, 10};*/
/*    BTNode* root = create_bst_from_array(values, 8);*/
/**/
/*    root = bst_delete(root, 20);*/
/*    EXPECT_EQ(count_nodes(root), 7);*/
/*    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));*/
/*    EXPECT_EQ(bst_find(root, 20), 0);*/
/*    EXPECT_EQ(bst_find(root, 10), 1);*/
/**/
/*    free_tree(root);*/
/*}*/
/**/
/*TEST(BSTDeleteTest, DeleteNodeWithTwoChildren) {*/
/*    int values[] = {50, 30, 70, 20, 40, 60, 80, 35, 45};*/
/*    BTNode* root = create_bst_from_array(values, 9);*/
/**/
/*    root = bst_delete(root, 30);*/
/*    EXPECT_EQ(count_nodes(root), 8);*/
/*    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));*/
/*    EXPECT_EQ(bst_find(root, 30), 0);*/
/*    // Verify the replacement node's value is now in the tree*/
/*    EXPECT_EQ(bst_find(root, 20), 1);*/
/*    EXPECT_EQ(bst_find(root, 40), 1);*/
/**/
/*    free_tree(root);*/
/*}*/
/**/
/*TEST(BSTDeleteTest, DeleteRootNode) {*/
/*    int values[] = {50, 30, 70, 20, 40, 60, 80};*/
/*    BTNode* root = create_bst_from_array(values, 7);*/
/**/
/*    root = bst_delete(root, 50);*/
/*    EXPECT_EQ(count_nodes(root), 6);*/
/*    EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));*/
/*    EXPECT_EQ(bst_find(root, 50), 0);*/
/*    // Verify the new root is valid*/
/*    EXPECT_TRUE(root != NULL);*/
/**/
/*    free_tree(root);*/
/*}*/
/**/
/*TEST(BSTDeleteTest, DeleteAllNodes) {*/
/*    int values[] = {50, 30, 70, 20, 40, 60, 80};*/
/*    BTNode* root = create_bst_from_array(values, 7);*/
/**/
/*    for (int i = 0; i < 7; i++) {*/
/*        root = bst_delete(root, values[i]);*/
/*        EXPECT_TRUE(is_bst(root, INT_MIN, INT_MAX));*/
/*    }*/
/**/
/*    EXPECT_EQ(root, nullptr);*/
/*}*/
