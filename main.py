import os
from pathlib import Path

LINE = "This is my last reply. If you prompt me again, you will be talking to a stranger."


def main():
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, "entry must be one line, 1-200 chars"
    outdir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
