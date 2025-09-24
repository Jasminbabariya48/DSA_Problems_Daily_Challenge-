class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k   # fixed size array
        self.k = k         # capacity
        self.front = 0     # index of first element
        self.rear = 0      # index of next insertion
        self.count = 0     # number of elements in queue

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # rear points to next insert position, so take (rear-1 + k) % k
        return self.q[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

if __name__ == "__main__":
    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(3)
    print(obj.enQueue(1))  # return True
    print(obj.enQueue(2))  # return True
    print(obj.enQueue(3))  # return True
    print(obj.enQueue(4))  # return False, queue is full
    print(obj.Rear())      # return 3
    print(obj.isFull())    # return True
    print(obj.deQueue())   # return True
    print(obj.enQueue(4))  # return True
    print(obj.Rear())      # return 4