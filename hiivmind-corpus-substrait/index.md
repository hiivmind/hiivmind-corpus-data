# Substrait Documentation Index

> Sources: 1 | Entries: 62 | Generated: 2026-06-30T18:07:38+10:00
> Generated from `index.yaml` — do not edit directly

---

## Community

- **Active Libraries** `substrait:community/active_libraries.md` - Pending re-scan ⏳ STALE
- **Community Overview** `substrait:community/index.md` - Community resources and participation. AI contribution policy: AI-assisted contributions accepted with disclosure of tools used; contributors must self-review generated content before requesting review
- **Governance** `substrait:governance.md` - Project governance model. Bar for inclusion: at least two of top four OSS data technologies (Arrow, Spark, Iceberg, Trino) must support feature ⏳ STALE
- **Powered By** `substrait:community/powered_by.md` - Projects using Substrait: Arrow (C++ and Rust compute kernels), Calcite, DataFusion, DuckDB, Ibis, Velox, Spark, Trino, Iceberg

## Expressions

- **Aggregate Functions** `substrait:expressions/aggregate_functions.md` - Functions that collapse many records into one value. Examples: SUM, COUNT, AVG. Used in measures of Aggregate relations. May have optional filter
- **Approximate Aggregates** `substrait:functions_aggregate_approx.yaml` - Approximate aggregate functions
- **Arithmetic Functions** `substrait:functions_arithmetic.yaml` - Scalar functions: add, subtract, multiply, divide, negate, modulus, power, sqrt, exp, cos, sin, tan, cosh, sinh, tanh, acos, asin, atan, acosh, asinh, atanh, atan2, sign, abs, factorial, bitwise_not, bitwise_and, bitwise_or, bitwise_xor. Each with typed implementations (i8-i64, fp32, fp64) and overflow/rounding options
- **Boolean Functions** `substrait:functions_boolean.yaml` - or, and, and_not, xor, not using Kleene logic (null = unknown). Aggregate: bool_and, bool_or
- **Comparison Functions** `substrait:functions_comparison.yaml` - not_equal, equal, is_not_distinct_from, is_distinct_from, lt, gt, lte, gte, between, is_null, is_not_null, is_nan, is_finite, is_infinite, nullif, coalesce, least, greatest
- **DateTime Functions** `substrait:functions_datetime.yaml` - extract (YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, ISO_WEEK, etc.), add, subtract, multiply for temporal arithmetic, assume_timezone, local_timestamp, strptime_time, strptime_date, strptime_timestamp, strftime, round_temporal, round_calendar
- **Decimal Aggregates** `substrait:functions_aggregate_decimal_output.yaml` - Aggregates with decimal output types
- **Decimal Arithmetic** `substrait:functions_arithmetic_decimal.yaml` - Decimal-specific: add, subtract, multiply, divide, modulus, abs, power with precision/scale tracking
- **Decimal Rounding** `substrait:functions_rounding_decimal.yaml` - ceil, floor, round for decimal types
- **Dynamic Parameters** `substrait:expressions/dynamic_parameters.md` - Parameterized query plans
- **Embedded Functions** `substrait:expressions/embedded_functions.md` - Function implementations embedded in plan. Common in data science workflows with business logic interspersed
- **Extended Expression** `substrait:expressions/extended_expression.md` - Extended expression capabilities
- **Extension Types** `substrait:extension_types.yaml` - User-defined type examples: point (latitude/longitude as i32), line (start/end as u!point). Demonstrates u! prefix for user-defined types
- **Field References** `substrait:expressions/field_references.md` - Identify portions of a record to operate on. Always numeric (not by name). structField.field: 1 = second field. Root types: RootReference (incoming record), OuterReference (correlated subqueries), Expression (expression result), LambdaParameterReference (lambda params). References only make sense relative to a schema context ⏳ STALE
- **Generic Aggregates** `substrait:functions_aggregate_generic.yaml` - count (values or records, with overflow options), any_value (arbitrary value from group, with ignore_nulls option). Both decomposable for distributed execution
- **Geometry Functions** `substrait:functions_geometry.yaml` - point, make_line, x_coordinate, y_coordinate, num_points, is_empty, is_closed, is_simple, is_ring, geometry_type, envelope, dimension, is_valid, collection_extract, flip_coordinates, remove_repeated_points, buffer, centroid, minimum_bounding_circle
- **Lambda Expressions** `substrait:expressions/lambda_expressions.md` - Inline anonymous functions for higher-order operations. Components: parameters (struct type), body (expression). Type is func<params -> return>. Parameter access via LambdaParameterReference with steps_out for nested scopes. LambdaInvocation for direct calls. Used with functions like transform and filter on collections. Supports closures ⏳ STALE
- **List Functions** `substrait:functions_list.yaml` - Higher-order: transform (map), filter, any_match, all_match. Utility: cardinality, sort (with direction/null placement options). Uses func<T -> R> lambda types
- **Logarithmic Functions** `substrait:functions_logarithmic.yaml` - ln, log10, log2, logb (arbitrary base), log1p. Typed for fp32/fp64
- **Rounding Functions** `substrait:functions_rounding.yaml` - ceil, floor, round with rounding mode options (TIE_TO_EVEN, TIE_AWAY_FROM_ZERO, TRUNCATE, CEILING, FLOOR)
- **Scalar Functions** `substrait:expressions/scalar_functions.md` - Function specification: functionReference (ID into extension list), outputType, arguments (positional). Functions defined in extension YAML files. Optional description field. Examples: is_null, index_in, equal, multiply. Arguments wrapped in value objects ⏳ STALE
- **Set Functions** `substrait:functions_set.yaml` - index_in for membership testing
- **Specialized Record Expressions** `substrait:expressions/specialized_record_expressions.md` - Expressions outside function paradigm: if/then/else, switch/case, cast. Cast is an expression type, not a function ⏳ STALE
- **String Functions** `substrait:functions_string.yaml` - concat, like, substring, regexp_match_substring, regexp_replace, regexp_count_substring, replace, reverse, lower, upper, char_length, bit_length, octet_length, trim, ltrim, rtrim, left, right, repeat, starts_with, ends_with, cap, lpad, rpad, string_agg, center, count_substring. Null handling and case sensitivity options
- **Subqueries** `substrait:expressions/subqueries.md` - Nested query expressions ⏳ STALE
- **Table Functions** `substrait:expressions/table_functions.md` - Convert values to 0..N output records. Examples: explode, pos-explode. Designed, not implemented
- **Type Variations** `substrait:type_variations.yaml` - Physical format variations: dict4 (4-byte dictionary encoded string, INHERITS), bigoffset (Arrow large string, SEPARATE), avro (Avro encoded struct), cstruct (C struct representation), dict2 (2-byte dictionary string)
- **User Defined Functions** `substrait:expressions/user_defined_functions.md` - Reusable named functions beyond core spec. Registered externally (drop file, special command)
- **Window Functions** `substrait:expressions/window_functions.md` - Relate a record to encompassing records. SQL examples: RANK, NTILE, ROW_NUMBER. Frame specification, partitioning, ordering

## Overview

- **About Substrait** `substrait:about.md` - Project vision: well-defined cross-language spec for data compute. Similar to Arrow (memory format) but for compute expressions. Why not SQL: lacks sufficient detail, not machine-processable. Why separate project: avoid coupling to single technology, like Arrow separated from Drill. Related: Apache Calcite (JVM SQL parsing), Apache Arrow (memory format)
- **FAQ** `substrait:faq.md` - Frequently asked questions about Substrait ⏳ STALE
- **Home** `substrait:index.md` - Substrait: format for describing compute operations on structured data. Cross-language specification. Benefits: avoids N-to-N system communication, makes components upgradeable, enables heterogeneous environments. Use cases: SQL parser to execution engine (Calcite to Arrow C++), serialize SQL views (Iceberg), submit to different engines (DataFusion, Postgres), plan visualization

## Specification

- **Breaking Change Policy** `substrait:spec/breaking_change_policy.md` - Pending re-scan ⏳ STALE
- **Extending Substrait** `substrait:spec/extending.md` - How to propose new read/write definition types and other extensions
- **Specification Status** `substrait:spec/specification.md` - Spec status: past initial design, in final stages. Complete components: Simple types, Compound types, Type variations, User-defined types, Field references, Scalar functions, Specialized record expressions, Aggregate functions, Window functions, User-defined functions, Embedded functions, Relation basics, Logical relations, Text serialization, Binary serialization. Designed not implemented: Table functions, User-defined relations, Embedded relations, Physical relations
- **Technology Principles** `substrait:spec/technology_principles.md` - Design principles guiding Substrait
- **Versioning** `substrait:spec/versioning.md` - Versioning policy for the specification

## Tools

- **Producer Tools** `substrait:tools/producer_tools.md` - Tools for generating Substrait plans
- **Substrait Validator** `substrait:tools/substrait_validator.md` - Validation tool: substrait-validator final_plan.json --out-file output.html. Shows schema and column indices at each point in plan. HTML report generation
- **Third Party Tools** `substrait:tools/third_party_tools.md` - Ecosystem tools for Substrait

## Tutorial

- **Examples** `substrait:tutorial/examples.md` - Additional example plans
- **SQL to Substrait Tutorial** `substrait:tutorial/sql_to_substrait.md` - Comprehensive walkthrough building a plan from SQL. Covers types (nullability, decimal parameters, nested types, NamedStruct), expressions (field references, literals, scalar functions), relations (Read, Filter, Join, Aggregate), field indices, emit (column reordering via outputMapping), and plans (extensionUrns, extensions, relations with Root) ⏳ STALE

## Type_system

- **Named Structs** `substrait:types/named_structs.md` - Structs with named fields for schemas. NamedStruct = struct type + column names. Names in depth-first order for nested types ⏳ STALE
- **Type Aliases** `substrait:types/type_aliases.md` - Shorthand names for common type configurations
- **Type Classes** `substrait:types/type_classes.md` - Complete type catalog: Simple numeric (boolean, i8-i128, fp32, fp64, decimal), Simple string/binary (string, binary, fixedchar, varchar, fixedbinary), Simple temporal (date, time, timestamp, timestamp_tz, interval_year, interval_day), Simple other (uuid), Compound (STRUCT, LIST, MAP, FUNC), User-defined (u! prefix) ⏳ STALE
- **Type Parsing** `substrait:types/type_parsing.md` - Syntax for describing types in text form. Function types: func<any1 -> any2> (single param), func<(any1, any2) -> any3> (multiple params). User-defined types use u!typename syntax ⏳ STALE
- **Type System Overview** `substrait:types/type_system.md` - Types have 4 components: Class (i8, string, STRUCT, extensions), Nullability (NULLABLE with ? suffix or REQUIRED), Variation (system-preferred or extension for in-memory format), Parameters (compound only, e.g. DECIMAL<10,2>). Strict type system: no coercion, all changes via explicit cast expressions
- **Type Variations** `substrait:types/type_variations.md` - Physical variations of base types, distinguished by in-memory format

## Unknown

- **Binary Serialization** `substrait:serialization/binary_serialization.md` - High performance, compact protobuf representation. Source of truth for spec. Well-commented proto files
- **Common Fields** `substrait:relations/common_fields.md` - Fields common to all relations ⏳ STALE
- **Embedded Relations** `substrait:relations/embedded_relations.md` - Relations with embedded machine code. Designed, not implemented
- **Extensions Overview** `substrait:extensions/index.md` - Extension mechanism for types and functions. Simple extensions in YAML files. URN identifiers reference extension files. Extension anchors link plan references to definitions. Optional metadata field. Deprecation support with since version, reason, metadata. Core extensions in extensions/ directory ⏳ STALE
- **Logical Relations** `substrait:relations/logical_relations.md` - Core relational operations: Read (Virtual Table, Named Table, Local Files, Iceberg Table), Filter (boolean condition), Sort (sortFields with direction), Project (adds columns via expressions), Cross Product, Join (INNER, OUTER, LEFT, RIGHT, SEMI, ANTI, SINGLE, MARK), Set (MINUS, INTERSECTION, UNION), Fetch (offset/limit), Aggregate (groupings, measures), Reference (DAG), Write (INSERT/DELETE/UPDATE/CTAS), Update, DDL (CREATE/DROP/ALTER) ⏳ STALE
- **Physical Relations** `substrait:relations/physical_relations.md` - Physical variants: hash join vs merge join vs nested loop. Designed, not implemented ⏳ STALE
- **Relation Basics** `substrait:relations/basics.md` - Relational algebra concepts. Relations = plan nodes (filter, project, join, etc.). Each relation has signature: inputs, outputs, property maintenance, direct output order. Emit property for column reordering/subsetting (default: direct). Relations contain or refer to child relations
- **Serialization Basics** `substrait:serialization/basics.md` - Overview of serialization formats
- **Text Serialization** `substrait:serialization/text_serialization.md` - Human-readable representation. Currently uses Protobuf JSON output (not official Substrait text format yet). Useful for debugging, unit tests
- **User Defined Relations** `substrait:relations/user_defined_relations.md` - Custom relational operations for specific platforms. Designed, not implemented

---

*Rendered from index.yaml at 2026-06-30T18:07:38+10:00*
