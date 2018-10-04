from dloud_ads import positional_list

def test_dummy():
	L = positional_list.PositionalList()
	p8 = L.add_last(8)
	assert p8.element() == 8
	assert L.first().element() == p8.element()
	p5 = L.add_after(p8, 5)
	assert p5.element() == 5
	assert L.first().element() == 8
	assert L.last().element() == 5
	assert L.before(p5).element() == 8
	assert L.after(p8).element() == 5
	assert L.after(p5) is None
	assert L.before(p8) is None
	p3 = L.add_before(p5, 3)
	assert p3.element() == 3
	assert [x for x in L] == [8,3,5]

	value5 = L.delete(L.last())
	assert value5 == 5
	assert len(L) == 2
	assert [x for x in L] == [8,3]

	value8 = L.replace(p8, 7)
	assert value8 == 8
	assert [x for x in L] == [7,3]

