# gemiTask Documentation

Welcome to gemiTask documentation! This guide will help you get started and make the most of your AI-powered task management.

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Features](#features)
4. [Command Reference](#command-reference)
5. [Configuration](#configuration)
6. [Advanced Usage](#advanced-usage)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)

## Installation

### From PyPI
```bash
pip install gemiTask
```

### From Source
```bash
git clone https://github.com/sanjaymalladi/gemiTask.git
cd gemiTask
pip install -e .
```

## Quick Start

1. **Get your Gemini API key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy your API key

2. **Configure gemiTask**
   ```bash
   # Create config directory
   mkdir -p ~/.config/gemiTask
   
   # Create config file
   echo '{
     "gemini_api_key": "your-api-key-here"
   }' > ~/.config/gemiTask/config.json
   ```

3. **Add your first task**
   ```bash
   gemiTask add "Build a landing page for product launch"
   ```

## Features

### 🤖 AI-Powered Task Breakdown
gemiTask uses Google's Gemini AI to analyze your tasks and break them down into actionable steps. When you add a task, the AI will:
- Suggest subtasks
- Estimate time requirements
- Identify dependencies
- Set appropriate deadlines
- Assign priority levels

### 📝 Natural Language Input
Describe your tasks naturally:
```bash
gemiTask add "Create a blog post about Python best practices"
gemiTask add "Plan next week's team meeting"
```

### ⏱️ Smart Time Management
- Automatic time estimates
- Deadline suggestions
- Priority-based scheduling
- Progress tracking

### 📋 Task Organization
- Subtask management
- Dependency tracking
- Priority levels (⭐ to ⭐⭐⭐⭐⭐)
- Status tracking

## Command Reference

### Task Management
```bash
# Add a new task
gemiTask add "Your task description"

# List all tasks
gemiTask list

# Show completed tasks
gemiTask list --done

# Mark task as done
gemiTask done <task_id>

# Get task breakdown
gemiTask breakdown <task_id>

# Get next task suggestion
gemiTask suggest
```

### Task Properties
Each task includes:
- Description
- Priority (1-5)
- Deadline
- Subtasks
- Dependencies
- Estimated time
- Completion status

## Configuration

### Config File Location
- Linux/Mac: `~/.config/gemiTask/config.json`
- Windows: `%APPDATA%\gemiTask\config.json`

### Configuration Options
```json
{
  "gemini_api_key": "your-api-key-here",
  "default_priority": 3,
  "date_format": "YYYY-MM-DD",
  "time_format": "24h"
}
```

## Advanced Usage

### Task Dependencies
Tasks can depend on other tasks:
```bash
# Add a dependent task
gemiTask add "Deploy to production" --depends-on 1
```

### Custom Priority
```bash
# Add high priority task
gemiTask add "Fix critical bug" --priority 1
```

### Export Tasks
```bash
# Export to JSON
gemiTask export tasks.json

# Export to CSV
gemiTask export tasks.csv
```

## Troubleshooting

### Common Issues

1. **API Key Issues**
   - Ensure your Gemini API key is valid
   - Check config file permissions
   - Verify API key format

2. **Task Creation Fails**
   - Check internet connection
   - Verify API key
   - Check task description format

3. **Storage Issues**
   - Verify write permissions
   - Check disk space
   - Ensure valid JSON format

### Getting Help
- Open an issue on GitHub
- Check existing issues
- Join our community

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Clone repository
git clone https://github.com/sanjaymalladi/gemiTask.git

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
flake8
```

### Code Style
- Follow PEP 8
- Use type hints
- Write tests for new features
- Update documentation 