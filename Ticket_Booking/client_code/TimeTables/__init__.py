from ._anvil_designer import TimeTablesTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

'''
This code defines the functionality of the Time Table page
'''

class TimeTables(TimeTablesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #Loads the train times from database.
    self.repeating_panel_1.items = anvil.server.call('get_traintimes')

  def BackButton_click(self, **event_args):
    open_form('MainForm.DatePicker')

  def LogOut_click(self, **event_args):
    anvil.users.logout()
    open_form('LoginForm')


  