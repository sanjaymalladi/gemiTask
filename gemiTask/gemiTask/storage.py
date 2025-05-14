import json
import os
from typing import List, Dict, Any, Optional
from .task import Task

tasks_file = os.path.join(os.path.dirname(__file__), 'tasks.json')

def _load_tasks() -> List[Dict[str, Any]]:
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, 'r') as f:
        return json.load(f)

def _save_tasks(tasks: List[Dict[str, Any]]) -> None:
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(task: Dict[str, Any]) -> None:
    tasks = _load_tasks()
    tasks.append(task)
    _save_tasks(tasks)

def list_tasks() -> List[Dict[str, Any]]:
    return _load_tasks()

def get_task(task_id: int) -> Optional[Dict[str, Any]]:
    tasks = _load_tasks()
    if 0 <= task_id < len(tasks):
        return tasks[task_id]
    return None

def mark_task_done(task_id: int) -> None:
    tasks = _load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
        _save_tasks(tasks) 