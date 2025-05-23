import pytest
import os
import csv

from project import Task, add_task, mark_task_complete, delete_task, save_tasks


@pytest.fixture
def empty():
    """Fixture of empty task list."""
    global tasks 
    tasks = []
    yield
    # Cleanup
    tasks = []

def test_create_task(empty):
    """Test task creation."""
    add_task("Test task", "Medium")
    assert len(tasks) == 1
    assert tasks[1].description == "Test task"
    assert tasks[1].priority == "Medium"
    assert not tasks[1].completed
    

def test_mark_completed(empty):
    """Test task completion function."""
    add_task("Test task", "High")
    mark_task_complete(1)
    assert tasks[1].completed
    

def test_delete_task(empty):
    """Test deletion of tasks."""
    add_task("Test task 1", "High")
    add_task("Test task 2", "Medium")
    delete_task(1)
    assert len(tasks) == 1
    assert tasks[1].id == 1
    
    
def test_priority_validation_error():
    """Test priority validation with raising error."""
    with pytest.raises(ValueError):
        Task(task_id=1, description="Test", priority="0")
        

def test_priority_validation():
    """"Test priority validation with valid input."""
    add_task("Test task", 1)
    assert tasks[1].priority == "High"
    

def test_save_load_cycle(empty):
    """Test full save and load cycle."""
    add_task("Test save", "Low")
    save_tasks()
    assert os.path.exists("tasks.csv")
    
    new_tasks = []
    with open("tasks.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_tasks.append(Task.from_dict(row))
    
    assert len(new_tasks) == 1
    assert new_tasks[0].description == "Test save"
    