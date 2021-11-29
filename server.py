from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/tickets')
def get_tickets():
   url = "https://zcc2707.zendesk.com/api/v2/tickets"
   token = 
   response = requests.get(url, headers={'Authorization': token})
   if response.status_code != 200:
      return render_template("something_is_not_working.html", response = response)
   data = response.json()
   next_page = data['next_page']
   previous_page = data['previous_page']
   tickets = data['tickets']
   while next_page is not None:
      response = requests.get(next_page, headers={'Authorization': token})
      if response.status_code != 200:
         return render_template("something_is_not_working.html", response = response)
      tickets.append(response.json()['tickets'])
      next_page = response.json()['next_page']
   #return data
   return render_template("ticket_list.html", tickets = tickets, next_page = next_page, previous_page = previous_page)

@app.route('/tickets/<id>', methods = ["GET"])
def get_ticket(id):
   url = "https://zcc2707.zendesk.com/api/v2/search.json?query="+id
   token = 
   response = requests.get(url, headers={'Authorization': token})
   if response.status_code != 200:
      return render_template("something_is_not_working.html", response = response)
   data = response.json()
   return render_template("ticket.html", ticket = data)


if __name__ == '__main__':
   app.run(debug=True)