---
description: Ask questions about Substrait documentation or manage this corpus
argument-hint: Question or command (e.g., "how do query plans work?", "refresh", "enhance")
allowed-tools: ["Read", "Grep", "Glob", "WebFetch", "AskUserQuestion", "Skill", "Task", "TodoWrite"]
---

# Substrait Corpus Navigator

Direct access to Substrait documentation. Covers cross-language query plans and data compute interoperability.

**User request:** $ARGUMENTS

**Corpus location:** `${CLAUDE_PLUGIN_ROOT}`

---

## Routing

### If no arguments provided

Show a brief help message:

```
Substrait Corpus - ask me anything about Substrait!

Examples:
  /hiivmind-corpus-substrait:navigate how do query plans work?
  /hiivmind-corpus-substrait:navigate relations and expressions
  /hiivmind-corpus-substrait:navigate Arrow integration

Maintenance:
  /hiivmind-corpus-substrait:navigate refresh     - Update index from upstream
  /hiivmind-corpus-substrait:navigate enhance X   - Add depth to topic X
  /hiivmind-corpus-substrait:navigate status      - Check corpus freshness
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
3. **Pass context** in your message: "Working in Substrait corpus at ${CLAUDE_PLUGIN_ROOT}. User wants to {action}."

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
- **Synonyms**: Related terms (e.g., "plan" → "relation", "expression")
- **Domain terms**: Substrait concepts (e.g., "proto" → "protobuf", "extension")

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
3. Identify index gaps and suggest `/hiivmind-corpus-substrait:navigate enhance {topic}`

---

## Source Access

### For git sources

**If `.source/{source_id}/` exists:**
Read from `.source/{source_id}/{docs_root}/{relative_path}`

**If no local clone:**
Fetch from GitHub

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

**User:** `/hiivmind-corpus-substrait:navigate how do query plans work?`

1. Grep `data/` for "query plan"
2. Find relevant entry
3. Read the source file
4. Answer with code examples

### Maintenance

**User:** `/hiivmind-corpus-substrait:navigate refresh`

1. Detect maintenance keyword
2. Load `hiivmind-corpus-refresh` with corpus context
