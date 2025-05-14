from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gemiTask",
    version="0.1.4",
    author="Sanjay Malladi",
    author_email="malladisanjay29@gmail.com",
    description="A CLI task manager with AI-powered task details generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanjaymalladi/gemiTask",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.7",
    install_requires=[
        "google-generativeai>=0.3.0",
        "python-dateutil>=2.8.2",
        "rich>=10.0.0",  # For beautiful terminal interface
        "typing-extensions>=4.0.0",  # For type hints
        "pydantic>=2.0.0",  # For data validation
    ],
    entry_points={
        "console_scripts": [
            "gemiTask=gemiTask.main:main",
        ],
    },
    keywords=[
        "cli",
        "task-management",
        "ai",
        "gemini",
        "productivity",
        "todo",
        "task-breakdown",
        "project-management",
        "terminal",
        "command-line",
    ],
    project_urls={
        "Bug Reports": "https://github.com/sanjaymalladi/gemiTask/issues",
        "Source": "https://github.com/sanjaymalladi/gemiTask",
        "Documentation": "https://github.com/sanjaymalladi/gemiTask/blob/main/README.md",
    },
) 