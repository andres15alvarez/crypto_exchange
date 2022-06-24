from utils import crypt


def test_hash_password_success():
    password = crypt.hash_password("holahola")
    hashed_password = "5819b005d5c142ae151889bcbe0872bbbdbeecc26c4785a48e65b04abd7a6926"
    assert password == hashed_password


def test_verify_password_success():
    hashed_password = "5819b005d5c142ae151889bcbe0872bbbdbeecc26c4785a48e65b04abd7a6926"
    password = "holahola"
    assert crypt.verify_password(password, hashed_password)

def test_verify_password_failure():
    hashed_password = "5819b005d5c142ae151889bcbe0872bbbdbeecc26c4785a48e65b04abd7a6926"
    wrong_password = "holoholo"
    assert not crypt.verify_password(wrong_password, hashed_password)
