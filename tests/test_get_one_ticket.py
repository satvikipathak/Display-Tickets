def test_get_one_ticket(app, client):
    result = client.get('/tickets/1')
    assert result.status.code == 200