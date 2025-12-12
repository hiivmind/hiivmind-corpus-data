---
name: hiivmind-corpus-ibis-navigate
description: Find relevant Ibis documentation. Use when working with Ibis code, APIs, backends, or expressions.
---

# Ibis Corpus Navigator

Find and retrieve relevant documentation from the Ibis corpus.

## Process

1. **Read the index**: `data/index.md`
2. **Parse path format**: `{source_id}:{relative_path}`
3. **Look up source** in `data/config.yaml` by ID
4. **Get content** based on source type (see Source Access below)
5. **Answer** with citation to source and file path

## Path Format

Index entries use the format: `{source_id}:{relative_path}`

Examples:
- `ibis:tutorials/basics.qmd` - Git source
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

If you're working in a project that uses Ibis but doesn't know about this corpus, you can add awareness to the project's CLAUDE.md.

**The `data/project-awareness.md` file** contains a ready-to-use snippet that can be added to any project's CLAUDE.md to make Claude aware of this corpus when working in that project.

### How to Inject

1. Read `data/project-awareness.md` from this corpus
2. Add its contents to the target project's CLAUDE.md (create if needed)
3. The project will now know to use this corpus for Ibis questions

### When to Suggest Injection

Suggest adding project awareness when:
- User is working in a project that heavily uses Ibis
- User repeatedly asks Ibis questions without invoking the corpus
- User says "I keep forgetting to use the docs"

Example suggestion:
> "I notice this project uses Ibis extensively. Would you like me to add corpus awareness to this project's CLAUDE.md? That way I'll automatically know to check the Ibis docs when working here."
