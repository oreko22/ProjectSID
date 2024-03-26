#pip install ucimlrepo
from ucimlrepo import fetch_ucirepo 
import pandas as pd
import mysql.connector
from mysql.connector import Error
  
# fetch dataset 
national_poll_on_healthy_aging_npha = fetch_ucirepo(id=936) 
  
# data (as pandas dataframes) 
X = national_poll_on_healthy_aging_npha.data.features 
y = national_poll_on_healthy_aging_npha.data.targets 
  
# metadata 
print(national_poll_on_healthy_aging_npha.metadata) 
print(X)
# variable information 
print(national_poll_on_healthy_aging_npha.variables) 

# Combine two dataframe to have the final dataset
npha=pd.concat([X, y], axis=1)
print(npha)

# Rename the columns of the dataset
new_name = {
    'Age': 'Age',
    'Physical_Health': 'Physical_Health',
    'Mental_Health': 'Mental_Health',
    'Dental_Health': 'Dental_Health',
    'Employment': 'Employ',
    'Stress_Keeps_Patient_from_Sleeping': 'Sleep_Stress',
    'Medication_Keeps_Patient_from_Sleeping': 'Sleep_Medication',
    'Pain_Keeps_Patient_from_Sleeping': 'Sleep_Pain',
    'Bathroom_Needs_Keeps_Patient_from_Sleeping': 'Sleep_Bathroom',
    'Uknown_Keeps_Patient_from_Sleeping': 'Sleep_Unknown',
    'Trouble_Sleeping': 'Trouble_Sleep',
    'Prescription_Sleep_Medication': 'Presc_Medication',
    'Race': 'Race',
    'Gender': 'Gender',
    'Number_of_Doctors_Visited': 'Num_Doctors'
}
npha = npha.rename(columns=new_name)

 # Generating the ID
id = range(1, 715) 

# Adding the column ID in DataFrame 
npha.insert(0, 'ID', id)

# Loading the dataframe in MYSQL
try:
    connexion = mysql.connector.connect(host='localhost',
                                       database='tp_sid',
                                       user='root',
                                       password='')
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}")


try:
    cursor = connexion.cursor()

    for i,row in npha.iterrows():
        sql = """INSERT INTO patients (ID,Age, Physical_Health, Mental_Health, Dental_Health, Employment, Sleep_Stress, Sleep_Medication, Sleep_Pain, Sleep_Bathroom, Sleep_Unknown, Trouble_Sleep, Presc_Medication, Race, Gender, Num_Doctors) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        #print(sql)
        cursor.execute(sql, tuple(row))

    connexion.commit()
    connexion.close()
    print("DataFrame chargé dans MySQL avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")



