# dlt Documentation Corpus

A data-only documentation corpus for dlt. Use with the `hiivmind-corpus` plugin for navigation and maintenance.

## What is This?

This repository contains:
- **Indexed documentation** - Structured index of dlt docs with summaries and cross-references
- **Source tracking** - Configuration tracking upstream documentation commits
- **Keywords** - Routing keywords for automatic corpus selection

This is NOT a Claude Code plugin. All operations (navigation, building, refreshing) are provided by the `hiivmind-corpus` plugin.

## Quick Start

### 1. Install the hiivmind-corpus plugin

```bash
# In Claude Code
/plugin install hiivmind/hiivmind-corpus
```

### 2. Register this corpus

```bash
# Register from GitHub
/hiivmind-corpus register github:hiivmind/hiivmind-corpus-dlt
```

### 3. Start asking questions

```
How do I create a pipeline with dlt?
What destinations does dlt support?
How do I use incremental loading in dlt?
```

## File Structure

```
hiivmind-corpus-dlt/
├── config.yaml          # Source definitions, keywords, tracking
├── index.md             # Main documentation index
├── index-*.md           # Sub-indexes (for large corpora)
├── uploads/             # Local document uploads
├── .source/             # Cloned docs (gitignored)
├── .cache/              # Web cache (gitignored)
└── README.md
```

## Maintenance

Use `hiivmind-corpus` skills to maintain this corpus:

| Command | Purpose |
|---------|---------|
| `/hiivmind-corpus refresh dlt` | Update from upstream changes |
| `/hiivmind-corpus enhance dlt <topic>` | Add depth to a topic |
| `/hiivmind-corpus build dlt` | Full rebuild |
| `/hiivmind-corpus add-source dlt <url>` | Add new source |

## config.yaml Schema

```yaml
schema_version: 2

corpus:
  name: "dlt"
  display_name: "dlt"
  keywords:            # For automatic routing
    - dlt
    - dlthub
    - dlt-hub
    - data load tool
    - pipeline

sources:
  - id: dlt
    type: git
    repo_url: https://github.com/...
    branch: main
    last_commit_sha: "..."
    last_indexed_at: "..."
```

## Requirements

- `hiivmind-corpus` plugin (provides all operations)
- Git (for source management)

## License

MIT
