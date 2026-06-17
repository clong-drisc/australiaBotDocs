import os
from pathlib import Path

ROOT = Path(".")
OUTPUT_DIR = ROOT / "combined-docs"

OUTPUT_DIR.mkdir(exist_ok=True)

# 7.5 MB target
MAX_SIZE = 7500 * 1024

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".html",
    ".htm",
    ".json",
    ".js",
    ".css",
    ".xml"
}

EXCLUDED_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    "combined-docs"
}


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"ERROR READING FILE: {e}"


top_level_folders = [
    p for p in ROOT.iterdir()
    if p.is_dir() and p.name not in EXCLUDED_DIRS
]

for folder in top_level_folders:

    part_num = 1

    output_file = OUTPUT_DIR / f"{folder.name}_part{part_num}.md"

    out = open(output_file, "w", encoding="utf-8")

    header = f"# {folder.name}\n\n"
    out.write(header)

    current_size = len(header.encode("utf-8"))

    for current_dir, dirs, files in os.walk(folder):

        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        current_path = Path(current_dir)

        relative_dir = current_path.relative_to(ROOT)

        folder_section = (
            f"\n\n---\n"
            f"\n## Folder: {relative_dir}\n\n"
        )

        section_bytes = len(folder_section.encode("utf-8"))

        if current_size + section_bytes > MAX_SIZE:
            out.close()

            part_num += 1

            output_file = OUTPUT_DIR / f"{folder.name}_part{part_num}.md"

            out = open(output_file, "w", encoding="utf-8")

            current_size = 0

        out.write(folder_section)
        current_size += section_bytes

        for file in sorted(files):

            file_path = current_path / file

            if file_path.suffix.lower() not in TEXT_EXTENSIONS:
                continue

            relative_file = file_path.relative_to(ROOT)

            content = read_file(file_path)

            block = (
                f"\n\n### File: {relative_file}\n\n"
                f"```text\n"
                f"{content[:50000]}\n"
                f"```\n"
            )

            block_bytes = len(block.encode("utf-8"))

            if current_size + block_bytes > MAX_SIZE:

                out.close()

                part_num += 1

                output_file = OUTPUT_DIR / f"{folder.name}_part{part_num}.md"

                out = open(output_file, "w", encoding="utf-8")

                current_size = 0

            out.write(block)
            current_size += block_bytes

    out.close()

    print(f"Generated files for: {folder.name}")

print("\nDone generating split documentation files.")