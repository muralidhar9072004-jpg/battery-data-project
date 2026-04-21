import pandas as pd

# Sample battery station data
data = {
    "Station": ["BLR01", "BLR02", "BLR03", "BLR04", "BLR05"],
    "SOC": [78, 52, 91, 61, 45],
    "Health": [95, 84, 98, 88, 79],
    "Status": ["Active", "Active", "Active", "Maintenance", "Active"]
}

# Create DataFrame
df = pd.DataFrame(data)

print("🔋 Battery Station Performance Report")
print(df)

# Average SOC
avg_soc = df["SOC"].mean()
print(f"\nAverage SOC: {avg_soc:.2f}%")

# Low SOC stations
low_soc = df[df["SOC"] < 60]
print("\n⚠️ Low SOC Stations:")
print(low_soc[["Station", "SOC"]])

# Weak health batteries
weak_health = df[df["Health"] < 85]
print("\n🛠️ Batteries Needing Attention:")
print(weak_health[["Station", "Health"]])

# Save report
df.to_csv("battery_report.csv", index=False)

print("\n✅ Report saved as battery_report.csv")
