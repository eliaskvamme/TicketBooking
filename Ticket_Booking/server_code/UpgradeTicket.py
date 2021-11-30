import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

'''
This server-side method contains the functions concidering upgrading tickets
'''

@anvil.server.callable
def upgradeTicket():
  print("You have upgraded your experience, enjoy!")
  user = anvil.users.get_user()
  user.update(IsUpgraded= True)

@anvil.server.callable
def removeUpgradedTicket():
  print("Upgraded Ticket is removed")
  user = anvil.users.get_user()
  user.update(IsUpgraded= False)