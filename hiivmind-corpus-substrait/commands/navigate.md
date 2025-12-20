---
description: Ask questions about Substrait documentation
argument-hint: Your question (e.g., "how do query plans work?", "relations and expressions")
allowed-tools: ["Read", "Grep", "Glob", "WebFetch", "AskUserQuestion", "Task", "TodoWrite"]
---

# Substrait Corpus Navigator

Direct access to Substrait documentation. Covers cross-language query plans and data compute interoperability.

**User request:** $ARGUMENTS

**Corpus location:** `${CLAUDE_PLUGIN_ROOT}`

---

## If No Arguments Provided

Show a brief help message:

```
Substrait Corpus - ask me anything about Substrait!

Examples:
  /hiivmind-corpus-substrait:navigate how do query plans work?
  /hiivmind-corpus-substrait:navigate relations and expressions
  /hiivmind-corpus-substrait:navigate Arrow integration

For maintenance, use the parent plugin:
  /hiivmind-corpus refresh substrait
  /hiivmind-corpus enhance substrait [topic]
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
3. Identify index gaps and suggest `/hiivmind-corpus enhance substrait {topic}`

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

## Making Projects Aware of This Corpus

If you're working in a project that uses Substrait but doesn't know about this corpus, you can add awareness to the project's CLAUDE.md.

**The `references/project-awareness.md` file** contains a ready-to-use snippet.

---

## Example Sessions

### Documentation Question

**User:** `/hiivmind-corpus-substrait:navigate how do query plans work?`

1. Grep `data/` for "query plan"
2. Find relevant entry
3. Read the source file
4. Answer with code examples

---

## Corpus Maintenance

For corpus maintenance, use the parent plugin:

```
/hiivmind-corpus refresh substrait     - Update index from upstream
/hiivmind-corpus enhance substrait X   - Add depth to topic X
/hiivmind-corpus status substrait      - Check corpus freshness
```
