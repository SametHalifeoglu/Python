monthConversions = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
}

print(monthConversions["jan"])
print(monthConversions.get("mar"))
print(monthConversions[5])
print(monthConversions.get(6))
print(monthConversions.get("jun"))
print(monthConversions.get("jun", "June"))