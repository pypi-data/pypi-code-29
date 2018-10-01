import os


def current_module_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def files_in_dir_by_extension(dir: str, extension: str) -> list:
    all_files = os.listdir(dir)
    result = list()
    for curr_file in all_files:
        if os.path.splitext(curr_file)[1][1:] == extension:
            result.append(os.path.join(dir, curr_file))
    return result
