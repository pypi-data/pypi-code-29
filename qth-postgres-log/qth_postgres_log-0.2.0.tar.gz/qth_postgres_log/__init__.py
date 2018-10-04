import asyncio
import asyncpg
import qth
import argparse
import getpass
import json
import datetime

from aiohttp import web

from .version import __version__

async def init_tables(loop, pg_client):
    """Create all required database tables/functions."""
    async with pg_client.transaction():
        await pg_client.execute("""
            CREATE TABLE IF NOT EXISTS qth_paths(
                path_id SERIAL PRIMARY KEY,
                path TEXT NOT NULL UNIQUE
            )
        """)
        await pg_client.execute("""
            CREATE TABLE IF NOT EXISTS qth_log(
                log_id SERIAL PRIMARY KEY,
                path_id SERIAL REFERENCES qth_paths,
                value JSONB,
                time TIMESTAMP NOT NULL
            )
        """)
        await pg_client.execute("""
            CREATE OR REPLACE FUNCTION qth_path_to_id(desired_path TEXT) RETURNS INTEGER AS $$
            DECLARE
                id INTEGER;
            BEGIN
                id := (SELECT path_id FROM qth_paths
                       WHERE path = desired_path
                       LIMIT 1);
                IF id IS NULL THEN
                    INSERT INTO qth_paths(path)
                    VALUES (desired_path)
                    RETURNING path_id INTO id;
                END IF;
                RETURN id;
            END;
            $$ LANGUAGE plpgsql
        """)
        await pg_client.execute("""
            CREATE OR REPLACE FUNCTION qth_json_to_double(input jsonb) RETURNS double precision AS $$
            BEGIN
                RETURN CAST(input::text AS double precision);
            EXCEPTION
                WHEN invalid_text_representation THEN
                    RETURN CASE input
                        WHEN NULL THEN 0.0
                        WHEN 'null'::jsonb THEN 0.0
                        WHEN 'false'::jsonb THEN 0.0
                        WHEN '""'::jsonb THEN 0.0
                        WHEN '[]'::jsonb THEN 0.0
                        WHEN '{}'::jsonb THEN 0.0
                        ELSE 1.0
                    END;
            END;
            $$ LANGUAGE plpgsql immutable
        """)


async def connect_to_qth(loop, qth_host, qth_port):
    """
    Connect to Qth. Returns the Qth Client object.
    """
    return qth.Client("qth_postgres_log", loop=loop,
                      host=qth_host, port=qth_port)

async def connect_to_postgres(loop, pg_user, pg_password, pg_database):
    """
    Connect to PostgreSQL and initialise the database if not already done.
    Returns the client object and a lock to hold while using the database.
    """
    pg_client = await asyncpg.connect(
        user=pg_user, password=pg_password,
        database=pg_database)
    
    pg_lock = asyncio.Lock(loop=loop)
    
    await init_tables(loop, pg_client)
    
    return pg_client, pg_lock
    

async def start_logging(qth_client, pg_client, pg_lock):
    """Start logging everything happening in Qth to the PostgreSQL database."""
    async def on_message(topic, data):
        async with pg_lock:
            if data is not qth.Empty:
                data = json.dumps(data)
            else:
                data = None
            await pg_client.execute("""
                INSERT INTO qth_log(path_id, value, time)
                VALUES (qth_path_to_id($1), $2, CURRENT_TIMESTAMP)
            """, topic, data)
    
    await qth_client.subscribe("#", on_message)


async def start_http_api(loop, pg_client, pg_lock,
                         http_host="0.0.0.0", http_port=8090):
    
    """
    Exposes a simple HTTP API for querying the logging database. Returns an
    aiohttp.web.AppRunner on which cleanup() should be called asynchronously to
    shut down the server.
    """
    
    async def query_value(request):
        # Qth Path to fetch
        path = request.query.get("path")
        if "path" is None:
            raise web.HTTPBadRequest(text="Expected 'path' to be in the query string.")
        
        # Limit for number of responses. Set to zero for no limit.
        try:
            limit = int(request.query.get("limit", "100"))
        except ValueError:
            raise web.HTTPBadRequest(text="Expected 'limit' to be an integer.")
        
        # Limit the date range included
        try:
            start = request.query.get("start")
            if start is not None:
                start = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            raise web.HTTPBadRequest(text="Expected 'start' to be a UTC ISO8601-style timestamp with format 'yyyy-mm-ddThh:mm:dd'.")
        try:
            end = request.query.get("end")
            if end is not None:
                end = datetime.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            raise web.HTTPBadRequest(text="Expected 'end' to be a UTC ISO8601-style timestamp with format 'yyyy-mm-ddThh:mm:dd'.")
        
        # Allow selecting part of the value
        try:
            index = request.query.get("index")
            
            # Convert to an array of strings and integers
            if index is not None:
                index = [json.loads(e) for e in index.split(",")]
                index = [e if isinstance(e, str) else int(e) for e in index]
        except ValueError:
            raise web.HTTPBadRequest(text="Expected 'index' to be a comma separated list of numbers and double quoted strings.")
        
        # Order by
        order_by = request.query.get("order", "time").strip().lower()
        if order_by not in ("time", "value", "-time", "-value"):
            raise web.HTTPBadRequest(text="Expected 'order' to be one of 'time', '-time', 'value' or '-value'.")
        if order_by[0] == "-":
            order_by = order_by[1:]
        else:
            order_by = "{} DESC".format(order_by)
        
        # Present summaries per unit time
        group_by = request.query.get("group")
        if group_by is not None:
            group_by = group_by.strip().lower()
            if group_by not in ("minute", "hour", "day", "dow", "week", "month", "quarter", "year"):
                raise web.HTTPBadRequest(text="Expected 'group' to be one of 'minute', 'hour', 'day', 'dow', 'week', 'month', 'quarter', 'year'")
        
        # Present summaries per coarse-grained time window
        window_by = request.query.get("window")
        if window_by is not None:
            window_by = window_by.strip().lower()
            if window_by not in ("minute", "hour", "day", "week", "month", "quarter", "year"):
                raise web.HTTPBadRequest(text="Expected 'window' to be one of 'minute', 'hour', 'day', 'week', 'month', 'quarter', 'year'")
        
        # Aggregation
        aggregate = request.query.get("aggregate", "avg").strip().lower()
        if aggregate not in ("count", "avg", "min", "max"):
            raise web.HTTPBadRequest(text="Expected 'aggregate' to be one of 'count', 'avg', 'min' or 'max'")
        
        # Not null
        try:
            allow_empty = bool(int(request.query.get("empty", "1")))
        except ValueError:
            raise web.HTTPBadRequest(text="Expected 'empty' to be 0 or 1.")
        
        # Over the remainder of the function, an SQL query will be built up
        # with 'args' containing substitution arguments.
        query = ""
        args = []
        
        # Build up a PGSQL JSONB index operator to select the required
        # index into the value.
        index_specifier = ""
        if index:
            for e in index:
                if isinstance(e, str):
                    args.append(e)
                    index_specifier += "->${}".format(len(args))
                else:
                    index_specifier += "->{}".format(e)
        
        # Assemble an expression for the value to fetch, adding appropriate
        # aggregation (and casting to double) if grouping or windowing.
        value_expression = "value{}".format(index_specifier)
        if group_by is not None or window_by is not None:
            value_expression = "({}(qth_json_to_double({})))::text".format(
                aggregate.upper(),
                value_expression
            )
        
        # Assemble an appropriate expression for the time to fetch,
        # rounding or extracting fields according to the group/window
        # options.
        time_expression = "qth_log.time"
        if window_by is not None:
            time_expression = "DATE_TRUNC('{}', {})".format(
                window_by,
                time_expression,
            )
        if group_by is not None:
            time_expression = "EXTRACT({} FROM {})".format(
                group_by.upper(),
                time_expression,
            )
        
        # As above but adds an arbitrary aggregation operator as required
        # when grouping is performed.
        if group_by is not None or window_by is not None:
            time_expression_aggregate = "MIN({})".format(time_expression)
        else:
            time_expression_aggregate = time_expression
        
        # Select log values for the specified path.
        args.append(path)
        query += """
            SELECT {} AS value, {} as time FROM qth_log
            WHERE path_id = qth_path_to_id(${})
        """.format(
            value_expression,
            time_expression_aggregate,
            len(args)
        )
        
        # Filter by start/end time if requested
        if start is not None:
            args.append(start)
            query += """
                AND time >= ${}::TIMESTAMP
            """.format(len(args))
        if end is not None:
            args.append(end)
            query += """
                AND time <= ${}::TIMESTAMP
            """.format(len(args))
        
        # Filter out values which are empty (either because they were deleted
        # or because the specified index doesn't exist).
        if not allow_empty:
            query += """
                AND value{} IS NOT NULL
            """.format(index_specifier)
        
        # Aggregate by time as required.
        if group_by or window_by:
            query += """
                GROUP BY {}
            """.format(time_expression)
        
        # Sort as required
        query += """
            ORDER BY {}
        """.format(order_by)
        
        # Limit number of results as required
        if limit:
            args.append(limit)
            query += """
                LIMIT ${}
            """.format(len(args))
        
        async with pg_lock:
            rows = await pg_client.fetch(query, *args)
        
        # Produce array of {"value": ..., "time": ...} dicts where the value is
        # omitted if empty.
        response = []
        for row in rows:
            row_out = {}
            if row["value"] is not None:
                row_out["value"] = json.loads(row["value"])
            if isinstance(row["time"], datetime.datetime):
                row_out["time"] = row["time"].isoformat()
            else:
                row_out["time"] = row["time"]
            response.append(row_out)
        
        return web.json_response(response)
    
    app = web.Application()
    app.add_routes([
        web.get("/value", query_value)
    ])
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, http_host, http_port)
    await site.start()
    
    return runner


async def async_main(loop,
                     qth_host, qth_port,
                     pg_user, pg_password, pg_database,
                     disable_http_api, http_host, http_port, http_api_url):
    qth_client = await connect_to_qth(loop, qth_host, qth_port)
    pg_client, pg_lock = await connect_to_postgres(loop, pg_user, pg_password, pg_database)
    
    if not disable_http_api:
        http_api_runner = await start_http_api(loop, pg_client, pg_lock, http_host, http_port)
        
        # Advertise the HTTP API via Qth
        if http_api_url is None:
            http_api_url = "http://{}:{}/".format(http_host, http_port)
        await qth_client.register("sys/log/api-url", qth.PROPERTY_ONE_TO_MANY,
                                  "URL at which a query API for the Qth logging system is hosted.",
                                  delete_on_unregister=True)
        await qth_client.set_property("sys/log/api-url", http_api_url)
    else:
        http_api_runner = None
    
    await start_logging(qth_client, pg_client, pg_lock)
    
    return qth_client, pg_client, http_api_runner


async def async_shutdown(qth_client, pg_client, http_api_runner):
    if http_api_runner is not None:
        await http_api_runner.cleanup()
    
    await qth_client.close()
    await pg_client.close()


def main():
    parser = argparse.ArgumentParser(
        description="A simple PostgreSQL-based logger for Qth.")
    parser.add_argument("--version", "-V", action="version",
                        version="%(prog)s {}".format(__version__))
    parser.add_argument("--qth-host",
                        default=None,
                        help="The hostname of the MQTT broker.")
    parser.add_argument("--qth-port",
                        default=None, type=int,
                        help="The port number for the MQTT broker.")
    parser.add_argument("--postgres-host", default=None,
                        help="The PostgreSQL server hostname.")
    parser.add_argument("--postgres-user", default=getpass.getuser(),
                        help="The PostgreSQL username.")
    parser.add_argument("--postgres-password", default="",
                        help="The PostgreSQL password.")
    parser.add_argument("--postgres-database", default=getpass.getuser(),
                        help="The PostgreSQL database.")
    parser.add_argument("--disable-http-api", action="store_true", default=False,
                        help="Don't serve the HTTP query API.")
    parser.add_argument("--http-api-host", default="localhost",
                        help="The host to serve the HTTP API from.")
    parser.add_argument("--http-api-port", default=8090,
                        help="The port to serve the HTTP API from (default 8090)")
    parser.add_argument("--http-api-url", default=None,
                        help="The URL to advertise the HTTP API as in the qth property sys/log/api-url")
    args = parser.parse_args()
    
    loop = asyncio.get_event_loop()
    try:
        qth_client, pg_client, http_api_runner = loop.run_until_complete(async_main(
            loop,
            qth_host=args.qth_host,
            qth_port=args.qth_port,
            pg_user=args.postgres_user,
            pg_password=args.postgres_password,
            pg_database=args.postgres_database,
            disable_http_api=args.disable_http_api,
            http_host=args.http_api_host,
            http_port=args.http_api_port,
            http_api_url=args.http_api_url
            ))
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete(async_shutdown(qth_client, pg_client, http_api_runner))


if __name__ == "__main__":
    main()
