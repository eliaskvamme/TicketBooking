from ._anvil_designer import BuyTicketFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import globalVariables

'''
This code defines the functionality of the Buy Ticket page
'''
class BuyTicketForm(BuyTicketFormTemplate):
  def __init__(self, **properties):
    global ticketInfoList
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    
#Function defining what happens when the adult ticket button is clicked, 
#The childrens and senior buttons works in the same way.
  def AdultTicketButton_click(self, **event_args):
    global ticketInfoList
    global pickedDate
    userName = anvil.users.get_user()['Name'] 
    #Calls the server side function that buys an adult ticket, with the parameters describing from, to and time of train.
    anvil.server.call('buyAdultTicket',globalVariables.ticketInfoList[0],globalVariables.ticketInfoList[1],globalVariables.ticketInfoList[2])
    #Deletes any upgrade that must be stored on the user
    anvil.server.call('removeUpgradedTicket')
    #Display a window with what ticket has been bought
    alert(f"You have bought an Adult Ticket to {globalVariables.ticketInfoList[0]} from {globalVariables.ticketInfoList[1]}\nThe train will depart at {globalVariables.ticketInfoList[2]}")
    #Deletes the variable containing selected train info
    globalVariables.pickedDate = None
    open_form('MainForm')

  def ChildrensTicketButton_click(self, **event_args):
    global ticketInfoList
    userName = anvil.users.get_user()['Name'] 
    anvil.server.call('buyChildrensTicket',globalVariables.ticketInfoList[0],globalVariables.ticketInfoList[1],globalVariables.ticketInfoList[2])
    anvil.server.call('removeUpgradedTicket')
    alert(f"You have bought a Childrens Ticket to {globalVariables.ticketInfoList[0]} fra {globalVariables.ticketInfoList[1]}\nThe train will depart at {globalVariables.ticketInfoList[2]}")
    globalVariables.pickedDate = None
    open_form('MainForm')
    
  def SeniorTicketButton_click(self, **event_args):
    global ticketInfoList
    userName = anvil.users.get_user()['Name'] 
    anvil.server.call('buySeniorTicket',globalVariables.ticketInfoList[0],globalVariables.ticketInfoList[1],globalVariables.ticketInfoList[2])
    anvil.server.call('removeUpgradedTicket')
    alert(f"You have bought a Senior Ticket to {globalVariables.ticketInfoList[0]} from {globalVariables.ticketInfoList[1]}\nThe train will depart at {globalVariables.ticketInfoList[2]}")
    globalVariables.pickedDate = None
    open_form('MainForm')

    '''
    Functions defining the function of back-button and logout button.
    '''
  def backButton_click(self, **event_args):
    open_form('MainForm.DatePicker')

  def LogoutButton_click(self, **event_args):
    anvil.users.logout()
    open_form('LoginForm')




