# Windsurf Rules

Read `AGENTS.md` first.

Canonical Windsurf rule: `../../Master.Prompt/.windsurf/rules/rules.md`
Read `AGENTS.md` first.
Use `../../Master.Doc/MSITM.6341/claude.md` for app-specific context.
Use `../../Master.Doc/_project/dbu-msitm-6341/claude.md` for project-shared runtime context.
Treat `../../Master.Prompt/` as the canonical command/workflow catalog.
Native workflows in `.windsurf/workflows/` should stay as relative wrappers back to `../../Master.Prompt/.windsurf/workflows/`.
Start with `/auto-pilot` unless the prompt explicitly chooses another route.
