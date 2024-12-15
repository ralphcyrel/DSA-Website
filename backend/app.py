from flask import Flask, render_template, request
from stack import Stack

app = Flask(__name__)

my_stack = Stack()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/projects', methods=["GET", "POST"])  # Route for projects with methods
def projects():
    stack_contents = ""
    if request.method == "POST":
        if "push" in request.form:
            data = request.form["data"]
            my_stack.push(data)
        elif "pop" in request.form:
            my_stack.pop()
        elif "peek" in request.form:
            stack_contents = my_stack.peek()
        elif "remove_beginning" in request.form:
            my_stack.remove_beginning()
        elif "remove_at_end" in request.form:
            my_stack.remove_at_end()
        elif "remove_at" in request.form:
            data = request.form["data"]
            my_stack.remove_at(data)

    # Get the current contents of the stack for display
    stack_contents = []
    current_node = my_stack.top
    while current_node:
        stack_contents.append(current_node.data)
        current_node = current_node.next
    stack_contents = " -> ".join(stack_contents)

    return render_template('projects.html', stack_contents=stack_contents)  # Pass stack_contents to template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)