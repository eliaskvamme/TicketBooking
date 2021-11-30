from ._anvil_designer import DatePickerTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import globalVariables
from datetime import datetime
'''
This code defines the functionality of the Date selection page
'''

class DatePicker(DatePickerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.date_picker_1.format = "%d-%m-%Y"
    
    
#function defining functionality of the date picker
  def date_picker_1_change(self, **event_args):
    global pickedDate
    #Saves the picked date to a gobal variable
    dateString = self.date_picker_1.date
    globalVariables.pickedDate = dateString
    

  def ConfirmDateButton_click(self, **event_args):
    if self.date_picker_1.date is None:
      alert("You have to choose a date")
    else:
      open_form('TimeTables')

  def BackButton_click(self, **event_args):
    open_form('MainForm')

  def Logout_click(self, **event_args):
    anvil.users.logout()
    open_form('LoginForm')




