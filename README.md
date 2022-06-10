# Thoth pre-commit hooks

## Usage

In `.pre-commit-config.yaml`:

```
---
repos:
  - repo: https://github.com/thoth-station/test-thoth-pre-commit-hook
    hooks:
      - id: thoth-advise
        args: ["--recommendation-type", "security"]
```
