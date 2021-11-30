from ._anvil_designer import LoginFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

'''
This code defines the functionality of the Login page
'''

class LoginForm(LoginFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
    
  
  def LogoutButton_click(self, **event_args):
    anvil.users.logout()

    
#Function checking if user is registerd with full name or just email.
  def checkUserHasName(self):
    user = anvil.users.get_user()
    userName = user['Name']
    if userName == None:
      open_form('UserNameForm')
      
    else:
      open_form('MainForm')
    

  def LoginButton_click(self, **event_args):
    anvil.users.login_with_form()
    self.checkUserHasName()

    
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    pass



  




  



