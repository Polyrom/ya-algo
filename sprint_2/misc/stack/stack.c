#include <stdio.h>
#include <stdlib.h>

#define STACK_FULL_ERR "ERROR: stack is full"
#define STACK_EMPTY_ERR "ERROR: stack is empty"

typedef struct Stack {
  int *items;
  int head;
  int cap;
  int size;
} Stack;

void Stack_initialize(Stack *stack, int cap) {
  stack->cap = cap;
  stack->items = (int *)malloc(cap * sizeof(int));
  if (stack->items == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(EXIT_FAILURE);
  }
  stack->size = 0;
  stack->head = 0;
}

void Stack_destroy(Stack *stack) {
  free(stack->items);
  stack->items = NULL;
}

void Stack_push(Stack *stack, int value, int *success) {
  if (stack->size == stack->cap) {
    *success = 0;
    return;
  }
  stack->items[stack->head] = value;
  stack->head++;
  stack->size++;
}

int Stack_pop(Stack *stack, int *success) {
  if (stack->size == 0) {
    *success = 0;
    return -1;
  }
  stack->head--;
  int val = stack->items[stack->head];
  stack->size--;
  return val;
}

void Stack_print(Stack *stack) {
  int i;
  printf("cap=%d size=%d head=%d\n", stack->cap, stack->size, stack->head);
  printf("[ ");
  for (i = 0; i < stack->size; i++) {
    printf("%d ", stack->items[i]);
  }
  printf("]\n");
}

void handle_stack_error(int *success, char *err_msg) {
  if (*success == 0) {
    fprintf(stderr, "%s\n", err_msg);
  }
  *success = 1;
}

int main() {
  Stack s;
  int success, popped;
  Stack_initialize(&s, 3);
  Stack_print(&s);
  popped = Stack_pop(&s, &success);
  handle_stack_error(&success, STACK_EMPTY_ERR);
  Stack_print(&s);
  Stack_push(&s, 12, &success);
  handle_stack_error(&success, STACK_FULL_ERR);
  Stack_print(&s);
  Stack_push(&s, 4, &success);
  handle_stack_error(&success, STACK_FULL_ERR);
  Stack_print(&s);
  Stack_push(&s, 6, &success);
  handle_stack_error(&success, STACK_FULL_ERR);
  Stack_print(&s);
  Stack_push(&s, 8, &success);
  handle_stack_error(&success, STACK_FULL_ERR);
  Stack_print(&s);
  popped = Stack_pop(&s, &success);
  handle_stack_error(&success, STACK_EMPTY_ERR);
  printf("popped item=%d\n", popped);
  Stack_print(&s);
  Stack_destroy(&s);
  return 0;
}
