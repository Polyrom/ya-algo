#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int val;
  struct Node *next;
} Node;

Node *add_list_element(int val) {
  Node *new_node = (Node *)malloc(sizeof(Node));
  if (new_node == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(EXIT_FAILURE);
  }
  new_node->val = val;
  new_node->next = NULL;
  return new_node;
}

void free_list(Node *head) {
  Node *current = head;
  Node *next;
  while (current != NULL) {
    next = current->next;
    free(current);
    current = next;
  }
}

Node *get_node_by_index(Node *head, int idx) {
  while (idx != 0 && head != NULL) {
    head = head->next;
    idx--;
  }
  return head;
}

int get_node_index_by_value(Node *head, int elem) {
  int i = 0;
  while (head != NULL) {
    if (head->val == elem) {
      return i;
    }
    head = head->next;
    i++;
  }
  return -1;
}

Node *delete_node(Node *head, int idx) {
  if (head == NULL)
    return NULL;
  if (idx == 0) {
    Node *new_head = head->next;
    free(head);
    return new_head;
  }
  Node *prev_node = get_node_by_index(head, idx - 1);
  if (prev_node == NULL || prev_node->next == NULL) {
    return head;
  }
  Node *node_to_delete = prev_node->next;
  prev_node->next = node_to_delete->next;
  free(node_to_delete);
  return head;
}

void print_list(Node *head) {
  Node *current = head;
  while (current != NULL) {
    printf("%d -> ", current->val);
    current = current->next;
  }
  printf("NULL\n");
}

int main() {
  Node *n1 = add_list_element(1);
  Node *n2 = add_list_element(2);
  Node *n3 = add_list_element(3);
  n1->next = n2;
  n2->next = n3;
  print_list(n1);
  int searched_val = 2;
  int idx = get_node_index_by_value(n1, searched_val);
  if (idx == -1) {
    printf("element with value %d not found\n", searched_val);
    puts("list:");
    print_list(n1);
    return EXIT_FAILURE;
  }
  printf("element with value %d found at index %d\n", searched_val, idx);
  Node *found_node = get_node_by_index(n1, idx);
  if (found_node != NULL) {
    printf("val of %dth element is %d\n", idx, found_node->val);
  } else {
    printf("%d is out of bounds\n", idx);
  }
  Node *new_head = delete_node(n1, idx);
  printf("list after deletion of node at index %d:\n", idx);
  print_list(new_head);
  free_list(n1);
}
