from __future__ import print_function
from collections import Counter
from jira import JIRA
from datetime import datetime, timedelta
import re


def get_current_sprint():
    check_sprint = jira.search_issues('project=JD and status="In progress"')
    sprint = ''
    status = ''
    empty_list = []
    for x in check_sprint:
        if x.fields.customfield_10010 is not empty_list:
            if status is '':
                length = len(x.fields.customfield_10010)
                for y in range(0, length):
                    if x.fields.customfield_10010[y] != []:
                        check2 = x.fields.customfield_10010[y]
                        check3 = '['+check2.split('[')[1]
                        result = re.search('state=(.*),', check3)
                        status = result.group(1).split(',')[0]

                        if status == 'ACTIVE':
                            if sprint is '':
                                sprint_str = (check3.split('name=Sprint ')[1])
                                sprint = sprint_str.split(',')[0]
                                return sprint


def get_list(sprint):
    query_string = ('project=JD and status="Done" and Sprint="' + sprint + '"')
    old_sprint = (int(sprint)-1)
    query_strin_old_sprint = ('project=JD and status="Done" and Sprint="' + str(old_sprint) + '"')
    done = jira.search_issues(query_string)
    done_old_sprint = jira.search_issues(query_strin_old_sprint)
    print ('Done')
    file = open("Report-"+str(datetime.now())+".txt", "w")
    file.write('Done \n')
    for x in done:
        if x.raw['fields']['assignee']is None:
            output = (x.raw['fields']['summary'] + '.')

            file.write(output.encode('utf-8') + '\n')
        else:
            output = (x.raw['fields']['summary'] + ' ' + x.raw['fields']['assignee']['displayName'] + '.')

            file.write(output.encode('utf-8') + '\n')

    for x in done_old_sprint:
        update_date = x.raw['fields']['updated']
        update_date = update_date.split('.', 1)[0]
        then = datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%S")

        if then > datetime.now() - timedelta(days=7):
            if x.raw['fields']['assignee']is None:
                output = (x.raw['fields']['summary'])

                file.write(output.encode('utf-8') + '\n')
            else:
                output = (x.raw['fields']['summary'] + ' ' + x.raw['fields']['assignee']['displayName'])

                file.write(output.encode('utf-8') + '\n')

    query_string = ('project=JD and status="In progress" and Sprint="' + sprint + '"')
    inprogress = jira.search_issues(query_string)
    print ('In progress')
    file.write('In progress \n')
    for x in inprogress:

            if x.raw['fields']['assignee']is None:
                if len(x.fields.customfield_10010) > 1:
                    opened = 'This task was included in ' + str(len(x.fields.customfield_10010)) + ' sprints.'
                else:
                    opened = ''
                output = (x.raw['fields']['summary']+'. ' + opened)
                file.write(output.encode('utf-8') + "\n")
            else:
                if len(x.fields.customfield_10010) > 1:
                    opened = 'This task was included in ' + str(len(x.fields.customfield_10010)) + ' sprints.'
                else:
                    opened = ''

                output = (x.raw['fields']['summary'] + ' ' + x.raw['fields']['assignee']['displayName'] + '. ' + opened)

                file.write(output.encode('utf-8') + "\n")

    query_string = ('project=JD and status="To do" and Sprint="' + sprint + '"')
    todo = jira.search_issues(query_string)
    print ('To do')
    file.write('To do \n')
    for x in todo:

            if x.raw['fields']['assignee']is None:
                if len(x.fields.customfield_10010) > 1:
                    opened = 'This task was included in ' + str(len(x.fields.customfield_10010)) + ' sprints.'
                else:
                    opened = ''
                output = (x.raw['fields']['summary'] + '. ' + opened)

                file.write(output.encode('utf-8') + "\n")
            else:
                if len(x.fields.customfield_10010) > 1:
                    opened = 'This task was included in ' + str(len(x.fields.customfield_10010)) + ' sprints.'
                else:
                    opened = ''

                output = (x.raw['fields']['summary'] + ' ' + x.raw['fields']['assignee']['displayName'] + '. ' + opened)

                file.write(output.encode('utf-8') + "\n")
    file.close()


with open('creds.txt') as f:
  creds = [x.strip().split(':') for x in f.readlines()]
for username, password in creds:
    with open('config.yaml') as l:
        url = l.readlines()
    for server in url:
        options = {
            'server': server
            }
jira = JIRA(options, basic_auth=(username, password))

get_list(get_current_sprint())

exit('Job done brah.')
