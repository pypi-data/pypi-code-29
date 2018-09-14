info_template = '''<?xml version="1.0" encoding="UTF-8" ?>
<Results>
<show>
<showid>{id}</showid>
<name>{name}</name>
<link>http://www.tvrage.com/foobar</link>
<country>US</country>
<started>1904</started>
<ended>0</ended>
<seasons>110</seasons>
<status>Returning Series</status>
<classification>Porn</classification>
<genres><genre>Adult Entertainment</genre></genres>
</show>
</Results>
'''

episodes_template = '''<?xml version="1.0" encoding="UTF-8" ?>
<Show>
<name>{name}</name>
<totalseasons>2</totalseasons>
<Episodelist>
<Season no="1">
<episode><epnum>1</epnum><seasonnum>01</seasonnum><prodnum>7G08</prodnum><airdate>1989-12-17</airdate><link>http://foo</link><title>Title 1</title></episode>
<episode><epnum>2</epnum><seasonnum>02</seasonnum><prodnum>7G02</prodnum><airdate>1990-01-14</airdate><link>http://foo</link><title>Title 2</title></episode>
</Season>
<Season no="2">
<episode><epnum>1</epnum><seasonnum>01</seasonnum><prodnum>7G08</prodnum><airdate>2014-12-1</airdate><link>http://foo</link><title>Title 1</title></episode>
<episode><epnum>2</epnum><seasonnum>02</seasonnum><prodnum>7G02</prodnum><airdate>{next_epi}</airdate><link>http://foo</link><title>Title 2</title></episode>
</Season>
</Episodelist>
</Show>
'''

__all__ = ['episodes_template', 'info_template']
