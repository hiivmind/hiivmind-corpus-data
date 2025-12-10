# Substrait Documentation Index

> Source: substrait (git) | 42 docs | Cross-language specification for data compute operations
> Last updated: 2025-12-10

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
- **Type Classes** `substrait:types/type_classes.md` - Simple types: integers (`i8`-`i128`), floats (`fp32`, `fp64`), `boolean`, `string`, `binary`, `date`, `time`, `timestamp`, `timestamp_tz`, `interval_year`, `interval_day`, `uuid`, `fixedchar`, `varchar`, `fixedbinary`, `decimal`. Compound types: `STRUCT`, `LIST`, `MAP`. User-defined types via extensions
- **Type Variations** `substrait:types/type_variations.md` - Physical variations of base types, distinguished by in-memory format
- **Type Aliases** `substrait:types/type_aliases.md` - Shorthand names for common type configurations
- **Type Parsing** `substrait:types/type_parsing.md` - Syntax for describing types in text form
- **Named Structs** `substrait:types/named_structs.md` - Structs with named fields for schemas. `NamedStruct` = struct type + column names. Names in depth-first order for nested types

---

## Expressions

- **Field References** `substrait:expressions/field_references.md` - Identify portions of a record to operate on. Always numeric (not by name). `structField.field: 1` = second field. `rootReference: {}` = relative to current schema. References only make sense relative to a schema context
- **Scalar Functions** `substrait:expressions/scalar_functions.md` - Function specification: `functionReference` (ID into extension list), `outputType`, `arguments` (positional). Functions defined in extension YAML files. Examples: `is_null`, `index_in`, `equal`, `multiply`. Arguments wrapped in `value` objects
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

- **Extensions Overview** `substrait:extensions/index.md` - Extension mechanism for types and functions. Simple extensions in YAML files. URN identifiers reference extension files. Extension anchors link plan references to definitions. Core extensions in `extensions/` directory: `functions_arithmetic.yaml`, `functions_comparison.yaml`, `functions_set.yaml`, etc.

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

- **Community Overview** `substrait:community/index.md` - Community resources and participation
- **Powered By** `substrait:community/powered_by.md` - Projects using Substrait: Arrow (C++, Rust compute kernels), Calcite, DataFusion, DuckDB, Ibis, Velox, Spark, Trino, Iceberg
- **Governance** `substrait:governance.md` - Project governance model. Bar for inclusion: at least two of top four OSS data technologies (Arrow, Spark, Iceberg, Trino) must support feature
