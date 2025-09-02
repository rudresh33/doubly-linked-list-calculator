#ROLL_NUMBERS_2305_&_2330
import math

class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.prev_state = None  # Reference to the previous state of the node
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        if not self.head:
            return None
        popped_data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return popped_data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def evaluate_expression(expression):
    current = expression.head
    while current:
        if current.data == 'sqrt':
            if current.next is not None:
                num = float(current.next.data)
                new_node = Node(str(math.sqrt(num)))  # Create a new node with the square root result
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:  # Update previous node's next reference
                    current.prev.next = new_node
                else:
                    expression.head = new_node  # If current node is head, update head reference
                current.prev = new_node
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                current.prev.prev_state = current.prev_state  # Save previous state
                current = current.next
                continue  # Skip to the next iteration
        elif current.data in {'+', '-', '*', '/', '%'}:
            if current.prev is not None and current.next is not None:
                num1 = float(current.prev.data)
                num2 = float(current.next.data)
                operator = current.data

                result = None
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        print("Error: Division by zero")
                        return None
                elif operator == '%':
                    result = (num1 / 100) * num2
                current.prev.data = str(result)
                current.prev.next = current.next.next
                if current.next.next:
                    current.next.next.prev = current.prev
                current.prev.prev_state = current.prev_state  # Save previous state
                current = current.next.next
                continue  # Skip to the next iteration
        current = current.next

    result = expression.head.data
    try:
        return float(result)
    except ValueError:
        return result

def print_history(history):
    print("\033[1;33m" + "** History **".center(60) + "\033[0m")
    print("-" * 60)
    if not history:
        print("\033[91mNo history available.\033[0m")
    else:
        for i, expression in enumerate(history):
            print(f"\033[94m{i+1}.\033[0m", end=" ")
            current = expression.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
    print("-" * 60)

def main():
    history = []  # Store previous states
    while True:
        print("\033[1;33m" + "** Welcome to the Linked List Calculator! **".center(60) + "\033[0m")
        print("-" * 60)
        print("\033[1mOptions:\033[0m")
        print("\033[94m1.\033[0m Perform basic arithmetic operations (+, -, *, /, %)")
        print("\033[94m2.\033[0m Calculate square roots (√)")
        print("\033[94m3.\033[0m Undo")
        print("\033[94m4.\033[0m Show History")
        print("\033[94m5.\033[0m Quit")
        print("-" * 60)

        choice = input("\033[1mEnter the number of your choice: \033[0m")

        if choice == '5':
            print("-" * 60)
            print("\033[1;33m" + "** Thank you for using the calculator. Goodbye! **".center(60) + "\033[0m")
            print("-" * 60)
            break

        if choice == '3':
            if history:  # Check if there is any previous state to undo
                expression = history.pop()  # Retrieve previous state
                print("\033[92mUndo successful.\033[0m")
            else:
                print("\033[91mCannot undo further. No history available.\033[0m")
            print("-" * 60)

        elif choice == '4':
            print("-" * 60)
            print_history(history)
            print("-" * 60)

        elif choice == '1':
            print("-" * 60)
            print("\033[1mEnter your arithmetic expression. Use spaces to separate operators and operands. For example: 5 + 7 / 2\033[0m")
            expression_str = input("\033[1mExpression: \033[0m")
            expression_list = DoublyLinkedList()
            for char in expression_str.split():
                expression_list.append(char)
            result = evaluate_expression(expression_list)
            if result is not None:
                print("\033[92mResult:\033[0m", result)
            history.append(expression_list)  # Store current state in history
            print("-" * 60)

        elif choice == '2':
            print("-" * 60)
            print("\033[1mEnter the number for which you want to calculate the square root.\033[0m")
            expression_str = input("\033[1mNumber: \033[0m")
            expression_list = DoublyLinkedList()
            expression_list.append('sqrt')
            expression_list.append(expression_str)
            result = evaluate_expression(expression_list)
            if result is not None:
                print("\033[92mSquare root of\033[0m", expression_str, "\033[92mis:\033[0m", result)
            history.append(expression_list)  # Store current state in history
            print("-" * 60)

        else:
            print("\033[91mInvalid choice! Please enter a valid option.\033[0m")
            print("-" * 60)

if __name__ == "__main__":
    main()