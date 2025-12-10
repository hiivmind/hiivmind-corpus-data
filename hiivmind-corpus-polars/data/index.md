# Polars Documentation Index

> Source: polars (git) | 119 docs | Focus: expressions, transformations, Arrow interop
> Last updated: 2025-12-10

---

## Getting Started

- **Introduction** `polars:index.md` - Overview of Polars: blazingly fast DataFrame library written in Rust, available for Python/R/NodeJS. Key features: parallel execution, lazy API, Arrow support, GPU acceleration
- **Getting Started** `polars:user-guide/getting-started.md` - First steps with Polars, basic DataFrame operations
- **Installation** `polars:user-guide/installation.md` - Installing Polars and optional feature flags

---

## Core Concepts

### Data Types and Structures
- **Data Types & Structures** `polars:user-guide/concepts/data-types-and-structures.md` - Series, DataFrame, Schema. Data types: numeric (Int8-Int128, Float16-64, Decimal), nested (List, Array, Struct), temporal (Date, Datetime, Duration), strings, categoricals. Uses Arrow Columnar Format internally
- **Expressions & Contexts** `polars:user-guide/concepts/expressions-and-contexts.md` - Core DSL concepts. Expressions are lazy transformations. Four contexts: `select` (column operations), `with_columns` (add columns), `filter` (row filtering), `group_by` (aggregations). Expression expansion for multi-column operations

### Lazy API
- **Lazy API Overview** `polars:user-guide/concepts/lazy-api.md` - LazyFrame vs DataFrame, query optimization benefits
- **Using the Lazy API** `polars:user-guide/lazy/using.md` - Converting between eager/lazy, when to use each
- **Query Optimizations** `polars:user-guide/lazy/optimizations.md` - Predicate pushdown, projection pushdown, slice pushdown
- **Schemas in Lazy** `polars:user-guide/lazy/schemas.md` - Schema inference and validation
- **Query Plans** `polars:user-guide/lazy/query-plan.md` - Understanding and visualizing query plans with `explain()`
- **Execution** `polars:user-guide/lazy/execution.md` - Collecting results, streaming execution
- **Sources & Sinks** `polars:user-guide/lazy/sources_sinks.md` - Lazy reading/writing from various formats
- **Streaming** `polars:user-guide/concepts/streaming.md` - Out-of-core processing for datasets larger than RAM

---

## Expressions

### Basic Operations
- **Basic Operations** `polars:user-guide/expressions/basic-operations.md` - Arithmetic (+, -, *, /), comparisons (>, <, ==), Boolean operations (&, |, ~), counting unique values (`n_unique`, `approx_n_unique`, `value_counts`), conditionals with `when().then().otherwise()`
- **Expression Expansion** `polars:user-guide/expressions/expression-expansion.md` - Apply same transformation to multiple columns: `pl.col("a", "b")`, `pl.col(pl.Float64)`, `pl.all()`, `pl.exclude()`
- **Casting** `polars:user-guide/expressions/casting.md` - Type conversion with `cast()`, strict vs lenient casting

### Data Type Operations
- **Strings** `polars:user-guide/expressions/strings.md` - String namespace (`str`): splitting, slicing, regex matching, replacement, case conversion
- **Lists & Arrays** `polars:user-guide/expressions/lists-and-arrays.md` - `List` (variable length) vs `Array` (fixed shape). List namespace for slicing (`head`, `tail`), `explode()`, element-wise ops with `eval()` and `element`, row-wise aggregation with `concat_list()`
- **Categorical Data & Enums** `polars:user-guide/expressions/categorical-data-and-enums.md` - Efficient string encoding. `Categorical` (runtime inference) vs `Enum` (predetermined categories)
- **Structs** `polars:user-guide/expressions/structs.md` - Composite type for multiple fields. Created by `value_counts()`, dict inference. `unnest()` to expand, `field()` to extract, `rename_fields()`. Use for multi-column deduplication and ranking
- **Missing Data** `polars:user-guide/expressions/missing-data.md` - Handling `null` values: `is_null()`, `fill_null()`, `drop_nulls()`, forward/backward fill

### Aggregation & Window Functions
- **Aggregation** `polars:user-guide/expressions/aggregation.md` - `group_by().agg()` context. Multiple aggregations, conditional aggregations, filtering within groups, nested grouping, sorting within groups. Avoid Python lambdas to preserve parallelization
- **Window Functions** `polars:user-guide/expressions/window-functions.md` - `over()` for group operations in select context. Ranking within groups, mapping strategies: `group_to_rows` (default), `explode` (faster), `join`. Windowed aggregations broadcast scalars
- **Folds** `polars:user-guide/expressions/folds.md` - Horizontal operations with `fold()`. Custom row-wise computations across columns, similar to `functools.reduce`. Use `concat_str()` for string concatenation

### Advanced
- **User-Defined Python Functions** `polars:user-guide/expressions/user-defined-python-functions.md` - `map_elements()`, `map_batches()` for custom Python logic. Performance implications with GIL
- **NumPy Functions** `polars:user-guide/expressions/numpy-functions.md` - Using NumPy ufuncs with Polars data

---

## Transformations

### Joins
- **Joins** `polars:user-guide/transformations/joins.md` - Comprehensive join operations:
  - **Equi joins**: `inner`, `left`, `right`, `full`, `semi`, `anti` - match on key equality
  - **Non-equi joins**: `join_where()` - match on arbitrary predicates (e.g., price comparisons)
  - **Asof joins**: `join_asof()` - match on nearest key (time series), with `tolerance` and `strategy`
  - **Cross join**: Cartesian product
  - Key expressions for dynamic matching, `coalesce` parameter for full joins

### Reshaping
- **Concatenation** `polars:user-guide/transformations/concatenation.md` - `concat()` modes: vertical (stack rows), horizontal (add columns), diagonal (combine both). Rechunking considerations
- **Pivot** `polars:user-guide/transformations/pivot.md` - Reshape data: group by columns become y-axis, pivot column becomes x-axis. Aggregations: first, last, sum, min, max, mean, median, len. Note: schema depends on data, collect before pivot in lazy
- **Unpivot** `polars:user-guide/transformations/unpivot.md` - Reverse of pivot, wide to long format

### Time Series
- **Parsing Dates/Times** `polars:user-guide/transformations/time-series/parsing.md` - String to datetime conversion
- **Filtering Time Series** `polars:user-guide/transformations/time-series/filter.md` - Date range filtering
- **Rolling Operations** `polars:user-guide/transformations/time-series/rolling.md` - Rolling windows for time series
- **Resampling** `polars:user-guide/transformations/time-series/resampling.md` - Downsampling/upsampling temporal data
- **Timezones** `polars:user-guide/transformations/time-series/timezones.md` - Timezone handling and conversion

---

## Arrow Interoperability

- **Arrow Producer/Consumer** `polars:user-guide/misc/arrow.md` - Zero-copy data exchange:
  - **PyArrow**: `to_arrow()` / `pl.from_arrow()` for DataFrame/Table conversion
  - **Zero-copy export**: `to_arrow(compat_level=...)` for guaranteed zero-copy
  - **PyCapsule Interface** (v1.3+): `pyarrow.table(df)` / `pyarrow.chunked_array(series)` - standard protocol for Arrow data sharing
  - **C Data Interface**: `Series._export_arrow_to_c()` / `Series._import_arrow_from_c()` for direct struct exchange without PyArrow
  - Works with [growing list of Arrow-compatible libraries](https://github.com/apache/arrow/issues/39195)

---

## IO Operations

- **IO Overview** `polars:user-guide/io/index.md` - Supported formats and common patterns
- **CSV** `polars:user-guide/io/csv.md` - `read_csv()`, `scan_csv()`, `write_csv()`
- **Parquet** `polars:user-guide/io/parquet.md` - Columnar format, predicate pushdown
- **JSON** `polars:user-guide/io/json.md` - JSON and NDJSON support
- **Excel** `polars:user-guide/io/excel.md` - Reading Excel files
- **Database** `polars:user-guide/io/database.md` - SQL database connections
- **Cloud Storage** `polars:user-guide/io/cloud-storage.md` - S3, GCS, Azure Blob
- **Multiple Files** `polars:user-guide/io/multiple.md` - Glob patterns, lazy scanning
- **Hive Partitioning** `polars:user-guide/io/hive.md` - Partitioned datasets
- **BigQuery** `polars:user-guide/io/bigquery.md` - Google BigQuery integration
- **Hugging Face** `polars:user-guide/io/hugging-face.md` - Loading datasets from HF

---

## SQL Interface

- **SQL Introduction** `polars:user-guide/sql/intro.md` - SQL context for Polars DataFrames
- **SELECT** `polars:user-guide/sql/select.md` - Query syntax
- **CREATE** `polars:user-guide/sql/create.md` - Creating tables
- **CTEs** `polars:user-guide/sql/cte.md` - Common Table Expressions
- **SHOW** `polars:user-guide/sql/show.md` - Metadata queries

---

## Migration Guides

- **From pandas** `polars:user-guide/migration/pandas.md` - Key differences, API mapping, performance tips
- **From Spark** `polars:user-guide/migration/spark.md` - Translating Spark patterns to Polars

---

## Advanced Topics

### Performance
- **GPU Support** `polars:user-guide/gpu-support.md` - NVIDIA GPU acceleration for in-memory workloads
- **GPU in Lazy API** `polars:user-guide/lazy/gpu.md` - GPU-accelerated query execution
- **Multiprocessing** `polars:user-guide/misc/multiprocessing.md` - Parallel processing patterns
- **Multiplexing** `polars:user-guide/lazy/multiplexing.md` - Efficient query reuse

### Extensibility
- **Plugins Overview** `polars:user-guide/plugins/index.md` - Extending Polars functionality
- **Expression Plugins** `polars:user-guide/plugins/expr_plugins.md` - Custom expression functions in Rust
- **IO Plugins** `polars:user-guide/plugins/io_plugins.md` - Custom data source/sink implementations

### Misc
- **Visualization** `polars:user-guide/misc/visualization.md` - Plotting with hvPlot, Altair, Plotly
- **Styling** `polars:user-guide/misc/styling.md` - DataFrame display formatting
- **Polars for LLMs** `polars:user-guide/misc/polars_llms.md` - Using Polars with language models
- **Comparison** `polars:user-guide/misc/comparison.md` - Polars vs other tools
- **Ecosystem** `polars:user-guide/ecosystem.md` - Related libraries and integrations

---

## API Reference

- **Python/Rust API** `polars:api/reference.md` - Links to full API documentation

---

## Development

- **Contributing** `polars:development/contributing/index.md` - How to contribute to Polars
- **IDE Setup** `polars:development/contributing/ide.md` - Development environment
- **Testing** `polars:development/contributing/test.md` - Running tests
- **CI** `polars:development/contributing/ci.md` - Continuous integration
- **Code Style** `polars:development/contributing/code-style.md` - Code conventions
- **Versioning** `polars:development/versioning.md` - Version policy

---

## Releases

- **Changelog** `polars:releases/changelog.md` - Version history
- **Upgrade to 1.0** `polars:releases/upgrade/1.md` - Breaking changes in v1.0
- **Upgrade to 0.20** `polars:releases/upgrade/0.20.md` - Changes in v0.20
- **Upgrade to 0.19** `polars:releases/upgrade/0.19.md` - Changes in v0.19
