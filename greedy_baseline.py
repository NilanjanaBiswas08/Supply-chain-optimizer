def greedy_assignment(factories, customers, capacity, demand, cost):
    remaining_capacity = capacity.copy()
    total_cost = 0
    assignment = []

    for j in customers:
        remaining_demand = demand[j]
        sorted_factories = sorted(factories, key=lambda i: cost[i, j])

        for i in sorted_factories:
            if remaining_demand <= 0:
                break
            available = remaining_capacity[i]
            if available <= 0:
                continue

            shipped = min(available, remaining_demand)
            total_cost += shipped * cost[i, j]
            remaining_capacity[i] -= shipped
            remaining_demand -= shipped
            assignment.append((i, j, shipped))

    return assignment, total_cost
