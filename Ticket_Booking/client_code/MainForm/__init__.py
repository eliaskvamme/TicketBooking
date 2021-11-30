from ._anvil_designer import MainFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import globalVariables

'''
This code defines the functionality of the Main page
'''


class MainForm(MainFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    

  def LogoutButton_click(self, **event_args):
    anvil.users.logout()
    open_form('LoginForm')

    
  def buyTicketButton_click(self, **event_args):
    open_form('MainForm.DatePicker')

  def ShowTicketButton_click(self, **event_args):
    global ticketInfoList
    #get info of user
    user = anvil.users.get_user()
    if user['Ticket'] == None:
      alert("You have no ticket, please buy one")
    elif user['IsUpgraded'] == True:
      alert(f"Name: {user['Name']}\nTicket type: Upgraded {user['Ticket']['type']} \nTicket valid on the train\nfrom {user['Ticket']['tFrom']} to {user['Ticket']['to']} \nwith departure {user['Ticket']['time']}")
    else:
      alert(f"Name: {user['Name']}\nTicket type: {user['Ticket']['type']} \nTicket valid on the train\nfrom {user['Ticket']['tFrom']} to {user['Ticket']['to']} \nwith departure {user['Ticket']['time']}")

      
  def TicketUpgradeButton_click(self, **event_args):
      
    user = anvil.users.get_user()
    ticketInfo = anvil.users.get_user()['Ticket']
    if ticketInfo == None:
      alert("You need to buy a ticket first")
    else:
      anvil.server.call('upgradeTicket')
      alert("You are upgraded, enjoy your trip!")
    

  def CancelTicketButton_click(self, **event_args):
    user = anvil.users.get_user()
    if user['Ticket'] == None:
      alert("You don't have a ticket to cancel")
    elif confirm("Are you sure you want to cancel your ticket?\nThis cannot be undone") == True:
      anvil.server.call('cancelTicket')
      alert("Your ticket was cancelled")
    else:
      alert("Your ticket was not cancelled")
    




