import os
import json
import hashlib
from datetime import datetime
from collections import defaultdict

ROOT = r"E:\football_v"
OUTPUT = os.path.join(
    ROOT,
    "reports",
    "CODE_LOGIC_DUPLICATE_AUDIT_V1.0.json"
)

SCAN_EXT = {
    ".py",
    ".js",
    ".ps1",
    ".yaml",
    ".yml"
}

IGNORE_DIR = {
    "reports",
    "FINAL_RELEASE_REPORT",
    "99_DOCUMENTATION",
    "__pycache__",
    ".git"
}


def collect_files():

    files = []

    for root, dirs, names in os.walk(ROOT):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIR
        ]

        for name in names:

            ext = os.path.splitext(name)[1].lower()

            if ext in SCAN_EXT:

                files.append(
                    os.path.join(root, name)
                )

    return files



def normalize_code(content):

    lines = []

    for line in content.splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        lines.append(line)

    return "\n".join(lines)



def hash_content(content):

    return hashlib.md5(
        content.encode(
            "utf-8",
            errors="ignore"
        )
    ).hexdigest()



def scan_duplicate_logic():

    result = defaultdict(list)

    files = collect_files()

    for file in files:

        try:

            with open(
                file,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                data = f.read()


            normalized = normalize_code(data)

            if len(normalized) < 80:
                continue


            h = hash_content(normalized)

            result[h].append(file)


        except Exception:
            pass


    duplicates = []

    for h, paths in result.items():

        if len(paths) > 1:

            duplicates.append({

                "hash": h,

                "files": paths,

                "risk": "MEDIUM",

                "action": "REVIEW"

            })


    return duplicates



def main():

    duplicates = scan_duplicate_logic()

    report = {

        "version":
        "CODE_LOGIC_DUPLICATE_AUDIT_V1.0",

        "time":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "scan_root":
        ROOT,

        "summary":

        {

            "duplicate_groups":
            len(duplicates)

        },

        "duplicate_groups":
        duplicates,

        "delete_candidates":
        [],

        "merge_candidates":
        []

    }


    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )


    print("="*50)
    print("Football AI OS Code Logic Duplicate Scanner")
    print("="*50)
    print("扫描文件:", len(collect_files()))
    print("重复组:", len(duplicates))
    print("报告:")
    print(OUTPUT)
    print("="*50)



if __name__ == "__main__":

    main()

