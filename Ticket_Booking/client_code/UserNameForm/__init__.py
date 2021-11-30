from ._anvil_designer import UserNameFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

'''
This code defines the functionality of the Users full name page
'''

class UserNameForm(UserNameFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
#Function receiving the user's name from input and saving it to the user in the database
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = user = anvil.users.get_user()
    user.update(Name=self.text_area_1.text)
    open_form('MainForm')
    

