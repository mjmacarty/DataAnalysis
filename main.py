# descriptives

def mean(iterable):
    return sum(iterable) / len(iterable)

def std(iterable):
    x_bar = mean(iterable)
    ss = sum([(x - x_bar)**2 for x in iterable])
    return (ss/ (len(iterable)-1)) **0.5

def describe(iterable):
    x_bar = mean(iterable)
    sd = std(iterable)

    print()
    print("decriptives")
    print("-"* 20)
    print(f"{'Count:':7s}{len(iterable):13d}")
    print(f"{'Mean':7s}{x_bar:13.2f}")
    print(f"{'St Dev:':7s}{sd:13.2f}")        