from main import password_Strengthener

def test_password_Strengthener():
    assert password_Strengthener("StrongPassword123!")
    assert not password_Strengthener("weakpassword")
    assert not password_Strengthener("AnotherWeakPassword")
    assert not password_Strengthener("Short1!")
    assert not password_Strengthener("ThisIsAVeryLongPasswordWithoutSpecialCharacterOrNumber")
    assert password_Strengthener("GoodP@ssw0rd")