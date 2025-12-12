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
/plugin marketplace add hiivmind/hiivmind-corpus-data

# Install the plugin
/plugin install hiivmind-corpus-narwhals

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
Please build the Narwhals documentation index
```

This requires the `hiivmind-corpus` meta-plugin to be installed.

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

### Index Updates

Refresh from upstream changes (uses `hiivmind-corpus-refresh`):

```
Refresh the Narwhals corpus from upstream
```

Full rebuild (uses `hiivmind-corpus-build`):

```
Rebuild the Narwhals documentation index from scratch
```

Enhance a specific topic (uses `hiivmind-corpus-enhance`):

```
Add more detail about @narwhalify decorator to the Narwhals index
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

The `data/config.yaml` and `data/index.md` files are managed by hiivmind-corpus skills. Do not edit them manually.

To add new sources, use `hiivmind-corpus-add-source`. To rebuild or enhance the index, use `hiivmind-corpus-build` or `hiivmind-corpus-enhance`.

## Requirements

- `hiivmind-corpus` meta-plugin installed (provides maintenance skills)
- Git (for cloning and updating documentation)
- Claude Code with plugin support

## License

MIT
