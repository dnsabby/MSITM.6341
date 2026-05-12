# AGENTS.md

Canonical app setup is stored in Master.Doc.

- ../../Master.Prompt/AGENTS.md
- ../../Master.Doc/MSITM.6341/app.json
- ../../Master.Doc/MSITM.6341/claude.md
- ../../Master.Doc/_project/dbu-msitm-6341/project.json
- ../../Master.Doc/_project/dbu-msitm-6341/_shared/

Treat `../../Master.Prompt` and `../../Master.Doc` as the centralized roots for this repo.
Use /auto-pilot for routing and /self-test to validate setup.
After every completed prompt or IDE command/workflow, run `node ../../Master.Prompt/.claude/scripts/maintenance/shared-memory-sync.js --json --promotion-scope orchestration-alignment --project dbu-msitm-6341 --master-prompt-root ../../Master.Prompt --master-doc-root ../../Master.Doc` so all IDEs keep shared-memory cache status and promotion backlog aligned.
