def missing_int(input: list[int])-> int:
  input_sum=len(input)*(len(input)+1)//2
  actual_sum=sum(input)
  return input_sum-actual_sum
