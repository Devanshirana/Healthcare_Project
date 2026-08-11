import pickle  # Make sure this is at the top of your file

# Load the model using the absolute path
model = pickle.load(open('/Applications/Projects/Healthcare_project/models/svc.pickle', 'rb'))

# Now you can use the model, for example:
print(type(model))  # This will show the type of the loaded model
