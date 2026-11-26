"""The Printer Apology (make.fun bounty u-eager-stork-81-9647-the-printer-apology-60229153).

Writes one short apology note from an office printer to /output/entry.txt.
Gate: UTF-8 text, 1-120 characters, not only whitespace, no trailing newline.
"""

LINE = "Sorry I choked on a staple. Nobody told me the agenda was armed, and now I rattle when I breathe."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
