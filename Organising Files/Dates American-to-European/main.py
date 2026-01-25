import os
import re
import shutil


def rename_dates():
    date_pattern = re.compile(
        r"""
        ^(.*?)
        ((0|1)\d)-
        ((0|1|2|3)\d)-
        ((19|20)\d\d)
        (.*?)$
        """,
        re.VERBOSE,
    )

    for foldername, subfolders, filenames in os.walk("."):
        for filename in filenames:
            match = date_pattern.search(filename)

            if match is None:
                continue

            before_part = match.group(1)
            month_part = match.group(2)
            day_part = match.group(4)
            year_part = match.group(6)
            after_part = match.group(8)

            euro_filename = (
                f"{before_part}{day_part}-{month_part}-{year_part}{after_part}"
            )

            abs_working_dir = os.path.abspath(foldername)
            old_path = os.path.join(abs_working_dir, filename)
            new_path = os.path.join(abs_working_dir, euro_filename)

            print(f'Renaming "{filename}" to "{euro_filename}"...')
            shutil.move(old_path, new_path)


if __name__ == "__main__":
    rename_dates()
