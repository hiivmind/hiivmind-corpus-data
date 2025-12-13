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
2. **Related hit**: Entry is in the right area but doesn't directly answer → **GO TO STEP 4 IMMEDIATELY**
3. **No hit in index**: The topic may not be indexed → **GO TO STEP 4 IMMEDIATELY**

**IMPORTANT:** If you searched for "to_native" and only found "Getting Started" without "native" in the description, that's a **related hit, not a direct hit**. Stop and ask the user before exploring further.

### Step 4: Clarify Before Exploring (IMPORTANT!)

**STOP HERE if you only found related content, not a direct answer.**

Don't start exploring, guessing paths, or searching the source files. Instead, **use AskUserQuestion** to clarify:

**Present these options:**

1. **Clarify the request** - Maybe the question can be rephrased
   - "Could you rephrase your question? I searched for '{terms}' but found no matches."
   - Suggest alternative terms: "Did you mean '{synonym}' or '{related_term}'?"

2. **Show what's available** - Help the user find related content
   - "The closest sections I found are: {list nearby sections}"
   - "Would any of these help: {list related entries}?"

3. **Identify an index gap** - If the user confirms their request was valid
   - "This topic isn't covered in the current index."
   - Offer next steps:
     - `hiivmind-corpus-enhance` - Add depth to a specific topic area
     - `hiivmind-corpus-add-source` - Add another documentation source
     - `hiivmind-corpus-refresh` - Check if upstream docs have new content

**Example response:**

> I searched the index for "native namespace", "to_native", and "from_native" but found no direct matches.
>
> **Options:**
> 1. **Rephrase**: Did you mean "converting dataframes" or "library interop"?
> 2. **Related sections**: The "Getting Started" section covers basic usage
> 3. **Index gap**: If you expected this topic to be covered, the index may need:
>    - Enhancing with `hiivmind-corpus-enhance` for more depth
>    - A new source added with `hiivmind-corpus-add-source`
>
> Which would you like to explore?

## Path Format

Index entries use the format: `{source_id}:{relative_path}`

Examples:
- `narwhals:basics/dataframe.md` - Git source
- `local:team-standards/coding-guidelines.md` - Local uploads
- `web:blog-posts/article-name.md` - Cached web content

## Source Access

### Worked Example (IMPORTANT - Follow This Pattern!)

**Index entry found:** `narwhals:basics/dataframe.md`

**Step 1 - Parse the path:**
- `source_id` = `narwhals` (everything before the colon)
- `relative_path` = `basics/dataframe.md` (everything after the colon)

**Step 2 - Look up source in config.yaml:**
```yaml
sources:
  - id: narwhals
    type: git
    repo_owner: narwhals-dev
    repo_name: narwhals
    branch: main
    docs_root: docs
```

**Step 3 - Construct the full path:**
- Local clone: `.source/narwhals/docs/basics/dataframe.md`
- GitHub URL: `https://raw.githubusercontent.com/narwhals-dev/narwhals/main/docs/basics/dataframe.md`

**CRITICAL:** The `relative_path` from the index is used EXACTLY as-is. NEVER invent or guess filenames!

### For git sources

**If `.source/{source_id}/` exists (local clone):**
Read directly from `.source/{source_id}/{docs_root}/{relative_path}`

**If no local clone:**

Fetch from GitHub using the EXACT path from the index:
```
https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{docs_root}/{relative_path}
```
Use WebFetch to retrieve content.

Or clone locally:
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
