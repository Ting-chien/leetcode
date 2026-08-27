---
name: commit
description: Commit pending changes under problems/ or WeeklyContest/ using this repo's message conventions - one commit for newly added problem solutions, a separate one for newly added Weekly Contest solutions, and separate "Update solution" commits for changes to existing solutions. Never mixes problems and Weekly Contest changes in the same commit. Use when the user asks to commit new or updated LeetCode/Weekly Contest solutions.
---

# Commit

Commits changes under `problems/` and `WeeklyContest/`. Root `README.md` is included in a problems commit when its Problems-table diff is for the problems in that commit. Everything else in the repo stays unstaged.

## Steps

1. **Discover changes**:
   ```
   git status --porcelain=v1 -uall -- problems WeeklyContest README.md
   ```
   `-uall` is required so untracked directories are expanded to individual files rather than collapsed to one line.

2. **Classify every line** under `problems/` and `WeeklyContest/`:
   - `??` (untracked) -> **added**
   - Anything with `M` (modified, tracked) -> **updated**
   - Anything else (deletions, renames, etc.) -> do not guess a message for it; flag it to the user and leave it unstaged.

   Root `README.md` is not a group of its own. Check `git diff README.md` when wrapping in step 5.

3. **Group by category and target**, never mixing problems with Weekly Contest, or "added" with "updated":
   - Files under `problems/{NNNN}_{slug}/...` -> group by problem number (strip leading zeros, e.g. `0056` -> `56`).
   - Files under `WeeklyContest/Weekly {N}/...` -> group by contest number as written (e.g. `512`).
   - This yields up to four groups: problems-added, problems-updated, weeklycontest-added, weeklycontest-updated. Skip any group with no files.

4. **Build one commit message per group**, problems in ascending number order, comma-separated, always singular "solution" regardless of count. For each problem, use the full name `{number}. {Canonical Title}` (e.g. `121. Best Time to Buy and Sell Stock`) — take it from the folder `README.md` H1, or else the official LeetCode title. Never `problem {n}`, never the number alone, never a shortened table label like `Max Profit`.
   - Problems added: `Add new solution to {n}. {Title}, {n}. {Title}, ...`
   - Weekly Contest added: `Add new solution to Weekly Contest {n1}, Weekly Contest {n2}, ...`
   - Problems updated: `Update solution for {n}. {Title}, {n}. {Title}, ...`
   - Weekly Contest updated: `Update solution for Weekly Contest {n1}, Weekly Contest {n2}, ...`

   Example: `Add new solution to 121. Best Time to Buy and Sell Stock, 435. Non-overlapping Intervals`

   If a problem/contest has files in both the added and updated set at once (e.g. one new language stub plus an edit to an existing solution), it's fine for its number to appear in both that group's commits - don't merge the two messages.

5. **Stage and commit each non-empty group separately**, in this order: problems-added, problems-updated, weeklycontest-added, weeklycontest-updated. Stage only the exact files belonging to that group (never `git add -A` or a bare `git add problems`/`git add WeeklyContest`, since that would sweep in other groups' files too).

   For a **problems** group, wrap root `README.md` into the same commit when `git diff README.md` updates the Problems table for a problem in that group (new row, checkmark, or folder link). Example: adding `problems/0121_max_profit/` and a new `121.` row in the table is one commit. If the README diff covers problems from more than one group, stage it with the first of those groups in commit order. If the README diff is not for the problems in this commit, leave `README.md` unstaged.

   ```
   git add -- <files for this group>
   git commit -m "<message for this group>"
   ```

6. **Report back** a short summary of the commits created (hash + message each). If `README.md` was wrapped or left unstaged, say so. If anything was skipped in step 2 (deletions/renames) or if other changes existed outside `problems/`/`WeeklyContest/`, mention that they were left untouched rather than silently ignoring them.

If there are no changes under `problems/` or `WeeklyContest/` at all, say so and do nothing.
