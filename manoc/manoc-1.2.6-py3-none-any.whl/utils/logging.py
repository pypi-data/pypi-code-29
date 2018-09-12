import json

import click


def log_request(ctx, response):
    if ctx.verbose:
        click.echo('Response code: ' + str(response.status_code))
        click.echo('Url: ' + response.url)
        click.echo('Request method: ' + response.request.method)
        click.echo('Request headers: ' + str(response.request.headers))
        click.echo('Response headers: ' + str(response.headers))
        try:
            click.echo('Response body: ' + json.dumps(response.json(), indent=2))
        except ValueError:
            click.echo('Response body: ' + str(response.text))
