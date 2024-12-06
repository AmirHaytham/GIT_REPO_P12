# 🎯 Exercise 1: Git Basics

[![Level](https://img.shields.io/badge/level-beginner-green.svg)](https://github.com/AmirHaytham/git-a-head)
[![Time](https://img.shields.io/badge/time-30%20minutes-blue.svg)](https://github.com/AmirHaytham/git-a-head)
[![Category](https://img.shields.io/badge/category-basics-orange.svg)](https://github.com/AmirHaytham/git-a-head)

> Master the fundamental Git commands and workflow

## 🎯 Objectives
By completing this exercise, you will:
- 📝 Create your first Git repository
- ✨ Make your first commit
- 📜 View repository history
- 🔍 Check repository status

## 📋 Prerequisites
- ✅ Git installed on your machine
- ✅ Basic command line knowledge
- ✅ Text editor of your choice

## 🚀 Steps

### 1️⃣ Repository Setup
```bash
# Initialize a new repository
git init my-first-repo
cd my-first-repo
```

### 2️⃣ Create Content
```bash
# Create a new file
echo "# My First Git Project" > README.md
```

### 3️⃣ Stage Changes
```bash
# Add file to staging area
git add README.md
```

### 4️⃣ Commit Changes
```bash
# Make your first commit
git commit -m "Initial commit: Add README"
```

### 5️⃣ View History
```bash
# Check repository status
git status

# View commit history
git log
```

## ✅ Expected Outcome
- A new Git repository is created
- README.md file is tracked
- First commit is recorded
- Clean working directory

## 🔍 Verification
Run these commands to verify your work:
```bash
git status  # Should show "nothing to commit"
git log     # Should show your commit
```

## 🎯 Extra Challenge
Try these additional tasks:
- [ ] Add more content to README.md
- [ ] Make multiple commits
- [ ] Use git diff to see changes
- [ ] Practice git status

## 🆘 Troubleshooting
Common issues and solutions:
- 🚫 "Not a git repository": Make sure you're in the correct directory
- ❌ "Nothing to commit": Ensure you've made changes to tracked files
- ⚠️ "Untracked files": Use git add to start tracking files

## 🔄 Clean Up
```bash
# Optional: Remove the repository when done
cd ..
rm -rf my-first-repo
```

## 📚 Further Reading
- [Git Basics Documentation](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
- [Git Init Documentation](https://git-scm.com/docs/git-init)
- [Git Commit Documentation](https://git-scm.com/docs/git-commit)

---
<p align="center">
Created by <a href="https://github.com/AmirHaytham">Amir Haytham</a> for the Git-A-Head Workshop
</p>
