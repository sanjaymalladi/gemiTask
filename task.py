from datetime import datetime
from typing import List, Optional

class Task:
    def __init__(
        self,
        description: str,
        done: bool = False,
        priority: int = 3,  # 1 (highest) to 5 (lowest)
        deadline: Optional[str] = None,
        subtasks: List[dict] = None,
        dependencies: List[str] = None,
        estimated_time: Optional[str] = None,
        created_at: Optional[str] = None
    ):
        self.description = description
        self.done = done
        self.priority = priority
        self.deadline = deadline
        self.subtasks = subtasks or []
        self.dependencies = dependencies or []
        self.estimated_time = estimated_time
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        return {
            'description': self.description,
            'done': self.done,
            'priority': self.priority,
            'deadline': self.deadline,
            'subtasks': self.subtasks,
            'dependencies': self.dependencies,
            'estimated_time': self.estimated_time,
            'created_at': self.created_at
        }

    @staticmethod
    def from_dict(data: dict) -> 'Task':
        return Task(
            description=data.get('description', ''),
            done=data.get('done', False),
            priority=data.get('priority', 3),
            deadline=data.get('deadline'),
            subtasks=data.get('subtasks', []),
            dependencies=data.get('dependencies', []),
            estimated_time=data.get('estimated_time'),
            created_at=data.get('created_at')
        )

    def __str__(self) -> str:
        status = '✓' if self.done else ' '
        priority_stars = '⭐' * (6 - self.priority)
        deadline_str = f" (due: {self.deadline})" if self.deadline else ""
        time_str = f" [⏱️ {self.estimated_time}]" if self.estimated_time else ""
        return f"[{status}] {priority_stars} {self.description}{deadline_str}{time_str}" 