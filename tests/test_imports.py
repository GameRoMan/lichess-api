def test_imports():
    import lichess

    assert lichess

    # ---

    from lichess import client, custom, LichessClient, schemas

    assert client
    assert custom
    assert LichessClient
    assert schemas
