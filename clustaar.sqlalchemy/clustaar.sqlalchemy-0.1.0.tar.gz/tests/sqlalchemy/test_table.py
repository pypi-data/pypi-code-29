import pytest


@pytest.fixture
def table(database):
    return database.subscriptions


class TestInsert():
    def test_save_object(self, table):
        assert table.count() == 0

        table.insert(user_id="1", bot_id="2", type="pape_news")

        assert table.count() == 1
        subscriptions = table.get()
        assert subscriptions[0].user_id == "1"
        assert subscriptions[0].bot_id == "2"

    def test_returns_a_model_instance(self, table):
        subscription = table.insert(user_id="1", bot_id="2", type="pape_news")
        assert subscription.user_id == "1"
        assert subscription.bot_id == "2"


class TestCount():
    def test_returns_records_count(self, table):
        assert table.count() == 0
        table.insert(user_id=1, bot_id=2, type="pape_news")
        table.insert(user_id=2, bot_id=2, type="pape_news")
        assert table.count() == 2

    def test_returns_records_in_function_of_conditions(self, table):
        assert table.count() == 0

        table.insert(user_id=1, bot_id=2, type="pape_news")
        table.insert(user_id=2, bot_id=2, type="pape_news2")
        table.insert(user_id=2, bot_id=2, type="pape_news3")

        assert table.count(conditions={"user_id": {">": "1"}}) == 2
        assert table.count(conditions={"type": ["pape_news2", "pape_news3"]}) == 2


class TestBulkInsert():
    def test_insert_records(self, table):
        table.bulk_insert(mappings=(
            {"user_id": 1, "bot_id": 2, "type": "pape_news"},
            {"user_id": 2, "bot_id": 2, "type": "pape_news"}
        ))
        assert table.count() == 2

    def test_does_not_raises_exception_on_duplicates(self, table):
        table.bulk_insert(mappings=(
            {"id": 50, "user_id": "1", "bot_id": "2", "type": "pape_news"},
            {"id": 50, "user_id": "1", "bot_id": "2", "type": "pape_news"}
        ))
        assert table.count() == 1


class TestDelete():
    def test_remove_object_from_db(self, table):
        sub = table.insert(user_id="1", bot_id="2", type="pape_news")
        table.insert(user_id="2", bot_id="2", type="pape_news")

        assert table.count() == 2
        table.delete(sub)
        assert table.count() == 1
        subscriptions = table.get()
        assert subscriptions[0].user_id == "2"
        assert subscriptions[0].bot_id == "2"


class TestDeleteWhere():
    def test_remove_object_from_db_with_conditon(self, table):
        table.insert(user_id="1", bot_id="2", type="pape_news")
        table.insert(user_id="2", bot_id="2", type="pape_news")

        assert table.count() == 2
        table.delete_where({"user_id": "1"})
        assert table.count() == 1
        subscriptions = table.get()
        assert subscriptions[0].user_id == "2"
        assert subscriptions[0].bot_id == "2"


class TestTruncate():
    def test_clear_the_table(self, table, database):
        table.insert(user_id="1", bot_id="2", type="pape_news")
        table.insert(user_id="2", bot_id="2", type="pape_news")

        assert table.count() == 2
        table.truncate()
        assert table.count() == 0


class TestGet():
    def test_returns_all_objects(self, table, database):
        table.insert(user_id="1", bot_id="2", type="pape_news")
        table.insert(user_id="2", bot_id="2", type="pape_news")

        objects = table.get()
        assert len(objects) == 2

    def test_returns_all_objects_in_safe_mode(self, table, database):
        subs = [{"user_id": i, "bot_id": "2", "type": "pape_news"} for i in list(range(10000))]
        subs2 = [{"user_id": i, "bot_id": "2", "type": "pape_news"} for i in list(range(10001, 20000))]

        table.bulk_insert(mappings=subs)
        table.bulk_insert(mappings=subs2)

        database.commit()

        objects = table.get(safe=True)

        assert len(objects.all()) == 19999

    def test_returns_N_objects(self, table):
        table.insert(user_id="1", bot_id="2", type="pape_news")
        table.insert(user_id="2", bot_id="2", type="pape_news")
        objects = table.get(limit=1)
        assert len(objects) == 1

    def test_returns_N_objects_ordered(self, table):
        table.insert(user_id="1", bot_id="2", type="pape_news")
        table.insert(user_id="2", bot_id="2", type="pape_news")
        objects = table.get(limit=1, sort="-user_id")

        assert len(objects) == 1
        assert objects[0].user_id == "2"

        objects = table.get(limit=1, sort="+user_id")

        assert len(objects) == 1
        assert objects[0].user_id == "1"

    def test_pagination(self, table):
        table.insert(user_id="1", bot_id="2", type="pape_news")
        table.insert(user_id="2", bot_id="2", type="pape_news")

        objects = table.get(limit=1, page=1)

        assert len(objects) == 1
        assert objects[0].user_id == "1"

        objects = table.get(limit=1, page=2)
        assert len(objects) == 1
        assert objects[0].user_id == "2"
