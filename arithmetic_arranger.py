def arithmetic_arranger(list, logic = False):
  up = ""
  down = ""
  middle = ""
  result = ""
  for item in list:
    if len(list) > 5:
      return "Error: Too many problems." 
    elif item.split(" ")[1] in "!@#$%^&*/":
      if item.split(" ")[1] == "*" or item.split(" ")[1] == "/":
        return "Error: Operator must be '+' or '-'."
      return None
    else:
      for i in item:
        if i in "abcdefghijklmnopqrstuvwxyz" or item in "abcdefghijklmnopqrstuvwxyz".upper():
          return "Error: Numbers must only contain digits."
          
    # up_value += item.split(" ")[0]
    # down_value += item.split(" ")[2]

    if len(item.split(" ")[0]) > 4 or len(item.split(" ")[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    # symbol += item.split(" ")[1]
    if "+" in item:
      hasil = int(item.split(" ")[0]) + int(item.split(" ")[2])
    else:
      hasil = int(item.split(" ")[0]) - int(item.split(" ")[2])
    length = max(len(item.split(" ")[0]), len(item.split(" ")[2])) + 2
    # result_value += str(hasil)

    if list[-1] != item:
      up += (length - len(item.split(" ")[0])) * " " + str(item.split(" ")[0]) + "    "
      down += item.split(" ")[1] + (length - len(item.split(" ")[2]) - 1) * " " + str(item.split(" ")[2]) + "    "
      middle += length * "-" + "    "
      result += (length - len(str(hasil))) * " " + str(hasil) + "    "
    else:
      up += (length - len(item.split(" ")[0])) * " " + str(item.split(" ")[0])
      down += item.split(" ")[1] + (length - len(item.split(" ")[2]) - 1) * " " + str(item.split(" ")[2])
      middle += length * "-"
      result += (length - len(str(hasil))) * " " + str(hasil)

  if logic:
    return up + "\n" + down + "\n" + middle + "\n" + result
  else:
    return up + "\n" + down + "\n" + middle