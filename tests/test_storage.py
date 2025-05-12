import pytest
import os
import json
from storage import add_task, list_tasks, mark_task_done, get_task

@pytest.fixture
def temp_storage(tmp_path):
    # Create a temporary tasks.json file
    tasks_file = tmp_path / "tasks.json"
    with open(tasks_file, 'w') as f:
        json.dump([], f)
    return str(tasks_file)

def test_add_task(temp_storage):
    task = {"description": "Test task", "done": False}
    add_task(task)
    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Test task"

def test_mark_task_done(temp_storage):
    task = {"description": "Test task", "done": False}
    add_task(task)
    mark_task_done(0)
    tasks = list_tasks()
    assert tasks[0]["done"]

def test_get_task(temp_storage):
    task = {"description": "Test task", "done": False}
    add_task(task)
    retrieved_task = get_task(0)
    assert retrieved_task["description"] == "Test task"
    assert not retrieved_task["done"]

def test_get_nonexistent_task(temp_storage):
    assert get_task(999) is None 