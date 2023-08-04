from flight_search import FlightSearch

# flight_search = FlightSearch()
# print(flight_search.get_country_code("Kazan"))

matrix_list = [
    ["A1", "B1", "C1"],
    ["A2", "B2", "C2"],
    ["A3", "B3", "C3"],
]

# print([item[0] for item in matrix_list])

M = [
    [1, 2, 3],
    [4, 5, 6],
]

# G = (sum(row) for row in M)
# print(next(G))
# print(next(G))

# print(list(map(sum, M)))

bob2 = dict(zip(["name", "job", "age"], ["Bob", "dev", 40]))
print(bob2)