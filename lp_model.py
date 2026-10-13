import pulp

def solve_transportation(factories, customers, capacity, demand, cost):
    prob = pulp.LpProblem("Transportation", pulp.LpMinimize)

    x = pulp.LpVariable.dicts("ship", (factories, customers), lowBound=0)

    prob += pulp.lpSum(cost[i, j] * x[i][j] for i in factories for j in customers)

    for i in factories:
        prob += pulp.lpSum(x[i][j] for j in customers) <= capacity[i], f"Supply_{i}"

    for j in customers:
        prob += pulp.lpSum(x[i][j] for i in factories) >= demand[j], f"Demand_{j}"

    prob.solve()

    plan = []
    for i in factories:
        for j in customers:
            if x[i][j].varValue > 0:
                plan.append((i, j, x[i][j].varValue))

    shadow_prices = {
        name: {"price": c.pi, "slack": c.slack}
        for name, c in prob.constraints.items()
    }

    return {
        "status": pulp.LpStatus[prob.status],
        "plan": plan,
        "total_cost": pulp.value(prob.objective),
        "shadow_prices": shadow_prices,
    }
