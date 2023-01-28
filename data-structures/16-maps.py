# maps are dictionaries
capitals = {
 "ZAF": "Pretoria", # South Africa
 "BKA": "Ouagadougou", # Burkina Faso 
 "SEN": "Dakar" # Senegal
}

# update item in map/dictionary, use index key
capitals["ZAF"] = ["Cape Town", "Slaapstad", "Jozi"]
print(capitals)

# retrieving a specific item from a specific key
print(capitals["ZAF"][2])