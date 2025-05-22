import csv
import os
from datetime import datetime
from tabulate import tabulate


class Task:
    """Represents a single task with OOP encapsulation."""

    def __init__(self, task_id, description, priority, created=None, completed=False):
        """ "Initialize task properties with validation."""
        if not description:
            raise ValueError("Missing task describtion!")
        if not isinstance(priority, str) or priority not in ["High", "Medium", "Low"]:
            raise ValueError("Invalid priority! Use: High, Medium, Low.")

        self.id = task_id
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.created = created if created else datetime.now().strftime("%Y-%m-%d")
        self.completed = completed

    def mark_completed(self):
        """Mark task as completed with validation"""
        if self.completed:
            raise ValueError(f"Task {self.id} is already completed!")
        self.completed = True
        return True

    def to_dict(self):
        """ "Convert to dictionary for CSV serialization"""
        return {
            "id": self.id,
            "description": self.description,
            "priority": self.priority,
            "created": self.created,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, dict):
        """Create Task object from dictionary."""
        return cls(
            task_id=int(dict["id"]),
            description=dict["description"],
            priority=dict["priority"],
            created=dict["created"],
            completed=bool(dict["completed"]),
        )


# Global tasks list
tasks = []


def main():
    """Run todo list application with menu system.
    Options:
    1. Add a new task
    2. View all tasks
    3. Mark as complete
    4. Delete a task
    5. Save & Exit
    Select number to proceed.
    """
    # Initialize tasks
    load_tasks()

    # Welcome message with Figlet possibly
    print("\n===== Todo List =====")

    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark as completed")
        print("4. Delete a task")
        print("5. Save & Exit")

        # User's choice
        try:
            choice = int(input("What do you want to do? Enter choice (1-5): "))

            # Add task
            if choice == 1:
                desc = input("Enter task description: ")
                print("\nPriority Options:")
                print("1. High")
                print("2. Medium")
                print("3. Low")
                priority = int(input("Enter priority (1-3): "))
                add_task(desc, priority)

            # View all tasks
            elif choice == 2:
                view_tasks()

            # Mark as complete
            elif choice == 3:
                view_tasks()
                task_id = int(input("Enter task ID to mark as completed: "))
                mark_task_complete(task_id)

            # Delete tasks
            elif choice == 4:
                view_tasks()
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)

            # Exit program
            elif choice == 5:
                save_tasks()
                print("Thanks you for using Todo. Goodbye!")
                break

            # Wrong choice, try again
            else:
                print("Invalid choice. Try again.")

        # Catching exceptions
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_task(description, priority):
    """Add new task with input validation."""
    try:
        # Validation
        if isinstance(priority, int):
            priority_map = {1: "High", 2: "Medium", 3: "Low"}
            priority = priority_map.get(priority, "Medium")

        # Create new Task obj
        new_task = Task(
            task_id=len(tasks) + 1,
            description=description,
            priority=priority,
        )

        tasks.append(new_task)
        print(f"Task added: {new_task.task_id} {description} (Priority: {priority})")
        save_tasks()
        return True

    except Exception as e:
        print(f"Error adding task: {e}")
        return False


def mark_task_complete(task_id):
    """ "Mark task as completed with ID validation."""
    try:
        for task in tasks:
            if task.id == task_id:
                task.mark_complete()
                print(f"Task {task_id} completed")
                save_tasks()
                return True
        raise ValueError(f"No task found with ID {task_id}")

    except Exception as e:
        print(f"Error: {e}")
        return False


def delete_task(task_id):
    """ "Delete task with ID validation and reindexing."""
    try:
        for i, task in enumerate(tasks):
            if task.id == task_id:
                del tasks[i]
                print(f"Task {task_id} removed!")

                # reindex ramining tasks
                for j, task in enumerate(tasks):
                    task.id = j + 1

                save_tasks()
                return True

        raise ValueError(f"No task found with ID {task_id}")

    except Exception as e:
        print(f"Error: {e}")
        return False


def view_tasks():
    """ "Display tasks in formatted table."""
    if not tasks:
        print("No tasks found!")
        return

    table_data = [
        [
            task.id,
            task.description,
            task.priority,
            task.created,
            "Completed" if task.completed else "Pending",
        ]
        for task in tasks
    ]

    print("\nTodo List:")
    print(
        tabulate(
            table_data,
            headers=["ID", "Description", "Priority", "Created", "Status"],
            tablefmt="grid",
        )
    )


def save_tasks():
    """Save tasks to CSV."""
    try:
        with open("tasks.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "description", "priority", "created", "completed"],
            )
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False


def load_tasks():
    """Load tasks from CSV, error handling included."""
    global tasks
    tasks = []

    if not os.path.exists("tasks.csv"):
        return False

    try:
        with open("tasks.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task.from_dict(row))
        return True
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return False


if __name__ == "__main__":
    main()
