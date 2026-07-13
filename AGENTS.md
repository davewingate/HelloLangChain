# Agent Notes

- Repo is intentionally minimal: only `app.py` is project source.
- Entrypoint is direct execution: `python app.py` (no package CLI, task runner, tests, lint, or CI in repo).
- Environment is direnv-managed (`.envrc` + `layout python3`), so Python env lives under `.direnv/`.
- Required shell env before `direnv allow`: `GITHUB_TOKEN` and `LANGSMITH_API_KEY` (`env_vars_required` in `.envrc`).
- Project follows LangSmith observability quickstart pattern, but provider is GitHub Copilot/GitHub Models; keep tracing
  config env-driven.
- No dependency manifest/lockfile is committed; if dependency steps change, update docs (`README.md`) explicitly.
