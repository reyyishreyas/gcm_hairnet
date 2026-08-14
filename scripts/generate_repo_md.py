#!/usr/bin/env python3
"""Regenerate REPOSITORY_CODE.md from actual source files."""

import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MD_FILE = REPO_ROOT / "REPOSITORY_CODE.md"

EXCLUDE_DIRS = {
    ".git", "__pycache__", "venv", ".pytest_cache",
    "gcm_hairnet.egg-info", "node_modules",
}

def extract_purpose(content: str, filename: str) -> str:
    """Extract a purpose description from file content."""
    lines = content.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("class "):
            class_name = stripped.split("(")[0].replace("class ", "").strip()
            return f"Defines `{class_name}` module/class."
        if stripped.startswith("def "):
            func_name = stripped.split("(")[0].replace("def ", "").strip()
            return f"Contains `{func_name}` function."
        if stripped.startswith('"""') or stripped.startswith("'''"):
            docstring = stripped.strip('"""').strip("'''").strip()
            if docstring:
                return docstring.split("\n")[0][:100]
    return f"Implementation of `{filename}`."

def generate_md() -> str:
    md_parts = []
    md_parts.append("# GCM-HAIRNet Repository Code\n")
    md_parts.append("Complete repository source code organized by module, with file descriptions and full implementations.\n")
    md_parts.append("---\n")

    py_files = sorted(REPO_ROOT.rglob("*.py"))

    for py_file in py_files:
        rel_path = py_file.relative_to(REPO_ROOT)
        parts = rel_path.parts

        if any(excl in parts for excl in EXCLUDE_DIRS):
            continue

        content = py_file.read_text(encoding="utf-8")
        purpose = extract_purpose(content, rel_path.name)

        md_parts.append(f"### `{rel_path}`\n")
        md_parts.append(f"**Purpose:** {purpose}\n")
        md_parts.append("```python")
        md_parts.append(content.rstrip())
        md_parts.append("```\n")
        md_parts.append("---\n")

    return "\n".join(md_parts)

if __name__ == "__main__":
    md_content = generate_md()
    MD_FILE.write_text(md_content, encoding="utf-8")
    print(f"Generated {MD_FILE} with content from {len(md_content.split('### `')) - 1} files.")
