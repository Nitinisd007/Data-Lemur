def intersection(a, b):
  return [1, 2, 3]
def intersection(a, b):
  new_l=[]
  for i in a:
    for j in b:
      if i==j:
        new_l.append(j)
      # else:
      #   continue
  return new_l
