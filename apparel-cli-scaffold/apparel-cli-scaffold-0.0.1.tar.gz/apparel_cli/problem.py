import clickclick


def print_problem(error):
    problem = error.response.json()
    clickclick.error('Failed.')
    clickclick.error('Status: {}'.format(problem['status']))
    clickclick.error('Title: {}'.format(problem['title']))
    clickclick.error('Details: {}'.format(problem['detail']))
    clickclick.error('FlowId: {}'.format(problem['flow_id']))
