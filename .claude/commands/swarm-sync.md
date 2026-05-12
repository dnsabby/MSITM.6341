# /swarm-sync

Canonical command: `../../Master.Prompt/.claude/commands/swarm-sync.md`

Read `AGENTS.md` first.
Use `../../Master.Doc/MSITM.6341/claude.md` for app-specific context.
Use `../../Master.Doc/_project/dbu-msitm-6341/claude.md` for project-shared runtime context.
Treat `../../Master.Prompt/` as the canonical command/workflow catalog.
Run `node ../../Master.Prompt/.claude/scripts/maintenance/orchestration-preflight.js --write` before governed planning, research, coding, QA, docs, or DevOps execution.
After every completed prompt or IDE command/workflow, run `node ../../Master.Prompt/.claude/scripts/maintenance/shared-memory-sync.js --json --promotion-scope orchestration-alignment --project dbu-msitm-6341 --master-prompt-root ../../Master.Prompt --master-doc-root ../../Master.Doc` so all IDEs keep shared-memory cache status and promotion backlog aligned.
Resolve shared scripts through `../../Master.Prompt/.claude/scripts/`.
Start with `/auto-pilot` when the prompt is not explicitly scoped to a different entrypoint.
After successful framework-managed pushes, record acceptance with `node ../../Master.Prompt/.claude/scripts/maintenance/orchestration-post-acceptance.js --write --event push`.
