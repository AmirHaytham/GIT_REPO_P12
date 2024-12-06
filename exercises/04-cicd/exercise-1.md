# Exercise 4: CI/CD with GitHub Actions
## Setting up Continuous Integration and Deployment

### 🎯 Objective
Learn how to implement CI/CD pipelines using GitHub Actions and Git.

### 📋 Prerequisites
- GitHub account
- Basic Git knowledge
- Python basics (for sample application)

### 🔨 Part 1: Basic CI Pipeline

#### 1. Create Sample Python Application
```python
# app.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# test_app.py
import unittest
from app import add, subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
```

#### 2. Setup GitHub Actions
Create `.github/workflows/ci.yml`:
```yaml
name: Python CI

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
    - name: Run tests
      run: |
        pytest test_app.py
```

### 🔨 Part 2: Adding Code Quality Checks

#### 1. Add Linting
Update `ci.yml`:
```yaml
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest flake8
    - name: Lint with flake8
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

### 🔨 Part 3: Automated Deployment

#### 1. Create Deploy Configuration
Create `.github/workflows/cd.yml`:
```yaml
name: Deploy

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    - name: Build
      run: |
        echo "Building package..."
    - name: Create Release
      uses: actions/create-release@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        tag_name: ${{ github.ref }}
        release_name: Release ${{ github.ref }}
        draft: false
        prerelease: false
```

### ✅ Practice Tasks
1. Set up the sample Python application
2. Configure GitHub Actions for CI
3. Add code quality checks
4. Create a test release

### 🎓 Learning Outcomes
- GitHub Actions configuration
- CI/CD pipeline setup
- Automated testing
- Release management
- Code quality automation

### 🔍 Extra Challenges
1. Add code coverage reporting
2. Implement multiple Python versions testing
3. Create Docker deployment
4. Add security scanning
5. Implement automatic version bumping
