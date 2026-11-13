#!/usr/bin/env python3
"""make.fun entry program.

Writes the artwork bundled in this repository
("Anak kucing.png") to /output/entry.png.
Standard library only, no network access, and the output bytes are
identical on every run, as the bounty requires.
"""
import os
import pathlib


def main() -> None:
    src = pathlib.Path(__file__).resolve().with_name(
        "Anak kucing.png"
    )
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.png").write_bytes(src.read_bytes())


if __name__ == "__main__":
    main()
