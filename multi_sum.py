def mul_sum(N1,N2):
  product = N1 * N2

  if product <= 1000:
    return product
  
  else:
    sum  = N1 + N2
    return sum


result = mul_sum(60, 60)

print(result)

result = mul_sum(10, 60)

print(result)