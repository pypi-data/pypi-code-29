import datetime


class UniverseByStrategyModel:
    def __init__(self, strategy: str=None, entity_ids: []=None, active_date: datetime = datetime.date(9999, 12, 31), parent_entity_id: int=None):
        self._entity_ids = []
        self._entity_ids = entity_ids
        self._strategy = strategy
        self._active_date = active_date
        self._parent_entity_id = parent_entity_id
