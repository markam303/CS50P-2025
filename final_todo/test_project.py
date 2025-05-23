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