#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.

date_pattern = re.compile(r"""^(.*?) # all text before the date
                          ((0|1)?\d)-         # one or two digits for the month
                          ((0|1|2|3)?\d)-     # one or two digits for the day
                          ((19|20)\d\d)       # four digits for the year
                          (.*?)$              # all text after the date
                          """, re.VERBOSE)
# Loop over the files in the working directory.
for us_filename in os.listdir('.'):
    match = date_pattern.search(us_filename)

    # Skip files without a date.
    if match is None:
        continue

    # Get the different parts of the filename.
    before_part = match.group(1)
    month_part = match.group(2)
    day_part = match.group(4)
    year_part = match.group(6)
    after_part = match.group(8)

    # Form the European-style filename.
    eu_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    us_filename = os.path.join(abs_working_dir, us_filename)
    eu_filename = os.path.join(abs_working_dir, eu_filename)

    # Rename the files.
    print('Renaming "%s" to "%s"' % (us_filename, eu_filename))
    # shutil.move(us_filename, eu_filename) # only uncomment after testing
