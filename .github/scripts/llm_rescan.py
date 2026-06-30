#!/usr/bin/env python3
import os
import sys
import yaml
import json
import urllib.request
import urllib.error

def call_gemini(api_key, content):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    prompt = (
        "You are an expert technical documentation indexer.\n"
        "Analyze the following documentation content and return a JSON object with these fields:\n"
        "- title: Clear, concise title of the document\n"
        "- summary: 1-2 sentence description of the content\n"
        "- tags: list of 3-5 search tag strings\n"
        "- keywords: list of significant technical terms, function names, or API identifiers\n"
        "- category: one of [reference, tutorial, guide, api, config, navigation, journal]\n\n"
        f"Content:\n{content[:6000]}"
    )
    
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "responseMimeType": "application/json"
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            text_response = res_data["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(text_response)
    except urllib.error.HTTPError as e:
        print(f"Gemini API Error: {e.read().decode('utf-8')}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Failed to call Gemini API: {e}", file=sys.stderr)
        return None

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Warning: GEMINI_API_KEY is not set. Skipping LLM scanning phase.")
        sys.exit(0)

    # Find all index.yaml files under directories
    for root, dirs, files in os.walk("."):
        if "index.yaml" in files and "config.yaml" in files:
            index_path = os.path.join(root, "index.yaml")
            print(f"Checking index: {index_path}")
            
            with open(index_path, "r") as f:
                index_data = yaml.safe_load(f)
            
            stale_entries = [e for e in index_data.get("entries", []) if e.get("stale") is True]
            if not stale_entries:
                print("No stale entries to process.")
                continue
                
            print(f"Processing {len(stale_entries)} stale entries...")
            
            updated_any = False
            for entry in stale_entries:
                eid = entry["id"]
                source_id = entry["source"]
                rel_path = entry["path"]
                
                # Construct file path locally
                source_file = os.path.join(root, ".source", source_id, rel_path)
                if not os.path.exists(source_file):
                    # Fallback if source folder structure differs
                    source_file = os.path.join(root, ".source", rel_path)
                    
                if not os.path.exists(source_file):
                    print(f"Error: Source file not found: {source_file}")
                    continue
                    
                with open(source_file, "r", errors="replace") as f:
                    content = f.read()
                    
                print(f"Summarizing: {eid}")
                res = call_gemini(api_key, content)
                if res:
                    entry["title"] = res.get("title", entry.get("title"))
                    entry["summary"] = res.get("summary", entry.get("summary"))
                    entry["tags"] = res.get("tags", entry.get("tags"))
                    entry["keywords"] = res.get("keywords", entry.get("keywords"))
                    entry["category"] = res.get("category", entry.get("category"))
                    entry["stale"] = False
                    entry["stale_since"] = None
                    updated_any = True
                else:
                    print(f"Failed to scan entry {eid}, leaving stale.")
                    
            if updated_any:
                with open(index_path, "w") as f:
                    yaml.dump(index_data, f, default_flow_style=False, sort_keys=False)
                print(f"Index updated: {index_path}")
                
                # Render index.md if render-index.sh is present
                render_sh = os.path.join(root, "render-index.sh")
                if os.path.exists(render_sh):
                    print(f"Re-rendering index.md for {root}")
                    os.system(f"bash {render_sh} {index_path}")

if __name__ == "__main__":
    main()
