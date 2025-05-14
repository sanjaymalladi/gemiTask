import os
import shutil
from pathlib import Path

def fix_package_structure():
    # Get the current directory
    current_dir = Path.cwd()
    project_root = current_dir.parent if current_dir.name == 'gemiTask' else current_dir
    
    # Create package directory
    package_dir = project_root / 'gemiTask' / 'gemiTask'
    package_dir.mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py
    init_file = package_dir / '__init__.py'
    init_file.touch()
    
    # Move Python files
    python_files = [
        'main.py',
        'gemini.py',
        'storage.py',
        'task.py'
    ]
    
    for file in python_files:
        src = project_root / 'gemiTask' / file
        if src.exists():
            dst = package_dir / file
            shutil.move(str(src), str(dst))
            print(f"Moved {file} to package directory")
    
    print("\nPackage structure fixed! Now run:")
    print("pip uninstall gemiTask")
    print("pip install -e .")

if __name__ == '__main__':
    fix_package_structure() 