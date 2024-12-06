# Exercise 3: Git Troubleshooting Scenarios
## Common Git Problems and Solutions

### 🎯 Objective
Learn how to handle common Git problems and fix mistakes.

### 📋 Prerequisites
- Basic Git knowledge
- Understanding of branching
- Completed previous exercises

### 🔨 Scenario 1: Fixing Bad Commits

#### Problem
You accidentally committed to the wrong branch

#### Solution
```bash
# Save your changes
git log -n 1  # Note the commit hash
git reset HEAD~1  # Undo the last commit, keeping changes
git stash  # Store the changes temporarily

# Switch to correct branch
git checkout correct-branch
git stash pop  # Apply the stored changes
git add .
git commit -m "✨ Add: Feature on correct branch"
```

### 🔨 Scenario 2: Resolving Merge Conflicts

#### Problem
Merge conflict when pulling changes

#### Solution
```bash
# Try to pull changes
git pull origin master

# If conflict occurs:
1. Open conflicted files
2. Look for conflict markers (<<<<<<, =======, >>>>>>>)
3. Edit files to resolve conflicts
4. Save files

# After resolving
git add .
git commit -m "🔀 Merge: Resolve conflicts with master"
```

### 🔨 Scenario 3: Recovering Lost Work

#### Problem
Accidentally deleted commits or lost work

#### Solution
```bash
# View reflog to find lost commits
git reflog

# Recover using reset or cherry-pick
git reset --hard HEAD@{2}  # Go back 2 positions
# OR
git cherry-pick <commit-hash>  # Pick specific commit
```

### 🔨 Scenario 4: Fixing Detached HEAD

#### Problem
Ended up in detached HEAD state

#### Solution
```bash
# Create new branch to save work
git branch temp-recovery

# Switch to the branch
git checkout temp-recovery

# Merge back to main branch if needed
git checkout master
git merge temp-recovery
```

### ✅ Practice Tasks
1. Create a commit on wrong branch and fix it
2. Create and resolve a merge conflict
3. Recover a deleted commit
4. Fix a detached HEAD state

### 🎓 Learning Outcomes
- Problem-solving in Git
- Recovery techniques
- Conflict resolution
- Understanding Git internals

### 🔍 Extra Challenges
1. Reset a pushed commit
2. Clean up multiple bad commits
3. Resolve complex merge conflicts
4. Recover deleted branches
