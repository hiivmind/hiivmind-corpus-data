# DataFusion Documentation Index

> Sources: 2 | Entries: 108 | Generated: 2026-07-02T00:00:00Z
> Generated from `index.yaml` — do not edit directly

---

## Python Bindings

- **null** `datafusion-python:contributor-guide/ffi.md` - Pending re-scan
- **null** `datafusion-python:contributor-guide/index.md` - Pending re-scan
- **null** `datafusion-python:contributor-guide/introduction.md` - Pending re-scan
- **null** `datafusion-python:user-guide/ai-coding-assistants.md` - Pending re-scan
- **null** `datafusion-python:user-guide/basics.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/aggregations.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/basic-info.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/expressions.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/functions.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/index.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/joins.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/select-and-filter.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/spark-functions.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/udf-and-udfa.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/views.md` - Pending re-scan
- **null** `datafusion-python:user-guide/common-operations/windows.md` - Pending re-scan
- **null** `datafusion-python:user-guide/configuration.md` - Pending re-scan
- **null** `datafusion-python:user-guide/data-sources.md` - Pending re-scan
- **null** `datafusion-python:user-guide/dataframe/execution-metrics.md` - Pending re-scan
- **null** `datafusion-python:user-guide/dataframe/index.md` - Pending re-scan
- **null** `datafusion-python:user-guide/dataframe/rendering.md` - Pending re-scan
- **null** `datafusion-python:user-guide/distributing-work.md` - Pending re-scan
- **null** `datafusion-python:user-guide/index.md` - Pending re-scan
- **null** `datafusion-python:user-guide/introduction.md` - Pending re-scan
- **null** `datafusion-python:user-guide/io/arrow.md` - Pending re-scan
- **null** `datafusion-python:user-guide/io/avro.md` - Pending re-scan
- **null** `datafusion-python:user-guide/io/csv.md` - Pending re-scan
- **null** `datafusion-python:user-guide/io/index.md` - Pending re-scan
- **null** `datafusion-python:user-guide/io/json.md` - Pending re-scan
- **null** `datafusion-python:user-guide/io/parquet.md` - Pending re-scan
- **null** `datafusion-python:user-guide/io/table_provider.md` - Pending re-scan
- **null** `datafusion-python:user-guide/sql.md` - Pending re-scan
- **null** `datafusion-python:user-guide/upgrade-guides.md` - Pending re-scan
- **Create Table (Python)** `datafusion-python:mdbook/src/usage/create-table.md` - Guide for creating tables from Python dicts, CSV, and Parquet files.
- **DataFusion Book** `datafusion-python:mdbook/src/index.md` - Introduction to DataFusion as a high-performance query engine with Python and SQL bindings.
- **DataFusion Quickstart (Python)** `datafusion-python:mdbook/src/quickstart.md` - Quick intro demonstrating DataFrame creation and queries using SQL and Python APIs.
- **Installation (Python)** `datafusion-python:mdbook/src/installation.md` - Installation guide for DataFusion Python using uv and pip, plus JupyterLab setup.
- **Query Plans (Python)** `datafusion-python:mdbook/src/usage/query-plans.md` - Understanding logical, optimized, and physical query plans with GraphViz visualization.
- **Query Table (Python)** `datafusion-python:mdbook/src/usage/query-table.md` - Querying tables using SQL and Python APIs with filtering and aggregation examples.
- **Summary** `datafusion-python:mdbook/src/SUMMARY.md` - Table of contents for DataFusion Python documentation.
- **Usage (Python)** `datafusion-python:mdbook/src/usage/index.md` - Overview of creating DataFrames from various data sources and querying with SQL or Python.

## guide

- **Adding User Defined Functions: Scalar/Window/Aggregate/Table Functions** `datafusion:library-user-guide/functions/adding-udfs.md` - User Defined Functions (UDFs) are functions that can be used in the context of DataFusion execution. This page covers how to add UDFs to DataFusion. In particular, it covers how to add Scalar, Window, ⚡ GREP - `grep -n '^## ' FILE -A 20`
- **Building Logical Plans** `datafusion:library-user-guide/building-logical-plans.md` - A logical plan is a structured representation of a database query that describes the high-level operations and transformations needed to retrieve data from a database or data source. It abstracts away
- **CLI Specific Functions** `datafusion:user-guide/cli/functions.md` - `datafusion-cli` comes with build-in functions that are not included in the DataFusion SQL engine by default. These functions are:
- **Catalogs, Schemas, and Tables** `datafusion:library-user-guide/catalogs.md` - This section describes how to create and manage catalogs, schemas, and tables in DataFusion. For those wanting to dive into the code quickly please see the [example](https://github.com/apache/datafusi
- **Custom Table Provider** `datafusion:library-user-guide/custom-table-providers.md` - One of DataFusion's greatest strengths is its extensibility. If your data lives in a custom format, behind an API, or in a system that DataFusion does not
- **DDL** `datafusion:user-guide/sql/ddl.md` - "DDL stands for ""Data Definition Language"" and relates to creating and modifying catalog objects such as Tables."
- **DML** `datafusion:user-guide/sql/dml.md` - "DML stands for ""Data Manipulation Language"" and relates to inserting and modifying data in tables."
- **Download** `datafusion:download.md` - Most users use DataFusion as a library in their Rust projects by adding it as a dependency in their `Cargo.toml` file and downloading it from the Rust [crates.io] package registry.
- **EXPLAIN** `datafusion:user-guide/sql/explain.md` - The `EXPLAIN` command shows the logical and physical execution plan for the specified SQL statement. EXPLAIN [ANALYZE] [VERBOSE] [FORMAT format] statement
- **Example Usage** `datafusion:user-guide/example-usage.md` - In this example some simple processing is performed on the [`example.csv`](https://github.com/apache/datafusion/blob/main/datafusion/core/tests/data/example.csv) file. Even [`more code examples`](http
- **Extending Operators** `datafusion:library-user-guide/extending-operators.md` - DataFusion supports extending operators by transforming [`LogicalPlan`] and [`ExecutionPlan`] through customized [optimizer rules](https://docs.rs/datafusion/latest/datafusion/optimizer/trait.Optimize
- **Extending SQL Syntax** `datafusion:library-user-guide/extending-sql.md` - DataFusion provides a flexible extension system that allows you to customize SQL parsing and planning without modifying the core codebase. This is useful when you
- **Extensions List** `datafusion:library-user-guide/extensions.md` - "DataFusion tries to provide a good set of features ""out of the box"" to quickly start with a working system, but it can't include every useful feature (e.g."
- **Format Options** `datafusion:user-guide/sql/format_options.md` - DataFusion supports customizing how data is read from or written to disk as a result of a `COPY`, `INSERT INTO`, or `CREATE EXTERNAL TABLE` statements. There are a few special options, file format (e.
- **Gentle Arrow Introduction** `datafusion:user-guide/arrow-introduction.md` - DataFusion uses [Apache Arrow] as its native in-memory format, so anyone using DataFusion will likely interact with Arrow at some point. This guide introduces the key Arrow concepts you need to know t
- **Information Schema** `datafusion:user-guide/sql/information_schema.md` - DataFusion supports showing metadata about the tables and views available. This information can be accessed using the views of the ISO SQL `information_schema` schema or the DataFusion specific `SHOW
- **Introduction** `datafusion:library-user-guide/index.md` - The library user guide explains how to use the DataFusion library as a dependency in your Rust project and customize its behavior using its extension APIs.
- **Introduction** `datafusion:user-guide/introduction.md` - DataFusion is a very fast, extensible query engine for building high-quality data-centric systems in [Rust](http://rustlang.org),
- **Local Files / Directories** `datafusion:user-guide/cli/datasources.md` - Files can be queried directly by enclosing the file, directory name or a remote location in single `'` quotes as shown in the examples.
- **Overview** `datafusion:user-guide/cli/overview.md` - DataFusion CLI (`datafusion-cli`) is an interactive command-line utility for executing SQL queries against any supported data files.
- **Prepared Statements** `datafusion:user-guide/sql/prepared_statements.md` - The `PREPARE` statement allows for the creation and storage of a SQL statement with placeholder arguments. The prepared statements can then be executed repeatedly in an efficient manner.
- **SELECT syntax** `datafusion:user-guide/sql/select.md` - The queries in DataFusion scan data from tables and return 0 or more rows. Please be aware that column names in queries are made lower-case, but not on the inferred schema. Accordingly, if you
- **Spark Compatible Functions** `datafusion:library-user-guide/functions/spark.md` - The [`datafusion-spark`] crate provides Apache Spark-compatible expressions for use with DataFusion.
- **Struct Type Coercion and Field Mapping** `datafusion:user-guide/sql/struct_coercion.md` - DataFusion uses **name-based field mapping** when coercing struct types across different operations. This document explains how struct coercion works, when it applies, and how to handle NULL fields. W
- **Subqueries** `datafusion:user-guide/sql/subqueries.md` - Subqueries (also known as inner queries or nested queries) are queries within a query.
- **Table Constraint Enforcement** `datafusion:library-user-guide/table-constraints.md` - Table providers can describe table constraints using the [`TableConstraint`] and [`Constraints`] APIs. These constraints include
- **Usage** `datafusion:user-guide/cli/usage.md` - See the current usage using `datafusion-cli --help`: Available commands inside DataFusion CLI are:
- **Using the SQL API** `datafusion:library-user-guide/using-the-sql-api.md` - DataFusion has a full SQL API that allows you to interact with DataFusion using SQL query strings. The simplest way to use the SQL API is to use the
- **Working with `Expr`s** `datafusion:library-user-guide/working-with-exprs.md` - "`Expr` is short for ""expression"". It is a core abstraction in DataFusion for representing a computation, and follows the standard ""expression tree"" abstraction found in most compilers and databases. F"

## reference

- **API health policy** `datafusion:contributor-guide/api-health.md` - DataFusion is used extensively as a library in other applications and has a large public API. We try to keep the API well maintained and minimize breaking
- **Aggregate Functions** `datafusion:user-guide/sql/aggregate_functions.md` - Aggregate functions operate on a set of values to compute a single result. Aggregate functions support the SQL `FILTER (WHERE ...)` clause to restrict which input rows contribute to the aggregate resu ⚡ GREP - `grep -n '^## ' FILE -A 20`
- **Architecture** `datafusion:contributor-guide/architecture.md` - DataFusion's code structure and organization is described in the [crates.io documentation], to keep it as close to the source as
- **Concepts, Readings, Events** `datafusion:user-guide/concepts-readings-events.md` - - **2024-06-13**: [2024 ACM SIGMOD International Conference on Management of Data: Apache Arrow DataFusion: A Fast, Embeddable, Modular Analytic Query Engine](https://dl.acm.org/doi/10.1145/3626246.36
- **Configuration Settings** `datafusion:user-guide/configs.md` - DataFusion configurations control various aspects of DataFusion planning and execution You can set the options programmatically via the [`ConfigOptions`] object. For
- **Crate Configuration** `datafusion:user-guide/crate-configuration.md` - This section contains information on how to configure builds of DataFusion in your Rust project. The [Configuration Settings] section lists options that
- **Data Types** `datafusion:user-guide/sql/data_types.md` - DataFusion uses Arrow, and thus the Arrow type system, for query execution. The SQL types from
- **DataFrame API** `datafusion:user-guide/dataframe.md` - A DataFrame represents a logical set of rows with the same named columns, similar to a [Pandas DataFrame] or [Spark DataFrame].
- **Development Environment** `datafusion:contributor-guide/development_environment.md` - This section describes how you can get started at developing DataFusion. For the fastest path to a working local environment, follow these steps
- **Expression API** `datafusion:user-guide/expressions.md` - DataFrame methods such as `select` and `filter` accept one or more logical expressions and there are many functions available for creating logical expressions. These are documented below.
- **Features** `datafusion:user-guide/features.md` - - [x] SQL Parser - [x] SQL Query Planner
- **Frequently Asked Questions** `datafusion:user-guide/faq.md` - "Apache Arrow is a library which provides a standardized memory representation for columnar data. It also provides ""kernels"" for performing common operations on this data."
- **HOWTOs** `datafusion:contributor-guide/howtos.md` - Make a PR to update the [rust-toolchain] file in the root of the repository. [rust-toolchain]: https://github.com/apache/datafusion/blob/main/rust-toolchain.toml
- **Introduction** `datafusion:contributor-guide/index.md` - We welcome and encourage contributions of all kinds, from all levels, such as: 1. Tickets with issue reports or feature requests
- **Invariants** `datafusion:contributor-guide/specification/invariants.md` - This document enumerates invariants of DataFusion's logical and physical planes (functions, and nodes). Some of these invariants are currently not enforced.
- **Metrics** `datafusion:user-guide/metrics.md` - DataFusion operators expose runtime metrics so you can understand where time is spent and how much data flows through the pipeline. See more in [EXPLAIN ANALYZE](sql/explain.md#explain-analyze). `Base
- **Operators and Literals** `datafusion:user-guide/sql/operators.md` - - [+ (plus)](#op_plus) - [- (minus)](#op_minus)
- **Output field name semantics** `datafusion:contributor-guide/specification/output-field-name-semantic.md` - This specification documents how field names in output record batches should be generated based on given user queries. The filed name rules apply to
- **Profiling Cookbook** `datafusion:library-user-guide/profiling.md` - The section contains examples how to perform CPU profiling for Apache DataFusion on different operating systems. [Video: how to CPU profile DataFusion with a Flamegraph](https://youtu.be/2z11xtYw_xs)
- **Query Optimizer** `datafusion:library-user-guide/query-optimizer.md` - [DataFusion][df] is an extensible query execution framework, written in Rust, that uses Apache Arrow as its in-memory format.
- **Reading Explain Plans** `datafusion:user-guide/explain-usage.md` - This section describes of how to read a DataFusion query plan. While fully comprehending all details of these plans requires significant expertise in the
- **Roadmap and Improvement Proposals** `datafusion:contributor-guide/roadmap.md` - The [project introduction](../user-guide/introduction) explains the overview and goals of DataFusion, and our development efforts largely
- **Scalar Functions** `datafusion:user-guide/sql/scalar_functions.md` - - [abs](#abs) - [acos](#acos) ⚡ GREP - `grep -n '^## ' FILE -A 20` ⏳ STALE
- **Special Functions** `datafusion:user-guide/sql/special_functions.md` - - [unnest](#unnest) - [unnest(struct)](#unnest-struct)
- **Testing** `datafusion:contributor-guide/testing.md` - Tests are critical to ensure that DataFusion is working properly and is not accidentally broken during refactorings. All new features
- **Upgrading Guides** `datafusion:library-user-guide/upgrading/[all-versions]` - Version migration guides covering all DataFusion releases from 46.0.0 through 54.0.0 with breaking changes, deprecations, and upgrade instructions for each version. ⚡ GREP - `grep -n '^## DataFusion' FILE -A 10`
- **Using the DataFrame API** `datafusion:library-user-guide/using-the-dataframe-api.md` - The [Users Guide] introduces the [`DataFrame`] API and this section describes that API in more depth.
- **Window Functions** `datafusion:user-guide/sql/window_functions.md` - A _window function_ performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate func
- **Workspace Dependency Graph** `datafusion:contributor-guide/architecture/dependency-graph.md` - This page shows the dependency relationships between DataFusion's workspace crates. This only includes internal dependencies, external crates like `Arrow` are not included

## tutorial

- **Installation** `datafusion:user-guide/cli/installation.md` - To build and install the latest release of `datafusion-cli` from source, do: `datafusion-cli` can also be installed via [Homebrew] (on MacOS) like this:

## unknown

- **null** `datafusion:contributor-guide/communication.md` - Pending re-scan
- **null** `datafusion:contributor-guide/governance.md` - Pending re-scan
- **null** `datafusion:contributor-guide/inviting.md` - Pending re-scan
- **null** `datafusion:contributor-guide/release_management.md` - Pending re-scan
- **null** `datafusion:library-user-guide/upgrading/49.0.0.md` - Pending re-scan
- **null** `datafusion:library-user-guide/upgrading/53.0.0.md` - Pending re-scan
- **null** `datafusion:library-user-guide/upgrading/54.0.0.md` - Pending re-scan
- **null** `datafusion:library-user-guide/upgrading/55.0.0.md` - Pending re-scan

---

*Rendered from index.yaml at 2026-07-02T00:00:00Z*
