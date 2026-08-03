# Substrait Documentation Index

> Sources: 1 | Entries: 62 | Generated: 2026-08-03T09:54:56Z
> Generated from `index.yaml` — do not edit directly

---

## Guide

- **FAQ** `substrait:faq.md` - FAQ covering post-join filter handling, project relation column output, and field naming representation in Substrait plans.
- **Governance** `substrait:governance.md` - Substrait governance structure: users, contributors, committers, and PMC; describes voting rules and decision-making processes for the project.

## Null

- **About Substrait** `substrait:about.md` - Project vision: well-defined cross-language spec for data compute. Similar to Arrow (memory format) but for compute expressions. Why not SQL: lacks sufficient detail, not machine-processable. Why separate project: avoid coupling to single technology, like Arrow separated from Drill. Related: Apache Calcite (JVM SQL parsing), Apache Arrow (memory format)
- **Aggregate Functions** `substrait:expressions/aggregate_functions.md` - Functions that collapse many records into one value. Examples: SUM, COUNT, AVG. Used in measures of Aggregate relations. May have optional filter
- **Approximate Aggregates** `substrait:functions_aggregate_approx.yaml` - Approximate aggregate functions
- **Arithmetic Functions** `substrait:functions_arithmetic.yaml` - Scalar functions: add, subtract, multiply, divide, negate, modulus, power, sqrt, exp, cos, sin, tan, cosh, sinh, tanh, acos, asin, atan, acosh, asinh, atanh, atan2, sign, abs, factorial, bitwise_not, bitwise_and, bitwise_or, bitwise_xor. Each with typed implementations (i8-i64, fp32, fp64) and overflow/rounding options
- **Binary Serialization** `substrait:serialization/binary_serialization.md` - High performance, compact protobuf representation. Source of truth for spec. Well-commented proto files
- **Boolean Functions** `substrait:functions_boolean.yaml` - or, and, and_not, xor, not using Kleene logic (null = unknown). Aggregate: bool_and, bool_or
- **Community Overview** `substrait:community/index.md` - Community resources and participation. AI contribution policy: AI-assisted contributions accepted with disclosure of tools used; contributors must self-review generated content before requesting review
- **Comparison Functions** `substrait:functions_comparison.yaml` - not_equal, equal, is_not_distinct_from, is_distinct_from, lt, gt, lte, gte, between, is_null, is_not_null, is_nan, is_finite, is_infinite, nullif, coalesce, least, greatest
- **DateTime Functions** `substrait:functions_datetime.yaml` - extract (YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, ISO_WEEK, etc.), add, subtract, multiply for temporal arithmetic, assume_timezone, local_timestamp, strptime_time, strptime_date, strptime_timestamp, strftime, round_temporal, round_calendar
- **Decimal Aggregates** `substrait:functions_aggregate_decimal_output.yaml` - Aggregates with decimal output types
- **Decimal Arithmetic** `substrait:functions_arithmetic_decimal.yaml` - Decimal-specific: add, subtract, multiply, divide, modulus, abs, power with precision/scale tracking
- **Decimal Rounding** `substrait:functions_rounding_decimal.yaml` - ceil, floor, round for decimal types
- **Dynamic Parameters** `substrait:expressions/dynamic_parameters.md` - Parameterized query plans
- **Embedded Functions** `substrait:expressions/embedded_functions.md` - Function implementations embedded in plan. Common in data science workflows with business logic interspersed
- **Embedded Relations** `substrait:relations/embedded_relations.md` - Relations with embedded machine code. Designed, not implemented
- **Examples** `substrait:tutorial/examples.md` - Additional example plans
- **Extended Expression** `substrait:expressions/extended_expression.md` - Extended expression capabilities
- **Extending Substrait** `substrait:spec/extending.md` - How to propose new read/write definition types and other extensions
- **Extension Types** `substrait:extension_types.yaml` - User-defined type examples: point (latitude/longitude as i32), line (start/end as u!point). Demonstrates u! prefix for user-defined types
- **Generic Aggregates** `substrait:functions_aggregate_generic.yaml` - count (values or records, with overflow options), any_value (arbitrary value from group, with ignore_nulls option). Both decomposable for distributed execution
- **Geometry Functions** `substrait:functions_geometry.yaml` - point, make_line, x_coordinate, y_coordinate, num_points, is_empty, is_closed, is_simple, is_ring, geometry_type, envelope, dimension, is_valid, collection_extract, flip_coordinates, remove_repeated_points, buffer, centroid, minimum_bounding_circle
- **Home** `substrait:index.md` - Substrait: format for describing compute operations on structured data. Cross-language specification. Benefits: avoids N-to-N system communication, makes components upgradeable, enables heterogeneous environments. Use cases: SQL parser to execution engine (Calcite to Arrow C++), serialize SQL views (Iceberg), submit to different engines (DataFusion, Postgres), plan visualization
- **List Functions** `substrait:functions_list.yaml` - Higher-order: transform (map), filter, any_match, all_match. Utility: cardinality, sort (with direction/null placement options). Uses func<T -> R> lambda types
- **Logarithmic Functions** `substrait:functions_logarithmic.yaml` - ln, log10, log2, logb (arbitrary base), log1p. Typed for fp32/fp64
- **Powered By** `substrait:community/powered_by.md` - Projects using Substrait: Arrow (C++ and Rust compute kernels), Calcite, DataFusion, DuckDB, Ibis, Velox, Spark, Trino, Iceberg
- **Producer Tools** `substrait:tools/producer_tools.md` - Tools for generating Substrait plans
- **Relation Basics** `substrait:relations/basics.md` - Relational algebra concepts. Relations = plan nodes (filter, project, join, etc.). Each relation has signature: inputs, outputs, property maintenance, direct output order. Emit property for column reordering/subsetting (default: direct). Relations contain or refer to child relations
- **Rounding Functions** `substrait:functions_rounding.yaml` - ceil, floor, round with rounding mode options (TIE_TO_EVEN, TIE_AWAY_FROM_ZERO, TRUNCATE, CEILING, FLOOR)
- **Serialization Basics** `substrait:serialization/basics.md` - Overview of serialization formats
- **Set Functions** `substrait:functions_set.yaml` - index_in for membership testing
- **Specification Status** `substrait:spec/specification.md` - Spec status: past initial design, in final stages. Complete components: Simple types, Compound types, Type variations, User-defined types, Field references, Scalar functions, Specialized record expressions, Aggregate functions, Window functions, User-defined functions, Embedded functions, Relation basics, Logical relations, Text serialization, Binary serialization. Designed not implemented: Table functions, User-defined relations, Embedded relations, Physical relations
- **String Functions** `substrait:functions_string.yaml` - concat, like, substring, regexp_match_substring, regexp_replace, regexp_count_substring, replace, reverse, lower, upper, char_length, bit_length, octet_length, trim, ltrim, rtrim, left, right, repeat, starts_with, ends_with, cap, lpad, rpad, string_agg, center, count_substring. Null handling and case sensitivity options
- **Substrait Validator** `substrait:tools/substrait_validator.md` - Validation tool: substrait-validator final_plan.json --out-file output.html. Shows schema and column indices at each point in plan. HTML report generation
- **Table Functions** `substrait:expressions/table_functions.md` - Convert values to 0..N output records. Examples: explode, pos-explode. Designed, not implemented
- **Technology Principles** `substrait:spec/technology_principles.md` - Design principles guiding Substrait
- **Text Serialization** `substrait:serialization/text_serialization.md` - Human-readable representation. Currently uses Protobuf JSON output (not official Substrait text format yet). Useful for debugging, unit tests
- **Third Party Tools** `substrait:tools/third_party_tools.md` - Ecosystem tools for Substrait
- **Type Aliases** `substrait:types/type_aliases.md` - Shorthand names for common type configurations
- **Type System Overview** `substrait:types/type_system.md` - Types have 4 components: Class (i8, string, STRUCT, extensions), Nullability (NULLABLE with ? suffix or REQUIRED), Variation (system-preferred or extension for in-memory format), Parameters (compound only, e.g. DECIMAL<10,2>). Strict type system: no coercion, all changes via explicit cast expressions
- **Type Variations** `substrait:types/type_variations.md` - Physical variations of base types, distinguished by in-memory format
- **Type Variations** `substrait:type_variations.yaml` - Physical format variations: dict4 (4-byte dictionary encoded string, INHERITS), bigoffset (Arrow large string, SEPARATE), avro (Avro encoded struct), cstruct (C struct representation), dict2 (2-byte dictionary string)
- **User Defined Functions** `substrait:expressions/user_defined_functions.md` - Reusable named functions beyond core spec. Registered externally (drop file, special command)
- **User Defined Relations** `substrait:relations/user_defined_relations.md` - Custom relational operations for specific platforms. Designed, not implemented
- **Versioning** `substrait:spec/versioning.md` - Versioning policy for the specification
- **Window Functions** `substrait:expressions/window_functions.md` - Relate a record to encompassing records. SQL examples: RANK, NTILE, ROW_NUMBER. Frame specification, partitioning, ordering

## Reference

- **Active Libraries** `substrait:community/active_libraries.md` - List of active Substrait library implementations: Go, Java, Python, Rust; and inactive implementations (C++, C#, JavaScript, Ruby) with links to each repository.
- **Breaking Change Policy** `substrait:spec/breaking_change_policy.md` - Policy for handling breaking changes in the Substrait specification: use dual-write migration strategy, URI-to-URN transition example, and process for deprecating old extension URIs.
- **Common Fields** `substrait:relations/common_fields.md` - Common fields shared by all Substrait relations: emit (output column projection), rel_anchor (for referencing relations), and hints (statistics, saved computations).
- **Extensions Overview** `substrait:extensions/index.md` - Substrait extension mechanism: how to define custom types, functions, and type variations using URIs/URNs and the u! prefix notation for portable cross-engine extensions.
- **Field References** `substrait:expressions/field_references.md` - Field reference types in Substrait expressions: RootReference, OuterReference, Expression, and LambdaParameterReference; covers masking and struct field access patterns.
- **Lambda Expressions** `substrait:expressions/lambda_expressions.md` - Lambda expressions in Substrait: inline anonymous functions for higher-order operations, parameter binding, and closure semantics for use in map/filter-style relations.
- **Logical Relations** `substrait:relations/logical_relations.md` - All logical relation types in Substrait: Read, Filter, Sort, Project, Join, Set, Fetch, Aggregate, Write, and DDL; each with their specific fields and semantics.
- **Named Structs** `substrait:types/named_structs.md` - Named structs in Substrait: depth-first field naming convention and their use in Read relation output schemas.
- **Physical Relations** `substrait:relations/physical_relations.md` - Physical relation variants in Substrait: hash join, nested-loop join, merge join, exchange, top-N sort, physical aggregate, and window operations for execution-layer plans.
- **Scalar Functions** `substrait:expressions/scalar_functions.md` - Scalar function definition in Substrait: function names, argument types, determinism, nullability handling, and return type specification; covers built-in and extension functions.
- **Specialized Record Expressions** `substrait:expressions/specialized_record_expressions.md` - Specialized record expressions beyond scalar functions: cast expressions, if-then-else, switch expressions, and singular-or-list; non-function expression types in Substrait.
- **Subqueries** `substrait:expressions/subqueries.md` - Subquery expressions in Substrait: scalar subqueries, IN predicates, and set predicates (EXISTS, UNIQUE); covers correlated and uncorrelated subquery forms.
- **Type Classes** `substrait:types/type_classes.md` - Substrait type system: simple types, compound types (List, Map, Struct), and user-defined extension types; covers nullability, type parameters, and the u! prefix for extension types.
- **Type Parsing** `substrait:types/type_parsing.md` - Type syntax and grammar for Substrait: notation for simple types, struct/nstruct forms, and the u! prefix for user-defined types; includes parsing rules and examples.

## Tutorial

- **SQL to Substrait Tutorial** `substrait:tutorial/sql_to_substrait.md` - Step-by-step tutorial converting SQL queries to Substrait plans: covers Read relations, Filter, Project, Aggregate, and Join with annotated plan examples.

---

*Rendered from index.yaml at 2026-08-03T09:54:56Z*
