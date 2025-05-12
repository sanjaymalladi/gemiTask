from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gemiTask",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered terminal task manager using Google's Gemini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gemiTask",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Scheduling",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "google-generativeai>=0.3.0",
        "python-dateutil>=2.8.2",
    ],
    entry_points={
        "console_scripts": [
            "gemiTask=gemiTask.main:main",
        ],
    },
) 