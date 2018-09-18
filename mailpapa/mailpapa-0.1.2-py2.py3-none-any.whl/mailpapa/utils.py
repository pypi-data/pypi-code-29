import random
import warnings

from .structures import DictValue

user_agents = [
    # Windows 10-based PC using Edge browser
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    # Chrome OS-based laptop using Chrome browser (Chromebook)
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    # Mac OS X-based computer using a Safari browser
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    # Linux-based PC using a Firefox browser
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    # Windows 7-based PC using a Chrome browser
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
]


def random_user_agent() -> dict:
    return {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }


ACCEPTED_PATTERNS = DictValue(
    {
        "LAST": "last",
        "FIRST": "first",
        "FIRST_LAST": "first_last",
        "LAST_FIRST": "last_first",
        "FIRSTDOTLAST": "first.last",
        "LASTDOTFIRST": "last.first",
        "FIRSTLAST": "firstlast",
        "LASTFIRST": "lastfirst",
        "FLAST": "flast",
        "LFIRST": "lfirst",
        "FIRSTL": "firstl",
        "LASTF": "lastf",
    }
)


def simulate_email(name: str, pattern: str) -> str:
    """Simulate emails based on company email pattern."""

    # TODO: Stinky function needs refactor sort of

    name = name.strip()
    name = name.split()

    # Strip off Special Characters
    # name = [re.sub('[^a-zA-Z0-9]+', '', n) for n in name]

    first, last = name[:2]

    if ACCEPTED_PATTERNS.FIRST == pattern:
        return f"{first}"
    elif ACCEPTED_PATTERNS.LAST == pattern:
        return f"{last}"

    elif ACCEPTED_PATTERNS.FIRST_LAST == pattern:
        return f"{first}_{last}"

    elif ACCEPTED_PATTERNS.LAST_FIRST == pattern:
        return f"{last}_{first}"

    elif ACCEPTED_PATTERNS.FIRSTDOTLAST == pattern:
        return f"{first}.{last}"

    elif ACCEPTED_PATTERNS.LASTDOTFIRST == pattern:
        return f"{last}.{first}"

    elif ACCEPTED_PATTERNS.FIRSTLAST == pattern:
        return f"{first}{last}"

    elif ACCEPTED_PATTERNS.LASTFIRST == pattern:
        return f"{last}{first}"

    elif ACCEPTED_PATTERNS.FLAST == pattern:
        return f"{first[0]}{last}"

    elif ACCEPTED_PATTERNS.LFIRST == pattern:
        return f"{last[0]}.{first}"

    elif ACCEPTED_PATTERNS.FIRSTL == pattern:
        return f"{first}{last[0]}"

    elif ACCEPTED_PATTERNS.LASTF == pattern:
        return f"{last}.{first[0]}"

    else:
        warnings.warn("No pattern was provided. Defaults to {first}.{last}pattern. ")
        return f"{first}.{last}"


def get_domain(url):
    url = url.split("://")
    index = (0, 1)[len(url) > 1]
    domain = url[index].split("?")[0].split("/")[0].split(":")[0].lower()
    return domain
