# 🌳 Exercise 2: Feature Branch Workflow
[![Level](https://img.shields.io/badge/level-intermediate-yellow.svg)](https://github.com/AmirHaytham/git-a-head)
[![Time](https://img.shields.io/badge/time-45%20minutes-blue.svg)](https://github.com/AmirHaytham/git-a-head)
[![Category](https://img.shields.io/badge/category-branching-brightgreen.svg)](https://github.com/AmirHaytham/git-a-head)

> Learn how to use feature branches for developing new features in isolation.

## 🎯 Objectives
By completing this exercise, you will learn to:
- 🌿 Create new feature branches
- 🔄 Switch between branches
- 🔀 Merge branches
- 🧹 Delete unused branches
- 📊 Visualize branch structure

## 📋 Prerequisites
- ✅ Completed Basic Git exercises
- ✅ Understanding of basic Git commands
- ✅ Git repository initialized

## 🔨 Tasks

### 1️⃣ Create Feature Branch
```bash
# Create and switch to new feature branch
git checkout -b feature/user-authentication

# Verify you're on the new branch
git branch
```

### 2️⃣ Develop the Feature
```bash
# Create a new file for the feature
echo "# User Authentication Module" > auth.md
echo "1. Login functionality" >> auth.md
echo "2. Registration system" >> auth.md

# Stage and commit changes
git add auth.md
git commit -m "✨ Add: User authentication structure"

# Make more changes
echo "3. Password reset" >> auth.md
git commit -am "✨ Add: Password reset feature"
```

### 3️⃣ Update from Master
```bash
# Get latest changes from master
git checkout master
git pull
git checkout feature/user-authentication
git merge master
```

### 4️⃣ Complete Feature
```bash
# Final touches to the feature
echo "4. Email verification" >> auth.md
git commit -am "✨ Add: Email verification"
```

### 5️⃣ Merge Back to Master
```bash
git checkout master
git merge feature/user-authentication
git push origin master
```

## ✅ Verification Steps
1. Feature branch exists locally
2. Multiple commits in feature branch
3. Clean merge with master
4. All changes visible in master

## 🎓 Learning Outcomes
- Feature branch creation
- Isolated development
- Branch switching
- Merging strategies
- Keeping branches up-to-date

## 🔍 Extra Challenges
1. Create multiple feature branches
2. Handle merge conflicts
3. Use interactive rebase
4. Create pull request

## 🔄 Clean Up
```bash
# Delete feature branch after merging
git branch -d feature/user-authentication
```

## 📚 Further Reading
- [Git Branching Documentation](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [Git Merge Documentation](https://git-scm.com/docs/git-merge)
- [Git Branch Documentation](https://git-scm.com/docs/git-branch)

## 🎨 Branch Visualization
```
main       A---B---C---D
            \         /
feature      E---F---G
```

---
<p align="center">
Created by <a href="https://github.com/AmirHaytham">Amir Haytham</a> for the Git-A-Head Workshop
</p>
