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
/plugin marketplace add hiivmind/hiivmind-corpus-polars

# Install the plugin
/plugin install hiivmind-corpus-polars

# Restart Claude Code
```

### Manual Installation

Clone this repository to your Claude Code plugins directory.

## First-Time Setup

After installing, invoke the maintenance skill to build the index:

```
Please build the Polars documentation index
```

This will:
1. Clone the Polars docs repository to `.source/`
2. Build the full index
3. Write `data/config.yaml` and `data/index.yaml`

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

### Manual Index Updates

Check if updates are available:

```
Check if the Polars documentation index needs updating
```

Force a full rebuild:

```
Rebuild the Polars documentation index from scratch
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
