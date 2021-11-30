import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

'''
This server-side method contains the function for cancelling the tickets
'''

@anvil.server.callable
def cancelTicket():
  user = anvil.users.get_user()
  anvil.server.call('removeUpgradedTicket')
  user['Ticket'] = None