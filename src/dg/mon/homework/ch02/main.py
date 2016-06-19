#!/bin/python
#__encoding=utf-8__
# !/usr/bin/python


class MyStack():
    def __init__(self, size):
        self.size = size;
        self.length = 0;
        self.stack = [];
        self.top = -1;

    def push(self, ele):
        if self.isFull():
            raise exception("out of range");
        else:
            self.stack.append(ele);
            self.top = self.top + 1;
            self.length = self.length + 1

    def pop(self):
        if self.isEmpty():
            raise exception("stack is empty");
        else:
            self.top = self.top - 1;
            self.length = self.length - 1;
            return self.stack.pop();

    def isFull(self):
        return self.top + 1 == self.size;

    def isEmpty(self):
        return self.top == -1;

    def __len__(self):
        return self.length;

    def __str__(self):
        return str(self.stack);


class MyQueue():
    def __init__(self, size):
        self.size = size;
        self.front = -1;
        self.rear = -1;
        self.queue = [];
        self.length = 0;

    def put(self, ele):
        if self.isFull():
            raise exception("queue is full");
        else:
            self.queue.append(ele);
            self.rear = self.rear + 1;
            self.length = self.length + 1;

    def get(self):
        if self.isEmpty():
            raise exception("queue is empty");
        else:
            self.front = self.front + 1;
            self.length = self.length - 1;
            return self.queue[self.front];

    def isFull(self):
        return self.rear - self.front + 1 == self.size;

    def isEmpty(self):
        return self.front == self.rear;

    def __len__(self):
        return self.length;

    def __str__(self):
        return str(self.queue);


if __name__ == "__main__":
    print "----------------Stack Test Start------------"
    stack = MyStack(5);
    print "before push, stack's length is : " + str(len(stack))
    for i in range(3):
        stack.push(i);
    print "after push, stack's length is : " + str(len(stack))
    stack.pop()
    print "after pop, stack's length is : " + str(len(stack))
    print "print content of stack : " + str(stack)
    print "----------------Stack Test End------------"

    print "----------------Queue Test Start------------"
    queue = MyQueue(10);
    print "before put, queue's length is : " + str(len(queue))
    for i in range(4):
        queue.put(i);
    print "after put, queue's length is : " + str(len(queue))
    print queue.get();
    print "after get, queue's length is : " + str(len(queue))
    print "print content of queue : " + str(queue)
    print "----------------Queue Test End------------"
