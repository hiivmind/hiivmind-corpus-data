# Ibis Documentation Index

> Source: ibis (git) | 143 docs | The portable Python dataframe library
> Last updated: 2025-12-10

---

## Getting Started

- **Introduction** `ibis:index.qmd` - Ibis: the portable Python dataframe library. Same API for ~20 backends, fast local dataframes with DuckDB (default), Polars, DataFusion. Iterate locally, deploy remotely by changing one line. Bridges SQL and Python
- **Why Ibis?** `ibis:why.qmd` - Comprehensive overview: portable API across backends, Python + SQL integration, scaling up/out, stream-batch unification, ecosystem integrations (pandas, Polars, visualization, ML libraries)
- **10 Minutes to Ibis** `ibis:tutorials/basics.qmd` - Quick tutorial: `filter`, `select`, `mutate`, `order_by`, `group_by`, `aggregate`. Uses DuckDB + Palmer penguins dataset. Interactive mode with `ibis.options.interactive = True`
- **Installation** `ibis:install.qmd` - Installing Ibis with backend-specific extras

---

## Core Concepts

### Data Types and Structures
- **Datatypes and Datashapes** `ibis:concepts/datatypes.qmd` - Every value has type (Integer, Float, String, Array) and shape (Scalar or Column). Broadcasting rules: Scalar+Scalar=Scalar, Column+Scalar=Column. Columns must be from same Table (no positional alignment like NumPy)
- **Type Casting** `ibis:concepts/casting.qmd` - Converting between data types with `cast()`
- **Backend & Table Hierarchy** `ibis:concepts/backend-table-hierarchy.qmd` - How backends, connections, and tables relate
- **Internals** `ibis:concepts/internals.qmd` - Under the hood: expression trees, compilation to SQL
- **Versioning** `ibis:concepts/versioning.qmd` - Version policy and compatibility

### Architecture
- **Composable Ecosystem** `ibis:concepts/composable-ecosystem.qmd` - How Ibis fits into the data ecosystem
- **Who Uses Ibis** `ibis:concepts/who.qmd` - Users and organizations
- **User Testimonials** `ibis:concepts/user-testimonials.qmd` - Real-world experiences

---

## Backends

### Local/Embedded
- **DuckDB** `ibis:backends/duckdb.qmd` - Default backend. `ibis.connect("duckdb://")`. Supports CSV, Parquet, Delta Lake, JSON, PyArrow. MotherDuck cloud support. Geospatial operations. Secret management for S3/cloud storage
- **Polars** `ibis:backends/polars.qmd` - Fast local dataframes with Polars backend
- **DataFusion** `ibis:backends/datafusion.qmd` - Apache DataFusion backend
- **pandas** `ibis:backends/pandas.qmd` - pandas backend for compatibility
- **Dask** `ibis:backends/dask.qmd` - Distributed computing with Dask

### Cloud Data Warehouses
- **BigQuery** `ibis:backends/bigquery.qmd` - Google BigQuery backend
- **Snowflake** `ibis:backends/snowflake.qmd` - Snowflake backend
- **Databricks** `ibis:backends/databricks.qmd` - Databricks backend
- **Athena** `ibis:backends/athena.qmd` - AWS Athena backend

### Databases
- **PostgreSQL** `ibis:backends/postgresql.qmd` - PostgreSQL backend
- **MySQL** `ibis:backends/mysql.qmd` - MySQL backend
- **SQLite** `ibis:backends/sqlite.qmd` - SQLite backend
- **ClickHouse** `ibis:backends/clickhouse.qmd` - ClickHouse backend
- **MS SQL** `ibis:backends/mssql.qmd` - Microsoft SQL Server backend
- **Oracle** `ibis:backends/oracle.qmd` - Oracle database backend
- **Trino** `ibis:backends/trino.qmd` - Trino distributed SQL backend
- **Exasol** `ibis:backends/exasol.qmd` - Exasol backend
- **Druid** `ibis:backends/druid.qmd` - Apache Druid backend
- **Impala** `ibis:backends/impala.qmd` - Apache Impala backend
- **RisingWave** `ibis:backends/risingwave.qmd` - RisingWave streaming database

### Streaming & Big Data
- **PySpark** `ibis:backends/pyspark.qmd` - Apache Spark via PySpark
- **Flink** `ibis:backends/flink.qmd` - Apache Flink streaming backend

### Backend Support
- **Support Matrix** `ibis:backends/support/matrix.qmd` - Operations supported per backend
- **Cloud Support Policy** `ibis:backends/support/cloud_support_policy.qmd` - Cloud backend support guidelines

---

## Coming From...

- **pandas** `ibis:tutorials/coming-from/pandas.qmd` - Comprehensive migration guide: immutable tables, lazy evaluation, no row index, `filter` vs `loc`, `mutate` vs column assignment, `order_by` vs `sort_values`, `aggregate` vs agg, `join` vs `merge`, `union` vs `concat`, NULL handling, type casting
- **SQL** `ibis:tutorials/coming-from/sql.qmd` - SQL to Ibis translation guide
- **dplyr** `ibis:tutorials/coming-from/dplyr.qmd` - R dplyr to Ibis translation guide

---

## How-To Guides

### Analytics
- **Analytics Basics** `ibis:how-to/analytics/basics.qmd` - Core analytics operations
- **Chaining Expressions** `ibis:how-to/analytics/chain_expressions.qmd` - Method chaining patterns
- **IMDB Analysis** `ibis:how-to/analytics/imdb.qmd` - Real-world example with IMDB data

### Configuration
- **Configuration Basics** `ibis:how-to/configure/basics.qmd` - Setting Ibis options and defaults

### Input/Output
- **IO Basics** `ibis:how-to/input-output/basics.qmd` - Reading and writing data
- **DuckDB + Parquet** `ibis:how-to/input-output/duckdb-parquet.qmd` - Working with Parquet files
- **GCS + DuckDB** `ibis:how-to/input-output/gcs_duckdb.qmd` - Google Cloud Storage integration
- **Multiple Backends** `ibis:how-to/input-output/multiple-backends.qmd` - Working with multiple backends simultaneously

### Time Series
- **Forward/Backward Fill** `ibis:how-to/timeseries/ffill_bfill_w_window.qmd` - Fill missing values with window functions
- **Sessionization** `ibis:how-to/timeseries/sessionize.qmd` - Session detection in time series

### Visualization
- **Altair** `ibis:how-to/visualization/altair.qmd` - Vega-Altair integration
- **Matplotlib** `ibis:how-to/visualization/matplotlib.qmd` - Matplotlib plotting
- **Plotly** `ibis:how-to/visualization/plotly.qmd` - Plotly interactive charts
- **plotnine** `ibis:how-to/visualization/plotnine.qmd` - ggplot2-style plotting
- **Seaborn** `ibis:how-to/visualization/seaborn.qmd` - Seaborn statistical visualization
- **Streamlit** `ibis:how-to/visualization/streamlit.qmd` - Streamlit dashboards
- **Marimo** `ibis:how-to/visualization/marimo.qmd` - Marimo notebooks
- **Graphs** `ibis:how-to/visualization/graphs.qmd` - Graph/network visualization

### Extending Ibis
- **Built-in Functions** `ibis:how-to/extending/builtin.qmd` - Using built-in functions
- **SQL Integration** `ibis:how-to/extending/sql.qmd` - Mixing SQL with Ibis expressions via `.sql()` method
- **Streaming** `ibis:how-to/extending/streaming.qmd` - Stream processing patterns
- **Unbound Expressions** `ibis:how-to/extending/unbound_expression.qmd` - Creating reusable expression templates

---

## Tutorials

### Backend-Specific
- **ClickHouse Tutorial** `ibis:tutorials/backends/clickhouse.qmd` - Getting started with ClickHouse
- **Flink Setup** `ibis:tutorials/backends/apache-flink/0_setup.qmd` - Apache Flink setup
- **Flink Single Feature** `ibis:tutorials/backends/apache-flink/1_single_feature.qmd` - Feature engineering with Flink
- **Starburst Galaxy Setup** `ibis:tutorials/backends/starburst-galaxy/0_setup.qmd` - Starburst setup
- **Starburst Basics** `ibis:tutorials/backends/starburst-galaxy/1_basics.qmd` - Basic operations with Starburst

### Browser
- **REPL** `ibis:tutorials/browser/repl.qmd` - In-browser Ibis REPL (WebAssembly)

---

## API Reference

### Expression API
- **Table Expressions** `ibis:reference/expression-tables.qmd` - `Table`, `GroupedTable`, `read_csv`, `read_parquet`, `read_json`, `read_delta`, `memtable`, `table`, `join`, `union`, `intersect`, `difference`, window functions (`row_number`, `rank`, `dense_rank`, `ntile`)
- **Column Selectors** `ibis:reference/selectors.qmd` - `ibis.selectors` module: `s.numeric()`, `s.matches()`, `s.all()`, `~s.matches()` for column selection patterns
- **Generic Expressions** `ibis:reference/expression-generic.qmd` - `Value`, `Column`, `Scalar`, `Deferred`, `literal`, `param`, `null`, `range`, `coalesce`, `least`, `greatest`, `ifelse`, `cases`, `asc`, `desc`, `to_sql`
- **Numeric Expressions** `ibis:reference/expression-numeric.qmd` - `NumericValue`, `NumericColumn`, `IntegerValue`, `FloatingValue`, `DecimalValue`, `BooleanValue`, `and_`, `or_`, `random`, constants `e`, `pi`
- **String Expressions** `ibis:reference/expression-strings.qmd` - `StringValue` with string manipulation methods
- **Temporal Expressions** `ibis:reference/expression-temporal.qmd` - `TimestampValue`, `DateValue`, `TimeValue`, `IntervalValue`, `DayOfWeek`, `now`, `today`, `date`, `time`, `timestamp`, `interval`
- **Collection Expressions** `ibis:reference/expression-collections.qmd` - `ArrayValue`, `MapValue`, `StructValue`, `array`, `map`, `struct` constructors
- **JSON Expressions** `ibis:reference/expression-json.qmd` - `JSONValue` for JSON manipulation
- **Geospatial Expressions** `ibis:reference/expression-geospatial.qmd` - `GeoSpatialValue`, `GeoSpatialColumn`, `point` for geospatial data
- **Misc Expressions** `ibis:reference/expression-misc.qmd` - `uuid`, `UUIDValue`, `INETValue`, `MACADDRValue`

### Type System
- **Data Types** `ibis:reference/datatypes.qmd` - `dtype`, `DataType`, all type classes (Int8-64, UInt8-64, Float16-64, Decimal, String, Binary, Boolean, Date, Time, Timestamp, Interval, Array, Map, Struct, JSON, UUID, INET, MACADDR, geospatial types)
- **Schemas** `ibis:reference/schemas.qmd` - `schema`, `Schema` for table schemas

### UDFs
- **Scalar UDFs** `ibis:reference/scalar-udfs.qmd` - Creating scalar user-defined functions
- **Aggregate UDFs** `ibis:reference/aggregate-udfs.qmd` - Creating aggregate user-defined functions (experimental)

### Connection
- **Connection APIs** `ibis:reference/connection.qmd` - `connect`, `get_backend`, `set_backend`

### Configuration
- **Interactive** `ibis:reference/Interactive.qmd` - Interactive mode settings
- **Options** `ibis:reference/Options.qmd` - Global options configuration
- **Repr** `ibis:reference/Repr.qmd` - Output representation settings
- **SQL** `ibis:reference/SQL.qmd` - SQL generation settings

### Advanced
- **Cursed Knowledge** `ibis:reference/cursed_knowledge.qmd` - Edge cases and gotchas

---

## Contributing

- **Development Environment** `ibis:contribute/01_environment.qmd` - Setting up dev environment
- **Workflow** `ibis:contribute/02_workflow.qmd` - Contribution workflow
- **Code Style** `ibis:contribute/03_style.qmd` - Code style guidelines
- **Maintainer's Guide** `ibis:contribute/04_maintainers_guide.qmd` - For maintainers
- **Reference** `ibis:contribute/05_reference.qmd` - Contributing reference
