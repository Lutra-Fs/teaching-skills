# Evals

Cases for `claude plugin eval`, one folder per skill (`plan-teaching/`). Each case's `scaffold.sh` copies `fixtures/Teaching/` into the run's working directory, so prompts use paths like `Teaching/SE/2026-27_Year_12`.

Run from the repo root:

```
claude plugin eval . --scaffold --allow-tools Write Edit Bash --trust-plugin --runs 3 -j 4
```

- `--scaffold` is needed, or the runs see an empty folder.
- `--allow-tools Write Edit Bash` is needed, or the runs only get read-only tools and cannot write plans or decks.
- Bash runs inside the sandbox, which on Linux needs `bubblewrap` and `socat`.
- Add `--ablation none` to skip the no-plugin baseline arm, or `--case <glob>` to run one case.
