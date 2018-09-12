import json

from redash_stmo.utils import add_resource

from redash.models import DataSource
from redash.handlers.base import BaseResource, get_object_or_404
from redash.permissions import require_access, view_only


DATASOURCE_VERSION_PARSE_INFO = {
    "pg": {
        "version_query": "select version()",
        "delimiter": " ",
        "index": 1
    },
    "redshift": {
        "version_query": "select version()",
        "delimiter": " ",
        "index": -1
    },
    "mysql": {
        "version_query": "select version()",
        "delimiter": "",
        "index": 0
    }
}

class DataSourceVersionResource(BaseResource):
    def get(self, data_source_id):
        data_source = get_object_or_404(
            DataSource.get_by_id_and_org,
            data_source_id,
            self.current_org
        )
        require_access(data_source.groups, self.current_user, view_only)
        try:
            version_info = get_data_source_version(data_source.query_runner)
        except Exception as e:
            return {"message": unicode(e), "ok": False}
        else:
            return {"message": version_info, "ok": True}

def get_data_source_version(query_runner):
    if query_runner.type() not in DATASOURCE_VERSION_PARSE_INFO:
        raise NotImplementedError

    parse_info = DATASOURCE_VERSION_PARSE_INFO[query_runner.type()]
    data, error = query_runner.run_query(parse_info["version_query"], None)
    if error is not None:
        raise Exception(error)
    try:
        version = json.loads(data)['rows'][0]['version']
    except KeyError as e:
        raise Exception(e)

    version = version.split(parse_info["delimiter"])[parse_info["index"]]
    return version

def datasource_version(app=None):
    add_resource(DataSourceVersionResource, '/api/data_sources/<data_source_id>/version')
