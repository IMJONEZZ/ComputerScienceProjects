def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print(el)
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result
