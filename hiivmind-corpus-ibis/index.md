# Ibis Documentation Index

> Sources: 1 | Entries: 95 | Generated: 2026-08-03T09:54:48Z
> Generated from `index.yaml` — do not edit directly

---

## Null

- **10 Minutes to Ibis** `ibis:tutorials/basics.qmd` - Quick tutorial: filter, select, mutate, order_by, group_by, aggregate. Uses DuckDB + Palmer penguins dataset. Interactive mode with ibis.options.interactive = True
- **AI & Automated Code Policy** `ibis:contribute/06_automated_code_and_ai.qmd` - AI/LLM contribution policy: AI tools allowed to assist, but all contributions require meaningful human review. Fully automated PR submissions (agents without human review) prohibited
- **Aggregate UDFs** `ibis:reference/aggregate-udfs.qmd` - Creating aggregate user-defined functions (experimental)
- **Altair Visualization** `ibis:how-to/visualization/altair.qmd` - Vega-Altair integration for visualization
- **Analytics Basics** `ibis:how-to/analytics/basics.qmd` - Core analytics operations
- **Backend & Table Hierarchy** `ibis:concepts/backend-table-hierarchy.qmd` - How backends, connections, and tables relate
- **BigQuery Backend** `ibis:backends/bigquery.qmd` - Google BigQuery backend
- **Browser REPL** `ibis:tutorials/browser/repl.qmd` - In-browser Ibis REPL (WebAssembly)
- **Built-in Functions** `ibis:how-to/extending/builtin.qmd` - Using built-in functions
- **Chaining Expressions** `ibis:how-to/analytics/chain_expressions.qmd` - Method chaining patterns
- **ClickHouse Backend** `ibis:backends/clickhouse.qmd` - ClickHouse backend
- **ClickHouse Tutorial** `ibis:tutorials/backends/clickhouse.qmd` - Getting started with ClickHouse backend
- **Cloud Support Policy** `ibis:backends/support/cloud_support_policy.qmd` - Cloud backend support guidelines
- **Code Style** `ibis:contribute/03_style.qmd` - Code style guidelines for Ibis
- **Collection Expressions** `ibis:reference/expression-collections.qmd` - ArrayValue (length, contains, unnest, filter, map, zip, sort, unique, flatten, intersection, union, remove, index, join), MapValue (get, keys, values, length, contains), StructValue (names, types, destructure). Constructors: array, map, struct
- **Column Selectors** `ibis:reference/selectors.qmd` - ibis.selectors module: s.numeric(), s.matches(), s.all(), ~s.matches() for column selection patterns
- **Coming from SQL** `ibis:tutorials/coming-from/sql.qmd` - SQL to Ibis translation guide
- **Coming from dplyr** `ibis:tutorials/coming-from/dplyr.qmd` - R dplyr to Ibis translation guide
- **Coming from pandas** `ibis:tutorials/coming-from/pandas.qmd` - Comprehensive migration guide: immutable tables, lazy evaluation, no row index, filter vs loc, mutate vs column assignment, order_by vs sort_values, aggregate vs agg, join vs merge, union vs concat, NULL handling, type casting
- **Composable Ecosystem** `ibis:concepts/composable-ecosystem.qmd` - How Ibis fits into the data ecosystem
- **Configuration Basics** `ibis:how-to/configure/basics.qmd` - Setting Ibis options and defaults
- **Connection APIs** `ibis:reference/connection.qmd` - connect, get_backend, set_backend
- **Contributing Reference** `ibis:contribute/05_reference.qmd` - Contributing reference documentation
- **Contribution Workflow** `ibis:contribute/02_workflow.qmd` - Contribution workflow for Ibis
- **Cursed Knowledge** `ibis:reference/cursed_knowledge.qmd` - Edge cases and gotchas in Ibis
- **Dask Backend** `ibis:backends/dask.qmd` - Distributed computing with Dask backend
- **Data Types Reference** `ibis:reference/datatypes.qmd` - Complete type system: dtype(), DataType base class. Numeric: Int8-Int64, UInt8-UInt64, Float16-Float64, Decimal. String/Binary: String, Binary. Boolean: Boolean. Temporal: Date, Time, Timestamp, Interval. Collections: Array, Map, Struct. Special: JSON, UUID, INET, MACADDR, geospatial types. GeoSpatial, Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon
- **DataFusion Backend** `ibis:backends/datafusion.qmd` - Apache DataFusion backend
- **Databricks Backend** `ibis:backends/databricks.qmd` - Databricks backend
- **Datatypes and Datashapes** `ibis:concepts/datatypes.qmd` - Every value has two properties: type (Integer, Float, String, Array, etc.) and shape (Scalar or Column). Type flavors define precision (e.g., int8 vs int64) without changing capabilities. Shape determines available methods: Columns have .mean(), .max(); Scalars don't. Broadcasting: Scalar+Scalar=Scalar, Column+Scalar=Column, Column+Column=Column (must be from same Table, no positional alignment like NumPy, requires explicit join)
- **Development Environment** `ibis:contribute/01_environment.qmd` - Setting up dev environment for Ibis contribution
- **Druid Backend** `ibis:backends/druid.qmd` - Apache Druid backend
- **DuckDB + Parquet** `ibis:how-to/input-output/duckdb-parquet.qmd` - Working with Parquet files using DuckDB backend
- **DuckDB Backend** `ibis:backends/duckdb.qmd` - Default backend. ibis.connect('duckdb://'). Supports CSV, Parquet, Delta Lake, JSON, PyArrow. MotherDuck cloud support. Geospatial operations. Secret management for S3/cloud storage
- **Exasol Backend** `ibis:backends/exasol.qmd` - Exasol backend
- **Flink Backend** `ibis:backends/flink.qmd` - Apache Flink streaming backend
- **Flink Setup** `ibis:tutorials/backends/apache-flink/0_setup.qmd` - Apache Flink setup tutorial
- **Flink Single Feature** `ibis:tutorials/backends/apache-flink/1_single_feature.qmd` - Feature engineering with Flink
- **Forward/Backward Fill** `ibis:how-to/timeseries/ffill_bfill_w_window.qmd` - Fill missing values with window functions
- **GCS + DuckDB** `ibis:how-to/input-output/gcs_duckdb.qmd` - Google Cloud Storage integration with DuckDB
- **Generic Expressions** `ibis:reference/expression-generic.qmd` - Value, Column, Scalar, Deferred, literal, param, null, range, coalesce, least, greatest, ifelse, cases, asc, desc, to_sql
- **Geospatial Expressions** `ibis:reference/expression-geospatial.qmd` - GeoSpatialValue (area, buffer, contains, covers, distance, intersection, transform, union, within, x, y), GeoSpatialColumn, point constructor
- **Graph Visualization** `ibis:how-to/visualization/graphs.qmd` - Graph/network visualization
- **IMDB Analysis** `ibis:how-to/analytics/imdb.qmd` - Real-world example with IMDB data
- **IO Basics** `ibis:how-to/input-output/basics.qmd` - Reading and writing data
- **Impala Backend** `ibis:backends/impala.qmd` - Apache Impala backend
- **Installation** `ibis:install.qmd` - Installing Ibis with backend-specific extras
- **Interactive Mode** `ibis:reference/Interactive.qmd` - Interactive mode settings
- **Internals** `ibis:concepts/internals.qmd` - Under the hood: expression trees, compilation to SQL
- **Introduction** `ibis:index.qmd` - Ibis: the portable Python dataframe library. Same API for 20+ backends, fast local dataframes with DuckDB (default), Polars, DataFusion. Iterate locally, deploy remotely by changing one line. Bridges SQL and Python
- **JSON Expressions** `ibis:reference/expression-json.qmd` - JSONValue: unwrap_as (cast JSON to typed values), JSON path access
- **MS SQL Backend** `ibis:backends/mssql.qmd` - Microsoft SQL Server backend
- **Maintainer's Guide** `ibis:contribute/04_maintainers_guide.qmd` - Guide for Ibis maintainers
- **Marimo Notebooks** `ibis:how-to/visualization/marimo.qmd` - Marimo notebook integration
- **Materialize Backend** `ibis:backends/materialize.qmd` - Materialize streaming database backend. Install via ibis-framework[materialize], connects on port 6875. Supports streaming via SUBSCRIBE. Added in Ibis 12.0.0
- **Matplotlib Visualization** `ibis:how-to/visualization/matplotlib.qmd` - Matplotlib plotting integration
- **Misc Expressions** `ibis:reference/expression-misc.qmd` - uuid generator, UUIDValue, INETValue (host, family), MACADDRValue
- **Multiple Backends** `ibis:how-to/input-output/multiple-backends.qmd` - Working with multiple backends simultaneously
- **Numeric Expressions** `ibis:reference/expression-numeric.qmd` - NumericValue (arithmetic, abs, ceil, floor, round, log, exp, trig), NumericColumn (sum, mean, std, var, median, quantile, corr, cov), IntegerValue, FloatingValue (isnan, isinf), DecimalValue, BooleanValue (any, all, ifelse), and_, or_, random, constants e, pi
- **Options** `ibis:reference/Options.qmd` - Global options configuration
- **Oracle Backend** `ibis:backends/oracle.qmd` - Oracle database backend
- **Plotly Visualization** `ibis:how-to/visualization/plotly.qmd` - Plotly interactive charts
- **Polars Backend** `ibis:backends/polars.qmd` - Fast local dataframes with Polars backend
- **PostgreSQL Backend** `ibis:backends/postgresql.qmd` - PostgreSQL backend
- **PySpark Backend** `ibis:backends/pyspark.qmd` - Apache Spark via PySpark
- **Repr Settings** `ibis:reference/Repr.qmd` - Output representation settings
- **RisingWave Backend** `ibis:backends/risingwave.qmd` - RisingWave streaming database
- **SQL Integration** `ibis:how-to/extending/sql.qmd` - Mixing SQL with Ibis expressions via .sql() method
- **SQL Settings** `ibis:reference/SQL.qmd` - SQL generation settings
- **SQLite Backend** `ibis:backends/sqlite.qmd` - SQLite backend
- **Scalar UDFs** `ibis:reference/scalar-udfs.qmd` - Creating scalar user-defined functions
- **Schemas** `ibis:reference/schemas.qmd` - schema(), Schema class for defining and inspecting table column types
- **Seaborn Visualization** `ibis:how-to/visualization/seaborn.qmd` - Seaborn statistical visualization
- **Sessionization** `ibis:how-to/timeseries/sessionize.qmd` - Session detection in time series
- **SingleStoreDB Backend** `ibis:backends/singlestoredb.qmd` - SingleStoreDB backend. Install via ibis-framework[singlestoredb], connects on port 3306. Added in Ibis 12.0.0
- **Snowflake Backend** `ibis:backends/snowflake.qmd` - Snowflake backend
- **Starburst Galaxy Basics** `ibis:tutorials/backends/starburst-galaxy/1_basics.qmd` - Basic operations with Starburst Galaxy
- **Starburst Galaxy Setup** `ibis:tutorials/backends/starburst-galaxy/0_setup.qmd` - Starburst Galaxy setup tutorial
- **Streaming** `ibis:how-to/extending/streaming.qmd` - Stream processing patterns with Ibis
- **Streamlit Dashboards** `ibis:how-to/visualization/streamlit.qmd` - Streamlit dashboard integration
- **String Expressions** `ibis:reference/expression-strings.qmd` - StringValue: length, lower, upper, strip, lstrip, rstrip, reverse, capitalize, contains, find, like, re_search, re_extract, re_replace, replace, split, concat, join, repeat, left, right, substr, lpad, rpad, translate, startswith, endswith, ascii_str, byte_length
- **Support Matrix** `ibis:backends/support/matrix.qmd` - Operations supported per backend
- **Table Expressions** `ibis:reference/expression-tables.qmd` - Table, GroupedTable, read_csv, read_parquet, read_json, read_delta, memtable, table, join, union, intersect, difference, window functions (row_number, rank, dense_rank, ntile)
- **Temporal Expressions** `ibis:reference/expression-temporal.qmd` - TimestampValue (year, month, day, hour, minute, second, epoch_seconds, truncate, between), DateValue (day_of_week, day_of_year), TimeValue, IntervalValue, DayOfWeek. Constructors: now, today, date, time, timestamp, interval
- **Trino Backend** `ibis:backends/trino.qmd` - Trino distributed SQL backend
- **Type Casting** `ibis:concepts/casting.qmd` - Converting between data types with cast()
- **Unbound Expressions** `ibis:how-to/extending/unbound_expression.qmd` - Creating reusable expression templates
- **User Testimonials** `ibis:concepts/user-testimonials.qmd` - Real-world experiences from Ibis users
- **Versioning** `ibis:concepts/versioning.qmd` - Version policy and compatibility
- **Who Uses Ibis** `ibis:concepts/who.qmd` - Users and organizations using Ibis
- **Why Ibis?** `ibis:why.qmd` - Comprehensive overview: portable API across 20+ backends, Python + SQL integration, scaling up/out, stream-batch unification, ecosystem integrations (pandas, Polars, visualization, ML libraries)
- **pandas Backend** `ibis:backends/pandas.qmd` - pandas backend for compatibility
- **plotnine Visualization** `ibis:how-to/visualization/plotnine.qmd` - ggplot2-style plotting with plotnine

## Reference

- **Athena Backend** `ibis:backends/athena.qmd` - Amazon Athena backend for Ibis: install with `ibis-framework[athena]`, connect via `ibis.athena.connect(s3_staging_dir=...)` — the S3 staging directory is required by pyathena for dumping query results.
- **MySQL Backend** `ibis:backends/mysql.qmd` - MySQL/MariaDB backend for Ibis: supports CSV, Parquet, and PyArrow outputs with memtable fallback; connect via `ibis.mysql.connect()` with host/port/database params or a `mysql://` URL; also works with MariaDB.

---

*Rendered from index.yaml at 2026-08-03T09:54:48Z*
