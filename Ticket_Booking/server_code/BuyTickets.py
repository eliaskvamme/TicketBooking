import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

'''
This server-side method contains the functions for buying tickets
'''

fullPrice = 160
reducedPrice = 80

@anvil.server.callable
def buyAdultTicket(to, tFrom, time):
  print("You have bought an Adult Ticket")
  user = anvil.users.get_user()
  print(f"To er {type(to)}, tFrom er {type(tFrom)}, time er {type(time)}")
  
  user.update(Ticket= {'to': to, 'tFrom': tFrom, 'time': time, 'type': 'Adult Ticket','price': fullPrice})
  
@anvil.server.callable
def buyChildrensTicket(to, tFrom, time):
  print("You have bought a Childrens Ticket")
  user = anvil.users.get_user()
  print(f"To er {type(to)}, tFrom er {type(tFrom)}, time er {type(time)}")
  
  user.update(Ticket= {'to': to, 'tFrom': tFrom, 'time': time, 'type': 'Childrens Ticket','price': reducedPrice})
  
  
@anvil.server.callable
def buySeniorTicket(to, tFrom, time):
  print("You have bought a Senior Ticket")
  user = anvil.users.get_user()
  print(f"To er {type(to)}, tFrom er {type(tFrom)}, time er {type(time)}")
  
  user.update(Ticket= {'to': to, 'tFrom': tFrom, 'time': time, 'type': 'Senior Ticket','price': reducedPrice})
  