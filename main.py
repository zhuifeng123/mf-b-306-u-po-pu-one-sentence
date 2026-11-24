from pathlib import Path

ENTRY = (
    "Imagine a vast invisible library where every book, letter, and picture ever "
    "written can be fetched in a blink by a wire that carries voices and images "
    "across the world."
)


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
