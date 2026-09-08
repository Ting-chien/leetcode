---
name: update-problem
description: Use when the user wants to update, sync, or fix an existing LeetCode problem under problems/, or add a language (py/js/go/java) to a problem that already has a folder.
---

# Update Problem

Same idea as `create-problem`, but for a problem that already has a folder under `problems/`. Does not create a new problem folder; if none exists, tell the user to use `create-problem` instead.

## Parameters

- **Problem name** (required) - the LeetCode problem title or number. If not given, ask with `AskUserQuestion`.
- **Language(s)** (optional) - one or more of `py` (Python), `js` (JavaScript), `go` (Go), `java` (Java). When given, add that language if it is missing (step 4).

## Solution file naming

Every language starts at `solution1.<ext>`. Additional approaches are `solution2.<ext>`, `solution3.<ext>`, … Never create an unnumbered `solution.<ext>`.

Older folders may still have a legacy unnumbered `solution.<ext>`. Leave those in place (do not rename). Treat them as that language's first solution when deciding the next number and when checking README checkmarks. If the only existing file is `solution.py` and the user asks for another Python approach, the new file is `solution2.py`.

## Stubs only — no answers

When creating a solution file, write **only** the function/class signature and the problem's examples as test cases in `main` / `if __name__ == '__main__'`. Comments may note expected output.

**Do not implement the algorithm.** No DFS/BFS/DP/Union-Find, no porting another language's solution in the same folder, no filling in the body because the user asked to "add Go" or similar.

If the user pasted their own solution code, put that in the file as they wrote it. Do not invent an implementation.

## Steps

1. **Resolve the problem name.** If missing, ask via `AskUserQuestion`.

2. **Find the existing folder** under `problems/` matching this problem (match on number if given, else fuzzy-match the snake_case title). If no matching folder exists, tell the user and suggest `create-problem` instead - do not create one yourself.

3. **Check the problem statement.** If the folder has no `README.md` (this repo has older problems predating that convention) or it looks stale, fetch the current statement from LeetCode/NeetCode (same lookup as `create-problem` step 2) and write/refresh `problems/{folder}/README.md`.

4. **If languages were requested**, add missing solution files for those languages:
   - If that language has no files yet, create `solution1.<ext>` as a stub only (signature + test cases, no algorithm). Same stub style as `create-problem` step 5.
   - If they asked for multiple approaches, continue `solution2.<ext>`, `solution3.<ext>`, … — still stubs unless the user pasted the code.
   - Do not overwrite existing solution files.

5. **Check each solution file that exists** in the folder (`solution1.py`, `solution1.js`, `solution1.go`, `solution1.java`, numbered variants, and any legacy unnumbered `solution.<ext>`) - is it non-empty, and does running it reproduce the expected output from the problem's examples? Use the same run commands as `create-problem`, targeting the actual filename:
   - Python: `python3 solution1.py`
   - JavaScript: `node solution1.js`
   - Go: `go run solution1.go` (one file at a time, never `go run .`)
   - Java: `javac solution1.java && java solution1` (from inside the problem folder). Delete every `.class` file `javac` produced in that folder after the run, whether tests passed or failed.

   Do not rewrite existing solution files - only inspect and run what's already there, plus whatever you created in step 4.

6. **Reconcile the README.md Problems table row** for this problem:
   - If there's no row yet, add one in numeric order (same row format as `create-problem` step 6).
   - Otherwise, diff the row's checkmarks against step 5's findings and correct any mismatch (add `✅` for a language now implemented+passing, remove it if every file for that language is missing/empty/failing).
   - Make sure the row's link (`problems/{folder}/`) still resolves to the actual folder name - fix it if the folder was renamed.

Report back a short summary of what changed (or that everything was already in sync) rather than silently editing.
