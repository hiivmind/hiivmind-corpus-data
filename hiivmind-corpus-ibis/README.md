# Ibis Documentation Corpus

A Claude Code plugin providing always-current access to Ibis documentation with intelligent navigation.

## Features

- **Indexed Navigation**: Structured index of all Ibis documentation with summaries, key concepts, and cross-references
- **Automatic Updates**: Incremental index updates from upstream documentation changes
- **Smart Matching**: Finds relevant docs based on concepts, summaries, and section headings

## Installation

### As a Plugin

```bash
# Add the marketplace containing this plugin
/plugin marketplace add hiivmind/hiivmind-corpus-ibis

# Install the plugin
/plugin install hiivmind-corpus-ibis

# Restart Claude Code
```

### Manual Installation

Clone this repository to your Claude Code plugins directory.

## First-Time Setup

After installing, invoke the maintenance skill to build the index:

```
Please build the Ibis documentation index
```

This will:
1. Clone the Ibis docs repository to `.source/`
2. Build the full index
3. Write `data/config.yaml` and `data/index.yaml`

## Usage

### Automatic Navigation

The navigation skill is model-invoked. Simply ask questions about Ibis:

```
How do I connect to DuckDB with Ibis?
What backends does Ibis support?
How do I perform a join in Ibis?
What's the difference between Ibis and pandas?
```

Claude will automatically find and cite relevant documentation.

### Manual Index Updates

Check if updates are available:

```
Check if the Ibis documentation index needs updating
```

Force a full rebuild:

```
Rebuild the Ibis documentation index from scratch
```

## Skills

### hiivmind-corpus-ibis-navigate

Finds relevant documentation for Ibis-related coding tasks. Automatically invoked when you ask about:

- Backend connections (DuckDB, BigQuery, Snowflake, PostgreSQL, etc.)
- Expression API (tables, columns, scalars)
- Data types and schemas
- UDFs (scalar and aggregate)
- Migration from pandas, SQL, or dplyr
- Time series operations
- Visualization integrations

## File Structure

```
hiivmind-corpus-ibis/
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
