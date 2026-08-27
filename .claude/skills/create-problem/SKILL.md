---
name: create-problem
description: Scaffold a new LeetCode problem in this repo - creates the problems/ folder, fetches the problem statement from LeetCode or NeetCode into a markdown file, generates solution stub files for requested languages, and adds a row to the Problems table in README.md. Use when the user wants to create, add, or start a new LeetCode problem.
---

# Create Problem

Scaffolds everything needed to start a new LeetCode problem in this repo, following the conventions already used under `problems/`.

## Parameters

- **Problem name** (required) - the LeetCode problem title, e.g. "Merge Intervals". If not given, ask with `AskUserQuestion`.
- **Language(s)** (optional) - one or more of `py` (Python), `js` (JavaScript), `go` (Go), `java` (Java). If not given, ask with `AskUserQuestion` (multiSelect) listing these four options. It is valid for the user to pick none - just skip step 4.

## Steps

1. **Resolve the problem name.** If missing, ask via `AskUserQuestion`.

2. **Look up the problem.** Fetch it from `https://leetcode.com/problems/<slug>/` (or `https://neetcode.io/` if LeetCode is unavailable/blocked) to determine:
   - The official problem number
   - The canonical title
   - Description, examples, and constraints
   If the title is ambiguous or you can't find a confident match, confirm with the user via `AskUserQuestion` before proceeding (never guess a problem number).

3. **Create the folder.** `problems/{number:04d}_{snake_case_title}/`, e.g. `problems/0056_merge_intervals/`. Zero-pad the number to 4 digits. Snake-case the canonical title (lowercase, non-alphanumeric -> `_`). If a folder for this problem number already exists, stop and tell the user to use `update-problem` instead.

4. **Write the problem statement.** Save it as `README.md` inside the new folder (GitHub renders this automatically when the folder is browsed, so the root README's existing folder-link style keeps working unchanged). Include: title + number, description, examples, and constraints. Note the source URL at the bottom.

5. **Create solution stubs**, one per requested language, named `solution.<ext>`:
   | Language | File | Stub |
   |---|---|---|
   | Python | `solution.py` | `class Solution:` with a method stub matching the LeetCode function signature if available, else a reasonable guess from the title/description |
   | JavaScript | `solution.js` | function/module stub matching the LeetCode signature if available |
   | Go | `solution.go` | `package main` + func stub |
   | Java | `solution.java` | `public class solution { ... }` - note: lowercase `solution` matching the filename, matching this repo's existing convention |

   Prefer LeetCode's own starter code for the language when you can retrieve it; otherwise write a minimal compilable/runnable stub (no implementation) plus a `main`/`if __name__ == '__main__'` block with the examples from the problem statement as test cases, matching the style of files already in `problems/` (see e.g. `problems/0056_merge_interval/solution1.java`).

6. **Update `README.md`'s Problems table** at the repo root:
   - Insert a new row in numeric order by problem number: `| {number}. [{Title}](problems/{folder}/) | {Python} | {JavaScript} | {Go} | {Java} |`
   - For each language column, put `✅` only if the corresponding solution file is **non-empty** (i.e. actually implemented, not just the stub from step 5) **and** running it produces output matching the problem's expected examples. Otherwise leave the cell blank.
   - Since step 5 normally produces empty stubs, columns are typically left blank right after creation - that's expected. Only mark `✅` if the user supplied working code as part of this request.

## Verifying a solution before marking ✅

Run the file and compare output against the examples from the problem statement:
- Python: `python3 solution.py`
- JavaScript: `node solution.js`
- Go: `go run solution.go`
- Java: `javac solution.java && java solution` (from inside the problem folder). Done only when every `.class` file `javac` produced in that folder is deleted (`solution.class`, `Solution1.class`, and any other compiled class). Delete them after the run whether tests passed or failed.

There's no test framework in this repo - correctness is judged by comparing the script's printed output for each example to the expected output in the problem statement.
