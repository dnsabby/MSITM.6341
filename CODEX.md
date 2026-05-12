# CODEX.md

Read `AGENTS.md` first. This is the lightweight CODEX-compatible shim for the centralized Master.Prompt architecture.

Canonical references:
- `AGENTS.md`
- `../../Master.Doc/MSITM.6341/claude.md`
- `../../Master.Doc/_project/dbu-msitm-6341/claude.md`
- `../../Master.Prompt/AGENTS.md`

Resolve shared commands, workflows, and hook logic through `../../Master.Prompt/`.
Start with `/auto-pilot` unless the prompt clearly needs a different workflow.
Run `node ../../Master.Prompt/.claude/scripts/maintenance/orchestration-preflight.js --write` before governed execution and `node ../../Master.Prompt/.claude/scripts/maintenance/orchestration-post-acceptance.js --write --event push` after accepted pushes.
After every completed prompt or IDE command/workflow, run `node ../../Master.Prompt/.claude/scripts/maintenance/shared-memory-sync.js --json --promotion-scope orchestration-alignment --project dbu-msitm-6341 --master-prompt-root ../../Master.Prompt --master-doc-root ../../Master.Doc` so all IDEs keep shared-memory cache status and promotion backlog aligned.

App-specific context: `../../Master.Doc/MSITM.6341/claude.md`
Project runtime context: `../../Master.Doc/_project/dbu-msitm-6341/claude.md`
Native wrapper catalog: `../../Master.Prompt/.claude/commands/` and `../../Master.Prompt/.windsurf/workflows/`.