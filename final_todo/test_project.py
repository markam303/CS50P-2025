import pytest
import os
import project
from project import Task


# Fixtures for testing
@pytest.fixture(autouse=True)
def clean_tasks():
    """Clean up tasks list before and after each test."""
    # Store original tasks
    original_tasks = project.tasks.copy()
    project.tasks.clear()

    yield

    # Restore original tasks
    project.tasks.clear()
    project.tasks.extend(original_tasks)


def test_task_creation():
    """Test basic Task object creation."""
    task = Task(1, "Test task", "High")

    assert task.id == 1
    assert task.description == "Test task"
    assert task.priority == "High"
    assert task.completed == False
    assert not task.created == None


def test_task_validation():
    """Test Task input validation."""
    # Test empty description
    with pytest.raises(ValueError):
        Task(1, "", "High")

    # Test whitespace-only description
    with pytest.raises(ValueError):
        Task(1, "   ", "High")

    # Test invalid priority
    with pytest.raises(ValueError):
        Task(1, "Test task", "Invalid")


def test_task_mark_complete():
    """Test marking task as complete."""
    task = Task(1, "Test task", "Medium")

    # First completion should succeed
    assert task.mark_complete() == True
    assert task.completed == True

    # Second completion should return False (already completed)
    assert task.mark_complete() == False


def test_task_to_dict():
    """Test task dictionary conversion."""
    task = Task(1, "Test task", "Low", "2025-01-01", True)
    task_dict = task.to_dict()

    expected = {
        "id": 1,
        "description": "Test task",
        "priority": "Low",
        "created": "2025-01-01",
        "completed": True,
    }
    assert task_dict == expected


def test_task_from_dict():
    """Test creating task from dictionary."""
    task_dict = {
        "id": "2",
        "description": "Test task 2",
        "priority": "High",
        "created": "2025-01-01",
        "completed": True,
    }

    task = Task.from_dict(task_dict)
    assert task.id == 2
    assert task.description == "Test task 2"
    assert task.priority == "High"
    assert task.completed == True


def test_add_task():
    """Test adding tasks to the list."""
    # Test successful addition
    assert project.add_task("Test task", "High") == True
    assert len(project.tasks) == 1
    assert project.tasks[0].description == "Test task"
    assert project.tasks[0].priority == "High"

    # Test numeric priority conversion
    assert project.add_task("Test task 2", 2) == True
    assert len(project.tasks) == 2
    assert project.tasks[1].priority == "Medium"


def test_add_task_validation():
    """Test add_task input validation."""
    # Test empty description
    assert project.add_task("", "High") == False
    assert len(project.tasks) == 0

    # Test whitespace-only description
    assert project.add_task("   ", "High") == False
    assert len(project.tasks) == 0

    # Test invalid numeric priority
    assert project.add_task("Test task", 5) == False
    assert len(project.tasks) == 0


def test_mark_task_complete():
    """Test marking tasks as complete."""
    # Add test tasks
    project.add_task("Task 1", "High")
    project.add_task("Task 2", "Medium")

    # Test successful completion
    assert project.mark_task_complete(1) == True
    assert project.tasks[0].completed is True

    # Test completing already completed task
    assert project.mark_task_complete(1) == False

    # Test invalid task ID
    assert project.mark_task_complete(99) == False


def test_mark_task_complete_empty_list():
    """Test marking task complete when no tasks exist."""
    assert project.mark_task_complete(1) == False


def test_delete_task():
    """Test deleting tasks."""
    # Add test tasks
    project.add_task("Task 1", "High")
    project.add_task("Task 2", "Medium")
    project.add_task("Task 3", "Low")

    # Delete middle task
    assert project.delete_task(2) == True
    assert len(project.tasks) == 2

    # Check ID reindexing
    assert project.tasks[0].id == 1
    assert project.tasks[0].description == "Task 1"
    assert project.tasks[1].id == 2
    assert project.tasks[1].description == "Task 3"

    # Test invalid task ID
    assert project.delete_task(99) == False


def test_delete_task_empty_list():
    """Test deleting task when no tasks exist."""
    assert project.delete_task(1) == False


def test_save_and_load_tasks():
    """Test saving and loading tasks with actual CSV file."""
    # Backup original CSV if it exists
    backup_file = None
    if os.path.exists("tasks.csv"):
        with open("tasks.csv", "r") as file:
            backup_content = file.read()
        backup_file = "tasks_backup.csv"
        with open(backup_file, "w") as file:
            file.write(backup_content)
        os.unlink("tasks.csv")

    try:
        # Add test tasks
        project.add_task("Task 1", "High")
        project.add_task("Task 2", "Medium")

        # Test save
        assert project.save_tasks() == True
        assert os.path.exists("tasks.csv")

        # Clear tasks and test load
        project.tasks.clear()
        assert project.load_tasks() == True
        assert len(project.tasks) == 2
        assert project.tasks[0].description == "Task 1"
        assert project.tasks[0].completed == False
        assert project.tasks[1].description == "Task 2"
        assert project.tasks[1].completed == False

    finally:
        # Cleanup test file
        if os.path.exists("tasks.csv"):
            os.unlink("tasks.csv")

        # Restore backup if it existed
        if backup_file and os.path.exists(backup_file):
            os.rename(backup_file, "tasks.csv")


def test_load_nonexistent_file():
    """Test loading from non-existent file."""
    # Ensure tasks.csv doesn't exist temporarily
    backup_exists = os.path.exists("tasks.csv")
    if backup_exists:
        os.rename("tasks.csv", "tasks_temp_backup.csv")

    try:
        assert project.load_tasks() == False
        assert len(project.tasks) == 0
    finally:
        # Restore backup if it existed
        if backup_exists:
            os.rename("tasks_temp_backup.csv", "tasks.csv")
            # Reload the original tasks
            project.load_tasks()


def test_task_str_method():
    """Test Task string representation."""
    task1 = Task(1, "Test task", "High", completed=False)
    task2 = Task(2, "Completed task", "Low", completed=True)

    assert "○" in str(task1)  # Pending task
    assert "✓" in str(task2)  # Completed task
    assert "Test task" in str(task1)
    assert "High" in str(task1)
