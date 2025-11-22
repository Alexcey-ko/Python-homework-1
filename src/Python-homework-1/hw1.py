"""Этот модуль предоставляет набор классов для работы с заказами клиента."""

class CustomerDataClass:
   """Класс для работы с данными клиента."""

   def __init__(self, customer_id, customer_name):
      """Конструктор класса.

      Args:
         customer_id (_int_): идентификатор клиента 
         customer_name (_string_): имя клиента
      """
      self.customer_id = customer_id
      self.customer_name = customer_name
      self.orders = []

   def add_order(self, order_object):
      """Создание заказа клиента.

      Args:
         order_object (_OrderDataClass_): заказ клиента
      """
      self.orders.append(order_object)

   def get_total_amount(self):
      """Вычисление общей суммы заказов.

      Returns:
         _float_: сумма заказов
      """
      total=0
      for o in self.orders:
         total = total + o.amount
      return total

class OrderDataClass:
   """Класс для работы с заказом клиента."""

   def __init__(self, order_id, amount):
      """Конструктор класса.

      Args:
         order_id (_int_): Идентификатор заказа
         amount (_float_): сумма заказа
      """
      self.orderId = order_id
      self.amount = amount


def calculate_discount(customer_obj):
   """Вычисление скидки заказа.

   Args:
      customer_obj (_CustomerDataClass_): клиент

   Returns:
      _float_: сумма скидки
   """
   total_amount = customer_obj.get_total_amount()
   discount = total_amount * 0.1 if total_amount > 1000 else 0
   return discount

def print_customer_report(customer_obj):
   """Вывод статистики клиента.

   Args:
      customer_obj (_CustomerDataClass_): клиент
   """
   print('Customer Report for:', customer_obj.customer_name)
   print('Total Orders:', len(customer_obj.orders))
   print('Total Amount:', customer_obj.get_total_amount())
   print('Discount:', calculate_discount(customer_obj))
   print('Average Order:', 0 if len(customer_obj.orders) == 0 else customer_obj.get_total_amount() / len(customer_obj.orders))

def main_program():
   """Запуск основной программы."""
   c1=CustomerDataClass(1,'SAP Customer')
   c2=CustomerDataClass(2,'Empty Customer')

   o1=OrderDataClass(101,500)
   o2=OrderDataClass(102,800)

   c1.add_order(o1)
   c1.add_order(o2)

   print_customer_report(c1)
   print_customer_report(c2) 

main_program()