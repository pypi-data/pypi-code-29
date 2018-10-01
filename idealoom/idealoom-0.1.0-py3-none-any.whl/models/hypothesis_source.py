from builtins import object
from datetime import datetime
import logging

from sqlalchemy import (
    Column, ForeignKey, Integer, DateTime, Table,
    UniqueConstraint, Unicode, String, Boolean,
    CheckConstraint, event, Index)
from sqlalchemy.orm import relationship
from future.utils import string_types
import simplejson as json
from rdflib_jsonld.context import Context
from pyramid.threadlocal import get_current_registry

from . import DiscussionBoundBase, Base
from .generic import ContentSource
from ..lib.sqla import get_named_class, get_named_object
from ..lib.generic_pointer import (
    UniversalTableRefColType, generic_relationship)
from ..lib.utils import get_global_base_url
from ..semantic import jsonld_context
from ..tests.utils import PyramidWebTestRequest
from .idea_content_link import Extract


log = logging.getLogger(__name__)


class ExtractSource(ContentSource):
    __tablename__ = 'abstract_extract_source'
    id = Column(Integer, ForeignKey(ContentSource.id), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'abstract_extract_source',
    }


class ImportedExtract(Extract):
    __tablename__ = 'extract_source'
    id = Column(Integer, ForeignKey(Extract.id), primary_key=True)
    import_source = Column(Integer, ForeignKey(ExtractSource.id))
    id_for_source = Column(String)
    access_url = Column()
    # unique for both


class HypothesisExtractSource(ExtractSource):
    __tablename__ = 'hypothesis_extract_source'
    id = Column(Integer, ForeignKey(ExtractSource.id), primary_key=True)
    api_key = Column(String)
    # search criteria
    user = Column(String)
    group = Column(String)
    tag = Column(Unicode)
    uri = Column(Unicode)
