# Exercise 5: Git Hooks
## Automating Git Workflows with Hooks

### 🎯 Objective
Learn how to use Git hooks to automate tasks and enforce standards in your Git workflow.

### 📋 Prerequisites
- Basic Git knowledge
- Basic shell scripting
- Completed previous exercises

### 🔨 Part 1: Pre-commit Hook

#### 1. Create Basic Pre-commit Hook
```bash
# Navigate to hooks directory
cd .git/hooks

# Create pre-commit hook
touch pre-commit
chmod +x pre-commit
```

#### 2. Add Code Quality Check
Add to `pre-commit`:
```bash
#!/bin/bash

echo "🔍 Running pre-commit checks..."

# Check for Python syntax errors
for file in $(git diff --cached --name-only | grep ".py$")
do
    if [ -f $file ]; then
        python -m py_compile $file
        if [ $? -ne 0 ]; then
            echo "❌ Python syntax error in $file"
            exit 1
        fi
    fi
done

# Check for trailing whitespace
if git diff --cached --check; then
    echo "✅ No trailing whitespace found"
else
    echo "❌ Trailing whitespace found"
    exit 1
fi

echo "✅ All checks passed!"
exit 0
```

### 🔨 Part 2: Commit-msg Hook

#### 1. Create Commit Message Hook
```bash
# Create commit-msg hook
touch .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

#### 2. Add Commit Message Validation
Add to `commit-msg`:
```bash
#!/bin/bash

commit_msg_file=$1
commit_msg=$(cat $commit_msg_file)

# Check for emoji prefix
if ! echo "$commit_msg" | grep -qE "^(🎉|✨|🐛|📝|♻️|🔧|🔥|✅|🔒|⬆️|⬇️|👷|📦) .*$"; then
    echo "❌ Commit message must start with an emoji"
    echo "Valid emojis: 🎉 ✨ 🐛 📝 ♻️ 🔧 🔥 ✅ 🔒 ⬆️ ⬇️ 👷 📦"
    exit 1
fi

# Check message length
if [ ${#commit_msg} -lt 10 ]; then
    echo "❌ Commit message too short"
    exit 1
fi

echo "✅ Commit message format valid!"
exit 0
```

### 🔨 Part 3: Pre-push Hook

#### 1. Create Pre-push Hook
```bash
# Create pre-push hook
touch .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

#### 2. Add Test Runner
Add to `pre-push`:
```bash
#!/bin/bash

echo "🧪 Running tests before push..."

# Run Python tests
python -m pytest
if [ $? -ne 0 ]; then
    echo "❌ Tests failed, push aborted"
    exit 1
fi

echo "✅ All tests passed!"
exit 0
```

### ✅ Practice Tasks
1. Set up pre-commit hook
2. Create commit message template
3. Implement pre-push tests
4. Test each hook's functionality

### 🎓 Learning Outcomes
- Git hooks setup
- Automated quality checks
- Commit message standards
- Test automation
- Workflow customization

### 🔍 Extra Challenges
1. Add code formatting check
2. Implement branch name validation
3. Create custom hook combinations
4. Add performance benchmarks
5. Implement security checks
