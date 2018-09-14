from typing import NamedTuple, Optional, Any, Dict

from bson import ObjectId


class Save(NamedTuple):
    op: str = 'save'
    id: Optional[ObjectId] = None


class Insert(NamedTuple):
    op: str = 'insert'
    id: Optional[ObjectId] = None


class UpdateOne(NamedTuple):
    update_data: Dict[str, Any]
    op: str = 'update_one'


class DeleteOne(NamedTuple):
    op: str = 'delete_one'


class Reload(NamedTuple):
    op: str = 'reload'


class SetField(NamedTuple):
    name: str
    value: Any
    op: str = 'set_field'


class ChangeChind(NamedTuple):
    path: str
    name: str
    log_item: NamedTuple
    op: str = 'change_chind'
