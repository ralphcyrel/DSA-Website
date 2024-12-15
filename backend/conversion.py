class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a class stack that has methods of push, pop, peek, isempty, and print
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):  # Add a new node to the top of the stack
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):  # Remove the node at the top of the stack
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):  # Return the data at the top of the stack
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):  # Determine if the stack has elements
        return self.top is None

    def print_stack(self):  # Print all the elements of the stack
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next


def precedence(operator):  # Set the precedence of the operators
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "^":
        return 3
    else:
        return 0


def left_stack(
        operator):  # Determine if the expression will be evaluated from left-right (+,-,*,/) or right to left (^)
    if operator in ["+", "-", "*", "/"]:
        return True
    return False


def infix_to_postfix(expression):  # Method to convert infix expression to postfix expression
    stack = Stack()
    output = []
    for term in expression:
        if term.isalnum():  # Determine if the term is variable or number
            output.append(term)
        elif term == '(':  # Left parenthesis
            stack.push(term)
        elif term == ')':  # Right parenthesis
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Discard the '(' from the stack
        elif term in "+-*/^":  # Operator
            while (not stack.is_empty() and
                   (precedence(stack.peek()) > precedence(term) or
                    (precedence(stack.peek()) == precedence(term) and left_stack(term)))):
                output.append(stack.pop())
            stack.push(term)
        else:
            raise ValueError("Invalid character in expression")

    # Pop any remaining operators in the stack
    while not stack.is_empty():
        output.append(stack.pop())

    return " ".join(output)


try:
    expression = input("Enter expression: ")
    for char in expression:
        if not (char.isalnum() or char in "+-*/^() "):
            raise ValueError("Error: Expression contains invalid characters")

    postfix = infix_to_postfix(expression.replace(" ", ""))
    print("Infix Expression: ", expression)
    print("Postfix Expression: ", postfix)
except ValueError as e:
    print(e)