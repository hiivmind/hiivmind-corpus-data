# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Overview

This is a **data-only documentation corpus** for dlt. It contains indexed documentation that can be queried via the `hiivmind-corpus` plugin.

**Important:** This is NOT a Claude Code plugin. Navigation and all operations are provided by the `hiivmind-corpus` plugin.

## How to Use This Corpus

### Registration

Register this corpus with your project using `hiivmind-corpus`:

```
/hiivmind-corpus register github:hiivmind/hiivmind-corpus-dlt
```

This adds an entry to `.hiivmind/corpus/registry.yaml` in your project.

### Navigation

Once registered, ask questions about dlt and the navigate skill will find relevant documentation:

```
How do I create a pipeline with dlt?
What destinations does dlt support?
How do I use incremental loading in dlt?
```

Or explicitly navigate:

```
/hiivmind-corpus navigate dlt "your question"
```

## Directory Structure

```
hiivmind-corpus-dlt/
├── config.yaml          # Source definitions and keywords
├── index.md             # Main documentation index
├── index-*.md           # Sub-indexes for tiered sections
├── uploads/             # Local document uploads
├── .source/             # Cloned git sources (gitignored)
├── .cache/              # Cached web content (gitignored)
└── README.md
```

## Key Files

| File | Purpose | Editable? |
|------|---------|-----------|
| `config.yaml` | Source definitions, keywords, commit tracking | Via `hiivmind-corpus-refresh` |
| `index.md` | Main documentation index with summaries | Via `hiivmind-corpus-build/enhance/refresh` |
| `index-*.md` | Sub-indexes for large sections | Via `hiivmind-corpus-build/enhance/refresh` |

## Maintenance

This corpus is maintained using `hiivmind-corpus` skills:

| Skill | Purpose |
|-------|---------|
| `hiivmind-corpus-build` | Build/rebuild the documentation index |
| `hiivmind-corpus-refresh` | Update index from upstream changes |
| `hiivmind-corpus-enhance` | Deepen coverage on specific topics |
| `hiivmind-corpus-add-source` | Add new documentation sources |

### Example Commands

```
# Refresh from upstream
/hiivmind-corpus refresh dlt

# Enhance a topic
/hiivmind-corpus enhance dlt <topic>

# Add another source
/hiivmind-corpus add-source dlt <url>
```

## Corpus Routing

This corpus auto-triggers for questions containing these keywords (defined in `config.yaml`):

- dlt
- dlthub
- dlt-hub
- data load tool
- pipeline

## Requirements

- `hiivmind-corpus` plugin installed (provides all operations)
- Git (for source cloning and updates)
