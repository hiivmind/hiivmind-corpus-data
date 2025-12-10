# Narwhals Documentation Index

> Source: narwhals (git) | 50 docs | Dataframe-agnostic compatibility layer
> Last updated: 2025-12-10

---

## Getting Started

- **Introduction** `narwhals:index.md` - Extremely lightweight compatibility layer between dataframe libraries. Full API support: cuDF, Modin, pandas, Polars, PyArrow. Lazy-only support: Daft, Dask, DuckDB, Ibis, PySpark, SQLFrame. Zero dependencies, uses subset of Polars API, 100% branch coverage, negligible overhead
- **Why Narwhals?** `narwhals:why.md` - Subtle differences between pandas and Polars (e.g., `3 in series` checks index vs values). Writing dataframe-agnostic code is hard without a unified API. Narwhals handles backwards compatibility internally
- **Installation** `narwhals:installation.md` - Installing Narwhals, quick start guide

---

## Intro Tutorial

### DataFrame Operations
- **DataFrame Basics** `narwhals:basics/dataframe.md` - Core workflow: `nw.from_native(df)` → express logic with Polars API → `nw.to_native()`. The `@nw.narwhalify` decorator simplifies this. Examples: descriptive stats with `select`, group-by with `agg`, horizontal operations with `nw.sum_horizontal`. Supports multiple inputs with `eager_only=True`
- **Series Operations** `narwhals:basics/series.md` - Working with Series in Narwhals, `series_only=True` parameter
- **Complete Example** `narwhals:basics/complete_example.md` - Building a dataframe-agnostic StandardScaler (scikit-learn style). `fit` method with `eager_only=True` (needs concrete values), `transform` stays lazy. Shows pandas, Polars eager, and Polars lazy working with same code
- **DataFrame Conversion** `narwhals:basics/dataframe_conversion.md` - Converting between native types with `to_native()`, `from_native()`

---

## Core Concepts

### Expression Model
- **How It Works** `narwhals:how_it_works.md` - Deep dive into Narwhals internals:
  - **Expression theory**: "An expression is a function from DataFrame to sequence of Series"
  - `nw.col('a')` translates to `lambda df: [df.loc[:, 'a']]` for pandas
  - **Expression nodes**: operations that compose expressions, inspectable via `._nodes`
  - **Expression metadata**: `expansion_kind`, `has_windows`, `n_orderable_ops`, `is_elementwise`, `preserves_length`, `is_scalar_like`, `is_literal`
  - **Broadcasting**: scalars broadcast to column length, backends handle differently
  - **Elementwise pushdown**: `over` nodes pushed past elementwise ops for SQL compatibility
  - **Group-by**: simple aggregations use native groupby, complex ones use `apply` with warning

### Behavioral Concepts
- **Order Dependence** `narwhals:concepts/order_dependence.md` - LazyFrames have undefined row order. Order-dependent operations (diff, shift, rolling) require explicit `order_by` in `over()`. `n_orderable_ops` metadata tracks this
- **pandas Index Handling** `narwhals:concepts/pandas_index.md` - Narwhals ignores pandas index. Use `reset_index()` before `from_native()` if you need index as column
- **Improving Group-By** `narwhals:concepts/improve_group_by_operation.md` - Optimizing group-by performance, avoiding `apply` overhead
- **Column Names** `narwhals:concepts/column_names.md` - Column naming conventions and handling duplicates
- **Boolean Operations** `narwhals:concepts/boolean.md` - Boolean logic across backends
- **Null Handling** `narwhals:concepts/null_handling.md` - NULL/NaN semantics across backends

---

## Stability & Compatibility

- **Backwards Compatibility** `narwhals:backcompat.md` - **Perfect backwards compatibility policy** (Rust editions-inspired):
  - `narwhals.stable.v1` and `narwhals.stable.v2`: promises never to change/remove public functions
  - Breaking changes go to main namespace (eventually `stable.v3`)
  - Stable APIs maintained indefinitely
  - **Recommendation**: `import narwhals as nw` for prototyping, `import narwhals.stable.v2 as nw` for production
  - Exceptions: unambiguous bugs, radical backend changes, type hint precision, "unstable" features
  - Lists all `main` vs `stable.v1` differences (deprecations, behavioral changes)
- **Overhead** `narwhals:overhead.md` - Negligible overhead, just Python function unwinding. Running pandas via Narwhals often more efficient than direct pandas (guards against API misuse)

---

## Advanced Topics

- **Extensions & Plugins** `narwhals:extending.md` - Extending Narwhals with custom functionality
- **Generating SQL** `narwhals:generating_sql.md` - SQL generation from Narwhals expressions
- **Ecosystem** `narwhals:ecosystem.md` - Libraries and tools using Narwhals
- **Security** `narwhals:security.md` - Security considerations
- **Resources** `narwhals:resources.md` - Additional learning resources

---

## API Completeness

Shows which methods are supported across backends (pandas, Polars, PyArrow, cuDF, Modin, etc.):

- **Overview** `narwhals:api-completeness/index.md` - API completeness summary
- **DataFrame Methods** `narwhals:api-completeness/dataframe.md` - Supported DataFrame operations per backend
- **LazyFrame Methods** `narwhals:api-completeness/lazyframe.md` - Supported LazyFrame operations per backend
- **Expr Methods** `narwhals:api-completeness/expr.md` - Supported expression methods
- **Expr.cat Methods** `narwhals:api-completeness/expr_cat.md` - Categorical expression methods
- **Expr.dt Methods** `narwhals:api-completeness/expr_dt.md` - Datetime expression methods
- **Expr.list Methods** `narwhals:api-completeness/expr_list.md` - List expression methods
- **Expr.name Methods** `narwhals:api-completeness/expr_name.md` - Name manipulation methods
- **Expr.str Methods** `narwhals:api-completeness/expr_str.md` - String expression methods
- **Expr.struct Methods** `narwhals:api-completeness/expr_struct.md` - Struct expression methods
- **Series Methods** `narwhals:api-completeness/series.md` - Supported Series operations
- **Series.cat Methods** `narwhals:api-completeness/series_cat.md` - Series categorical methods
- **Series.dt Methods** `narwhals:api-completeness/series_dt.md` - Series datetime methods
- **Series.list Methods** `narwhals:api-completeness/series_list.md` - Series list methods
- **Series.str Methods** `narwhals:api-completeness/series_str.md` - Series string methods
- **Series.struct Methods** `narwhals:api-completeness/series_struct.md` - Series struct methods

---

## API Reference

### Core API
- **Overview** `narwhals:api-reference/index.md` - API reference overview
- **Narwhals Module** `narwhals:api-reference/narwhals.md` - Top-level functions: `from_native`, `to_native`, `narwhalify`, `col`, `lit`, `all`, `sum_horizontal`, `mean_horizontal`, `concat`, `when/then/otherwise`, etc.
- **DataFrame** `narwhals:api-reference/dataframe.md` - `DataFrame` class: `select`, `with_columns`, `filter`, `group_by`, `join`, `sort`, `head`, `tail`, `unique`, `drop`, `rename`, `cast`, `to_native`, `schema`, `columns`, `shape`
- **LazyFrame** `narwhals:api-reference/lazyframe.md` - `LazyFrame` class: lazy equivalents of DataFrame methods plus `collect`, `explain`
- **Series** `narwhals:api-reference/series.md` - `Series` class: element-wise operations, aggregations, type conversions

### Expression API
- **Expr** `narwhals:api-reference/expr.md` - `Expr` class: column expressions, arithmetic, comparisons, aggregations, window functions via `over()`
- **Expr.cat** `narwhals:api-reference/expr_cat.md` - Categorical namespace: `get_categories`
- **Expr.dt** `narwhals:api-reference/expr_dt.md` - Datetime namespace: `year`, `month`, `day`, `hour`, `minute`, `second`, `millisecond`, `microsecond`, `nanosecond`, `ordinal_day`, `weekday`, `total_minutes`, `total_seconds`, etc.
- **Expr.list** `narwhals:api-reference/expr_list.md` - List namespace: `len`, `get`, `contains`, `first`, `last`, `mean`, `min`, `max`, `sum`, `sort`, `unique`
- **Expr.name** `narwhals:api-reference/expr_name.md` - Name manipulation: `keep`, `map`, `prefix`, `suffix`, `to_lowercase`, `to_uppercase`
- **Expr.str** `narwhals:api-reference/expr_str.md` - String namespace: `len`, `to_lowercase`, `to_uppercase`, `starts_with`, `ends_with`, `contains`, `slice`, `head`, `tail`, `strip`, `replace`, `split`
- **Expr.struct** `narwhals:api-reference/expr_struct.md` - Struct namespace: `field`

### Series Namespaces
- **Series.cat** `narwhals:api-reference/series_cat.md` - Series categorical methods
- **Series.dt** `narwhals:api-reference/series_dt.md` - Series datetime methods
- **Series.list** `narwhals:api-reference/series_list.md` - Series list methods
- **Series.str** `narwhals:api-reference/series_str.md` - Series string methods
- **Series.struct** `narwhals:api-reference/series_struct.md` - Series struct methods

### GroupBy
- **GroupBy** `narwhals:api-reference/group_by.md` - `GroupBy` class: `agg`, `iter`
- **LazyGroupBy** `narwhals:api-reference/lazy_group_by.md` - `LazyGroupBy` class for lazy operations

### Types & Utilities
- **Schema** `narwhals:api-reference/schema.md` - `Schema` class for column type definitions
- **Data Types** `narwhals:api-reference/dtypes.md` - All dtypes: `Int8`-`Int128`, `UInt8`-`UInt64`, `Float32`, `Float64`, `Boolean`, `String`, `Categorical`, `Enum`, `Date`, `Datetime`, `Duration`, `Object`, `Array`, `List`, `Struct`, `Unknown`
- **Selectors** `narwhals:api-reference/selectors.md` - Column selectors: `by_dtype`, `numeric`, `boolean`, `string`, `categorical`, `all`
- **Typing** `narwhals:api-reference/typing.md` - Type hints: `FrameT`, `DataFrameT`, `IntoFrameT`, `IntoDataFrameT`, `IntoFrame`, `IntoDataFrame`, `IntoExpr`, `IntoSeries`
- **Dependencies** `narwhals:api-reference/dependencies.md` - Backend detection utilities: `is_pandas_dataframe`, `is_polars_dataframe`, `get_polars`, `get_pandas`, etc.
- **Implementation** `narwhals:api-reference/implementation.md` - Backend implementation details
- **Exceptions** `narwhals:api-reference/exceptions.md` - Exception classes
- **Testing** `narwhals:api-reference/testing.md` - Testing utilities for Narwhals code
- **Utils** `narwhals:api-reference/utils.md` - Utility functions
