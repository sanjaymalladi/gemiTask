# gemiTask

A powerful AI-powered command-line task management tool that helps you easily manage and track task progress with the help of Google's Gemini AI.

## Features

- 🤖 AI-Powered Task Analysis: Break down complex tasks into actionable steps
- 📝 Natural Language Input: Describe tasks in plain English
- 🌲 Subtask Support: Break down large tasks into manageable subtasks
- 🔄 Task Status Tracking: Track task progress (pending, in progress, done)
- ⭐ Priority Management: Set priority levels from 1 (highest) to 5 (lowest)
- 🔗 Task Dependencies: Set dependencies between tasks
- 💾 Local Storage: Auto-save task data in JSON format
- 🎨 Beautiful Terminal Interface: Clear visual display with Rich
- 🔑 Flexible API Key Management: Multiple ways to set your Gemini API key

## Installation

```bash
pip install gemiTask
```

## Quick Start

1. **Get your Gemini API key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy your API key

2. **Set up your API key** (Choose one method)
   ```bash
   # Method 1: Set via command line
   gemiTask set-api-key
   # Or directly with the key:
   gemiTask set-api-key --key "your-api-key"

   # Method 2: Set via environment variable
   export GEMINI_API_KEY="your-api-key"  # Linux/Mac
   set GEMINI_API_KEY=your-api-key       # Windows
   ```

## Usage

### 1. Add a New Task
```bash
# Basic usage
gemiTask add "Complete project documentation"

# Add with priority (1-5, where 1 is highest)
gemiTask add "Complete project documentation" -p 1

# Add with deadline
gemiTask add "Complete project documentation" -d "2024-03-20"

# Add with both priority and deadline
gemiTask add "Complete project documentation" -p 1 -d "2024-03-20"
```

### 2. List Tasks
```bash
# List all tasks
gemiTask list

# List completed tasks
gemiTask list --done

# Example output:
# 📋 Task List
# └── 1: Project Documentation (Priority: 1)
#     ├── Deadline: 2024-03-20
#     ├── Estimated Time: 18 hours
#     └── Subtasks:
#         ├── 1.1: Research and gather requirements (2 hours)
#         └── 1.2: Create initial design mockup (4 hours)
```

### 3. Task Management
```bash
# Mark task as done
gemiTask done 1

# Get detailed task breakdown
gemiTask breakdown 1

# Get AI suggestions for next task
gemiTask suggest
```

### 4. Task Details
Each task includes:
- Description
- Priority (1-5)
- Deadline
- Subtasks with time estimates
- Dependencies
- Estimated total time
- Completion status

## Advanced Features

### AI-Powered Task Breakdown
When you add a task, gemiTask uses Gemini AI to:
- Break down the task into logical subtasks
- Estimate realistic timeframes
- Identify dependencies
- Suggest appropriate deadlines
- Set priority levels

### Smart Task Suggestions
The `suggest` command uses AI to:
- Analyze task priorities
- Consider deadlines
- Check dependencies
- Recommend the next best task to work on

## Data Storage

Task data is stored in `tasks.json` in your project directory. This enables:
- Version control of task data with project code
- Easy sharing of task status in teams
- Simple viewing and editing of task data

## Use Cases

### Personal Project Management
- Track project progress
- Break down large tasks
- Prioritize work
- Get AI-powered task breakdowns

### Team Collaboration
- Manage tasks in code repositories
- Share task status via Git
- Track dependencies
- Coordinate work with AI assistance

### Daily Work Management
- To-do list management
- Progress tracking
- Task planning
- Smart task prioritization

## Development

### Install Development Dependencies
```bash
pip install -e ".[dev]"
```

### Run Tests
```bash
pytest
```

### Build Project
```bash
python -m build
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. See our [Contributing Guide](CONTRIBUTING.md) for details.

## Author

- Sanjay Malladi (@sanjaymalladi)
- Email: malladisanjay29@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Links

- [GitHub](https://github.com/sanjaymalladi/gemiTask)
- [PyPI](https://pypi.org/project/gemiTask/)
- [Issue Tracker](https://github.com/sanjaymalladi/gemiTask/issues)
- [Documentation](https://github.com/sanjaymalladi/gemiTask/blob/main/README.md) 