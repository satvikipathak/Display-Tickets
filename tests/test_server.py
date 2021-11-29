def test_get_one_ticket(app, client):
    response = client.get('/tickets/1')
    assert response.status_code == 200

def test_error_on_nonexistent_ticket_id(app, client):
    #Test with a ticket id that doesn't exist. Our error handling should work and return 200.
    response = client.get('/tickets/102')
    assert response.status_code == 200

def test_get_all_tickets(app, client):
    response = client.get('/tickets')
    assert response.status_code == 200

def test_error_on_get_all_tickets(app, client):
    response = client.get('/tickets/')
    assert response.status_code != 200

def test_error_on_nonexistent_api(app, client):
    response = client.get('/people')
    assert response.status_code != 200