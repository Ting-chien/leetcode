---
name: create-problem
description: Use when the user wants to create, add, or start a new LeetCode problem, or scaffold a new folder under problems/.
---

# Create Problem

Scaffolds everything needed to start a new LeetCode problem in this repo, following the conventions already used under `problems/`.

## Parameters

- **Problem name** (required) - the LeetCode problem title, e.g. "Merge Intervals". If not given, ask with `AskUserQuestion`.
- **Language(s)** (optional) - one or more of `py` (Python), `js` (JavaScript), `go` (Go), `java` (Java). If not given, ask with `AskUserQuestion` (multiSelect) listing these four options. It is valid for the user to pick none - just skip step 5.

## Solution file naming

Every language starts at `solution1.<ext>`. Additional approaches are `solution2.<ext>`, `solution3.<ext>`, … Never create an unnumbered `solution.<ext>`.

## Stubs only — no answers

When creating a solution file, write **only** the function/class signature and the problem's examples as test cases in `main` / `if __name__ == '__main__'`. Comments may note expected output.

**Do not implement the algorithm.** No DFS/BFS/DP/Union-Find, no porting another language's solution in the same folder, no filling in the body because the user asked to "add Go" or similar.

If the user pasted their own solution code, put that in the file as they wrote it. Do not invent an implementation.

## Steps

1. **Resolve the problem name.** If missing, ask via `AskUserQuestion`.

2. **Look up the problem.** Fetch it from `https://leetcode.com/problems/<slug>/` (or `https://neetcode.io/` if LeetCode is unavailable/blocked) to determine:
   - The official problem number
   - The canonical title
   - Description, examples, and constraints
   If the title is ambiguous or you can't find a confident match, confirm with the user via `AskUserQuestion` before proceeding (never guess a problem number).

3. **Create the folder.** `problems/{number:04d}_{snake_case_title}/`, e.g. `problems/0056_merge_intervals/`. Zero-pad the number to 4 digits. Snake-case the canonical title (lowercase, non-alphanumeric -> `_`). If a folder for this problem number already exists, stop and tell the user to use `update-problem` instead.

4. **Write the problem statement.** Save it as `README.md` inside the new folder (GitHub renders this automatically when the folder is browsed, so the root README's existing folder-link style keeps working unchanged). Include: title + number, description, examples, and constraints. Note the source URL at the bottom.

5. **Create solution stubs**, one per requested language, named `solution1.<ext>`. If the user asked for multiple approaches in the same language, continue with `solution2.<ext>`, `solution3.<ext>`, …
   | Language | First file | Stub |
   |---|---|---|
   | Python | `solution1.py` | `class Solution:` with a method stub matching the LeetCode function signature if available, else a reasonable guess from the title/description |
   | JavaScript | `solution1.js` | function/module stub matching the LeetCode signature if available |
   | Go | `solution1.go` | `package main` + func stub. Each numbered Go file is independently runnable; use `go run solution1.go`, never `go run .` (duplicate `main` / symbols). |
   | Java | `solution1.java` | `public class solution1 { ... }` - class name matches the filename |

   Prefer LeetCode's own starter code for the language when you can retrieve it; otherwise write a minimal compilable/runnable stub (**signature + test cases only, no implementation**) matching the style of files already in `problems/` (see e.g. `problems/0056_merge_interval/solution1.java`).

6. **Update `README.md`'s Problems table** at the repo root:
   - Insert a new row in numeric order by problem number: `| {number}. [{Title}](problems/{folder}/) | {Python} | {JavaScript} | {Go} | {Java} |`
   - For each language column, put `✅` only if at least one corresponding solution file is **non-empty** (i.e. actually implemented, not just the stub from step 5) **and** running it produces output matching the problem's expected examples. Otherwise leave the cell blank.
   - Since step 5 normally produces empty stubs, columns are typically left blank right after creation - that's expected. Only mark `✅` if the user supplied working code as part of this request.

## Verifying a solution before marking ✅

Run each numbered file for that language and compare output against the examples from the problem statement. Substitute `solution2`, `solution3`, … as needed:
- Python: `python3 solution1.py`
- JavaScript: `node solution1.js`
- Go: `go run solution1.go` (one file at a time)
- Java: `javac solution1.java && java solution1` (from inside the problem folder). Delete every `.class` file `javac` produced in that folder after the run, whether tests passed or failed.

There's no test framework in this repo - correctness is judged by comparing the script's printed output for each example to the expected output in the problem statement.
