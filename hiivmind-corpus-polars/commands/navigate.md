---
description: Ask questions about Polars documentation or manage this corpus
argument-hint: Question or command (e.g., "how do lazy frames work?", "refresh", "enhance expressions")
allowed-tools: ["Read", "Grep", "Glob", "WebFetch", "AskUserQuestion", "Skill", "Task", "TodoWrite"]
---

# Polars Corpus Navigator

Direct access to Polars documentation. Covers DataFrames, expressions, lazy API, I/O, and Rust/Python bindings.

**User request:** $ARGUMENTS

**Corpus location:** `${CLAUDE_PLUGIN_ROOT}`

---

## Routing

### If no arguments provided

Show a brief help message:

```
Polars Corpus - ask me anything about Polars!

Examples:
  /hiivmind-corpus-polars:navigate how do lazy frames work?
  /hiivmind-corpus-polars:navigate group_by and aggregation
  /hiivmind-corpus-polars:navigate reading parquet files

Maintenance:
  /hiivmind-corpus-polars:navigate refresh     - Update index from upstream
  /hiivmind-corpus-polars:navigate enhance X   - Add depth to topic X
  /hiivmind-corpus-polars:navigate status      - Check corpus freshness
```

### If arguments match a maintenance command

| Pattern | Skill to Load |
|---------|---------------|
| `refresh`, `update`, `sync` | `hiivmind-corpus-refresh` |
| `enhance {topic}` | `hiivmind-corpus-enhance` |
| `status`, `freshness`, `stale?` | `hiivmind-corpus-refresh` (status mode) |
| `add source {url}` | `hiivmind-corpus-add-source` |
| `awareness`, `inject`, `claude.md` | `hiivmind-corpus-awareness` |

**How to invoke parent skills:**

1. **Set corpus context** - All paths are relative to `${CLAUDE_PLUGIN_ROOT}`
2. **Load the skill** via the Skill tool (e.g., `hiivmind-corpus-refresh`)
3. **Pass context** in your message: "Working in Polars corpus at ${CLAUDE_PLUGIN_ROOT}. User wants to {action}."

### Otherwise: Navigate (default path)

This is a documentation question. Follow the navigation process below.

---

## Navigation Process

1. **Search the indexes first** - Grep `data/` for relevant terms
2. **If no search matches, read the index**: `data/index.md`
3. **Parse path format**: `{source_id}:{relative_path}`
4. **Look up source** in `data/config.yaml` by ID
5. **Get content** based on source type
6. **Answer** with citation to source and file path

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
3. Identify index gaps and suggest `/hiivmind-corpus-polars:navigate enhance {topic}`

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

## Example Sessions

### Documentation Question

**User:** `/hiivmind-corpus-polars:navigate how do lazy frames work?`

1. Grep `data/` for "lazy"
2. Find entry like `polars:concepts/lazy-api.md`
3. Read from `.source/polars/docs/concepts/lazy-api.md`
4. Answer with code examples

### Maintenance

**User:** `/hiivmind-corpus-polars:navigate refresh`

1. Detect maintenance keyword
2. Load `hiivmind-corpus-refresh` with corpus context
