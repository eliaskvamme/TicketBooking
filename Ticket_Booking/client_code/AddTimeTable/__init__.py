from ._anvil_designer import AddTimeTableTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables




class AddTimeTable(AddTimeTableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
  

  def file_loader_1_change(self, file, **event_args):
    anvil.server.call('store_data',file)

