# Next Session Prompt — Teaching AI: Build B1 & B2

Copy-paste this into your next Claude Code session:

---

Let's work on teaching-ai. I need to build two modules:

**B1: Terminal Basics** (`modules/b1-terminal-basics.qmd`) — ~75 min hands-on module teaching econ students command line fundamentals. Should cover:
- What is a shell / why should economists care (reproducibility, automation, power tools)
- Navigating the filesystem: pwd, ls, cd, ~, .., tab completion
- Reading files: cat, head, tail, less
- Searching: grep (basic patterns, piping)
- File operations: mkdir, cp, mv, rm (with safety warnings)
- Pipes and redirection: |, >, >>
- Practical exercise: navigate to a project folder, find a specific variable in a .do file using grep, count observations in a CSV using wc
- Economist-relevant framing throughout (not generic CS intro)
- Include "why not just use Finder/Explorer?" motivation
- Mac/zsh focus (our students), note Windows/WSL differences briefly

**B2: Git & GitHub Essentials** (`modules/b2-git-github.qmd`) — ~75 min hands-on module. Should cover:
- Why version control matters (the "final_v2_REAL_final.do" problem)
- Mental model: snapshots, not diffs. The staging area concept
- Core workflow: clone, status, add, commit, push, pull
- Reading a diff, reading a commit history
- GitHub: repos, README, browsing code/history online
- Practical exercise: clone a sample repo, make changes, commit, push
- When things go wrong: common mistakes and how to fix them (forgot to pull, committed wrong file)
- Explicitly NOT covering: branches, merges, PRs, rebasing (save for advanced module)
- Connect to reproducibility and collaboration in economics research

Both modules should follow the same format as A1-A3 (learning objectives, module-meta badges with `badge-technical` instead of `badge-no-code`, exercises, discussion questions, instructor notes). Check existing modules for format reference.

After writing both, update `_quarto.yml` navbar to link them, update `index.qmd` module table to link them (remove "coming soon"), and run `quarto render && git add -A && git commit && git push`.
