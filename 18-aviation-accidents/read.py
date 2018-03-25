from operator import itemgetter
from utils import linDictSearch, biSearch

with open("AviationData.txt") as f:
    aviation_data = f.readlines()
    
aviation_list = []  
headers = []

for i, d in enumerate(aviation_data):
    splited = d.split("|")
    
    for j, v in enumerate(splited):
        splited[j] = v.strip()
        
    if i==0:
        splited.append("State")
        splited.append("MM/YYYY")
        headers = splited
    else:
        if ", " in splited[4]:
            splited.append(splited[4].split(", ")[1])
        else:
            splited.append("")
            
        splited.append(splited[3][3:])
        aviation_list.append(splited)
       
    
aviation_list = sorted(aviation_list, key=itemgetter(2))

lax_code = []
        
lax_code.append(biSearch(aviation_list, "LAX94LA336", 2))
        
#print(headers, lax_code) 

aviation_dict_list = []

for l in aviation_list:
    try:
        aviation_dict_list.append(dict(zip(headers, l)))
    except:
        print("headers:", headers, "list:", l)
        break
    
    
lax_dict = []
lax_dict.append(linDictSearch(aviation_dict_list, "LAX94LA336"))

state_accidents = {}
monthly_injuries = {}

for row in aviation_dict_list:
    if row["Investigation Type"]=="Accident" and row["Country"]=="United States":
        if row["State"] in state_accidents:
            state_accidents[row["State"]] += 1
        else:
            state_accidents[row["State"]] = 1
    
    fatal = 0
    serious = 0
    
    if row["Total Fatal Injuries"]:
        fatal = int(row["Total Fatal Injuries"])
        
    if row["Total Serious Injuries"]:        
        serious = int(row["Total Serious Injuries"])
    
    if row["MM/YYYY"] in monthly_injuries:
        monthly_injuries[row["MM/YYYY"]] += fatal + serious
    else:
        monthly_injuries[row["MM/YYYY"]] = fatal + serious
        
            
sorted_states = sorted(state_accidents.items(), key=itemgetter(1), reverse=True)

print(sorted_states[0])
#print(monthly_injuries)

monthes = monthly_injuries.keys()
injuries = monthly_injuries.values()

monthes_inj_desc = sorted(monthly_injuries.items(), key=itemgetter(1), reverse=True)

for m in monthes_inj_desc:
    print(m[0], m[1])
	
#Map out accidents using the basemap library for matplotlib.
#Count the number of accidents by air carrier.
#Count the number of accidents by airplane make and model.
#Figure out what percentage of accidents occur under adverse weather conditions.	