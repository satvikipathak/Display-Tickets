from flask import Flask, render_template
import requests

app = Flask(__name__)
app.config.from_pyfile('./config/app.conf')

@app.route('/tickets')
def get_tickets():
   url = app.config.get("GET_ALL_TICKETS_API")
   token = app.config.get("OAUTH_ACCESS_TOKEN")
   response = requests.get(url, headers={'Authorization': token})
   if response.status_code != 200:
      return render_template("something_is_not_working.html", response = response)
   data = response.json()
   tickets = data['tickets']
   #return data
   return render_template("ticket_list.html", tickets = tickets)

@app.route('/tickets/<id>', methods = ["GET"])
def get_ticket(id):
   url = app.config.get("GET_SINGLE_TICKET_API") + id
   token = app.config.get("OAUTH_ACCESS_TOKEN")
   response = requests.get(url, headers={'Authorization': token})
   if response.status_code != 200:
      return render_template("something_is_not_working.html", response = response)
   data = response.json()
   return render_template("ticket.html", ticket = data)


if __name__ == '__main__':
   app.run(debug=True)