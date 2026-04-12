# DataFusion Documentation Corpus

A data-only documentation corpus for DataFusion. Use with the `hiivmind-corpus` plugin for navigation and maintenance.

## What is This?

This repository contains:
- **Indexed documentation** - Structured index of DataFusion docs with summaries and cross-references
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
/hiivmind-corpus register github:hiivmind/hiivmind-corpus-datafusion
```

### 3. Start asking questions

```
"How do I create a DataFrame in DataFusion?"
"What SQL functions does DataFusion support?"
"How do I register a CSV file as a table?"
```

## File Structure

```
hiivmind-corpus-datafusion/
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
| `/hiivmind-corpus refresh datafusion` | Update from upstream changes |
| `/hiivmind-corpus enhance datafusion <topic>` | Add depth to a topic |
| `/hiivmind-corpus build datafusion` | Full rebuild |
| `/hiivmind-corpus add-source datafusion <url>` | Add new source |

## config.yaml Schema

```yaml
schema_version: 2

corpus:
  name: "datafusion"
  display_name: "DataFusion"
  keywords:            # For automatic routing
    - datafusion
    - datafusion-python
    - apache datafusion
    - dataframe sql

sources:
  - id: datafusion
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
