---
name: hiivmind-corpus-navigate-narwhals
description: Find relevant Narwhals documentation. Use when writing dataframe-agnostic code that works with pandas, Polars, PyArrow, cuDF, Modin, Dask, DuckDB, Ibis, or PySpark.
---

# Narwhals Corpus Navigator

Find and retrieve relevant documentation from the Narwhals corpus.

## Process

1. **Search the indexes first** (see Index Search section below)
   - Extract key concepts from the question
   - Grep the index files for those terms
   - If matches found → use those entries directly
2. **If no search matches, read the index**: `data/index.md`
3. **Parse path format**: `{source_id}:{relative_path}`
4. **Look up source** in `data/config.yaml` by ID
5. **Get content** based on source type (see Source Access below)
6. **Answer** with citation to source and file path

## Index Search (Recommended First Step)

**Before reading sections sequentially, SEARCH the indexes for relevant terms.**

### Step 1: Extract Key Concepts

Analyze the user's question and extract:
- **Explicit terms**: Words directly used in the question
- **Synonyms**: Related terms (e.g., "filter" → also try "select", "where", "mask")
- **Domain terms**: Technical concepts that might appear in docs (e.g., "pandas" → also try "polars", "dataframe", "native")

### Step 2: Search Index Files

```bash
# Search for each term in the index
grep -ri "{term}" data/ --include="*.md"
```

**Tip:** Search for the most specific term first. If no matches, broaden to synonyms.

### Step 3: Use Search Results

If grep finds matches:
1. **Direct hit**: Entry description matches the question → use that path
2. **Related hit**: Entry is in the right area → read that section for context
3. **No hit in index**: The topic may not be indexed yet → report this as an index gap

### Step 4: Report Index Gaps

If the user's question cannot be answered because the index lacks relevant entries:

> "The index doesn't have entries for '{term}'. The closest match is '{related_section}'.
> If this topic should be covered, consider running `hiivmind-corpus-enhance` to add depth to this area."

## Path Format

Index entries use the format: `{source_id}:{relative_path}`

Examples:
- `narwhals:basics/dataframe.md` - Git source
- `local:team-standards/coding-guidelines.md` - Local uploads
- `web:blog-posts/article-name.md` - Cached web content

## Source Access

### For git sources

Look up the source in `data/config.yaml` to get `repo_owner`, `repo_name`, `branch`, and `docs_root`.

**If `.source/{source_id}/` exists (local clone):**
Read directly from `.source/{source_id}/{docs_root}/{path}`

**If no local clone:**

Option A - Fetch on demand:
```
https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{docs_root}/{path}
```
Use WebFetch to retrieve content. No clone needed.

Option B - Clone locally:
```bash
git clone --depth 1 {repo_url} .source/{source_id}
```

**Staleness check for git sources:**
After reading, compare the source's `last_commit_sha` in config to the local clone:
```bash
cd .source/{source_id} && git rev-parse HEAD
```
If clone is **newer** than indexed SHA → warn user: "The docs have been updated since the index was built. Consider running refresh to update the index."

### For local sources

Read directly from: `data/uploads/{source_id}/{path}`

Local sources are user-uploaded files stored within the corpus.

### For web sources

Read from cache: `.cache/web/{source_id}/{cached_file}`

If cache miss, look up the URL in `data/config.yaml` and fetch fresh content.

## File Locations

- **Index**: `data/index.md`
- **Config**: `data/config.yaml` (has sources array with per-source tracking)
- **Git sources**: `.source/{source_id}/` (cloned repos, gitignored)
- **Local sources**: `data/uploads/{source_id}/` (user-uploaded files)
- **Web cache**: `.cache/web/{source_id}/` (fetched web content, gitignored)

## Output

- Cite the source ID and file path for reference
- Include code examples from the docs
- Suggest related docs from the same index section
- Note source type and freshness warnings if relevant

## Making Projects Aware of This Corpus

If you're working in a project that uses Narwhals but doesn't know about this corpus, you can add awareness to the project's CLAUDE.md.

**The `data/project-awareness.md` file** contains a ready-to-use snippet that can be added to any project's CLAUDE.md to make Claude aware of this corpus when working in that project.

### How to Inject

1. Read `data/project-awareness.md` from this corpus
2. Add its contents to the target project's CLAUDE.md (create if needed)
3. The project will now know to use this corpus for Narwhals questions

### When to Suggest Injection

Suggest adding project awareness when:
- User is working in a project that heavily uses Narwhals
- User repeatedly asks Narwhals questions without invoking the corpus
- User says "I keep forgetting to use the docs"

Example suggestion:
> "I notice this project uses Narwhals extensively. Would you like me to add corpus awareness to this project's CLAUDE.md? That way I'll automatically know to check the Narwhals docs when working here."
