#include <stdio.h>
#include <stdlib.h>

typedef struct FixedSizeQueue {
  int cap;
  int head;
  int tail;
  int size;
  int *items;
} FixedSizeQueue;

void FSQ_initialize(FixedSizeQueue *fsq, int cap) {
  fsq->items = (int *)malloc(cap * sizeof(int));
  if (fsq->items == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(EXIT_FAILURE);
  }
  fsq->cap = cap;
  fsq->head = 0;
  fsq->tail = 0;
  fsq->size = 0;
}

void FSQ_destroy(FixedSizeQueue *fsq) {
  free(fsq->items);
  fsq->items = NULL;
}

int FSQ_push(FixedSizeQueue *fsq, int item) {
  if (fsq->size >= fsq->cap) {
    return -1;
  }
  fsq->items[fsq->tail] = item;
  fsq->tail = (fsq->tail + 1) % fsq->cap;
  fsq->size++;
  return 0;
}

int FSQ_pop(FixedSizeQueue *fsq, int *success) {
  if (fsq->size == 0) {
    *success = 0;
    return -1;
  }
  int val = fsq->items[fsq->head];
  fsq->items[fsq->head] = 0;
  fsq->head = (fsq->head + 1) % fsq->cap;
  fsq->size--;
  *success = 1;
  return val;
}

char is_FSQ_empty(FixedSizeQueue *fsq) { return fsq->size == 0; }

int main() {
  FixedSizeQueue fsq;
  int is_push_success, is_pop_success;
  FSQ_initialize(&fsq, 5);
  int popped = FSQ_pop(&fsq, &is_pop_success);
  if (is_pop_success == 0) {
    fprintf(stderr, "error: cannot pop from empty queue\n");
  }
  int i;
  for (i = 4; i < 10; i++) {
    is_push_success = FSQ_push(&fsq, i);
    if (is_push_success == -1) {
      fprintf(stderr, "error: queue already full\n");
    }
  }
  popped = FSQ_pop(&fsq, &is_pop_success);
  if (is_pop_success == 0) {
    fprintf(stderr, "error: cannot pop from empty queue\n");
  }
  printf("popped expected = %d, got = %d\n", 4, popped);
  for (i = 0; i < fsq.cap; i++) {
    printf("%d ", fsq.items[i]);
    puts("");
  }
  char is_empty = is_FSQ_empty(&fsq);
  printf("is queue empty? %s\n", is_empty ? "true" : "false");
  FSQ_destroy(&fsq);
  return 0;
}
