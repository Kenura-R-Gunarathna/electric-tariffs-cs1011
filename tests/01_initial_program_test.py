INF = "INF"

power = power_track = 190

billing = []

rates = [
    {"min": 0, "max": 60, "rate": 15},
    {"min": 60, "max": 90, "rate": 18},
    {"min": 90, "max": 120, "rate": 30},
    {"min": 120, "max": 180, "rate": 42},
    {"min": 180, "max": INF, "rate": 65}
]

for rate in rates:
    if str(rate["max"]).upper() != "INF":
        increment = rate["max"] - rate["min"]
    else:
        increment = rate["min"]

    units_diff = power_track - increment

    if units_diff >= 0:
        billing.append({"units": increment, "rate": rate["rate"]})
    else:
        billing.append({"units": power_track, "rate": rate["rate"]})
        break

    power_track -= increment

print(billing)
