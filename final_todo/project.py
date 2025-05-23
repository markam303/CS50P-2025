import csv
import os
from datetime import datetime
from tabulate import tabulate


class Task:
    """Represents a single task with OOP encapsulation."""

    def __init__(self, task_id, description, priority, created=None, completed=False):
        """ "Initialize task properties with validation."""
        if not description or not description.strip():
            raise ValueError("Missing task describtion!")
        
        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("Invalid priority! Use: High, Medium, Low.")

        self.id = task_id
        self.description = description.strip()
        self.priority = priority
        self.created = created if created else datetime.now().strftime("%Y-%m-%d")
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} {self.description} ({self.priority})"

    def mark_complete(self):
        """Mark task as completed with validation"""
        if self.completed:
            return False
        self.completed = True
        return True

    def to_dict(self):
        """Convert to dictionary for CSV serialization"""
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
        # Handle boolean conversion for completed field
        completed = dict["completed"]
        if isinstance(completed, str):
            completed = completed.capitalize() 
            if completed == "True":
                completed = True
            else:
                completed = False
            
        return cls(
            task_id=int(dict["id"]),
            description=dict["description"],
            priority=dict["priority"],
            created=dict["created"],
            completed=completed,
        )


# Global tasks list
tasks = []

def add_task(description: str, priority) -> bool:
    """Add new task with input validation."""
    # Validation
    if not description or not description.strip():
        return False
    
    if isinstance(priority, int):
        priority_map = {1: "High", 2: "Medium", 3: "Low"}
        if priority not in priority_map:
            return False
        priority = priority_map.get(priority, "Medium")

    try:
        # Create new Task obj
        new_task = Task(
            task_id=len(tasks) + 1,
            description=description,
            priority=priority,
        )

        tasks.append(new_task)
        print(f"Task added: {new_task.id} {new_task.description} (Priority: {new_task.priority})")
        save_tasks()
        return True

    except ValueError as e:
        print(f"Error adding task: {e}")
        return False


def mark_task_complete(task_id: int) -> bool:
    """ "Mark task as completed with ID validation."""
    if not tasks:
        print("No tasks found!")
        return False
    
    # Find and mark task
    for task in tasks:
        if task.id == task_id:
            if task.completed:
                print(f"Task {task_id} is already marked as completed.")
                return False
            else:
                task.mark_complete()
                print(f"Task {task_id} completed!")
                save_tasks()
                return True
    
    print(f"Error: No task found!")
    return False
    

def delete_task(task_id: int) -> bool:
    """ "Delete task with ID validation and reindexing."""
    if not tasks:
        print("No tasks to delete!")
        return False
    

    for i, task in enumerate(tasks):
        if task.id == task_id:
            deleted_task = tasks.pop[i]
            print(f"Task {task_id} {deleted_task.description} removed!")

            # reindex ramining tasks
            for j, task in enumerate(tasks):
                task.id = j + 1

            save_tasks()
            return True

    print(f"No task found with ID {task_id}")
    return False


def view_tasks() -> None:
    """ "Display all tasks in formatted table."""
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

    print("\n" + ("=" * 60))
    print("\nTodo List")
    print("=" * 60)
    print(
        tabulate(
            table_data,
            headers=["ID", "Description", "Priority", "Created", "Status"],
            tablefmt="grid",
        )
    )


def save_tasks() -> None:
    """Save tasks to CSV with atomic write."""
    try:
        with open("tasks.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["ID", "Description", "Priority", "Created", "Completed"],
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
    
    # Menu 
    print("\nOptions:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark as completed")
    print("4. Delete a task")
    print("5. Save & Exit")
    
    while True:
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
                try:
                    priority = int(input("Enter priority (1-3): "))
                    assert 1 <= priority <= 3
                except (ValueError, AssertionError):
                    print("Invalid priority")
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



if __name__ == "__main__":
    main()
