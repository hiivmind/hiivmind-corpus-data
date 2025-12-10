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
/plugin marketplace add hiivmind/hiivmind-corpus-substrait

# Install the plugin
/plugin install hiivmind-corpus-substrait

# Restart Claude Code
```

### Manual Installation

Clone this repository to your Claude Code plugins directory.

## First-Time Setup

After installing, invoke the maintenance skill to build the index:

```
Please build the Substrait documentation index
```

This will:
1. Clone the Substrait docs repository to `.source/`
2. Build the full index
3. Write `data/config.yaml` and `data/index.yaml`

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

### Manual Index Updates

Check if updates are available:

```
Check if the Substrait documentation index needs updating
```

Force a full rebuild:

```
Rebuild the Substrait documentation index from scratch
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

Edit `data/config.yaml` to customize:

- **include_patterns**: File patterns to index
- **exclude_patterns**: Files to skip
- **language_filter**: Documentation language
- **priority_paths**: Sections to index with more detail

## Requirements

- Git (for cloning and updating documentation)
- Claude Code with plugin support

## License

MIT
