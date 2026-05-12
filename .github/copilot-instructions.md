# Copilot Instructions

Read `AGENTS.md` first. It is the canonical operator contract for this repository.

Start with `/auto-pilot` for routing and `/self-test` to validate setup.

App-specific context: `../../Master.Doc/MSITM.6341/claude.md`
Framework contract: `../../Master.Prompt/AGENTS.md`

Keep canonical app and project documentation in Master.Doc. Keep local AI files lightweight.
After every completed prompt or IDE command/workflow, run `node ../../Master.Prompt/.claude/scripts/maintenance/shared-memory-sync.js --json --promotion-scope orchestration-alignment --project dbu-msitm-6341 --master-prompt-root ../../Master.Prompt --master-doc-root ../../Master.Doc` so all IDEs keep shared-memory cache status and promotion backlog aligned.
