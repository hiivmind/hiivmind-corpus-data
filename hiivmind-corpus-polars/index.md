# Polars Documentation Index

> Sources: 1 | Entries: 112 | Generated: 2026-08-31T13:12:43Z
> Generated from `index.yaml` — do not edit directly

---

## Api

- **Python/Rust API** `polars:api/reference.md` - Links to full API documentation for Python and Rust

## Config

- **Anonymous Results** `polars:polars-on-premises/bare-metal/configuration/anonymous-results.md` - Configure anonymous results sink for remote queries without explicit output: shared filesystem (NFS/CephFS) and S3-compatible storage backends
- **Anonymous Users** `polars:polars-on-premises/bare-metal/configuration/anonymous-users.md` - Pending re-scan
- **Configuration Reference** `polars:polars-on-premises/bare-metal/configuration/reference.md` - Complete TOML config reference: cluster_id, instance_id, license, memory_limit, scheduler, worker, observatory, monitoring, static_leader. Env var overrides via PC_CUBLET__section__key
- **Example Configurations** `polars:polars-on-premises/bare-metal/configuration/example-configurations.md` - Complete TOML examples for single-node and multi-node clusters with all network ports customized
- **License** `polars:polars-on-premises/bare-metal/configuration/license.md` - License key requirements (JSON format), file path config, EULA acceptance via POLARS_EULA_ACCEPTED
- **Monitoring** `polars:polars-on-premises/bare-metal/configuration/monitoring.md` - Observatory and monitoring: SQLite profiling storage, in-memory host metrics buffer, cgroup-based metrics collection
- **Network Addresses** `polars:polars-on-premises/bare-metal/configuration/network-addresses.md` - All configurable network services: scheduler client/worker, observatory/REST API, worker task/shuffle. Default bind addresses and public address config for NAT/multi-node
- **OpenLineage** `polars:polars-on-premises/bare-metal/configuration/openlineage.md` - Pending re-scan
- **Persistence** `polars:polars-on-premises/bare-metal/configuration/persistence.md` - Pending re-scan
- **Resource Limits** `polars:polars-on-premises/bare-metal/configuration/resource-limits.md` - CPU and memory management: two-process architecture (main + executor), OOM behavior, delegated cgroup setup via memory_limit, manual systemd cgroup config
- **Shuffle Data** `polars:polars-on-premises/bare-metal/configuration/shuffle-data.md` - Three shuffle storage options: worker-local SSD, shared filesystem (NFS/CephFS), S3-compatible. Performance trade-offs per option
- **Static Leader** `polars:polars-on-premises/bare-metal/configuration/static-leader.md` - static_leader section identifying cluster leader node and public addresses, enabling shared config files with per-node instance_id overrides

## Guide

- **AKS Deployment** `polars:polars-on-premises/kubernetes/cloud-providers/azure-kubernetes-service.md` - Pending re-scan
- **Airflow Integration** `polars:polars-cloud/integrations/airflow.md` - Comprehensive Airflow patterns: auth decorators, await_result(), cluster lifecycle management (context managers, named manifests, manual shutdown), parallel single-node execution, multi-stage pipelines
- **Billing Overview** `polars:polars-on-premises/billing/index.md` - Pending re-scan
- **CI** `polars:development/contributing/ci.md` - Continuous integration
- **Code Style** `polars:development/contributing/code-style.md` - Code conventions
- **Compute Context** `polars:polars-cloud/context/compute-context.md` - Create and configure compute contexts for distributed execution. Save as named manifests via register(), set global defaults with pc.set_compute_context(). Ephemeral contexts create new clusters; reuse clusters via manifests
- **Contributing** `polars:development/contributing/index.md` - How to contribute to Polars. Includes git bisect workflow for bug hunting. AI contribution policy: must disclose AI-generated code, attest personal review, no AI on good first issue tickets
- **Distributed Engine** `polars:polars-cloud/run/distributed-engine.md` - Running queries on Polars Cloud distributed engine
- **Distributed Engine** `polars:polars-on-premises/run/distributed-engine.md` - Pending re-scan
- **Distributed Glossary** `polars:polars-cloud/run/glossary.md` - Key distributed execution terms: DSL, query, logical/physical plans, scheduler, worker, stage graph, stage, partition, shuffle
- **EKS Deployment** `polars:polars-on-premises/kubernetes/cloud-providers/amazon-elastic-kubernetes-service.md` - Pending re-scan
- **Environment Variables** `polars:polars-on-premises/bare-metal/environment-variables.md` - Environment variable reference for on-premises deployment
- **GKE Deployment** `polars:polars-on-premises/kubernetes/cloud-providers/google-kubernetes-engine.md` - Pending re-scan
- **IDE Setup** `polars:development/contributing/ide.md` - Development environment setup
- **Kubernetes Deployment Overview** `polars:polars-on-premises/kubernetes/index.md` - Full Kubernetes deployment reference for Polars On-Prem: Helm chart parameters, deployed resources (scheduler/workers/storage pods), production config for anonymous results (S3/SeaweedFS), shuffle storage options, resource limits, OOM behavior on cgroup v2, and air-gapped Enterprise mode.
- **On-Premises Getting Started** `polars:polars-on-premises/bare-metal/getting-started.md` - Initial bare-metal deployment setup
- **On-Premises Overview** `polars:polars-on-premises/index.md` - Deploying Polars as a self-hosted distributed engine
- **OpenLineage Integration** `polars:polars-on-premises/integrations/openlineage.md` - Pending re-scan
- **Python Environment** `polars:polars-on-premises/bare-metal/python-environment.md` - Python environment configuration for on-premises deployment
- **Query Profiler** `polars:polars-cloud/run/query-profile.md` - Visual query profiling with bottleneck indicators (CPU time, I/O time, memory-intensive, single-node, in-memory fallback). Distributed query walkthrough with stage graph analysis and cross-region I/O diagnosis
- **Remote Query Execution** `polars:polars-on-premises/run/remote-query.md` - Pending re-scan
- **Slurm Quickstart** `polars:polars-on-premises/bare-metal/misc/slurm.md` - Guide to running Polars On-Prem on Slurm clusters: static leader election, scheduler/worker TOML config generation, sbatch job scripts using polars-cloud ClusterContext, and parallel query submission via `srun`.
- **Testing** `polars:development/contributing/test.md` - Running tests
- **Versioning** `polars:development/versioning.md` - Version policy

## Journal

- **On-Premises Releases** `polars:polars-on-premises/releases.md` - Release history for Polars On-Prem; latest 0.6.3 (1 Jul 2026) bundles polars 1.42.1 and polars-cloud 0.9.0 with distributed Expression lowering, improved ClusterContext API, distributed Iceberg sink, manual cluster scaling, and new disk I/O metrics.

## Reference

- **Aggregation** `polars:user-guide/expressions/aggregation.md` - group_by().agg() context. Multiple aggregations, conditional aggregations, filtering within groups, nested grouping, sorting within groups. Avoid Python lambdas to preserve parallelization
- **Arrow Producer/Consumer** `polars:user-guide/misc/arrow.md` - Zero-copy data exchange: PyArrow to_arrow()/pl.from_arrow() for DataFrame/Table conversion, zero-copy export with compat_level, PyCapsule Interface (v1.3+) standard protocol, C Data Interface for direct struct exchange without PyArrow
- **Basic Operations** `polars:user-guide/expressions/basic-operations.md` - Arithmetic (+, -, *, /), comparisons (>, <, ==), Boolean operations (&, |, ~), counting unique values (n_unique, approx_n_unique, value_counts), conditionals with when().then().otherwise()
- **BigQuery** `polars:user-guide/io/bigquery.md` - Google BigQuery integration
- **CSV** `polars:user-guide/io/csv.md` - read_csv(), scan_csv(), write_csv()
- **Casting** `polars:user-guide/expressions/casting.md` - Type conversion with cast(), strict vs lenient casting
- **Categorical Data and Enums** `polars:user-guide/expressions/categorical-data-and-enums.md` - Efficient string encoding. Categorical (runtime inference) vs Enum (predetermined categories). Cat namespace (cat). v1.32.0+ categoricals always use lexical ordering
- **Changelog** `polars:releases/changelog.md` - Version history
- **Cloud Storage** `polars:user-guide/io/cloud-storage.md` - S3, GCS, Azure Blob. Cloud retry configuration via storage_options, global credential providers, writing to file objects for unsupported formats
- **Comparison** `polars:user-guide/misc/comparison.md` - Polars vs other tools
- **Concatenation** `polars:user-guide/transformations/concatenation.md` - concat() modes: vertical (stack rows), horizontal (add columns), diagonal (combine both). Rechunking considerations
- **Data Types and Structures** `polars:user-guide/concepts/data-types-and-structures.md` - Series (1D homogeneous), DataFrame (2D heterogeneous, uniquely named series), Schema (column-to-type mapping). Inspection methods: head, tail, glimpse, sample, describe. Schema override via schema dict or schema_overrides parameter. Arrow Columnar Format internally. Full type table including numeric (Int8-Int128, UInt8-UInt128, Float16/32/64, Decimal), temporal (Date, Time, Datetime, Duration), nested (List, Array, Struct), string/binary, categorical/enum, boolean, null, object. IEEE 754 floating point with NaN equality semantics
- **DataType Expressions** `polars:user-guide/lazy/datatype_exprs.md` - Runtime type inspection and manipulation with pl.dtype_of(). Express relations between expression datatypes, inspect type info at runtime, cast columns to match another column's type. Useful for utility functions, heterogeneous data sources
- **Database** `polars:user-guide/io/database.md` - SQL database connections
- **Ecosystem** `polars:user-guide/ecosystem.md` - Related libraries and integrations
- **Excel** `polars:user-guide/io/excel.md` - Reading Excel files
- **Execution** `polars:user-guide/lazy/execution.md` - Collecting results, streaming execution
- **Expression Expansion** `polars:user-guide/expressions/expression-expansion.md` - Apply same transformation to multiple columns: pl.col('a', 'b'), pl.col(pl.Float64), pl.all(), pl.exclude()
- **Expression Plugins** `polars:user-guide/plugins/expr_plugins.md` - Custom expression functions in Rust for extending Polars
- **Expressions Overview** `polars:user-guide/expressions/index.md` - Expression categories: essentials (basic ops, expansion, casting), type-specific namespaces (str, list, arr, cat, struct, dt), operation types (aggregation, window, folds), user-defined functions
- **Expressions and Contexts** `polars:user-guide/concepts/expressions-and-contexts.md` - Core DSL concepts. Expressions are lazy transformations. Four contexts: select (column operations), with_columns (add columns), filter (row filtering), group_by (aggregations). Expression expansion for multi-column operations
- **Filtering Time Series** `polars:user-guide/transformations/time-series/filter.md` - Date range filtering
- **Folds** `polars:user-guide/expressions/folds.md` - Horizontal operations with fold(). Custom row-wise computations across columns, similar to functools.reduce. Use concat_str() for string concatenation
- **GPU Support** `polars:user-guide/gpu-support.md` - NVIDIA GPU acceleration for in-memory workloads
- **GPU in Lazy API** `polars:user-guide/lazy/gpu.md` - GPU-accelerated query execution in lazy mode
- **Hive Partitioning** `polars:user-guide/io/hive.md` - Partitioned datasets
- **Hugging Face** `polars:user-guide/io/hugging-face.md` - Loading datasets from Hugging Face Hub
- **IO Overview** `polars:user-guide/io/index.md` - Supported formats and common patterns for reading and writing data
- **IO Plugins** `polars:user-guide/plugins/io_plugins.md` - Custom data source/sink implementations
- **JSON** `polars:user-guide/io/json.md` - JSON and NDJSON support. Lazy scanning with scan_ndjson() for LazyFrame-based NDJSON reading
- **Joins** `polars:user-guide/transformations/joins.md` - Comprehensive join operations: equi joins (inner, left, right, full, semi, anti), non-equi joins (join_where with arbitrary predicates), asof joins (join_asof with nearest key, tolerance, strategy), cross join. Key expressions for dynamic matching, coalesce parameter
- **Lazy API Overview** `polars:user-guide/concepts/lazy-api.md` - LazyFrame vs DataFrame, query optimization benefits
- **Lists and Arrays** `polars:user-guide/expressions/lists-and-arrays.md` - List (variable length) vs Array (fixed shape). List namespace (list): slicing (head, tail), explode(), element-wise ops with eval() and element, row-wise aggregation with concat_list(). Array namespace (arr): fixed-shape operations
- **Migration from Spark** `polars:user-guide/migration/spark.md` - Translating Spark patterns to Polars
- **Migration from pandas** `polars:user-guide/migration/pandas.md` - Key differences, API mapping, performance tips for migrating from pandas to Polars
- **Missing Data** `polars:user-guide/expressions/missing-data.md` - Handling null values: is_null(), fill_null(), drop_nulls(), forward/backward fill. null is distinct from NaN (floating point only)
- **Multiple Files** `polars:user-guide/io/multiple.md` - Glob patterns, lazy scanning multiple files
- **Multiplexing** `polars:user-guide/lazy/multiplexing.md` - Efficient query reuse in lazy mode
- **Multiprocessing** `polars:user-guide/misc/multiprocessing.md` - Parallel processing patterns
- **NumPy Functions** `polars:user-guide/expressions/numpy-functions.md` - Using NumPy ufuncs with Polars data
- **Parquet** `polars:user-guide/io/parquet.md` - Columnar format, predicate pushdown
- **Parsing Dates and Times** `polars:user-guide/transformations/time-series/parsing.md` - String to datetime conversion
- **Pivot** `polars:user-guide/transformations/pivot.md` - Reshape data: group by columns become y-axis, pivot column becomes x-axis. Aggregations: first, last, sum, min, max, mean, median, len. Lazy workarounds: collect first or specify on_columns for static schema declaration
- **Plugins Overview** `polars:user-guide/plugins/index.md` - Extending Polars functionality with plugins
- **Polars for LLMs** `polars:user-guide/misc/polars_llms.md` - Using Polars with language models. Official MCP server at https://mcp.pola.rs/mcp for LLM access to Polars/Cloud docs via npx mcp-remote
- **Query Optimizations** `polars:user-guide/lazy/optimizations.md` - Predicate pushdown, projection pushdown, slice pushdown
- **Query Plans** `polars:user-guide/lazy/query-plan.md` - Understanding and visualizing query plans with explain()
- **Resampling** `polars:user-guide/transformations/time-series/resampling.md` - Downsampling/upsampling temporal data
- **Rolling Operations** `polars:user-guide/transformations/time-series/rolling.md` - Rolling windows for time series
- **SQL CREATE** `polars:user-guide/sql/create.md` - Creating tables in SQL context
- **SQL CTEs** `polars:user-guide/sql/cte.md` - Common Table Expressions in SQL context
- **SQL Introduction** `polars:user-guide/sql/intro.md` - SQL context for Polars DataFrames
- **SQL SELECT** `polars:user-guide/sql/select.md` - Query syntax for SQL interface
- **SQL SHOW** `polars:user-guide/sql/show.md` - Metadata queries in SQL context
- **Schemas in Lazy** `polars:user-guide/lazy/schemas.md` - Schema inference and validation in lazy mode
- **Sources and Sinks** `polars:user-guide/lazy/sources_sinks.md` - Lazy reading/writing from various formats. Multiplexing sinks for writing to multiple outputs simultaneously. PartitionBy for splitting output across files with max_rows_per_file
- **Streaming** `polars:user-guide/concepts/streaming.md` - Out-of-core processing for datasets larger than RAM
- **Strings** `polars:user-guide/expressions/strings.md` - String namespace (str): splitting, slicing, regex matching, replacement, case conversion. Access via col('name').str.to_uppercase()
- **Structs** `polars:user-guide/expressions/structs.md` - Composite type for multiple fields. Struct namespace (struct): unnest() to expand, field() to extract, rename_fields(). Created by value_counts(), dict inference. Use for multi-column deduplication and ranking
- **Styling** `polars:user-guide/misc/styling.md` - DataFrame display formatting
- **Timezones** `polars:user-guide/transformations/time-series/timezones.md` - Timezone handling and conversion
- **Unpivot** `polars:user-guide/transformations/unpivot.md` - Reverse of pivot, wide to long format
- **Upgrade to 0.19** `polars:releases/upgrade/0.19.md` - Changes in v0.19
- **Upgrade to 0.20** `polars:releases/upgrade/0.20.md` - Changes in v0.20
- **Upgrade to 1.0** `polars:releases/upgrade/1.md` - Breaking changes in v1.0
- **User-Defined Python Functions** `polars:user-guide/expressions/user-defined-python-functions.md` - map_elements(), map_batches() for custom Python logic. Performance implications with GIL. Recommends Polars plugins (expression/IO) as higher-performance alternative
- **Using the Lazy API** `polars:user-guide/lazy/using.md` - Converting between eager/lazy, when to use each
- **Visualization** `polars:user-guide/misc/visualization.md` - Plotting with hvPlot, Altair, Plotly
- **Window Functions** `polars:user-guide/expressions/window-functions.md` - over() for group operations in select context. Ranking within groups, mapping strategies: group_to_rows (default), explode (faster), join. Windowed aggregations broadcast scalars

## Tutorial

- **Getting Started** `polars:user-guide/getting-started.md` - First steps with Polars, basic DataFrame operations
- **Installation** `polars:user-guide/installation.md` - Installing Polars and optional feature flags
- **Introduction** `polars:index.md` - Overview of Polars: blazingly fast DataFrame library written in Rust, available for Python/R/NodeJS. Key features: parallel execution, lazy API, Arrow support, GPU acceleration
- **On-Premises Getting Started** `polars:polars-on-premises/getting-started.md` - Kubernetes quickstart for Polars On-Prem: create workspace and service account via CLI or portal, deploy 2-worker cluster with Helm chart, port-forward scheduler/observatory/storage, then run a remote LazyFrame query.

## Unknown

- **checkpointing** `polars:polars-on-premises/bare-metal/configuration/checkpointing.md` - Pending re-scan

---

*Rendered from index.yaml at 2026-08-31T13:12:43Z*
