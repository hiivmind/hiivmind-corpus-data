# Substrait Documentation Index

> Source: substrait (git) | 43 docs | Cross-language specification for data compute operations
> Last updated: 2026-03-25

---

## Overview

- **Home** `substrait:index.md` - Substrait: format for describing compute operations on structured data. Cross-language specification. Benefits: avoids N-to-N system communication, makes components upgradeable, enables heterogeneous environments. Use cases: SQL parser to execution engine (Calcite to Arrow C++), serialize SQL views (Iceberg), submit to different engines (DataFusion, Postgres), plan visualization
- **About Substrait** `substrait:about.md` - Project vision: well-defined cross-language spec for data compute. Similar to Arrow (memory format) but for compute expressions. Why not SQL: lacks sufficient detail, not machine-processable. Why separate project: avoid coupling to single technology, like Arrow separated from Drill. Related: Apache Calcite (JVM SQL parsing), Apache Arrow (memory format). Name: "sub-strait" = underlayment connecting pools of data
- **FAQ** `substrait:faq.md` - Frequently asked questions about Substrait

---

## Specification

- **Specification Status** `substrait:spec/specification.md` - Spec status: past initial design, in final stages. Components overview table:
  - **Complete**: Simple types, Compound types, Type variations, User-defined types, Field references, Scalar functions, Specialized record expressions, Aggregate functions, Window functions, User-defined functions, Embedded functions, Relation basics, Logical relations, Text serialization, Binary serialization
  - **Designed not implemented**: Table functions, User-defined relations, Embedded relations, Physical relations
- **Technology Principles** `substrait:spec/technology_principles.md` - Design principles guiding Substrait
- **Versioning** `substrait:spec/versioning.md` - Versioning policy for the specification
- **Extending Substrait** `substrait:spec/extending.md` - How to propose new read/write definition types and other extensions

---

## Type System

- **Type System Overview** `substrait:types/type_system.md` - Types have 4 components:
  1. **Class** (always): `i8`, `string`, `STRUCT`, extensions - describes non-null values
  2. **Nullability** (always): `NULLABLE` (`?` suffix) or `REQUIRED` (no suffix) - null is a special value, not a separate type
  3. **Variation** (always): system-preferred `[0]` or extension - in-memory format variations
  4. **Parameters** (compound only): `<10, 2>` for DECIMAL, `<i32, string>` for STRUCT
  - **Strict type system**: no coercion, all changes via explicit cast expressions
- **Type Classes** `substrait:types/type_classes.md` - Complete type catalog:
  - **Simple numeric**: `boolean`, `i8`, `i16`, `i32`, `i64`, `i128`, `fp32`, `fp64`, `decimal<P,S>`
  - **Simple string/binary**: `string`, `binary`, `fixedchar<L>`, `varchar<L>`, `fixedbinary<L>`
  - **Simple temporal**: `date`, `time`, `timestamp`, `timestamp_tz`, `interval_year`, `interval_day`
  - **Simple other**: `uuid`
  - **Compound**: `STRUCT<T1,T2,...>`, `LIST<T>`, `MAP<K,V>`, `FUNC<T->R>` (function/lambda types for higher-order operations)
  - **User-defined**: extension types with `u!` prefix (e.g., `u!point`)
- **Type Variations** `substrait:types/type_variations.md` - Physical variations of base types, distinguished by in-memory format
- **Type Aliases** `substrait:types/type_aliases.md` - Shorthand names for common type configurations
- **Type Parsing** `substrait:types/type_parsing.md` - Syntax for describing types in text form. Function types: `func<any1 -> any2>` (single param), `func<(any1, any2) -> any3>` (multiple params). User-defined types use `u!typename` syntax. Precision type naming updated to match grammar
- **Named Structs** `substrait:types/named_structs.md` - Structs with named fields for schemas. `NamedStruct` = struct type + column names. Names in depth-first order for nested types

---

## Expressions

- **Field References** `substrait:expressions/field_references.md` - Identify portions of a record to operate on. Always numeric (not by name). `structField.field: 1` = second field. Root types: `RootReference` (incoming record), `OuterReference` (correlated subqueries), `Expression` (expression result), `LambdaParameterReference` (lambda params). References only make sense relative to a schema context
- **Scalar Functions** `substrait:expressions/scalar_functions.md` - Function specification: `functionReference` (ID into extension list), `outputType`, `arguments` (positional). Functions defined in extension YAML files. Optional `description` field at function-level and per-implementation. Examples: `is_null`, `index_in`, `equal`, `multiply`. Arguments wrapped in `value` objects
- **Lambda Expressions** `substrait:expressions/lambda_expressions.md` - Inline anonymous functions for higher-order operations. Components: `parameters` (struct type), `body` (expression). Type is `func<params -> return>`. Parameter access via `LambdaParameterReference` with `steps_out` for nested scopes. `LambdaInvocation` for direct calls. Used with functions like `transform` and `filter` on collections. Supports closures referencing outer lambdas, input records, and outer queries
- **Aggregate Functions** `substrait:expressions/aggregate_functions.md` - Functions that collapse many records into one value. Examples: SUM, COUNT, AVG. Used in `measures` of Aggregate relations. May have optional filter
- **Window Functions** `substrait:expressions/window_functions.md` - Relate a record to encompassing records. SQL examples: RANK, NTILE, ROW_NUMBER. Frame specification, partitioning, ordering
- **Specialized Record Expressions** `substrait:expressions/specialized_record_expressions.md` - Expressions outside function paradigm: if/then/else, switch/case, cast. Cast is an expression type, not a function
- **User Defined Functions** `substrait:expressions/user_defined_functions.md` - Reusable named functions beyond core spec. Registered externally (drop file, special command)
- **Embedded Functions** `substrait:expressions/embedded_functions.md` - Function implementations embedded in plan. Common in data science workflows with business logic interspersed
- **Table Functions** `substrait:expressions/table_functions.md` - Convert values to 0..N output records. Examples: explode, pos-explode. (Designed, not implemented)
- **Dynamic Parameters** `substrait:expressions/dynamic_parameters.md` - Parameterized query plans
- **Subqueries** `substrait:expressions/subqueries.md` - Nested query expressions
- **Extended Expression** `substrait:expressions/extended_expression.md` - Extended expression capabilities

---

## Relations

- **Relation Basics** `substrait:relations/basics.md` - Relational algebra concepts. Relations = plan nodes (filter, project, join, etc.). Each relation has signature: inputs, outputs, property maintenance, direct output order. Emit property for column reordering/subsetting (default: `direct`). Relations contain or refer to child relations
- **Common Fields** `substrait:relations/common_fields.md` - Fields common to all relations
- **Logical Relations** `substrait:relations/logical_relations.md` - Core relational operations:
  - **Read**: 0 inputs, 1 output. Types: Virtual Table (embedded data), Named Table (catalog reference), Local Files (URI with format), Iceberg Table. Has `filter`, `bestEffortFilter`, `projection`, schema
  - **Filter**: 1 input, boolean `condition` expression
  - **Sort**: 1 input, `sortFields` list with direction
  - **Project**: 1 input, adds columns via `expressions` (doesn't remove/reorder - use emit)
  - **Cross Product**: 2 inputs, Cartesian product
  - **Join**: 2 inputs (left, right), `expression` for join condition, `type` enum (INNER, OUTER, LEFT, RIGHT, SEMI, ANTI, SINGLE, MARK)
  - **Set**: 2+ inputs. Types: MINUS, INTERSECTION, UNION (with variants: Primary, Multiset, All, Distinct)
  - **Fetch**: offset/limit for pagination
  - **Aggregate**: `groupings` (grouping sets), `measures` (aggregate expressions). Extra column for grouping set index
  - **Reference**: DAG construction, shared subtrees (multi-query optimization)
  - **Write**: INSERT/DELETE/UPDATE/CTAS operations
  - **Update**: Column transformations on named table
  - **DDL**: CREATE/DROP/ALTER for TABLE/VIEW
- **Physical Relations** `substrait:relations/physical_relations.md` - Physical variants: hash join vs merge join vs nested loop. (Designed, not implemented)
- **User Defined Relations** `substrait:relations/user_defined_relations.md` - Custom relational operations for specific platforms. (Designed, not implemented)
- **Embedded Relations** `substrait:relations/embedded_relations.md` - Relations with embedded "machine code". (Designed, not implemented)

---

## Serialization

- **Serialization Basics** `substrait:serialization/basics.md` - Overview of serialization formats
- **Binary Serialization** `substrait:serialization/binary_serialization.md` - High performance, compact protobuf representation. Source of truth for spec. Well-commented proto files
- **Text Serialization** `substrait:serialization/text_serialization.md` - Human-readable representation. Currently uses Protobuf JSON output (not official Substrait text format yet). Useful for debugging, unit tests

---

## Extensions

- **Extensions Overview** `substrait:extensions/index.md` - Extension mechanism for types and functions. Simple extensions in YAML files. URN identifiers reference extension files. Extension anchors link plan references to definitions. Optional `metadata` field at top-level, type, and function scopes. Deprecation support: `deprecated` field with `since` version, optional `reason`/`metadata` (applies to types, type variations, functions, implementations). Core extensions in `extensions/` directory

### Standard Function Extensions

#### Arithmetic & Math
- **Arithmetic Functions** `substrait:../extensions/functions_arithmetic.yaml` ⚡ GREP - 1951 lines. Scalar functions: `add`, `subtract`, `multiply`, `divide`, `negate`, `modulus`, `power`, `sqrt`, `exp`, `cos`, `sin`, `tan`, `cosh`, `sinh`, `tanh`, `acos`, `asin`, `atan`, `acosh`, `asinh`, `atanh`, `atan2`, `sign`, `abs`, `factorial`, `bitwise_not`, `bitwise_and`, `bitwise_or`, `bitwise_xor`. Each with typed implementations (i8–i64, fp32, fp64) and overflow/rounding options. Search: `grep -n "name:" functions_arithmetic.yaml`
- **Decimal Arithmetic** `substrait:../extensions/functions_arithmetic_decimal.yaml` ⚡ GREP - 249 lines. Decimal-specific: `add`, `subtract`, `multiply`, `divide`, `modulus`, `abs`, `power` with precision/scale tracking
- **Logarithmic Functions** `substrait:../extensions/functions_logarithmic.yaml` ⚡ GREP - 255 lines. `ln`, `log10`, `log2`, `logb` (arbitrary base), `log1p`. Typed for fp32/fp64
- **Rounding Functions** `substrait:../extensions/functions_rounding.yaml` ⚡ GREP - 271 lines. `ceil`, `floor`, `round` with rounding mode options (TIE_TO_EVEN, TIE_AWAY_FROM_ZERO, TRUNCATE, CEILING, FLOOR)
- **Decimal Rounding** `substrait:../extensions/functions_rounding_decimal.yaml` - 83 lines. `ceil`, `floor`, `round` for decimal types

#### Comparison & Boolean
- **Comparison Functions** `substrait:../extensions/functions_comparison.yaml` ⚡ GREP - 323 lines. `not_equal`, `equal`, `is_not_distinct_from`, `is_distinct_from`, `lt`, `gt`, `lte`, `gte`, `between`, `is_null`, `is_not_null`, `is_nan`, `is_finite`, `is_infinite`, `nullif`, `coalesce`, `least`, `greatest`
- **Boolean Functions** `substrait:../extensions/functions_boolean.yaml` - 141 lines. `or`, `and`, `and_not`, `xor`, `not` using Kleene logic (null = unknown). Aggregate: `bool_and`, `bool_or`

#### String & DateTime
- **String Functions** `substrait:../extensions/functions_string.yaml` ⚡ GREP - 1577 lines. `concat`, `like`, `substring`, `regexp_match_substring`, `regexp_replace`, `regexp_count_substring`, `replace`, `reverse`, `lower`, `upper`, `char_length`, `bit_length`, `octet_length`, `trim`, `ltrim`, `rtrim`, `left`, `right`, `repeat`, `starts_with`, `ends_with`, `cap`, `lpad`, `rpad`, `string_agg`, `center`, `count_substring`. Null handling and case sensitivity options
- **DateTime Functions** `substrait:../extensions/functions_datetime.yaml` ⚡ GREP - 1119 lines. `extract` (YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, ISO_WEEK, etc.), `add`, `subtract`, `multiply` for temporal arithmetic, `assume_timezone`, `local_timestamp`, `strptime_time`, `strptime_date`, `strptime_timestamp`, `strftime`, `round_temporal`, `round_calendar`

#### Collections & Sets
- **List Functions** `substrait:../extensions/functions_list.yaml` - 132 lines. Higher-order: `transform` (map), `filter`, `any_match`, `all_match`. Utility: `cardinality`, `sort` (with direction/null placement options). Uses `func<T -> R>` lambda types
- **Set Functions** `substrait:../extensions/functions_set.yaml` - 28 lines. `index_in` for membership testing

#### Aggregate Functions
- **Generic Aggregates** `substrait:../extensions/functions_aggregate_generic.yaml` - 42 lines. `count` (values or records, with overflow options), `any_value` (arbitrary value from group, with ignore_nulls option). Both decomposable for distributed execution
- **Decimal Aggregates** `substrait:../extensions/functions_aggregate_decimal_output.yaml` - 42 lines. Aggregates with decimal output types
- **Approximate Aggregates** `substrait:../extensions/functions_aggregate_approx.yaml` - 19 lines. Approximate aggregate functions

#### Geometry
- **Geometry Functions** `substrait:../extensions/functions_geometry.yaml` ⚡ GREP - 240 lines. `point`, `make_line`, `x_coordinate`, `y_coordinate`, `num_points`, `is_empty`, `is_closed`, `is_simple`, `is_ring`, `geometry_type`, `envelope`, `dimension`, `is_valid`, `collection_extract`, `flip_coordinates`, `remove_repeated_points`, `buffer`, `centroid`, `minimum_bounding_circle`

### Extension Type Definitions
- **Extension Types** `substrait:../extensions/extension_types.yaml` - User-defined type examples: `point` (latitude/longitude as i32), `line` (start/end as `u!point`). Demonstrates `u!` prefix for user-defined types
- **Type Variations** `substrait:../extensions/type_variations.yaml` - Physical format variations: `dict4` (4-byte dictionary encoded string, INHERITS), `bigoffset` (Arrow large string, SEPARATE), `avro` (Avro encoded struct), `cstruct` (C struct representation), `dict2` (2-byte dictionary string)

---

## Tutorial

- **SQL to Substrait Tutorial** `substrait:tutorial/sql_to_substrait.md` - **Comprehensive walkthrough** building a plan from SQL:
  ```sql
  SELECT product_name, product_id, sum(quantity * price) as sales
  FROM orders INNER JOIN products ON orders.product_id = products.product_id
  WHERE INDEX_IN("Computers", categories) IS NULL
  GROUP BY product_name, product_id
  ```
  Covers:
  - **Types**: nullability enum, decimal parameters, nested types (list, struct), `NamedStruct` for schemas
  - **Expressions**: field references (numeric, not names), literals, scalar functions (`is_null`, `index_in`), expression trees
  - **Relations**: Read (namedTable, baseSchema), Filter (input + condition), Join (left, right, type, expression), Aggregate (groupings, measures)
  - **Field indices**: implicit schema at each point, output order rules per relation type
  - **Emit**: column reordering/subsetting via `common.emit.outputMapping`
  - **Plans**: `extensionUrns`, `extensions` (function anchors), `relations` with Root (provides final column names)
- **Examples** `substrait:tutorial/examples.md` - Additional example plans

---

## Tools

- **Producer Tools** `substrait:tools/producer_tools.md` - Tools for generating Substrait plans
- **Substrait Validator** `substrait:tools/substrait_validator.md` - Validation tool: `substrait-validator final_plan.json --out-file output.html`. Shows schema and column indices at each point in plan. HTML report generation
- **Third Party Tools** `substrait:tools/third_party_tools.md` - Ecosystem tools for Substrait

---

## Community

- **Community Overview** `substrait:community/index.md` - Community resources and participation. AI contribution policy: AI-assisted contributions accepted with disclosure of tools used; contributors must self-review generated content before requesting review
- **Powered By** `substrait:community/powered_by.md` - Projects using Substrait: Arrow (C++, Rust compute kernels), Calcite, DataFusion, DuckDB, Ibis, Velox, Spark, Trino, Iceberg
- **Governance** `substrait:governance.md` - Project governance model. Bar for inclusion: at least two of top four OSS data technologies (Arrow, Spark, Iceberg, Trino) must support feature
