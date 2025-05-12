import argparse
from storage import add_task, list_tasks, mark_task_done, get_task
from gemini import generate_task_details
from task import Task
from typing import List

parser = argparse.ArgumentParser(prog='gemiTask', description='AI-powered CLI Task Manager')
subparsers = parser.add_subparsers(dest='command')

# Add task
add_parser = subparsers.add_parser('add', help='Add a new task')
add_parser.add_argument('description', type=str, help='Task description')

# List tasks
list_parser = subparsers.add_parser('list', help='List all tasks')
list_parser.add_argument('--done', action='store_true', help='Show completed tasks')

# Mark task as done
done_parser = subparsers.add_parser('done', help='Mark a task as done')
done_parser.add_argument('task_id', type=int, help='Task ID to mark as done')

# Task breakdown
breakdown_parser = subparsers.add_parser('breakdown', help='Show detailed breakdown of a task')
breakdown_parser.add_argument('task_id', type=int, help='Task ID to break down')

# Suggest next task
suggest_parser = subparsers.add_parser('suggest', help='Get AI suggestions for next task')

def print_task_list(tasks: List[Task], show_done: bool = False):
    if not tasks:
        print('No tasks found.')
        return
    
    for idx, task in enumerate(tasks, 1):
        if not show_done and task.done:
            continue
        print(f"{idx}. {task}")

def print_task_breakdown(task: Task):
    print(f"\n📋 Task: {task.description}")
    print(f"⏱️ Estimated Time: {task.estimated_time or 'Not specified'}")
    print(f"📅 Deadline: {task.deadline or 'Not specified'}")
    
    if task.subtasks:
        print("\n📝 Subtasks:")
        for idx, subtask in enumerate(task.subtasks, 1):
            print(f"  {idx}. {subtask['description']} ({subtask.get('estimated_time', 'No time estimate')})")
    
    if task.dependencies:
        print("\n🔗 Dependencies:")
        for dep in task.dependencies:
            print(f"  - {dep}")

def main():
    args = parser.parse_args()
    
    if args.command == 'add':
        task_details = generate_task_details(args.description)
        add_task(task_details)
        print(f"✅ Task added: {task_details['description']}")
        print_task_breakdown(Task.from_dict(task_details))
        
    elif args.command == 'list':
        tasks = [Task.from_dict(t) for t in list_tasks()]
        print_task_list(tasks, args.done)
        
    elif args.command == 'done':
        task = get_task(args.task_id - 1)
        if task:
            mark_task_done(args.task_id - 1)
            print(f"✅ Marked task as done: {task['description']}")
        else:
            print("❌ Task not found")
            
    elif args.command == 'breakdown':
        task = get_task(args.task_id - 1)
        if task:
            print_task_breakdown(Task.from_dict(task))
        else:
            print("❌ Task not found")
            
    elif args.command == 'suggest':
        tasks = [Task.from_dict(t) for t in list_tasks()]
        pending_tasks = [t for t in tasks if not t.done]
        if pending_tasks:
            # Sort by priority and deadline
            pending_tasks.sort(key=lambda x: (x.priority, x.deadline or '9999-12-31'))
            print("\n🎯 Suggested next task:")
            print_task_breakdown(pending_tasks[0])
        else:
            print("✨ No pending tasks! Time to add new ones.")
            
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 