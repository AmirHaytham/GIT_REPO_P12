# 🎣 Exercise 5: Git Hooks

[![Level](https://img.shields.io/badge/level-advanced-red.svg)](https://github.com/AmirHaytham/git-a-head)
[![Time](https://img.shields.io/badge/time-60%20minutes-blue.svg)](https://github.com/AmirHaytham/git-a-head)
[![Category](https://img.shields.io/badge/category-hooks-purple.svg)](https://github.com/AmirHaytham/git-a-head)

> Learn how to automate Git workflows using hooks

## 🎯 Objectives
By completing this exercise, you will learn to:
- 🔄 Create custom Git hooks
- 🛠️ Automate Git workflows
- 🧪 Implement pre-commit checks
- 📊 Add commit message validation
- 🔍 Set up automated testing

## 📋 Prerequisites
- ✅ Strong Git fundamentals
- ✅ Basic shell scripting
- ✅ Understanding of Git internals
- ✅ Completed previous exercises

## 🚀 Steps

### 1️⃣ Setup Hooks Directory
```bash
# Navigate to hooks directory
cd .git/hooks

# Create backup of sample hooks
mkdir samples
mv *.sample samples/
```

### 2️⃣ Create Pre-commit Hook
```bash
# Create pre-commit hook
cat > pre-commit << 'EOF'
#!/bin/bash

echo "🔍 Running pre-commit checks..."

# Check for trailing whitespace
if git diff --cached --check; then
    echo "✅ No trailing whitespace found"
else
    echo "❌ Found trailing whitespace"
    exit 1
fi

# Run tests if they exist
if [ -f "pytest" ]; then
    echo "🧪 Running tests..."
    python -m pytest
fi

echo "✨ Pre-commit checks passed!"
exit 0
EOF

chmod +x pre-commit
```

### 3️⃣ Create Commit-msg Hook
```bash
# Create commit-msg hook
cat > commit-msg << 'EOF'
#!/bin/bash

commit_msg=$(cat "$1")
pattern="^(feat|fix|docs|style|refactor|test|chore):.+$"

if [[ $commit_msg =~ $pattern ]]; then
    echo "✅ Commit message format is valid"
    exit 0
else
    echo "❌ Invalid commit message format"
    echo "Format should be: <type>: <description>"
    echo "Types: feat, fix, docs, style, refactor, test, chore"
    exit 1
fi
EOF

chmod +x commit-msg
```

### 4️⃣ Create Pre-push Hook
```bash
# Create pre-push hook
cat > pre-push << 'EOF'
#!/bin/bash

echo "🚀 Running pre-push checks..."

# Run comprehensive tests
echo "🧪 Running full test suite..."
python -m pytest --verbose

# Check code coverage
if [ -f "coverage" ]; then
    echo "📊 Checking code coverage..."
    coverage run -m pytest
    coverage report --fail-under=80
fi

echo "✨ All pre-push checks passed!"
exit 0
EOF

chmod +x pre-push
```

## ✅ Expected Outcomes
- 🔄 Automated pre-commit checks
- 📝 Standardized commit messages
- 🧪 Automated test execution
- 🔍 Code quality enforcement

## 🔍 Testing the Hooks
1. Make changes to files
2. Try committing with invalid message
3. Try pushing with failing tests
4. Verify hook behaviors

## 🎯 Extra Challenges
Try implementing:
- [ ] Code formatting checks
- [ ] Branch name validation
- [ ] Issue number verification
- [ ] Custom error messages
- [ ] Hook bypass mechanism

## 🆘 Troubleshooting
Common issues and solutions:
- 🚫 Hook not executing: Check permissions
- ❌ Script errors: Debug with set -x
- ⚠️ Path issues: Use full paths
- 🔄 Hook bypass: Use --no-verify

## 🔧 Hook Types
| Hook | Timing | Common Uses |
|------|---------|------------|
| pre-commit | Before commit creation | Code quality checks |
| commit-msg | After commit message written | Message validation |
| pre-push | Before push to remote | Comprehensive testing |
| post-commit | After commit creation | Notifications |

## 📚 Further Reading
- [Git Hooks Documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- [Sample Git Hooks](https://github.com/git/git/tree/master/templates)
- [Hook Best Practices](https://www.atlassian.com/git/tutorials/git-hooks)

## 🔄 Clean Up
```bash
# Disable hooks if needed
cd .git/hooks
mv pre-commit pre-commit.disabled
mv commit-msg commit-msg.disabled
mv pre-push pre-push.disabled
```

---
<p align="center">
Created by <a href="https://github.com/AmirHaytham">Amir Haytham</a> for the Git-A-Head Workshop
</p>
