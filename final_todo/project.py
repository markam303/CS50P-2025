import csv
import os
from datetime import datetime
from tabulate import tabulate
from pyfiglet import Figlet, figlet_format


class Task:
    """Represents a single task with OOP encapsulation."""

    def __init__(self, task_id, description, priority, created=None, completed=False):
        """Initialize task properties with validation."""
        if not description or not description.strip():
            raise ValueError("Error: missing task description")

        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("Error: Invalid priority. Use: High, Medium, Low")

        self.id = task_id
        self.description = description.strip()
        self.priority = priority
        self.created = created if created else datetime.now().strftime("%Y-%m-%d")
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} {self.description} ({self.priority})"

    def mark_complete(self):
        """Mark task as completed with validation."""
        if self.completed:
            return False
        self.completed = True
        return True

    def to_dict(self):
        """Convert to dictionary for CSV serialization."""
        return {
            "id": self.id,
            "description": self.description,
            "priority": self.priority,
            "created": self.created,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, task_dict):
        """Create Task object from dictionary."""
        # Handle boolean conversion for completed field
        completed = task_dict["completed"]
        if isinstance(completed, str):
            completed = completed.lower() == "true"

        return cls(
            task_id=int(task_dict["id"]),
            description=task_dict["description"],
            priority=task_dict["priority"],
            created=task_dict["created"],
            completed=completed,
        )


# Global tasks list
tasks = []


def add_task(description: str, priority) -> bool:
    """Add new task with input validation."""
    # Validation
    # if not description or not description.strip():
    #    return False

    if isinstance(priority, int):
        priority_map = {1: "High", 2: "Medium", 3: "Low"}
        if priority not in priority_map:
            return False
        priority = priority_map[priority]

    try:
        # Create new Task obj
        new_task = Task(
            task_id=len(tasks) + 1,
            description=description,
            priority=priority,
        )

        tasks.append(new_task)
        print(
            f"Task added: {new_task.id} {new_task.description} (Priority: {new_task.priority})"
        )
        save_tasks()
        return True

    except ValueError as e:
        print(f"Error adding task: {e}")
        return False


def mark_task_complete(task_id: int) -> bool:
    """Mark task as completed with ID validation."""
    if not tasks:
        print("Error: No tasks found")
        return False

    # Find and mark task
    for task in tasks:
        if task.id == task_id:
            if task.completed:
                print(f"Task {task_id} is already marked as completed")
                return False
            task.mark_complete()
            print(f"Task {task_id} completed!")
            save_tasks()
            return True

    # Return when no tasks was found
    print(f"Error: No task found with ID {task_id}")
    return False


def delete_task(task_id: int) -> bool:
    """Delete task with ID validation and reindexing."""
    if not tasks:
        print("Error: No tasks to delete")
        return False

    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            print(f"Task {task_id} {task.description} removed!")

            # reindex remaining tasks
            for j, task in enumerate(tasks):
                task.id = j + 1

            save_tasks()
            return True

    print(f"Error: No task found with ID {task_id}")
    return False


def view_tasks() -> None:
    """Display all tasks in formatted table."""
    if not tasks:
        print("Error: no tasks found")
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

    print("\n" + ("-" * 60))
    print((" " * 26) + "Todo List")
    print("-" * 60)
    print(
        tabulate(
            table_data,
            headers=["id", "description", "priority", "created", "status"],
            tablefmt="grid",
        )
    )


def save_tasks() -> bool:
    """Save tasks to CSV with atomic write."""
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


def load_tasks() -> bool:
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


def main():
    """Main application entry point with interactive menu."""
    # Initialize tasks
    load_tasks()

    # Welcome message with Figlet possibly
    print()
    print(figlet_format("TODO", font="basic"))
    print(f"Loaded {len(tasks)} existing tasks")

    while True:
        # Menu
        print("\n============ Todo List ============")
        print("Options:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark as completed")
        print("4. Delete a task")
        print("5. Save & Exit")

        # User's choice
        try:
            choice = int(input("\nWhat do you want to do? Enter choice (1-5): "))

            # Add task
            if choice == 1:
                description = input("Enter task description: ")
                print("\nPriority Options:")
                print("1. High")
                print("2. Medium")
                print("3. Low")

                while True:
                    try:
                        priority = int(input("Enter priority (1-3): "))
                        assert 1 <= priority <= 3
                        break
                    except (ValueError, AssertionError):
                        print("Invalid priority")
                add_task(description, priority)

            # View all tasks
            elif choice == 2:
                view_tasks()

            # Mark as complete
            elif choice == 3:
                view_tasks()
                try:
                    task_id = int(input("Enter task ID to mark as completed: "))
                    mark_task_complete(task_id)
                except ValueError:
                    print("Error: Please enter a valid number")

            # Delete tasks
            elif choice == 4:
                view_tasks()
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    delete_task(task_id)
                except ValueError:
                    print("Error: Please enter a valid number")

            # Exit program
            elif choice == 5:
                save_tasks()
                print("\nThanks you for using Todo. Goodbye!\n")
                break

            # Wrong choice, try again
            else:
                print("Error: Invalid choice. Try again")

        # Catching exceptions
        except ValueError:
            print("Error: Invalid input. Please enter a number")


if __name__ == "__main__":
    main()
