
def count(m):
    sum = 0

    if isinstance(m, (list, tuple, set)):
        for item in m:
            sum += count(item)

    if isinstance(m, dict):
        for key, value in m.items():
            sum += count(key)
            sum += count(value)

    if isinstance(m, int):
        sum += m

    if isinstance(m, str):
        sum += len(m)

    return sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = count(data_structure)
print(result)