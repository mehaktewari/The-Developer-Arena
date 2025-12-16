from library_system.member import Member

def test_member_limit():
    m = Member("Alex", "M1")
    assert m.can_borrow() is True
