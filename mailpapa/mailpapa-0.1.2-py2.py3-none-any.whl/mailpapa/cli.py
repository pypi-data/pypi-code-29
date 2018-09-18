import argparse
import sys
import mailpapa
from tabulate import tabulate

def main(**kwargs):
  parser = argparse.ArgumentParser(description='Search for Emails in the Wild')
  parser.add_argument('company', help="Company name")
  parser.add_argument('domain', help="Company domain")
  parser.add_argument('-p', '--pattern', help="Email Pattern", default=mailpapa.ACCEPTED_PATTERNS.FIRSTDOTLAST)
  parser.add_argument('-r', '--role', default="ceo", help="Employee Positions")
  output = parser.add_argument_group(title="Save Options")
  output.add_argument('-j', '--json', metavar='file', help="Save emails in a JSON file in the given location.")

  args = parser.parse_args()
  
  company = args.company
  domain = args.domain
  pattern = args.pattern
  positions = args.role
  jsonfile = args.json

  response = mailpapa.search(company, domain, pattern, positions)
  if not response.ok:
    sys.exit("Failed to fetch emails")
  
  if jsonfile is not None:
    response.save(jsonfile)
    sys.exit(0)
  
  table = []
  emails = response.emails
  for email in emails:
    table.append([email.name, email.address])
  sys.exit(0)


if __name__ == "__main__":
  main()
