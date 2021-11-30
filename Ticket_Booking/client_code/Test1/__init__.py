from ._anvil_designer import Test1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Test1(Test1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    global liste
    self.liste =[1,2,3]
    user = anvil.users.get_user()
    
    
    row = app_tables.users.get(email=anvil.users.get_user()['email'])
    ticketType = row['Ticket']['type']
    ticketPrice = row['Ticket']['price']
    
    

    
    
    
    
    user.update(Ticket= {'type': 'Adult Ticket','price': 160})
    self.get_person_for_number('555-555-5555')
    print(ticketType)
    print(ticketPrice)
    #app_tables.users.get(Ticket= )
  
    
    
    
  def getListe(self):
    print(self.liste)
    return self.liste
  
  
  
  
    
  '''    # Any code you write here will run when the form opens.
    
    app_tables.people.add_row(
    name = "Kermit the Frog",
    contact_details = {
             'phone': [
                {'type': 'work',
                         'number': '555-555-5555'},
                {'type': 'home',
                         'number': '555-123-4567'}
               ]
                       })'''
    
  def get_person_for_number(self,phone_number):
    # We have a phone call for this number. Who is it?
    return print(app_tables.people.get(
  contact_details = {'phone': [{'number': phone_number}]}
    	)['name'])
    
  
  