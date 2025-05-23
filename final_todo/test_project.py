import pytest
import os
import csv
import tempfile
from project import Task, add_task, mark_task_complete, delete_task, save_tasks, load_tasks, tasks

# Fixtures for testing
@pytest.fixture
def clean_tasks():
    """Clean up tasks list before and after each test."""
    import project
    project.tasks.clear()
    yield
    project.tasks.clear()

@pytest.fixture
def temp_csv():
    """Create temporary CSV file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        temp_file = f.name
    yield temp_file
    # Cleanup
    if os.path.exists(temp_file):
        os.unlink(temp_file)

def test_task_creation():
    """Test basic Task object creation."""
    task = Task(1, "Test task", "High")
    
    assert task.id == 1
    assert task.description == "Test task"
    assert task.priority == "High"
    assert task.completed is False
    assert task.created is not None

def test_task_validation():
    """Test Task input validation."""
    # Test empty description
    with pytest.raises(ValueError, match="Task description cannot be empty"):
        Task(1, "", "High")
    
    # Test invalid priority
    with pytest.raises(ValueError, match="Priority must be"):
        Task(1, "Test task", "Invalid")

def test_task_mark_complete():
    """Test marking task as complete."""
    task = Task(1, "Test task", "Medium")
    
    # First completion should succeed
    result = task.mark_complete()
    assert result is True
    assert task.completed is True
    
    # Second completion should return False (already completed)
    result = task.mark_complete()
    assert result is False

def test_task_to_dict():
    """Test task dictionary conversion."""
    task = Task(1, "Test task", "Low", "2024-01-01", True)
    task_dict = task.to_dict()
    
    expected = {
        "id": 1,
        "description": "Test task",
        "priority": "Low",
        "created": "2024-01-01",
        "completed": True
    }
    assert task_dict == expected

def test_task_from_dict():
    """Test creating task from dictionary."""
    task_dict = {
        "id": "2",
        "description": "Test task 2",
        "priority": "High",
        "created": "2024-01-01",
        "completed": "true"
    }
    
    task = Task.from_dict(task_dict)
    assert task.id == 2
    assert task.description == "Test task 2"
    assert task.priority == "High"
    assert task.completed is True

def test_add_task(clean_tasks):
    """Test adding tasks to the list."""
    import project
    
    # Test successful addition
    result = add_task("Test task", "High")
    assert result is True
    assert len(project.tasks) == 1
    assert project.tasks[0].description == "Test task"
    assert project.tasks[0].priority == "High"
    
    # Test numeric priority conversion
    result = add_task("Test task 2", 2)
    assert result is True
    assert len(project.tasks) == 2
    assert project.tasks[1].priority == "Medium"

def test_add_task_validation(clean_tasks):
    """Test add_task input validation."""
    import project
    
    # Test empty description
    result = add_task("", "High")
    assert result is False
    assert len(project.tasks) == 0
    
    # Test invalid numeric priority
    result = add_task("Test task", 5)
    assert result is False
    assert len(project.tasks) == 0

def test_mark_task_complete(clean_tasks):
    """Test marking tasks as complete."""
    import project
    
    # Add test tasks
    add_task("Task 1", "High")
    add_task("Task 2", "Medium")
    
    # Test successful completion
    result = mark_task_complete(1)
    assert result is True
    assert project.tasks[0].completed is True
    
    # Test completing already completed task
    result = mark_task_complete(1)
    assert result is False
    
    # Test invalid task ID
    result = mark_task_complete(99)
    assert result is False

def test_delete_task(clean_tasks):
    """Test deleting tasks."""
    import project
    
    # Add test tasks
    add_task("Task 1", "High")
    add_task("Task 2", "Medium")
    add_task("Task 3", "Low")
    
    # Delete middle task
    result = delete_task(2)
    assert result is True
    assert len(project.tasks) == 2
    
    # Check ID reindexing
    assert project.tasks[0].id == 1
    assert project.tasks[1].id == 2
    assert project.tasks[1].description == "Task 3"
    
    # Test invalid task ID
    result = delete_task(99)
    assert result is False

def test_save_load_tasks(clean_tasks, temp_csv):
    """Test saving and loading tasks."""
    import project
    
    # Set temporary file path
    original_filename = "tasks.csv"
    
    # Add test tasks
    add_task("Task 1", "High")
    add_task("Task 2", "Medium")
    project.tasks[0].mark_complete()
    
    # Test save
    result = save_tasks()
    assert result is True
    assert os.path.exists("tasks.csv")
    
    # Clear tasks and test load
    project.tasks.clear()
    result = load_tasks()
    assert result is True
    assert len(project.tasks) == 2
    assert project.tasks[0].description == "Task 1"
    assert project.tasks[0].completed is True
    assert project.tasks[1].description == "Task 2"
    assert project.tasks[1].completed is False
    
    # Cleanup test file
    if os.path.exists("tasks.csv"):
        os.unlink("tasks.csv")

def test_load_nonexistent_file(clean_tasks):
    """Test loading from non-existent file."""
    import project
    
    # Ensure file doesn't exist
    if os.path.exists("nonexistent.csv"):
        os.unlink("nonexistent.csv")
    
    # Should return False but not crash
    assert load_tasks() == False
    assert len(project.tasks) == 0
