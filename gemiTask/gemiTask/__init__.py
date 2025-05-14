"""
gemiTask - A CLI task manager with AI-powered task details generation
"""

from .main import main
from .task import Task
from .storage import add_task, list_tasks, mark_task_done, get_task
from .gemini import generate_task_details, get_api_key

__version__ = "0.1.1"
__all__ = ["main", "Task", "add_task", "list_tasks", "mark_task_done", "get_task", "generate_task_details", "get_api_key"]
