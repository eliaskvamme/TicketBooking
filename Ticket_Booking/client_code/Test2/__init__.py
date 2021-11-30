from ._anvil_designer import Test2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Test1 import Test1


class Test2(Test2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    #Test1.getListe(Test1())
    #print(var)
    
  def cancelTicket(self):
    user = anvil.users.get_user()
    #anvil.server.call('removeUpgradedTicket')
    user['Ticket'] = None
      
    

  def button_1_click(self, **event_args):
    user = anvil.users.get_user()
    print(user['Ticket']['to'])
    print("Håper den er slettet nå")

