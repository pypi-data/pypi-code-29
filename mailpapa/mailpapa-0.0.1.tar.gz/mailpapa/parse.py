from .compatible import BeautifulSoup
from .models import Email, MailpapaException, Response
from .utils import random_user_agent, simulate_email


def parse_linkedin(html, domain, pattern):

    soup = BeautifulSoup(html, features="html.parser")
    names = soup.findAll("a", {"class": "professional__name"})
    positions = soup.findAll("p", {"class": "professional__headline"})
    names_positions = zip(names, positions)

    results = []

    for name, position in names_positions:
        name = name.getText().replace("\n", " ").title()

        # Some name appear to have multispaces strip multispace to onespace
        # Eg "JOHN    DOE     CON" to "JOHN DOE CON"
        name = " ".join(name.split())

        # Avoid accounts with blank profession
        pos = position.getText()
        if pos == "":
            continue

        # Avoid accounts with ambiguous profession eg "JOHN DOE -> CEO"
        # We really want "JOHN DOE -> CEO AT CONTOSO"
        if len(pos.split()) == 1:
            continue

        address = f"{simulate_email(name, pattern)}@{domain}"
        results.append(Email(name=name, position=pos, address=address))
    return results
