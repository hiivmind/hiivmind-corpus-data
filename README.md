# hiivmind-corpus-data

A Claude Code plugin marketplace providing always-current documentation access for data engineering libraries.

## Corpus Plugins

| Plugin | Description |
|--------|-------------|
| [hiivmind-corpus-polars](./hiivmind-corpus-polars/) | Polars DataFrame library - fast dataframes in Python and Rust |
| [hiivmind-corpus-ibis](./hiivmind-corpus-ibis/) | Ibis - portable dataframe expressions across 20+ SQL backends |
| [hiivmind-corpus-narwhals](./hiivmind-corpus-narwhals/) | Narwhals - dataframe-agnostic code for pandas, Polars, PyArrow |
| [hiivmind-corpus-substrait](./hiivmind-corpus-substrait/) | Substrait - cross-language query plans and data compute interop |

## Installation

```bash
# Add this marketplace
/plugin marketplace add hiivmind/hiivmind-corpus-data

# Install individual plugins
/plugin install hiivmind-corpus-polars
/plugin install hiivmind-corpus-ibis
/plugin install hiivmind-corpus-narwhals
/plugin install hiivmind-corpus-substrait
```

## Maintenance

This marketplace is managed by **hiivmind-corpus** skills:

| Skill | Purpose |
|-------|---------|
| `hiivmind-corpus-init` | Add a new corpus to this marketplace |
| `hiivmind-corpus-build` | Build/rebuild a corpus index |
| `hiivmind-corpus-enhance` | Deepen coverage on specific topics |
| `hiivmind-corpus-refresh` | Update index from upstream changes |

### Adding a New Corpus

Run `hiivmind-corpus-init` from this directory - it will detect the existing marketplace and create a new corpus plugin as a subdirectory.

### Refreshing Documentation

```
Refresh all corpus indexes from upstream
```

## Requirements

- `hiivmind-corpus` meta-plugin installed
- Claude Code with plugin support

## License

MIT
