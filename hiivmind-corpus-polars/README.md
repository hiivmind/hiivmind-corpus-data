# Polars Documentation Corpus

A Claude Code plugin providing always-current access to Polars documentation with intelligent navigation.

## Features

- **Indexed Navigation**: Structured index of all Polars documentation with summaries, key concepts, and cross-references
- **Automatic Updates**: Incremental index updates from upstream documentation changes
- **Smart Matching**: Finds relevant docs based on concepts, summaries, and section headings

## Installation

### As a Plugin

```bash
# Add the marketplace containing this plugin
/plugin marketplace add hiivmind/hiivmind-corpus-data

# Install the plugin
/plugin install hiivmind-corpus-polars

# Restart Claude Code
```

### Manual Installation

Clone this repository to your Claude Code plugins directory.

## Maintenance Skills

This corpus is managed by **hiivmind-corpus** skills:

| Skill | Purpose |
|-------|---------|
| `hiivmind-corpus-add-source` | Add new documentation sources |
| `hiivmind-corpus-build` | Build/rebuild the documentation index |
| `hiivmind-corpus-enhance` | Deepen coverage on specific topics |
| `hiivmind-corpus-refresh` | Update index from upstream changes |

### First-Time Setup

After installing, use the `hiivmind-corpus-build` skill to build the index:

```
Please build the Polars documentation index
```

This requires the `hiivmind-corpus` meta-plugin to be installed.

## Usage

### Automatic Navigation

The navigation skill is model-invoked. Simply ask questions about Polars:

```
How do I read a CSV file with Polars?
What expressions can I use for string manipulation?
How do I perform a groupby aggregation in Polars?
What's the difference between lazy and eager evaluation?
```

Claude will automatically find and cite relevant documentation.

### Index Updates

Refresh from upstream changes (uses `hiivmind-corpus-refresh`):

```
Refresh the Polars corpus from upstream
```

Full rebuild (uses `hiivmind-corpus-build`):

```
Rebuild the Polars documentation index from scratch
```

Enhance a specific topic (uses `hiivmind-corpus-enhance`):

```
Add more detail about lazy evaluation to the Polars index
```

## Skills

### hiivmind-corpus-polars-navigate

Finds relevant documentation for Polars-related coding tasks. Automatically invoked when you ask about:

- DataFrame and LazyFrame operations
- Expressions and contexts
- Data types and structures
- IO operations (CSV, Parquet, JSON, etc.)
- Joins, aggregations, and transformations
- Time series operations
- SQL interface
- GPU acceleration
- Polars Cloud

## File Structure

```
hiivmind-corpus-polars/
├── .claude-plugin/
│   └── plugin.json           # Plugin manifest
├── skills/
│   └── navigate/
│       └── SKILL.md          # Documentation navigation
├── data/
│   ├── config.yaml           # Source repo + settings
│   └── index.md              # Generated documentation index
├── .source/                  # Cloned docs repo (gitignored)
└── README.md
```

## Configuration

The `data/config.yaml` and `data/index.md` files are managed by hiivmind-corpus skills. Do not edit them manually.

To add new sources, use `hiivmind-corpus-add-source`. To rebuild or enhance the index, use `hiivmind-corpus-build` or `hiivmind-corpus-enhance`.

## Requirements

- `hiivmind-corpus` meta-plugin installed (provides maintenance skills)
- Git (for cloning and updating documentation)
- Claude Code with plugin support

## License

MIT
