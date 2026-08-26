---
name: update-problem
description: Reconcile an existing LeetCode problem's folder under problems/ with its row in the README.md Problems table - refresh the statement, check which solution files are implemented and passing, and fix the README checkmarks/link if they're out of date. Use when the user wants to update, sync, or fix the info for a problem they've already added.
---

# Update Problem

Same idea as `create-problem`, but for a problem that already has a folder under `problems/`. Never creates new files or folders - only reconciles state that already exists.

## Parameters

- **Problem name** (required) - the LeetCode problem title or number. If not given, ask with `AskUserQuestion`.

## Steps

1. **Resolve the problem name.** If missing, ask via `AskUserQuestion`.

2. **Find the existing folder** under `problems/` matching this problem (match on number if given, else fuzzy-match the snake_case title). If no matching folder exists, tell the user and suggest `create-problem` instead - do not create one yourself.

3. **Check the problem statement.** If the folder has no `README.md` (this repo has older problems predating that convention) or it looks stale, fetch the current statement from LeetCode/NeetCode (same lookup as `create-problem` step 2) and write/refresh `problems/{folder}/README.md`.

4. **Check each solution file that exists** in the folder (`solution.py`, `solution.js`, `solution.go`, `solution.java`, or numbered variants like `solution1.py` already present in this folder) - is it non-empty, and does running it reproduce the expected output from the problem's examples? Use the same run commands as `create-problem`:
   - Python: `python3 solution.py`
   - JavaScript: `node solution.js`
   - Go: `go run solution.go`
   - Java: `javac solution.java && java solution`

   Do not write or edit solution files yourself - only inspect and run what's already there.

5. **Reconcile the README.md Problems table row** for this problem:
   - If there's no row yet, add one in numeric order (same row format as `create-problem` step 6).
   - Otherwise, diff the row's checkmarks against step 4's findings and correct any mismatch (add `✅` for a language now implemented+passing, remove it if the file is missing/empty/failing).
   - Make sure the row's link (`problems/{folder}/`) still resolves to the actual folder name - fix it if the folder was renamed.

Report back a short summary of what changed (or that everything was already in sync) rather than silently editing.
