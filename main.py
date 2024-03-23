#pip install ucimlrepo

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
national_poll_on_healthy_aging_npha = fetch_ucirepo(id=936) 
  
# data (as pandas dataframes) 
X = national_poll_on_healthy_aging_npha.data.features 
y = national_poll_on_healthy_aging_npha.data.targets 
  
# metadata 
print(national_poll_on_healthy_aging_npha.metadata) 
  
# variable information 
print(national_poll_on_healthy_aging_npha.variables) 
