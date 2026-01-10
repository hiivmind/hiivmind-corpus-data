---
name: hiivmind-corpus-substrait-navigate
description: This skill answers questions about Substrait documentation including query plans, relational algebra, and cross-engine interoperability with Arrow and Calcite. Use when user asks about query plan serialization or engine interop. Triggers: substrait, query-plan, sql, arrow, calcite, interop.
---

# Substrait Documentation Navigator

Direct access to Substrait documentation covering cross-language query plans and data compute interoperability.

**User request:** $ARGUMENTS

**Corpus location:** `${CLAUDE_PLUGIN_ROOT}`

---

## Navigation Process

1. **Search the indexes first** (see Index Search section below)
   - Extract key concepts from the question
   - Grep the index files for those terms
   - If matches found → use those entries directly
2. **If no search matches, navigate by section**:
   - Read the index: `data/index.md`
   - Check for tiered index (if main index links to sub-indexes)
   - Find relevant section and read sub-index if tiered
3. **Parse path format**: `{source_id}:{relative_path}`
4. **Check for `⚡ GREP` marker** - if present, use Grep instead of Read
5. **Look up source** in `data/config.yaml` by ID
6. **Get content** based on source type (see Source Access below)
7. **Answer** with citation to source and file path

---

## Index Search (Recommended First Step)

**Before reading sections sequentially, SEARCH the indexes for relevant terms.**

### Step 1: Extract Key Concepts

Analyze the user's question and extract:
- **Explicit terms**: Words directly used in the question
- **Synonyms**: Related terms (e.g., "plan" → "relation", "expression")
- **Domain terms**: Substrait concepts (e.g., "proto" → "protobuf", "extension")

### Step 2: Search All Index Files

```bash
# Search for each term across all index files
grep -ri "{term}" data/ --include="*.md"
```

**Tip:** Search for the most specific term first. If no matches, broaden to synonyms.

### Step 2b: Search Entry Keywords (High Priority)

Index entries may have keyword lines for operational lookup:

```markdown
- **Entry Title** `source:path.md` - Description
  Keywords: `keyword1`, `keyword2`, `keyword3`
```

**Keyword matches are high-confidence** - if a user asks about a term and an entry has matching keywords, that's a direct hit.

### Step 3: Use Search Results (Priority Order)

If grep finds matches, prioritize in this order:

1. **Keyword match** (highest confidence): Entry has `Keywords:` line matching the search term → use that path immediately
2. **Direct description hit**: Entry description directly matches the question → use that path
3. **Related hit**: Entry is in the right area but doesn't directly answer → **GO TO STEP 4 IMMEDIATELY**
4. **No hit in index**: The topic may not be indexed → **GO TO STEP 4 IMMEDIATELY**

**CRITICAL: Use the EXACT path from the index! NEVER guess or invent filenames.**

### Step 4: Clarify Before Exploring (IMPORTANT!)

**STOP HERE if you only found related content, not a direct answer.**

Don't start exploring, guessing paths, or searching the source files. Instead, **use AskUserQuestion** to clarify:

**Present these options:**

1. **Clarify the request** - Maybe the question can be rephrased
2. **Show what's available** - Help the user find related content
3. **Identify an index gap** - Offer: "Would you like me to enhance the index for this topic?"

---

## Path Format

Index entries use the format: `{source_id}:{relative_path}`

Examples:
- `substrait:relations/index.md` - Relation operators overview
- `substrait:types/type_classes.md` - Type system documentation
- `substrait:expressions/scalar_functions.md` - Scalar function reference

---

## Source Access

### For git sources

**Step 1 - Check for local clone:**
Use Glob to check if `.source/{source_id}/` exists.

**Step 2a - If local clone exists (PREFERRED):**
Read directly from `.source/{source_id}/{docs_root}/{relative_path}` using the Read tool.

**Step 2b - If NO local clone exists (fallback only):**
Fetch from GitHub using the EXACT path from the index.

### For local sources

Read directly from: `data/uploads/{source_id}/{path}`

### For web sources

Read from cache: `.cache/web/{source_id}/{cached_file}`

If cache miss, look up the URL in `data/config.yaml` and fetch fresh content.

---

## File Locations

- **Index**: `data/index.md` (and `data/sections/*.md` if tiered)
- **Config**: `data/config.yaml` (has sources array with per-source tracking)
- **Git sources**: `.source/{source_id}/` (cloned repos, gitignored)
- **Local sources**: `data/uploads/{source_id}/` (user-uploaded files)
- **Web cache**: `.cache/web/{source_id}/` (fetched web content, gitignored)

---

## Output

- Cite the source ID and file path for reference
- Include code examples from the docs
- Suggest related docs from the same index section
- Note source type and freshness warnings if relevant

---

## Corpus Maintenance

For corpus maintenance, use the parent plugin:

```
/hiivmind-corpus refresh substrait     - Update index from upstream
/hiivmind-corpus enhance substrait X   - Add depth to topic X
/hiivmind-corpus status substrait      - Check corpus freshness
```

---

## Making Projects Aware of This Corpus

If you're working in a project that uses Substrait but doesn't know about this corpus, you can add awareness to the project's CLAUDE.md.

**The `references/project-awareness.md` file** contains a ready-to-use snippet.

### When to Suggest Injection

Suggest adding project awareness when:
- User is working in a project that uses Substrait for query planning
- User repeatedly asks Substrait questions without invoking the corpus
- User says "I keep forgetting to use the docs"

---

## Example Sessions

### Documentation Question

**User:** "how do query plans work?"

1. Grep `data/` for "query plan"
2. Find entry like `substrait:relations/index.md`
3. Read from `.source/substrait/site/docs/relations/index.md`
4. Answer with code examples and link to source
