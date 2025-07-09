import shutil

# Reference: https://docs.python.org/3/library/shutil.html
def copy_entire_directory(src, dest):
    shutil.copytree(src, dest, dirs_exist_ok=True)

# Converts time string in 'HH:MM' format into total minutes since ICU admission.
def convert_time_minutes(t):
    hours, minutes = map(int, t.split(':'))
    return hours * 60 + minutes
