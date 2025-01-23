INF = float('inf')

billing = {"plan": "", "description": []}

tariff_collection = [
    {"name": "Plan A", "min": 0, "max": 60, "tariffs": [
        {"min": 0, "max": 30, "rate": 6},
        {"min": 30, "max": 60, "rate": 9},
    ]},
    {"name": "Plan B", "min": 60, "max": INF, "tariffs": [
        {"min": 0, "max": 60, "rate": 15},
        {"min": 60, "max": 90, "rate": 18},
        {"min": 90, "max": 120, "rate": 30},
        {"min": 120, "max": 180, "rate": 42},
        {"min": 180, "max": INF, "rate": 65},
    ]}
]


def set_billing(tariffs_list, power_track):
    global billing
    billing["plan"] = tariffs_list["name"]
    for rate in tariffs_list["tariffs"]:
        increment = rate["max"] - rate["min"]
        units_diff = power_track - increment

        if units_diff >= 0:
            billing["description"].append({"units": increment, "rate": rate["rate"]})
        else:
            billing["description"].append({"units": power_track, "rate": rate["rate"]})
            break

        power_track -= increment


def set_tariff_collection(tariff_collection_list, power):
    for tariff_group in tariff_collection_list:
        increment = tariff_group["max"] - tariff_group["min"]
        units_diff = power - increment

        if units_diff <= 0:
            set_billing(tariff_group, power)
            break


def get_billing():
    total_cost = 0
    for item in billing["description"]:
        item["cost"] = item["units"] * item["rate"]
        total_cost += item["cost"]
    billing["total"] = total_cost


def display_billing():
    """Display the calculated billing information."""
    print("\nElectricity Billing System")
    print(f"Selected Plan: {billing['plan']}")
    print("-" * 50)

    for idx, item in enumerate(billing["description"], start=1):
        print(f"{idx}. Units: {item['units']} \t| Rate: {item['rate']} \t| Cost: {item['cost']}")

    print("-" * 50)
    print(f"Total Cost: {billing['total']}")
    print("-" * 50)


def main():
    print("Welcome to the Electricity Billing System!")

    # Take user input for power usage
    while True:
        try:
            power = int(input("Enter your power consumption in units: "))
            if power < 0:
                raise ValueError("Power consumption cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    # Process the billing
    set_tariff_collection(tariff_collection, power)
    get_billing()

    # Display the results
    display_billing()

    print("\nThank you for using the system!")


if __name__ == "__main__":
    main()
