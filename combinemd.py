#!/usr/bin/env python3
"""
combines all .md files under this directory (recursively) into combined.md

Usage:
    python combinemd.py
"""

from pathlib import Path

OUTPUT_NAME = "combined.md"
SEPARATOR = "\n\n&& && && &&\n\n"


def format_size(num_bytes: int) -> str:
    """Return a human-readable size string."""
    for unit in ["bytes", "KB", "MB", "GB"]:
        if num_bytes < 1024 or unit == "GB":
            return f"{num_bytes:.2f} {unit}" if unit != "bytes" else f"{num_bytes} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.2f} GB"


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    output_path = base_dir / OUTPUT_NAME

    # Find all .md files under base_dir, recursively
    md_files = []
    for path in base_dir.rglob("*.md"):
        # Skip the output file if it already exists so we do not include it
        if path.resolve() == output_path.resolve():
            continue
        if path.is_file():
            md_files.append(path)

    if not md_files:
        print("No .md files found to combine.")
        return

    # Sort for deterministic order
    md_files.sort()

    # Estimate final size
    total_source_bytes = sum(p.stat().st_size for p in md_files)
    separator_bytes = len(SEPARATOR.encode("utf-8")) * max(len(md_files) - 1, 0)
    estimated_total_bytes = total_source_bytes + separator_bytes

    print(f"Found {len(md_files)} .md files under {base_dir}")
    print(f"Estimated combined file size: {format_size(estimated_total_bytes)}")

    # Optional: show output path
    print(f"Output file will be: {output_path}")

    proceed = input("Proceed with combining files? [y/N]: ").strip().lower()
    if proceed != "y":
        print("Aborted. No file written.")
        return

    # Combine files
    with output_path.open("w", encoding="utf-8", newline="") as out_f:
        for idx, path in enumerate(md_files):
            text = path.read_text(encoding="utf-8", errors="ignore")
            out_f.write(text)
            if idx != len(md_files) - 1:
                out_f.write(SEPARATOR)

    print(f"Done. Wrote combined markdown to: {output_path}")
    print(f"Final size: {format_size(output_path.stat().st_size)}")


if __name__ == "__main__":
    main()
