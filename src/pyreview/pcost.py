""" 
pcost.py
"""

def portfolio_cost(filename):
    """
    portfolio_cost
    """
    total_cost = 0

    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            try:
                number = int(line.split()[1])
            except ValueError as err:
                print("Could not read number because", err)
                number = 0
            try:
                price = float(line.split()[2])
            except ValueError as err:
                print("Could not convert price because", err)
                price = 0.0
            total_cost += number * price

    return total_cost

if __name__ == "__main__":
    print(portfolio_cost('Data/portfolio3.dat'))
