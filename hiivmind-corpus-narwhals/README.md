# Narwhals Documentation Corpus

A Claude Code plugin providing always-current access to Narwhals documentation with intelligent navigation.

## Features

- **Indexed Navigation**: Structured index of all Narwhals documentation with summaries, key concepts, and cross-references
- **Automatic Updates**: Incremental index updates from upstream documentation changes
- **Smart Matching**: Finds relevant docs based on concepts, summaries, and section headings

## Installation

### As a Plugin

```bash
# Add the marketplace containing this plugin
/plugin marketplace add hiivmind/hiivmind-corpus-narwhals

# Install the plugin
/plugin install hiivmind-corpus-narwhals

# Restart Claude Code
```

### Manual Installation

Clone this repository to your Claude Code plugins directory.

## First-Time Setup

After installing, invoke the maintenance skill to build the index:

```
Please build the Narwhals documentation index
```

This will:
1. Clone the Narwhals docs repository to `.source/`
2. Build the full index
3. Write `data/config.yaml` and `data/index.yaml`

## Usage

### Automatic Navigation

The navigation skill is model-invoked. Simply ask questions about Narwhals:

```
How do I write dataframe-agnostic code with Narwhals?
What's the difference between @narwhalify and from_native/to_native?
How do I handle pandas index in Narwhals?
What backends does Narwhals support?
```

Claude will automatically find and cite relevant documentation.

### Manual Index Updates

Check if updates are available:

```
Check if the Narwhals documentation index needs updating
```

Force a full rebuild:

```
Rebuild the Narwhals documentation index from scratch
```

## Skills

### hiivmind-corpus-narwhals-navigate

Finds relevant documentation for Narwhals-related coding tasks. Automatically invoked when you ask about:

- Writing dataframe-agnostic library code
- Supporting multiple backends (pandas, Polars, PyArrow, cuDF, Modin, Dask, DuckDB, Ibis, PySpark)
- Expression API (Polars-like syntax)
- The `@narwhalify` decorator and `from_native`/`to_native`
- Type hints and static typing with Narwhals
- Backwards compatibility and stable API versions
- Performance overhead considerations

## File Structure

```
hiivmind-corpus-narwhals/
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
