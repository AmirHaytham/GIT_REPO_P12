# Exercise 1: Git Basics
## Setting Up Your First Repository

### 🎯 Objective
Learn the basic Git workflow by creating a repository and making your first commits.

### 📋 Prerequisites
- Git installed
- Text editor
- Terminal/Command prompt

### 🔨 Tasks

#### 1. Repository Setup
```bash
# Initialize a new repository
git init my-first-repo

# Navigate to the repository
cd my-first-repo
```

#### 2. First Commit
```bash
# Create a README file
echo "# My First Repository" > README.md

# Stage the file
git add README.md

# Commit the file
git commit -m "📝 Initial commit: Add README"
```

#### 3. Making Changes
```bash
# Edit README.md
echo "This is my first Git repository" >> README.md

# Check status
git status

# Stage and commit changes
git add README.md
git commit -m "✨ Update: Add description to README"
```

#### 4. Viewing History
```bash
# View commit history
git log

# View changes
git diff HEAD~1
```

### ✅ Verification
- Repository is initialized
- README.md exists
- Two commits in history
- Changes visible in diff

### 🎓 Learning Outcomes
- Basic Git commands
- Repository initialization
- Staging changes
- Creating commits
- Viewing history

### 🔍 Extra Challenge
1. Add more files
2. Create .gitignore
3. View specific commits
4. Compare different versions
