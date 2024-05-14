# define a class Task
class Task:
    def __init__(self, title, description, status='Pending'):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status}"

# creating a class TodoList to manage tasks
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task_status(self, task_title, new_status):
        for task in self.tasks:
            if task.title == task_title:
                task.status = new_status
                break

    def delete_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)
                print("--------------------")

    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task.title},{task.description},{task.status}\n")

    def load_tasks_from_file(self, filename):
        self.tasks = []
        with open(filename, 'r') as f:
            for line in f:
                title, description, status = line.strip().split(',')
                self.tasks.append(Task(title, description, status))

def main():
    todo_list = TodoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Update Task Status")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Save Tasks to File")
        print("6. Load Tasks from File")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(Task(title, description))
            print("Task added successfully!")

        elif choice == '2':
            title = input("Enter task title to update status: ")
            new_status = input("Enter new status (e.g., Completed, In Progress, Pending): ")
            todo_list.update_task_status(title, new_status)
            print("Task status updated successfully!")

        elif choice == '3':
            title = input("Enter task title to delete: ")
            todo_list.delete_task(title)
            print("Task deleted successfully!")

        elif choice == '4':
            print("===== List of Tasks =====")
            todo_list.list_tasks()

        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks_to_file(filename)
            print("Tasks saved to file successfully!")

        elif choice == '6':
            filename = input("Enter filename to load tasks from: ")
            todo_list.load_tasks_from_file(filename)
            print("Tasks loaded from file successfully!")

        elif choice == '7':
            print("Exiting the To-Do List application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
