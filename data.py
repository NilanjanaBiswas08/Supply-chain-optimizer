factories = ["F1", "F2"]
customers = ["C1", "C2"]

capacity = {"F1": 10, "F2": 10}
demand   = {"C1": 10, "C2": 10}

cost = {
    ("F1", "C1"): 1,
    ("F1", "C2"): 2,
    ("F2", "C1"): 3,
    ("F2", "C2"): 100,
}
