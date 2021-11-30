from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import globalVariables
from datetime import datetime
from ... import globalVariables

'''
This code defines the functionality of the Train Time Table
'''

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

#Function defining what happens when one of the links in the time table is clicked
  def link_1_click(self, **event_args):
    alert(f"From: {self.item['From']} \nTo:{self.item['To']} \nTime: {self.item['Time']}")
    global ticketInfoList
    
    #Stores the train data, station travelling from, to, and at which time.
    globalVariables.ticketInfoList = []
    globalVariables.ticketInfoList.append(self.item['To'])
    globalVariables.ticketInfoList.append(self.item['From'])
    globalVariables.ticketInfoList.append(f"{self.item['Time']}, {globalVariables.pickedDate}")
    
    open_form('BuyTicketForm')
    

