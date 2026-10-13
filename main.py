from data import factories, customers, capacity, demand, cost
from lp_model import solve_transportation
from greedy_baseline import greedy_assignment

def main():
    result = solve_transportation(factories, customers, capacity, demand, cost)

    print("--- LP Optimal Solution ---")
    print("Status:", result["status"])
    for i, j, units in result["plan"]:
        print(f"{i} -> {j}: {units} units")
    print("Total cost:", result["total_cost"])

    print("\n--- Shadow Prices ---")
    for name, info in result["shadow_prices"].items():
        print(f"{name}: price={info['price']}, slack={info['slack']}")

    greedy_plan, greedy_cost = greedy_assignment(factories, customers, capacity, demand, cost)

    print("\n--- Greedy Baseline ---")
    for i, j, units in greedy_plan:
        print(f"{i} -> {j}: {units} units")
    print("Greedy cost:", greedy_cost)

    savings = greedy_cost - result["total_cost"]
    pct = (savings / greedy_cost) * 100
    print(f"\nLP saves {savings:.1f} ({pct:.1f}%) vs greedy baseline")

if __name__ == "__main__":
    main()
