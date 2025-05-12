import json
import os
import google.generativeai as genai
from typing import Dict, Any

def load_config() -> Dict[str, Any]:
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)

def init_gemini():
    config = load_config()
    genai.configure(api_key=config['gemini_api_key'])
    return genai.GenerativeModel('gemini-2.0-flash')

def generate_task_details(description: str) -> Dict[str, Any]:
    model = init_gemini()
    
    prompt = f"""You are a task management AI. Analyze this task and break it down into a structured format.
    Task: {description}
    
    Provide a JSON response with these exact fields:
    {{
        "priority": number (1-5, where 1 is highest),
        "deadline": string (YYYY-MM-DD format),
        "estimated_time": string (e.g., "2 hours", "3 days"),
        "subtasks": [
            {{
                "description": string,
                "estimated_time": string
            }}
        ],
        "dependencies": [string]
    }}

    Make sure to:
    1. Break down the task into 3-5 logical subtasks
    2. Estimate realistic timeframes
    3. Identify any dependencies
    4. Set a reasonable deadline
    5. Return ONLY the JSON object, no other text
    """
    
    try:
        response = model.generate_content(prompt)
        # Extract JSON from the response
        response_text = response.text.strip()
        # Find the first { and last } to extract just the JSON object
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        if start >= 0 and end > start:
            json_str = response_text[start:end]
            task_details = json.loads(json_str)
            
            return {
                'description': description,
                'done': False,
                'priority': task_details.get('priority', 3),
                'deadline': task_details.get('deadline'),
                'subtasks': task_details.get('subtasks', []),
                'dependencies': task_details.get('dependencies', []),
                'estimated_time': task_details.get('estimated_time')
            }
        else:
            raise ValueError("No JSON object found in response")
            
    except Exception as e:
        print(f"Warning: AI analysis failed: {str(e)}")
        # Fallback to basic task creation with some default subtasks
        return {
            'description': description,
            'done': False,
            'priority': 3,
            'subtasks': [
                {'description': 'Research and gather requirements', 'estimated_time': '2 hours'},
                {'description': 'Create initial design mockup', 'estimated_time': '4 hours'},
                {'description': 'Implement core functionality', 'estimated_time': '8 hours'},
                {'description': 'Test and refine', 'estimated_time': '4 hours'}
            ],
            'dependencies': [],
            'estimated_time': '18 hours'
        } 