from hypothesis import given
from hypothesis.strategies import from_regex
from uribuilder.builder import UriBuilder

SCHEMA = r"\A[a-zA-Z][a-zA-Z0-9+.-]*\Z"
UNRESERVED = "[a-zA-Z0-9._~-]"
PCT_ENCODED = "%[a-fA-F0-9]{2}"
SUB_DELIMS = "[!$&'()*+,;=]"
HOST = r"\A(?:{unreserved}|{pct_encoded}|{sub_delims})*\Z".format(unreserved=UNRESERVED,
                                                                  pct_encoded=PCT_ENCODED,
                                                                  sub_delims=SUB_DELIMS)

PCHAR = "(?:{unreserved}|{pct_encoded}|{sub_delims}|[:@])".format(unreserved=UNRESERVED,
                                                                  pct_encoded=PCT_ENCODED,
                                                                  sub_delims=SUB_DELIMS)
SEGMENT = "{pchar}*".format(pchar=PCHAR)
SEGMENT_NZ = "{pchar}+".format(pchar=PCHAR)
PATH_ABEMPTY = "((?:/{segment})*)".format(segment=SEGMENT)
PATH_ABSOLUTE = "(/(?:{segment_nz}(?:/{segment})*)?)".format(segment=SEGMENT,
                                                             segment_nz=SEGMENT_NZ)
PATH_ROOTLESS = "({segment_nz}(?:/{segment})*)".format(segment=SEGMENT,
                                                       segment_nz=SEGMENT_NZ)
PATH_EMPTY = "()"

HIER_PART = "\A(?:{path_abempty}|{path_absolute}|{path_rootless}|{path_empty})\Z".format(path_abempty=PATH_ABEMPTY,
                                                                                         path_absolute=PATH_ABSOLUTE,
                                                                                         path_rootless=PATH_ROOTLESS,
                                                                                         path_empty=PATH_EMPTY)

FRAGMENT = "\A((?:{pchar}|[/?])*)\Z".format(pchar=PCHAR)
QUERY = "\A((?:{pchar}|[/?])*)\Z".format(pchar=PCHAR)


@given(from_regex(SCHEMA), from_regex(HOST), from_regex(HIER_PART), from_regex(QUERY), from_regex(FRAGMENT))
def test_some_stuff(schema, host, path, query, fragment):
    uri = UriBuilder().schema(schema).netloc(host).path(path).fragment(fragment).build()
    print(uri)
