from pathlib import Path
import time


def get_setting_path() -> Path:
    global_path = Path("/etc/dashbase/")
    user_path = Path("~/.dashbase/").expanduser()
    if global_path.exists():
        return global_path

    if not user_path.exists():
        user_path.mkdir(exist_ok=True)

    return user_path


def convert_millsecond(mills) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S.{}%z".format(mills % 1000), time.localtime(mills / 1000))
