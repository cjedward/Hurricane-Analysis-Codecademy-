# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
#######################################################################
# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def damages_updated(table):
  phrase = 'Damages not recorded'
  damage_floats = []
  for i in table:
    if i == phrase:
      damage_floats.append(i)
    elif i[-1] == "M":
      temp_num = i[:-1]
      num = float(temp_num)
      num = num * conversion.get("M")
      damage_floats.append(num)
    else: 
      temp_num = i[:-1]
      num = float(temp_num)
      num = num * conversion.get("B")
      damage_floats.append(num)
  return damage_floats
#print(add_floats(damages))
updated_damages = damages_updated(damages)
###################################################################
# 2 
# Create a Table
# Create and view the hurricanes dictionary
hurricane_info_dict = {}
def hurricane_dicts():
  for index in range(len(names)):
    hurricane_info_dict[names[index]]={
    "Name": names[index],
    "Month": months[index],
    "Year": years[index],
    "Max Sustained Wind": max_sustained_winds[index],
    "Areas Affected": areas_affected[index],
    "Damage": updated_damages[index],
    "Deaths": deaths[index]
    }
  return hurricane_info_dict
#print(hurricane_dicts())
###################################################################    
# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def hurricanes_by_year(dictionary):
  hurricanes_by_year = {}
  for index in dictionary:
    current_hurricane = dictionary[index]
    current_year = dictionary[index]["Year"]
    if current_year not in hurricanes_by_year:
      hurricanes_by_year[current_year] = [current_hurricane]
    else:
      hurricanes_by_year[current_year].append(current_hurricane)
  return hurricanes_by_year

new_dict = hurricane_dicts()
#print(hurricanes_by_year(new_dict))
##########################################################################
# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
def damaged_area_counter(areas_affected_list):
  areas_affected_count = {}
  count = 0
  for area_list in areas_affected_list:
    for area in area_list:
      if area not in areas_affected_count:
        count = 1
        areas_affected_count[area] = count
      else:
         areas_affected_count[area] += 1

  return areas_affected_count

most_affected_counted = damaged_area_counter(areas_affected)
##################################################################
# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def most_affected(affected_count_dict):
  max_count = 0
  current_count = 0
  most_affected = "No hurricane picked yet"

  for area in affected_count_dict:
    current_count = affected_count_dict.get(area)
    if current_count > max_count:
      max_count = current_count
      most_affected = str(area)
    else:
      continue
  return {most_affected : max_count}
# most_affected and most_affected_count test
#print(most_affected(most_affected_counted))
#################################################################
# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths

def most_deadliest(hurricanes):
  most_deaths = 0
  deadlist_hurricane = "Not selected yet..."
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Deaths"] > most_deaths:
      most_deaths = hurricanes[hurricane]["Deaths"]
      deadlist_hurricane = hurricanes[hurricane]["Name"]
    else:
      continue

  return {deadlist_hurricane : most_deaths}

#test_dict = hurricane_dicts()
#print(most_deadliest(test_dict))
##################################################################
# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key

def hurricanes_by_mortality(dictionary):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  canes_by_mortality = {}
  rating = 0
  for canes in dictionary:
    current_hurricane = dictionary[canes]
    mortality = dictionary[canes]["Deaths"]
    if mortality < mortality_scale[1]:
      rating = 0
    elif mortality < mortality_scale[2] and mortality > mortality_scale[1]:
      rating = 1
    elif mortality < mortality_scale[3] and mortality > mortality_scale[2]:
      rating = 2
    elif mortality < mortality_scale[4] and mortality > mortality_scale[3]:
      rating = 3
    else:
      rating = 4
    canes_by_mortality[rating] = [current_hurricane]
  return canes_by_mortality

#test_dict = hurricane_dicts()
#print(hurricanes_by_mortality(test_dict))
#############################################################################
# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost

def cane_with_most_damage(hurricanes):
  max_damage = 0
  cane_with_max_damage = "Not set yet"
  for cane in hurricanes:
    current_cane = hurricanes[cane]
    if hurricanes[cane]["Damage"] == "Damages not recorded":
      continue
    elif hurricanes[cane]["Damage"] > max_damage:
      max_damage = hurricanes[cane]["Damage"]
      cane_with_max_damage = current_cane
    else:
      continue
  #print("""The hurricane with the most damage is {} 
 # with ${} in damages""".format(cane_with_max_damage["Name"],max_damage))
cane_with_most_damage(new_dict)
##############################################################################
# 9
# Rating Hurricanes by Damage
# categorize hurricanes in new dictionary with damage severity as key
def most_damage(dictionary):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
  canes_by_damage_ratings = {}
  for cane in dictionary:
    current_cane = dictionary[cane]
    current_damage = current_cane["Damage"]
    if type(current_damage) != float:
      continue
    elif current_damage < damage_scale[1]:
      rating = 0
    elif current_damage < damage_scale[2] and current_damage > damage_scale[1]:
      rating = 1
    elif current_damage < damage_scale[3] and current_damage > damage_scale[2]:
      rating = 2
    elif current_damage < damage_scale[4] and current_damage > damage_scale[3]:
      rating = 3
    else:
      rating = 4
    canes_by_damage_ratings[rating] = [current_cane]
  return canes_by_damage_ratings


#print(most_damage(new_dict))

