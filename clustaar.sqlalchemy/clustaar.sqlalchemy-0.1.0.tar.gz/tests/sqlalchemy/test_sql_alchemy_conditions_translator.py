import pytest

from clustaar.sqlalchemy.sql_alchemy_conditions_translator import SQLAlchemyConditionsTranslator
from tests.fixtures.tables import Subscription


@pytest.fixture
def translator():
    return SQLAlchemyConditionsTranslator(model=Subscription)


class TestMapConditions():
    def test_returns_equals_conditions(self, translator):
        conditions = translator.map_conditions({"user_id": 1})
        assert str(conditions[0]) == str(Subscription.user_id == 1)

    def test_returns_ilike_conditions(self, translator):
        conditions = translator.map_conditions({"user_id": {"contains": "clu"}})
        assert str(conditions[0]) == str(Subscription.user_id.ilike("%clu%"))

    def test_returns_in_conditions(self, translator):
        conditions = translator.map_conditions({"user_id": [1]})
        assert str(conditions[0]) == str(Subscription.user_id.in_([1]))

    def test_returns_in_conditions_for_set(self, translator):
        conditions = translator.map_conditions({"user_id": {1}})
        assert str(conditions[0]) == str(Subscription.user_id.in_([1]))

    def test_returns_lower_or_equal_than_condition(self, translator):
        conditions = translator.map_conditions({"user_id": {"<=": 12}})
        assert str(conditions[0]) == str(Subscription.user_id <= 12)

    def test_returns_lower_than_condition(self, translator):
        conditions = translator.map_conditions({"user_id": {"<": 12}})
        assert str(conditions[0]) == str(Subscription.user_id < 12)

    def test_returns_greater_or_equal_than_condition(self, translator):
        conditions = translator.map_conditions({"user_id": {">=": 12}})
        assert str(conditions[0]) == str(Subscription.user_id >= 12)

    def test_returns_greater_than_condition(self, translator):
        conditions = translator.map_conditions({"user_id": {">": 12}})
        assert str(conditions[0]) == str(Subscription.user_id > 12)

    def test_returns_not_equal_to_condition(self, translator):
        conditions = translator.map_conditions({"user_id": {"!=": 1}})
        assert str(conditions[0]) == str(Subscription.user_id != 1)
