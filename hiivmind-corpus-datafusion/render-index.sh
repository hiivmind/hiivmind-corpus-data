#!/usr/bin/env bash
# render-index.sh — Deterministic index.yaml → index.md renderer
# Multi-source: shows Python bindings first, then core entries by category.
#
# Usage: bash render-index.sh index.yaml
# Requires: yq 4.0+ (mikefarah/yq)

set -euo pipefail

INDEX_YAML="${1:?Usage: render-index.sh <path-to-index.yaml>}"
DIR=$(dirname "$INDEX_YAML")
CONFIG_YAML="${DIR}/config.yaml"

if [ ! -f "$INDEX_YAML" ]; then
  echo "Error: $INDEX_YAML not found" >&2
  exit 1
fi

if [ ! -f "$CONFIG_YAML" ]; then
  echo "Error: $CONFIG_YAML not found (needed for corpus name)" >&2
  exit 1
fi

CORPUS_NAME=$(yq '.corpus.display_name // .corpus.name' "$CONFIG_YAML")
SOURCE_COUNT=$(yq '.sources | length' "$CONFIG_YAML")
ENTRY_COUNT=$(yq '.meta.entry_count' "$INDEX_YAML")
GENERATED_AT=$(yq '.meta.generated_at' "$INDEX_YAML")

OUTPUT="${DIR}/index.md"

render_tsv() {
  while IFS=$'\t' read -r title id summary size grep_hint stale; do
    line="- **${title}** \`${id}\` - ${summary}"
    if [[ "$size" == "large" && -n "$grep_hint" ]]; then
      line+=" ⚡ GREP - \`${grep_hint}\`"
    fi
    if [[ "$stale" == "true" ]]; then
      line+=" ⏳ STALE"
    fi
    echo "$line"
  done
}

{
  echo "# ${CORPUS_NAME} Documentation Index"
  echo ""
  echo "> Sources: ${SOURCE_COUNT} | Entries: ${ENTRY_COUNT} | Generated: ${GENERATED_AT}"
  echo '> Generated from `index.yaml` — do not edit directly'
  echo ""
  echo "---"

  # Python Bindings section first
  echo ""
  echo "## Python Bindings"
  echo ""
  SRC_FILTER="datafusion-python" yq -r '
    .entries
    | map(select(.source == env(SRC_FILTER)))
    | sort_by(.title)
    | .[]
    | [.title, .id, .summary, .size, (.grep_hint // ""), (.stale | tostring)]
    | @tsv
  ' "$INDEX_YAML" | render_tsv

  # Core entries by category
  CATEGORIES=$(SRC_FILTER="datafusion-python" yq -r '
    .entries[] | select(.source != env(SRC_FILTER)) | .category
  ' "$INDEX_YAML" | sort -u)

  for CAT in $CATEGORIES; do
    echo ""
    CAT_HEADING=$(echo "$CAT" | sed 's/\b\(.\)/\u\1/g')
    echo "## ${CAT_HEADING}"
    echo ""

    export CAT_FILTER="$CAT"
    export SRC_FILTER="datafusion-python"
    yq -r '
      .entries
      | map(select(.category == env(CAT_FILTER) and .source != env(SRC_FILTER)))
      | sort_by(.title)
      | .[]
      | [.title, .id, .summary, .size, (.grep_hint // ""), (.stale | tostring)]
      | @tsv
    ' "$INDEX_YAML" | render_tsv
  done

  echo ""
  echo "---"
  echo ""
  echo "*Rendered from index.yaml at ${GENERATED_AT}*"
} > "$OUTPUT"

echo "Rendered ${OUTPUT} (${ENTRY_COUNT} entries)"
