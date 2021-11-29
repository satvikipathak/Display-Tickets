def test_get_one_ticket(app, client):
    response = client.get('/tickets/1')
    assert response.status_code == 200

def test_error_on_nonexistent_ticket_id(app, client):
    #Test with a ticket id that doesn't exist
    response = client.get('/tickets/102')
    assert response.status_code != 200

def test_get_all_tickets(app, client):
    response = client.get('/tickets')
    assert response.status_code == 200


def test_response_data_for_get_one_ticket(app, client):
    #Test ticket details for ticket id 1 are as per expected
    response = client.get('/tickets/1')
    assert response.status_code == 200
    print(response)
    print(response.json())
    data = response.json()
    to_display = data['results']
    assert to_display[0]['id'] == 1
    assert to_display[0]['status'] == 'open'
    assert to_display[0]['priority'] == 'normal'
    assert to_display[1]['name'] == 'The Customer'
    assert to_display[2]['name'] == 'Satviki Sanjay Pathak'

