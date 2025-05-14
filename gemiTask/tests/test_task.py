import pytest
from task import Task

def test_task_creation():
    task = Task("Test task")
    assert task.description == "Test task"
    assert not task.done
    assert task.priority == 3
    assert not task.subtasks
    assert not task.dependencies

def test_task_with_subtasks():
    subtasks = [
        {"description": "Subtask 1", "estimated_time": "1 hour"},
        {"description": "Subtask 2", "estimated_time": "2 hours"}
    ]
    task = Task("Test task", subtasks=subtasks)
    assert len(task.subtasks) == 2
    assert task.subtasks[0]["description"] == "Subtask 1"

def test_task_to_dict():
    task = Task("Test task", priority=1, deadline="2024-12-31")
    task_dict = task.to_dict()
    assert task_dict["description"] == "Test task"
    assert task_dict["priority"] == 1
    assert task_dict["deadline"] == "2024-12-31"

def test_task_from_dict():
    task_dict = {
        "description": "Test task",
        "done": True,
        "priority": 2,
        "deadline": "2024-12-31",
        "subtasks": [{"description": "Subtask 1", "estimated_time": "1 hour"}],
        "dependencies": ["Task 1"]
    }
    task = Task.from_dict(task_dict)
    assert task.description == "Test task"
    assert task.done
    assert task.priority == 2
    assert task.deadline == "2024-12-31"
    assert len(task.subtasks) == 1
    assert len(task.dependencies) == 1 