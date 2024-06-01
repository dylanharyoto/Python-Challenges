class Category:
  def __init__(self, category):
    self.category_name = category
    self.ledger = []

  def __repr__(self):
    x = int((30 - len(self.category_name)) / 2) * "*"
    name = x + self.category_name + x + "\n"
    lists = ""
    for item in self.ledger:
      if len(item["description"]) > 23:
        item["description"] = item["description"][:int((len(item["description"]) - 23) * -1)]
      y = int(30 - len(item["description"]) - len(format(item["amount"], ".2f"))) * " "
      lists += item["description"] + y + str(format(item["amount"], ".2f")) + "\n"
    total = "Total: " + format(self.get_balance(), ".2f")
    return name + lists + total

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description = ""):
    self.amount = amount
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": amount * -1, "description": description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance
  
  def transfer(self, amount, category):
    if self.check_funds(amount) == True:
      self.withdraw(amount, "Transfer to " + category.category_name)
      category.deposit(amount, "Transfer from " + self.category_name)
      return True
    return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True


def create_spend_chart(categories):
  datas = []
  names = []
  for item in categories:
    datas.append(item.ledger)
    names.append(item.category_name)

  total = 0
  values = []
  for data in datas:
    z = 0
    for item in data:
      if item["amount"] < 0:
        z += item["amount"]
        total += item["amount"]
    values.append(z)
  results = []
  for value in values:
    j = value / total * 100
    if value / total * 100 < 10:
      j = 0
    results.append(round(round(j), -1))

  text = "Percentage spent by category" + "\n"

  table = ""
  for i in range(100, -10, -10):
    if len(str(i)) == 1: table += "  "
    elif len(str(i)) == 2: table += " "
    table += str(i) + "| "
    fill = None
    for index, result in enumerate(results):
      if i <= result and index == 0:
        table += "o"
        fill = True
      elif i <= result and index == 1:
        if fill: table += "  o"
        else: table += "   o"
        fill = True
      elif i <= result and index == 2:
        if fill: table += "  o"
        else: table += "   o"
    table += "\n"

  line = "    ----------" + "\n"

  label = ""
  for i in range(len(max(names, key = len))):
    label += "     "
    for index, name in enumerate(names):
      if i >= len(min(names, key = len)):
          try: label += list(name)[i] + "  "
          except IndexError: label += "   "
      else:
        label += list(name)[i] + "  "
    label += "\n"
    
  return text + table + line + label