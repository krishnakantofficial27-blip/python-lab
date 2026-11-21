"""Generate a residential electricity bill from meter readings."""

ELECTRICITY_DUTY_RATE = 0.05
FIXED_METER_CHARGE = 100.0

def main() -> None:
    """Collect consumer details, calculate charges, and print the bill."""
    print("========== ELECTRICITY BILL GENERATOR ==========")
    consumer_name = input("Enter Consumer Name: ").strip()
    consumer_id = input("Enter Consumer ID: ").strip()
    previous_reading = float(input("Enter Previous Meter Reading (kWh): "))
    current_reading = float(input("Enter Current Meter Reading (kWh): "))
    cost_per_unit = float(input("Enter Cost per Unit (INR): "))

    if current_reading < previous_reading:
        raise ValueError("Current meter reading cannot be lower than previous reading.")
    if cost_per_unit < 0:
        raise ValueError("Cost per unit cannot be negative.")

    units_consumed = current_reading - previous_reading
    energy_charge = units_consumed * cost_per_unit
    electricity_duty = energy_charge * ELECTRICITY_DUTY_RATE
    net_bill = energy_charge + electricity_duty + FIXED_METER_CHARGE

    print("\n=============== ELECTRICITY BILL ===============")
    print(f"Consumer Name        : {consumer_name}")
    print(f"Consumer ID          : {consumer_id}")
    print(f"Units Consumed       : {units_consumed:.2f} kWh")
    print(f"Energy Charge        : INR {energy_charge:.2f}")
    print(f"Electricity Duty (5%): INR {electricity_duty:.2f}")
    print(f"Fixed Meter Charge   : INR {FIXED_METER_CHARGE:.2f}")
    print("------------------------------------------------")
    print(f"Net Bill Amount      : INR {net_bill:.2f}")
    print("================================================")
if __name__ == "__main__":
    main()