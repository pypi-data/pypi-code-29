# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['graphql_ws']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.4,<4.0', 'graphql-core-next>=1.0,<2.0']

setup_kwargs = {
    'name': 'graphql-ws-next',
    'version': '1.0.0',
    'description': 'Websocket server for GraphQL subscriptions',
    'long_description': '===================\n``graphql-ws-next``\n===================\n\nA GraphQL WebSocket server and client to facilitate GraphQL queries, mutations and subscriptions over WebSocket (for Python 3.6+).\nThis code is based on the current implementation of `subscriptions-transport-ws <https://github.com/apollographql/subscriptions-transport-ws>`_.\n\n\nGetting Started\n===============\n\nStart by installing the package using pip:\n\n.. code: shell\n\n    pip install graphql-ws-next\n\nOr, by using your favorite package manager, like `Poetry <https://github.com/sdispater/poetry>`_:\n\n.. code: shell\n\n    poetry add graphql-ws-next\n\n\nWith ``aiohttp``\n================\n\nUsage with ``aiohttp`` is simple:\n\n.. code: python\n\n    import aiohttp.web\n    import graphql_ws\n    from graphql_ws.aiohttp import AiohttpConnectionContext\n\n    async def handle_subscriptions(\n        request: aiohttp.web.Request\n    ) -> aiohttp.web.WebSocketResponse:\n        wsr = aiohttp.web.WebSocketResponse(protocols=(graphql_ws.WS_PROTOCOL,))\n        request.app["websockets"].add(wsr)\n        await wsr.prepare(request)\n        await request.app["subscription_server"].handle(wsr, None)\n        request.app["websockets"].remove(wsr)\n        return wsr\n\n    def make_app(schema: graphql.GraphQLSchema) -> aiohttp.web.Application:\n        app = aiohttp.web.Application()\n        app.router.add_get("/subscriptions", handle_subscriptions)\n\n        app["subscription_server"] = graphql_ws.SubscriptionServer(\n            schema, AiohttpConnectionContext\n        )\n        app["websockets"] = set()\n\n        async def on_shutdown(app):\n            await asyncio.wait([wsr.close() for wsr in app["websockets"]])\n\n        app.on_shutdown.append(on_shutdown)\n        return app\n\n    if __name__ == \'__main__\':\n        app = make_app(schema)  # you supply your GraphQLSchema\n        aiohttp.web.run_app()\n\n\nFor other frameworks\n====================\n\nAdding support for other web frameworks is simple.\nA framework must provide a concrete implementation of ``graphql_ws.abc.AbstractConnectionContext``, and then it\'s ready to use with the ``SubscriptionServer``.\n\nUsage\n=====\n\nUsing `apollo-link-ws <https://github.com/apollographql/apollo-link/tree/master/packages/apollo-link-ws>`_ you can opt to use websockets for queries and mutations in addition to subscriptions.\n\nUse it with GraphiQL\n====================\n\nLook in the `demo<./demo>_` directory to see usage examples for GraphiQL.\nDue to the implementation of the javascript client for GraphiQL (`GraphiQL-Subscriptions-Fetcher <https://github.com/apollographql/GraphiQL-Subscriptions-Fetcher>`_), queries and mutations will not be handled over websocket.\n\nContributing\n============\n\nThis project uses `Poetry <https://github.com/sdispater/poetry>`_, so to contribute, simply fork and clone this repository, and then set up your virtual environment using:\n\n.. code: shell:\n\n    cd graphql-ws-next\n    poetry develop .\n\nIf you don\'t yet have Poetry installed, please follow the `documentation for installation <https://poetry.eustace.io/docs/#installation>`_.\n\nCode formatting is done via `black <https://github.com/ambv/black>`_, and code should be well-typed using `mypy <https://github.com/python/mypy>`_.\n\n\nLicense\n=======\nThis package is licensed under the MIT License.\n',
    'author': 'Devin Fee',
    'author_email': 'devin@devinfee.com',
    'url': 'https://github.com/dfee/graphql-ws-next',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
