"""Copy theme.css and manifest.json into a vault: <vault>/.obsidian/themes/Suzuri/

usage: python scripts/install.py <vault folder>
Obsidian reloads the theme without a restart.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    vault = Path(sys.argv[1])
    if not (vault / ".obsidian").is_dir():
        raise SystemExit(f"not an Obsidian vault (no .obsidian folder): {vault}")
    dest = vault / ".obsidian" / "themes" / "Suzuri"
    dest.mkdir(parents=True, exist_ok=True)
    for name in ("theme.css", "manifest.json"):
        shutil.copy2(ROOT / name, dest / name)
    print(f"installed to {dest}")


if __name__ == "__main__":
    main()
