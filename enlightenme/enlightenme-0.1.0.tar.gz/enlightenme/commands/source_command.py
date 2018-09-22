import click

from enlightenme.news import news_manager, news_output
from enlightenme.sources import Source


class SourceCommand(click.Group):
    help = "helps getting latest news from specified sources"

    def list_commands(self, ctx):
        return [name for name in Source.get_all_sources()]

    def get_command(self, ctx: click.Context, cmd_name):
        if cmd_name not in self.list_commands(ctx):
            ctx.fail("Invalid source %s supplied. See --help" % cmd_name)

        @click.pass_context
        def callback(cmd_ctx: click.Context, *args, **kwargs):
            keywords = ctx.params.get('keywords', "")
            format_type = ctx.params.get('format')
            output = ctx.params.get('output')

            keywords = keywords.split(",") if keywords else None

            news_fetchers = news_manager.NewsManager(
                cmd_name,
                source_params=cmd_ctx.params,
                format_type=format_type,
                keywords=keywords)

            click.echo("Fetching news from source: %s" % cmd_name)
            content = news_fetchers.fetch_and_format()
            news_output.NewsOutput(content).write_to(file_name=output)

        source_class = Source.get_source(cmd_name)
        return click.Command(name=cmd_name,
                             callback=callback,
                             params=source_class.params(),
                             help=source_class.HELP,
                             short_help=source_class.HELP)
