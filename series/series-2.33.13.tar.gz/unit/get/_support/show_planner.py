from datetime import date, timedelta

from golgi import Config  # NOQA

from unit._fixtures.get.tvrage import info_template, episodes_template


class ShowPlannerTestMixin:

    def setup(self, *a, **kw):
        def after(days):
            return (date.today() + timedelta(days=days)).strftime('%Y-%m-%d')
        super().setup(*a, **kw)
        shows = ['series1', 'series2']
        Config.override('series', monitor=shows)
        tomorrow = after(1)
        later = after(21)
        self._data = [
            ['1001', 1001, 'Series 1', tomorrow],
            ['1002', 1002, 'Series 2', later],
            ['1003', 1003, 'Series 3', later],
            ['1004', 1004, 'Series 4', later],
            ['1005', 1005, 'Series 5', later],
        ]
        self._series_info = dict([
            [k, info_template.format(id=i, name=n)]
            for k, i, n, d in self._data
        ])
        self._series_episodes = dict([
            [k, episodes_template.format(name=n, next_epi=d)]
            for k, i, n, d in self._data
        ])

__all__ = ['ShowPlannerTestMixin']
