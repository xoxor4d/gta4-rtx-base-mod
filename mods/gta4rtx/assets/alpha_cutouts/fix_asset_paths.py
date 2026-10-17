from pathlib import Path

WRONG = b"@../../_git_gta4-rtx-base-mod/mods/gta4rtx/deps/"
RIGHT = b"@../../deps/"


def main():
    folder = Path(__file__).resolve().parent
    fixed = 0
    for path in sorted(folder.glob("*.usda")):
        data = path.read_bytes()
        count = data.count(WRONG)
        if count:
            path.write_bytes(data.replace(WRONG, RIGHT))
            print(f"{path.name}: {count} path(s) fixed")
            fixed += 1
    print(f"done, {fixed} file(s) changed")


if __name__ == "__main__":
    main()
