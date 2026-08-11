import pandas as pd
import pickle
import os

# Ensure models folder exists
os.makedirs('models', exist_ok=True)

# 0. Save symptom_list.pkl from Training.csv
train_df = pd.read_csv('Dataset/Training.csv')
symptom_list = train_df.columns[:-1].tolist()  # All columns except 'prognosis'
with open('models/symptom_list.pkl', 'wb') as f:
    pickle.dump(symptom_list, f)
print("✅ models/symptom_list.pkl saved successfully.")

# 1. Save description.pkl
desc_df = pd.read_csv('Dataset/description.csv')
desc_dict = pd.Series(desc_df.Description.values, index=desc_df.Disease).to_dict()
with open('models/description.pkl', 'wb') as f:
    pickle.dump(desc_dict, f)
print("✅ models/description.pkl saved successfully.")

# 2. Save precautions.pkl
prec_df = pd.read_csv('Dataset/precautions_df.csv')
precaution_dict = prec_df.set_index('Disease').T.apply(lambda x: x.dropna().tolist()).to_dict()
with open('models/precautions.pkl', 'wb') as f:
    pickle.dump(precaution_dict, f)
print("✅ models/precautions.pkl saved successfully.")

# 3. Save medications.pkl
med_df = pd.read_csv('Dataset/medications.csv')
med_dict = med_df.groupby('Disease')['Medication'].apply(list).to_dict()
with open('models/medications.pkl', 'wb') as f:
    pickle.dump(med_dict, f)
print("✅ models/medications.pkl saved successfully.")

# 4. Save workouts.pkl
workout_df = pd.read_csv('Dataset/workout_df.csv')
workout_dict = workout_df.groupby('disease')['workout'].apply(list).to_dict()
with open('models/workouts.pkl', 'wb') as f:
    pickle.dump(workout_dict, f)
print("✅ models/workouts.pkl saved successfully.")

# 5. Save diets.pkl
diet_df = pd.read_csv('Dataset/diets.csv')
diet_dict = diet_df.groupby('Disease')['Diet'].apply(list).to_dict()
with open('models/diets.pkl', 'wb') as f:
    pickle.dump(diet_dict, f)
print("✅ models/diets.pkl saved successfully.")

print("🎉 All .pkl files saved to /models")
