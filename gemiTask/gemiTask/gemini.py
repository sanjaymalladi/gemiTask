import json
import os
import google.generativeai as genai
from typing import Dict, Any
from getpass import getpass
from .task import Task

def get_api_key() -> str:
    # First try environment variable
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key:
        return api_key
    
    # Then try config file
    try:
        config_path = os.path.join(os.path.expanduser('~'), '.config', 'gemiTask', 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                if 'gemini_api_key' in config:
                    return config['gemini_api_key']
    except Exception:
        pass
    
    # Finally, prompt user
    print("\n🔑 Gemini API Key not found!")
    print("Please enter your Gemini API key (get it from https://makersuite.google.com/app/apikey)")
    api_key = getpass("API Key: ").strip()
    
    # Save to config file for future use
    try:
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            json.dump({'gemini_api_key': api_key}, f)
        print("✅ API key saved for future use")
    except Exception as e:
        print(f"⚠️ Could not save API key: {str(e)}")
    
    return api_key

def init_gemini():
    api_key = get_api_key()
    if not api_key:
        raise ValueError("No API key provided. Please set GEMINI_API_KEY environment variable or use set-api-key command.")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Configure safety settings
    safety_settings = {
        "HARASSMENT": "block_none",
        "HATE_SPEECH": "block_none",
        "SEXUALLY_EXPLICIT": "block_none",
        "DANGEROUS_CONTENT": "block_none",
    }
    
    return model

def generate_task_details(description: str) -> Dict[str, Any]:
    try:
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
        
        response = model.generate_content(prompt)
        
        if not response or not response.text:
            raise ValueError("Empty response from Gemini API")
            
        # Extract JSON from the response
        response_text = response.text.strip()
        
        # Find the first { and last } to extract just the JSON object
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        
        if start < 0 or end <= start:
            raise ValueError("No JSON object found in response")
            
        json_str = response_text[start:end]
        task_details = json.loads(json_str)
        
        # Validate required fields
        required_fields = ['priority', 'deadline', 'estimated_time', 'subtasks']
        for field in required_fields:
            if field not in task_details:
                raise ValueError(f"Missing required field: {field}")
        
        return {
            'description': description,
            'done': False,
            'priority': min(max(task_details.get('priority', 3), 1), 5),  # Ensure priority is between 1-5
            'deadline': task_details.get('deadline'),
            'subtasks': task_details.get('subtasks', []),
            'dependencies': task_details.get('dependencies', []),
            'estimated_time': task_details.get('estimated_time')
        }
            
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