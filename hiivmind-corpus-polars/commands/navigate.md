---
description: Ask questions about Polars documentation
argument-hint: Your question (e.g., "how do lazy frames work?", "group_by and aggregation")
allowed-tools: ["Read", "Grep", "Glob", "WebFetch", "AskUserQuestion", "Task", "TodoWrite"]
---

# Polars Corpus Navigator

Direct access to Polars documentation. Covers DataFrames, expressions, lazy API, I/O, and Rust/Python bindings.

**User request:** $ARGUMENTS

**Corpus location:** `${CLAUDE_PLUGIN_ROOT}`

---

## If No Arguments Provided

Show a brief help message:

```
Polars Corpus - ask me anything about Polars!

Examples:
  /hiivmind-corpus-polars:navigate how do lazy frames work?
  /hiivmind-corpus-polars:navigate group_by and aggregation
  /hiivmind-corpus-polars:navigate reading parquet files

For maintenance, use the parent plugin:
  /hiivmind-corpus:hiivmind_corpus refresh polars
  /hiivmind-corpus:hiivmind_corpus enhance polars [topic]
```

---

## Navigation Process

1. **Search the indexes first** - Grep `data/` for relevant terms
2. **If no search matches, read the index**: `data/index.md`
3. **Parse path format**: `{source_id}:{relative_path}`
4. **Check for `⚡ GREP` marker** - if present, use Grep instead of Read
5. **Look up source** in `data/config.yaml` by ID
6. **Get content** based on source type
7. **Answer** with citation to source and file path

---

## Index Search (Recommended First Step)

### Step 1: Extract Key Concepts

Analyze the user's question and extract:
- **Explicit terms**: Words directly used
- **Synonyms**: Related terms (e.g., "filter" → "select", "where")
- **Domain terms**: Polars concepts (e.g., "lazy" → "LazyFrame", "collect")

### Step 2: Search Index Files

```bash
grep -ri "{term}" data/ --include="*.md"
```

### Step 3: Use Search Results

1. **Direct hit** → use that path
2. **Related hit** → clarify with user first
3. **No hit** → clarify with user first

**CRITICAL: Use the EXACT path from the index! NEVER guess filenames.**

### Step 4: Clarify Before Exploring

If only related content found, use AskUserQuestion to:
1. Clarify the request
2. Show what's available
3. Identify index gaps and suggest `/hiivmind-corpus enhance polars {topic}`

---

## Source Access

### For git sources (Polars docs)

**If `.source/{source_id}/` exists:**
Read from `.source/{source_id}/{docs_root}/{relative_path}`

**If no local clone:**
Fetch from GitHub: `https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{docs_root}/{path}`

### For web sources

Read from cache: `.cache/web/{source_id}/{relative_path}`

---

## File Locations

- **Index**: `data/index.md`
- **Config**: `data/config.yaml`
- **Git sources**: `.source/{source_id}/`
- **Web cache**: `.cache/web/{source_id}/`

---

## Output

- Cite source ID and file path
- Include code examples
- Suggest related docs
- Note freshness warnings if relevant

---

## Making Projects Aware of This Corpus

If you're working in a project that uses Polars but doesn't know about this corpus, you can add awareness to the project's CLAUDE.md.

**The `references/project-awareness.md` file** contains a ready-to-use snippet.

---

## Example Sessions

### Documentation Question

**User:** `/hiivmind-corpus-polars:navigate how do lazy frames work?`

1. Grep `data/` for "lazy"
2. Find entry like `polars:concepts/lazy-api.md`
3. Read from `.source/polars/docs/source/concepts/lazy-api.md`
4. Answer with code examples

---

## Corpus Maintenance

For corpus maintenance, use the parent plugin:

```
/hiivmind-corpus:hiivmind_corpus refresh polars     - Update index from upstream
/hiivmind-corpus:hiivmind_corpus enhance polars X   - Add depth to topic X
/hiivmind-corpus:hiivmind_corpus status polars      - Check corpus freshness
```
