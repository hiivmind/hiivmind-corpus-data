# Substrait Documentation Corpus

A Claude Code plugin providing always-current access to Substrait documentation with intelligent navigation.

## Features

- **Indexed Navigation**: Structured index of all Substrait documentation with summaries, key concepts, and cross-references
- **Automatic Updates**: Incremental index updates from upstream documentation changes
- **Smart Matching**: Finds relevant docs based on concepts, summaries, and section headings

## Installation

### As a Plugin

```bash
# Add the marketplace containing this plugin
/plugin marketplace add hiivmind/hiivmind-corpus-data

# Install the plugin
/plugin install hiivmind-corpus-substrait

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
Please build the Substrait documentation index
```

This requires the `hiivmind-corpus` meta-plugin to be installed.

## Usage

### Automatic Navigation

The navigation skill is model-invoked. Simply ask questions about Substrait:

```
What is a Substrait plan?
How do I represent a JOIN in Substrait?
What expression types does Substrait support?
How do I define custom functions in Substrait?
```

Claude will automatically find and cite relevant documentation.

### Index Updates

Refresh from upstream changes (uses `hiivmind-corpus-refresh`):

```
Refresh the Substrait corpus from upstream
```

Full rebuild (uses `hiivmind-corpus-build`):

```
Rebuild the Substrait documentation index from scratch
```

Enhance a specific topic (uses `hiivmind-corpus-enhance`):

```
Add more detail about custom functions to the Substrait index
```

## Skills

### hiivmind-corpus-substrait-navigate

Finds relevant documentation for Substrait-related tasks. Automatically invoked when you ask about:

- Cross-language query plan representation
- Relations (Read, Filter, Join, Aggregate, Project, Sort, etc.)
- Expression types (scalar, aggregate, window functions)
- Type system (simple types, compound types, nullability)
- Serialization formats (protobuf binary, JSON text)
- Extensions and custom functions
- Integration with Arrow, Calcite, Spark, Trino, DuckDB, DataFusion

## File Structure

```
hiivmind-corpus-substrait/
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
