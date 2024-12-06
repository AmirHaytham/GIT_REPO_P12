# Exercise 2: Feature Branch Workflow
## Working with Feature Branches

### 🎯 Objective
Learn how to use feature branches for developing new features in isolation.

### 📋 Prerequisites
- Completed Basic Git Exercise
- Understanding of basic Git commands
- Git repository initialized

### 🔨 Tasks

#### 1. Create Feature Branch
```bash
# Create and switch to new feature branch
git checkout -b feature/user-authentication

# Verify you're on the new branch
git branch
```

#### 2. Develop the Feature
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

#### 3. Update from Master
```bash
# Get latest changes from master
git checkout master
git pull
git checkout feature/user-authentication
git merge master
```

#### 4. Complete Feature
```bash
# Final touches to the feature
echo "4. Email verification" >> auth.md
git commit -am "✨ Add: Email verification"
```

#### 5. Merge Back to Master
```bash
git checkout master
git merge feature/user-authentication
git push origin master
```

### ✅ Verification Steps
1. Feature branch exists locally
2. Multiple commits in feature branch
3. Clean merge with master
4. All changes visible in master

### 🎓 Learning Outcomes
- Feature branch creation
- Isolated development
- Branch switching
- Merging strategies
- Keeping branches up-to-date

### 🔍 Extra Challenges
1. Create multiple feature branches
2. Handle merge conflicts
3. Use interactive rebase
4. Create pull request
