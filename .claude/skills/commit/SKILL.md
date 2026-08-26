---
name: commit
description: Commit pending changes under problems/ or WeeklyContest/ using this repo's message conventions - one commit for newly added problem solutions, a separate one for newly added Weekly Contest solutions, and separate "Update solution" commits for changes to existing solutions. Never mixes problems and Weekly Contest changes in the same commit. Use when the user asks to commit new or updated LeetCode/Weekly Contest solutions.
---

# Commit

Commits changes scoped strictly to `problems/` and `WeeklyContest/`. Nothing else in the repo is staged, committed, or otherwise touched by this skill, even if `git status` shows other pending changes.

## Steps

1. **Discover changes**, scoped to the two directories only:
   ```
   git status --porcelain=v1 -uall -- problems WeeklyContest
   ```
   `-uall` is required so untracked directories are expanded to individual files rather than collapsed to one line.

2. **Classify every line**:
   - `??` (untracked) -> **added**
   - Anything with `M` (modified, tracked) -> **updated**
   - Anything else (deletions, renames, etc.) -> do not guess a message for it; flag it to the user and leave it unstaged.

3. **Group by category and target**, never mixing problems with Weekly Contest, or "added" with "updated":
   - Files under `problems/{NNNN}_{slug}/...` -> group by problem number (strip leading zeros, e.g. `0056` -> `56`).
   - Files under `WeeklyContest/Weekly {N}/...` -> group by contest number as written (e.g. `512`).
   - This yields up to four groups: problems-added, problems-updated, weeklycontest-added, weeklycontest-updated. Skip any group with no files.

4. **Build one commit message per group**, numbers in ascending order, comma-separated, always singular "solution" regardless of count:
   - Problems added: `Add new solution to problem {n1}, problem {n2}, ...`
   - Weekly Contest added: `Add new solution to Weekly Contest {n1}, Weekly Contest {n2}, ...`
   - Problems updated: `Update solution for problem {n1}, problem {n2}, ...`
   - Weekly Contest updated: `Update solution for Weekly Contest {n1}, Weekly Contest {n2}, ...`

   If a problem/contest has files in both the added and updated set at once (e.g. one new language stub plus an edit to an existing solution), it's fine for its number to appear in both that group's commits - don't merge the two messages.

5. **Stage and commit each non-empty group separately**, in this order: problems-added, problems-updated, weeklycontest-added, weeklycontest-updated. Stage only the exact files belonging to that group (never `git add -A` or a bare `git add problems`/`git add WeeklyContest`, since that would sweep in other groups' files too):
   ```
   git add -- <files for this group>
   git commit -m "<message for this group>"
   ```

6. **Report back** a short summary of the commits created (hash + message each). If anything was skipped in step 2 (deletions/renames) or if changes existed outside `problems/`/`WeeklyContest/`, mention that they were left untouched rather than silently ignoring them.

If there are no changes under `problems/` or `WeeklyContest/` at all, say so and do nothing.
