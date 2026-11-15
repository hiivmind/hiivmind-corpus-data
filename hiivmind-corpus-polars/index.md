# Polars Documentation Index

> Sources: 1 | Entries: 79 | Generated: 2026-11-15T00:53:26Z
> Generated from `index.yaml` — do not edit directly

---

## Api

- **Python/Rust API** `polars:api/reference.md` - Links to full API documentation for Python and Rust

## Guide

- **CI** `polars:development/contributing/ci.md` - Continuous integration
- **Casting** `polars:user-guide/expressions/casting.md` - Explains converting column data types with cast, including the strict parameter, downcasting numerics, string/numeric and boolean conversions, and parsing or formatting temporal types.
- **Categorical data and enums** `polars:user-guide/expressions/categorical-data-and-enums.md` - Compares the Categorical and Enum data types for string columns with a limited set of values, showing how to create, order and compare them. Also explains why they are more performant than plain strings, including encodings and the shared global mapping.
- **Code Style** `polars:development/contributing/code-style.md` - Code conventions
- **Comparison with other tools** `polars:user-guide/misc/comparison.md` - Short comparison of Polars with pandas, Dask, Modin, Spark and DuckDB, with links to benchmarks and migration guides.
- **Concatenation** `polars:user-guide/transformations/concatenation.md` - Describes vertical, horizontal and diagonal concatenation of DataFrames with concat, when each fails or produces nulls, and the rechunk option and its default.
- **Excel** `polars:user-guide/io/excel.md` - Explains reading and writing Excel files from Python, the available read engines (fastexcel, xlsx2csv, openpyxl) and the xlsxwriter dependency for write_excel.
- **Expression expansion** `polars:user-guide/expressions/expression-expansion.md` - Shows how one expression can expand to many by column name, data type or regex, how to exclude and rename columns, how to generate expressions programmatically, and how to use selectors with set operations. Ends with a reference of selector functions.
- **Generating Polars code with LLMs** `polars:user-guide/misc/polars_llms.md` - Practical approaches for getting LLMs to produce valid Polars code: the Polars skill for agents, the Polars MCP server, system prompts, web search and including examples in prompts.
- **IDE configuration** `polars:development/contributing/ide.md` - Recommendations for configuring VS Code (rust-analyzer, Ruff, CodeLLDB) for Polars development, including a combined Rust/Python debugging setup, plus a placeholder for JetBrains IDEs.
- **Introduction** `polars:user-guide/sql/intro.md` - Introduces SQL support in Polars through SQLContext: registering frames, attaching Iceberg catalogs and running DDL/DML against them, executing queries lazily or eagerly, querying multiple sources, and which SQL features are supported.
- **Multiplexing queries** `polars:user-guide/lazy/multiplexing.md` - Explains why branching a LazyFrame re-evaluates its query plan on every collect, which can give unstable results, and how collect_all combines the diverging plans into one optimized execution with shared subplans.
- **Overview** `polars:development/contributing/index.md` - The contributor guide for Polars: reporting bugs, suggesting enhancements, setting up a local Rust and Python environment, opening pull requests, contributing to documentation and the API reference, and the maintainer release flow.
- **Parsing** `polars:user-guide/transformations/time-series/parsing.md` - Covers Polars' temporal data types and how to parse dates from CSV files, cast strings to dates, extract date features with the dt namespace, and handle datetimes with mixed UTC offsets.
- **Sources and sinks** `polars:user-guide/lazy/sources_sinks.md` - Explains why LazyFrame queries should use scan_* readers, and how sinks stream query results to disk or cloud storage, including partitioned output, failure behaviour and multiplexing several sinks in one query.
- **Streaming** `polars:user-guide/concepts/streaming.md` - Describes executing lazy queries in batches with the streaming engine, how to inspect the physical plan of a streaming query, and how to monitor per-node metrics in Polars Nanook.
- **Strings** `polars:user-guide/expressions/strings.md` - Covers working with string data through the str namespace: checking, extracting and replacing patterns with regex, concatenating, changing case, stripping characters and slicing.
- **Structs** `polars:user-guide/expressions/structs.md` - Introduces the Struct data type: where it arises (such as value_counts), how to unnest, build, extract from and rename its fields, and practical uses like finding duplicate rows, multi-column ranking and passing several columns to one expression.
- **Styling** `polars:user-guide/misc/styling.md` - Shows how to style a DataFrame for presentation with the DataFrame.style property, which returns a Great Tables object, covering headers, row stubs, column spanners, number formatting and cell styling.
- **Test suite** `polars:development/contributing/test.md` - Describes the components of the py-polars test suite (unit, parametric, benchmark tests and doctests), how to run each, and guidelines for writing new tests and docstring examples.
- **Versioning** `polars:development/versioning.md` - Version policy
- **Window functions** `polars:user-guide/expressions/window-functions.md` - Explains window functions with over: computing operations per group within select, the mapping strategies group_to_rows, explode and join, windowed aggregations that broadcast scalars, and further exercises using a Pokémon dataset.

## Journal

- **Version 0.20** `polars:releases/upgrade/0.20.md` - Upgrade guide for Polars 0.20 listing breaking changes with before/after examples (join null handling, outer join keys, count ignoring nulls, NaN equality, data type instantiation, replace, value_counts) and the cum_* renames.
- **Version 1.0** `polars:releases/upgrade/1.md` - Upgrade guide for Polars 1.0 listing breaking changes with before/after examples (Series constructor strictness, replace/replace_strict, parquet hive partitioning, pivot, read_excel engine and more) and the LazyFrame schema property deprecation. ⚡ GREP - `"grep -n ""^### "" FILE"`

## Navigation

- **Ecosystem** `polars:user-guide/ecosystem.md` - A non-exhaustive list of libraries and tools that integrate with Polars, grouped into Apache Arrow, IO, machine learning and other tools such as DuckDB, Great Tables, LanceDB, Mage, marimo and Narwhals.

## Reference

- **Aggregation** `polars:user-guide/expressions/aggregation.md` - group_by().agg() context. Multiple aggregations, conditional aggregations, filtering within groups, nested grouping, sorting within groups. Avoid Python lambdas to preserve parallelization
- **Arrow Producer/Consumer** `polars:user-guide/misc/arrow.md` - Zero-copy data exchange: PyArrow to_arrow()/pl.from_arrow() for DataFrame/Table conversion, zero-copy export with compat_level, PyCapsule Interface (v1.3+) standard protocol, C Data Interface for direct struct exchange without PyArrow
- **Basic Operations** `polars:user-guide/expressions/basic-operations.md` - Arithmetic (+, -, *, /), comparisons (>, <, ==), Boolean operations (&, |, ~), counting unique values (n_unique, approx_n_unique, value_counts), conditionals with when().then().otherwise()
- **BigQuery** `polars:user-guide/io/bigquery.md` - Google BigQuery integration
- **CSV** `polars:user-guide/io/csv.md` - read_csv(), scan_csv(), write_csv()
- **Changelog** `polars:releases/changelog.md` - Version history
- **Cloud Storage** `polars:user-guide/io/cloud-storage.md` - S3, GCS, Azure Blob. Cloud retry configuration via storage_options, global credential providers, writing to file objects for unsupported formats
- **Data Types and Structures** `polars:user-guide/concepts/data-types-and-structures.md` - Series (1D homogeneous), DataFrame (2D heterogeneous, uniquely named series), Schema (column-to-type mapping). Inspection methods: head, tail, glimpse, sample, describe. Schema override via schema dict or schema_overrides parameter. Arrow Columnar Format internally. Full type table including numeric (Int8-Int128, UInt8-UInt128, Float16/32/64, Decimal), temporal (Date, Time, Datetime, Duration), nested (List, Array, Struct), string/binary, categorical/enum, boolean, null, object. IEEE 754 floating point with NaN equality semantics
- **DataType Expressions** `polars:user-guide/lazy/datatype_exprs.md` - Runtime type inspection and manipulation with pl.dtype_of(). Express relations between expression datatypes, inspect type info at runtime, cast columns to match another column's type. Useful for utility functions, heterogeneous data sources
- **Database** `polars:user-guide/io/database.md` - SQL database connections
- **Execution** `polars:user-guide/lazy/execution.md` - Collecting results, streaming execution
- **Expressions Overview** `polars:user-guide/expressions/index.md` - Expression categories: essentials (basic ops, expansion, casting), type-specific namespaces (str, list, arr, cat, struct, dt), operation types (aggregation, window, folds), user-defined functions
- **Expressions and Contexts** `polars:user-guide/concepts/expressions-and-contexts.md` - Core DSL concepts. Expressions are lazy transformations. Four contexts: select (column operations), with_columns (add columns), filter (row filtering), group_by (aggregations). Expression expansion for multi-column operations
- **Filtering Time Series** `polars:user-guide/transformations/time-series/filter.md` - Date range filtering
- **Folds** `polars:user-guide/expressions/folds.md` - Horizontal operations with fold(). Custom row-wise computations across columns, similar to functools.reduce. Use concat_str() for string concatenation
- **GPU Support** `polars:user-guide/gpu-support.md` - NVIDIA GPU acceleration for in-memory workloads
- **GPU in Lazy API** `polars:user-guide/lazy/gpu.md` - GPU-accelerated query execution in lazy mode
- **Hive Partitioning** `polars:user-guide/io/hive.md` - Partitioned datasets
- **Hugging Face** `polars:user-guide/io/hugging-face.md` - Loading datasets from Hugging Face Hub
- **IO Overview** `polars:user-guide/io/index.md` - Supported formats and common patterns for reading and writing data
- **JSON** `polars:user-guide/io/json.md` - JSON and NDJSON support. Lazy scanning with scan_ndjson() for LazyFrame-based NDJSON reading
- **Joins** `polars:user-guide/transformations/joins.md` - Comprehensive join operations: equi joins (inner, left, right, full, semi, anti), non-equi joins (join_where with arbitrary predicates), asof joins (join_asof with nearest key, tolerance, strategy), cross join. Key expressions for dynamic matching, coalesce parameter
- **Lazy API Overview** `polars:user-guide/concepts/lazy-api.md` - LazyFrame vs DataFrame, query optimization benefits
- **Lists and Arrays** `polars:user-guide/expressions/lists-and-arrays.md` - List (variable length) vs Array (fixed shape). List namespace (list): slicing (head, tail), explode(), element-wise ops with eval() and element, row-wise aggregation with concat_list(). Array namespace (arr): fixed-shape operations
- **Migration from Spark** `polars:user-guide/migration/spark.md` - Translating Spark patterns to Polars
- **Migration from pandas** `polars:user-guide/migration/pandas.md` - Key differences, API mapping, performance tips for migrating from pandas to Polars
- **Missing Data** `polars:user-guide/expressions/missing-data.md` - Handling null values: is_null(), fill_null(), drop_nulls(), forward/backward fill. null is distinct from NaN (floating point only)
- **Multiple Files** `polars:user-guide/io/multiple.md` - Glob patterns, lazy scanning multiple files
- **Multiprocessing** `polars:user-guide/misc/multiprocessing.md` - Parallel processing patterns
- **NumPy Functions** `polars:user-guide/expressions/numpy-functions.md` - Using NumPy ufuncs with Polars data
- **Parquet** `polars:user-guide/io/parquet.md` - Columnar format, predicate pushdown
- **Pivot** `polars:user-guide/transformations/pivot.md` - Reshape data: group by columns become y-axis, pivot column becomes x-axis. Aggregations: first, last, sum, min, max, mean, median, len. Lazy workarounds: collect first or specify on_columns for static schema declaration
- **Plugins Overview** `polars:user-guide/plugins/index.md` - Extending Polars functionality with plugins
- **Query Optimizations** `polars:user-guide/lazy/optimizations.md` - Predicate pushdown, projection pushdown, slice pushdown
- **Query Plans** `polars:user-guide/lazy/query-plan.md` - Understanding and visualizing query plans with explain()
- **Resampling** `polars:user-guide/transformations/time-series/resampling.md` - Downsampling/upsampling temporal data
- **Rolling Operations** `polars:user-guide/transformations/time-series/rolling.md` - Rolling windows for time series
- **SELECT** `polars:user-guide/sql/select.md` - Shows the SELECT statement in Polars SQL, including GROUP BY, ORDER BY, JOIN, built-in functions, and the read_csv, read_ndjson, read_parquet and read_ipc table functions with their named options.
- **SQL CREATE** `polars:user-guide/sql/create.md` - Creating tables in SQL context
- **SQL CTEs** `polars:user-guide/sql/cte.md` - Common Table Expressions in SQL context
- **SQL SHOW** `polars:user-guide/sql/show.md` - Metadata queries in SQL context
- **Schemas in Lazy** `polars:user-guide/lazy/schemas.md` - Schema inference and validation in lazy mode
- **Timezones** `polars:user-guide/transformations/time-series/timezones.md` - Timezone handling and conversion
- **Unpivot** `polars:user-guide/transformations/unpivot.md` - Reverse of pivot, wide to long format
- **Upgrade to 0.19** `polars:releases/upgrade/0.19.md` - Changes in v0.19
- **User-Defined Python Functions** `polars:user-guide/expressions/user-defined-python-functions.md` - map_elements(), map_batches() for custom Python logic. Performance implications with GIL. Recommends Polars plugins (expression/IO) as higher-performance alternative
- **Using the Lazy API** `polars:user-guide/lazy/using.md` - Converting between eager/lazy, when to use each
- **Visualization** `polars:user-guide/misc/visualization.md` - Plotting with hvPlot, Altair, Plotly

## Tutorial

- **Expression Plugins** `polars:user-guide/plugins/expr_plugins.md` - Walks through creating a custom expression plugin in Rust, from the Cargo setup and the polars_expr function to the Python registration, with sections on accepting kwargs and computing output data types.
- **Getting started** `polars:user-guide/getting-started.md` - A tour of the fundamentals of Polars: installing it, reading and writing data, using expressions in the select, with_columns, filter and group_by contexts, and combining dataframes with joins and concatenation.
- **IO Plugins** `polars:user-guide/plugins/io_plugins.md` - Describes the IO plugin interfaces for custom file formats: FileReader/FileReaderBuilder with scan_external_reader, LazyFrameResolver for dynamic path resolution, and generator-based sources registered with register_io_source.
- **Installation** `polars:user-guide/installation.md` - Installing Polars and optional feature flags
- **Introduction** `polars:index.md` - Overview of Polars: blazingly fast DataFrame library written in Rust, available for Python/R/NodeJS. Key features: parallel execution, lazy API, Arrow support, GPU acceleration

---

*Rendered from index.yaml at 2026-11-15T00:53:26Z*
