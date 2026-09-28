from node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        if self.front is None:
            return None

        return self.front.value

    def print_queue(self):
        current = self.front

        if current is None:
            print("Queue is empty.")
            return

        while current:
            print("-", current.value)
            current = current.next


queue = Queue()


while True:
    print("\n--- Help Desk Ticketing System ---")
    print("1. Add customer")
    print("2. Help next customer")
    print("3. View next customer")
    print("4. View all waiting customers")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        name = input("Enter customer name: ")
        queue.enqueue(name)
        print(name, "added to the queue.")

    elif choice == "2":
        name = queue.dequeue()

        if name is None:
            print("No customers waiting.")
        else:
            print("Helped:", name)

    elif choice == "3":
        name = queue.peek()

        if name is None:
            print("No customers waiting.")
        else:
            print("Next customer:", name)

    elif choice == "4":
        print("Waiting customers:")
        queue.print_queue()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")