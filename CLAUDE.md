# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a **hiivmind-corpus marketplace** - a collection of documentation corpus plugins for data engineering libraries. Each subdirectory with a `hiivmind-corpus-*` prefix is a separate corpus plugin.

Currently contains:
- `hiivmind-corpus-polars` - Polars DataFrame library documentation
- `hiivmind-corpus-ibis` - Ibis portable dataframe expressions documentation
- `hiivmind-corpus-narwhals` - Narwhals dataframe-agnostic library documentation
- `hiivmind-corpus-substrait` - Substrait cross-language query plans documentation

## IMPORTANT: Maintenance Skills

This marketplace and its corpus plugins are managed by the **hiivmind-corpus** plugin system. Use these skills:

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| `hiivmind-corpus-init` | Add a new corpus plugin to this marketplace | Adding docs for a new library |
| `hiivmind-corpus-add-source` | Add sources to an existing corpus | Extending a corpus with more docs |
| `hiivmind-corpus-build` | Build/rebuild a corpus index | After adding sources |
| `hiivmind-corpus-enhance` | Deepen coverage on specific topics | When more detail is needed |
| `hiivmind-corpus-refresh` | Update index from upstream changes | When source docs have been updated |

### Example Usage

```
# Add a new corpus to this marketplace
"Add DuckDB documentation to this corpus collection"

# Build an existing corpus's index
"Build the hiivmind-corpus-polars index"

# Refresh all corpora from upstream
"Refresh all corpus indexes from upstream"

# Enhance a topic
"Add more detail about lazy evaluation to the Polars index"
```

## Directory Structure

```
hiivmind-corpus-data/
├── .claude-plugin/
│   ├── plugin.json               # Marketplace manifest
│   └── marketplace.json          # References all corpus plugins
├── CLAUDE.md                     # This file
├── README.md
├── .gitignore
│
├── hiivmind-corpus-polars/
│   ├── .claude-plugin/plugin.json
│   ├── skills/navigate/SKILL.md
│   ├── data/config.yaml
│   ├── data/index.md
│   ├── .source/                  # Gitignored
│   └── .cache/                   # Gitignored
│
├── hiivmind-corpus-ibis/
│   └── ...
│
├── hiivmind-corpus-narwhals/
│   └── ...
│
└── hiivmind-corpus-substrait/
    └── ...
```

## Key Files

| File | Purpose | Editable? |
|------|---------|-----------|
| `.claude-plugin/marketplace.json` | Plugin registry | **No** - managed by `hiivmind-corpus-init` |
| `*/data/config.yaml` | Source definitions per corpus | **No** - use `hiivmind-corpus-add-source` |
| `*/data/index.md` | Documentation index per corpus | **No** - use `hiivmind-corpus-build/enhance/refresh` |
| `*/skills/navigate/SKILL.md` | Navigation skill per corpus | Yes, for customization |

## Adding a New Corpus

To add documentation for another data library to this marketplace:

1. Run `hiivmind-corpus-init` from this directory
2. Context will be detected as "Existing hiivmind-corpus marketplace"
3. New corpus will be created as a subdirectory
4. `marketplace.json` will be updated automatically
5. Run `hiivmind-corpus-build` to build the new corpus's index

**Do NOT manually create corpus directories** - always use `hiivmind-corpus-init`.

## Requirements

- `hiivmind-corpus` meta-plugin must be installed (provides maintenance skills)
- Git (for source cloning and updates)
