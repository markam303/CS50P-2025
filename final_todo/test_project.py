import pytest
import os
from project import Task, add_task, mark_task_complete, delete_task


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
    assert tasks[0].description == "Test task"
    assert tasks[0].priority == "Medium"
    assert not tasks[0].completed
    

def test_mark_completed(empty):
    """Test task completion function."""
    add_task("Test task", "High")
    mark_task_complete(1)
    assert tasks[0].completed
    

def test_delete_task(empty):
    """Test deletion of tasks."""
    add_task("Test task 1", "High")
    add_task("Test task 2", "Medium")
    delete_task(1)
    assert len(tasks) == 1
    assert tasks[0].id == 1
    
    
def test_priority_validation():
    """Test priority validation."""
    with pytest.raises(ValueError):
        Task(task_id=1, description="Test", priority="0")