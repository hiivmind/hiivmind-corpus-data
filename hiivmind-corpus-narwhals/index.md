# Narwhals Documentation Index

> Sources: 1 | Entries: 66 | Generated: 2026-08-31T13:12:46Z
> Generated from `index.yaml` — do not edit directly

---

## Null

- **API Completeness Overview** `narwhals:api-completeness/index.md` - API completeness summary showing which methods are supported across backends (pandas, Polars, PyArrow, cuDF, Modin)
- **API Reference Overview** `narwhals:api-reference/index.md` - API reference overview for Narwhals
- **Backwards Compatibility** `narwhals:backcompat.md` - Perfect backwards compatibility policy for library authors: `narwhals.stable.v1` and `narwhals.stable.v2` are frozen forever; breaking changes go into the main namespace then a new stable version, so libraries can pin independently.
- **Boolean Operations** `narwhals:concepts/boolean.md` - Boolean logic across backends, how &, |, ~ work consistently
- **Column Names** `narwhals:concepts/column_names.md` - Column naming conventions and handling duplicates
- **Complete Example** `narwhals:basics/complete_example.md` - Building a dataframe-agnostic StandardScaler (scikit-learn style). fit method with eager_only=True (needs concrete values), transform stays lazy. Shows pandas, Polars eager, and Polars lazy working with same code
- **Data Types** `narwhals:api-reference/dtypes.md` - Full dtype hierarchy: DType base, NumericType (Int8–Int128, UInt8–UInt128, Float16/32/64, Decimal), TemporalType (Date, Datetime, Duration, Time), Categorical, Enum, String, Boolean, List, Array, Struct, Object, Unknown, and new Int128/UInt128 types.
- **DataFrame API Reference** `narwhals:api-reference/dataframe.md` - DataFrame class: select, with_columns, filter, group_by, join, sort, head, tail, unique, drop, rename, cast, to_native, schema, columns, shape
- **DataFrame Basics** `narwhals:basics/dataframe.md` - Core workflow: nw.from_native(df) then express logic with Polars API then nw.to_native(). The @nw.narwhalify decorator simplifies this. Examples: descriptive stats with select, group-by with agg, horizontal operations with nw.sum_horizontal. Supports multiple inputs with eager_only=True
- **DataFrame Conversion** `narwhals:basics/dataframe_conversion.md` - Converting between native types with to_native(), from_native()
- **DataFrame Methods Completeness** `narwhals:api-completeness/dataframe.md` - Supported DataFrame operations per backend
- **Dependencies API Reference** `narwhals:api-reference/dependencies.md` - Backend detection utilities: is_pandas_dataframe, is_polars_dataframe, get_polars, get_pandas
- **Ecosystem** `narwhals:ecosystem.md` - Non-exhaustive list of 30+ libraries using Narwhals for dataframe interoperability, including altair, bokeh, lightgbm, marimo, pandera, plotly, scikit-learn, scikit-lego, and others. Open PRs accepted to add missing projects.
- **Exceptions API Reference** `narwhals:api-reference/exceptions.md` - Exception classes
- **Expr API Reference** `narwhals:api-reference/expr.md` - Expr class: column expressions, arithmetic, comparisons, aggregations, window functions via over(), any_value for arbitrary group value selection, trigonometric functions (cos, sin)
- **Expr Methods Completeness** `narwhals:api-completeness/expr.md` - Supported expression methods per backend
- **Expr.cat API Reference** `narwhals:api-reference/expr_cat.md` - Categorical namespace: get_categories
- **Expr.cat Methods Completeness** `narwhals:api-completeness/expr_cat.md` - Categorical expression methods per backend
- **Expr.dt API Reference** `narwhals:api-reference/expr_dt.md` - Datetime namespace: year, month, day, hour, minute, second, millisecond, microsecond, nanosecond, ordinal_day, weekday, total_minutes, total_seconds
- **Expr.dt Methods Completeness** `narwhals:api-completeness/expr_dt.md` - Datetime expression methods per backend
- **Expr.list API Reference** `narwhals:api-reference/expr_list.md` - List namespace: len, get, contains, mean, median, min, max, sort, sum, unique
- **Expr.list Methods Completeness** `narwhals:api-completeness/expr_list.md` - List expression methods per backend
- **Expr.name API Reference** `narwhals:api-reference/expr_name.md` - Name manipulation: keep, map, prefix, suffix, to_lowercase, to_uppercase
- **Expr.name Methods Completeness** `narwhals:api-completeness/expr_name.md` - Name manipulation methods per backend
- **Expr.str API Reference** `narwhals:api-reference/expr_str.md` - String namespace: len, to_lowercase, to_uppercase, starts_with, ends_with, contains, slice, head, tail, strip, replace, split, pad_start, pad_end
- **Expr.str Methods Completeness** `narwhals:api-completeness/expr_str.md` - String expression methods per backend
- **Expr.struct API Reference** `narwhals:api-reference/expr_struct.md` - Struct namespace: field
- **Expr.struct Methods Completeness** `narwhals:api-completeness/expr_struct.md` - Struct expression methods per backend
- **Extensions & Plugins** `narwhals:extending.md` - Extending Narwhals with custom functionality
- **Generating SQL** `narwhals:generating_sql.md` - SQL generation from Narwhals expressions. New narwhals.sql module with nw.sql.table() for creating SQLTable objects and to_sql() for converting expressions to SQL strings
- **GroupBy API Reference** `narwhals:api-reference/group_by.md` - GroupBy class: agg, iter
- **How It Works** `narwhals:how_it_works.md` - Deep dive into Narwhals internals. Expression theory: an expression is a function from DataFrame to sequence of Series. nw.col translates to lambda for pandas. Expression nodes compose expressions, inspectable via _nodes. Expression metadata: expansion_kind, has_windows, n_orderable_ops, is_elementwise, preserves_length, is_scalar_like, is_literal. Broadcasting, elementwise pushdown, group-by internals
- **Implementation API Reference** `narwhals:api-reference/implementation.md` - Backend implementation details
- **Improving Group-By** `narwhals:concepts/improve_group_by_operation.md` - Optimizing group-by performance, avoiding apply overhead
- **Installation** `narwhals:installation.md` - Installing Narwhals, quick start guide
- **Introduction** `narwhals:index.md` - Extremely lightweight compatibility layer for dataframe libraries. Full API support: cuDF, Modin, pandas, Polars, PyArrow. Lazy-only support: Daft, Dask, DuckDB, Ibis, PySpark, SQLFrame. Zero dependencies; uses only the Polars API subset.
- **LazyFrame API Reference** `narwhals:api-reference/lazyframe.md` - LazyFrame class: lazy equivalents of DataFrame methods plus collect, explain
- **LazyFrame Methods Completeness** `narwhals:api-completeness/lazyframe.md` - Supported LazyFrame operations per backend
- **LazyGroupBy API Reference** `narwhals:api-reference/lazy_group_by.md` - LazyGroupBy class for lazy operations
- **Narwhals Module** `narwhals:api-reference/narwhals.md` - Top-level Narwhals functions: col, lit, all, concat, from_native, to_native, narwhalify, from_dict, from_arrow, from_numpy, schema, and 50+ additional utility and expression functions for dataframe-agnostic code.
- **Null Handling** `narwhals:concepts/null_handling.md` - NULL/NaN semantics across backends. Narwhals normalizes null behavior for consistent results regardless of backend
- **Order Dependence** `narwhals:concepts/order_dependence.md` - LazyFrames have undefined row order. Order-dependent operations (diff, shift, rolling) require explicit order_by in over(). first/last now accept optional order_by parameter. n_orderable_ops metadata tracks this
- **Overhead** `narwhals:overhead.md` - Negligible overhead, just Python function unwinding. Running pandas via Narwhals often more efficient than direct pandas (guards against API misuse)
- **Resources** `narwhals:resources.md` - Additional learning resources
- **SQL Module API Reference** `narwhals:api-reference/sql.md` - narwhals.sql module: nw.sql.table() to create SQLTable objects, SQLTable.to_sql() to generate SQL from Narwhals expressions
- **Schema API Reference** `narwhals:api-reference/schema.md` - Schema class for column type definitions
- **Security** `narwhals:security.md` - Security considerations
- **Selectors API Reference** `narwhals:api-reference/selectors.md` - Column selectors: by_dtype, numeric, boolean, string, categorical, all. Use type hierarchy for selection (e.g., by_dtype(nw.NumericType) selects all numeric columns)
- **Series API Reference** `narwhals:api-reference/series.md` - Series class: element-wise operations, aggregations, type conversions, any_value for arbitrary value selection, trigonometric functions (cos, sin)
- **Series Methods Completeness** `narwhals:api-completeness/series.md` - Supported Series operations per backend
- **Series Operations** `narwhals:basics/series.md` - Working with Series in Narwhals, series_only=True parameter
- **Series.cat API Reference** `narwhals:api-reference/series_cat.md` - Series categorical methods
- **Series.cat Methods Completeness** `narwhals:api-completeness/series_cat.md` - Series categorical methods per backend
- **Series.dt API Reference** `narwhals:api-reference/series_dt.md` - Series datetime methods
- **Series.dt Methods Completeness** `narwhals:api-completeness/series_dt.md` - Series datetime methods per backend
- **Series.list API Reference** `narwhals:api-reference/series_list.md` - Series list methods: len, get, contains, mean, median, min, max, sort, sum, unique
- **Series.list Methods Completeness** `narwhals:api-completeness/series_list.md` - Series list methods per backend
- **Series.str API Reference** `narwhals:api-reference/series_str.md` - Series string methods
- **Series.str Methods Completeness** `narwhals:api-completeness/series_str.md` - Series string methods per backend
- **Series.struct API Reference** `narwhals:api-reference/series_struct.md` - Series struct methods
- **Series.struct Methods Completeness** `narwhals:api-completeness/series_struct.md` - Series struct methods per backend
- **Testing API Reference** `narwhals:api-reference/testing.md` - Testing utilities: assert_frame_equal, assert_series_equal
- **Typing API Reference** `narwhals:api-reference/typing.md` - Type hints: FrameT, DataFrameT, IntoFrameT, IntoDataFrameT, IntoFrame, IntoDataFrame, IntoExpr, IntoSeries
- **Utils API Reference** `narwhals:api-reference/utils.md` - Utility functions
- **Why Narwhals?** `narwhals:why.md` - Subtle differences between pandas and Polars (e.g., 3 in series checks index vs values). Writing dataframe-agnostic code is hard without a unified API. Narwhals handles backwards compatibility internally
- **pandas Index Handling** `narwhals:concepts/pandas_index.md` - Narwhals ignores pandas index. Use reset_index() before from_native() if you need index as column

---

*Rendered from index.yaml at 2026-08-31T13:12:46Z*
