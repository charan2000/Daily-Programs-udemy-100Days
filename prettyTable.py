from prettytable import PrettyTable

obj = PrettyTable()
obj.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
obj.add_column("Type", ["Electric", "Water", "Fire"])
print(obj)
