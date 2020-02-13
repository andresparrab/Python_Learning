class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print("Here is your shopping cart!")

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print("your order history!")

andres_parra = ReturningCustomer("ID: 12345")
andres_parra.display_cart()
andres_parra.display_order_history()
print(andres_parra.customer_id)