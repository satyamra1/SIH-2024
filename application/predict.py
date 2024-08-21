import sqlite3
import pandas as pd
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../db_directory/test.db")
with sqlite3.connect(db_path) as db:
    
    data=pd.read_sql_query("SELECT * from Basic", db)




#---------------------------------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
#data = pd.read_csv('basic.csv')

# Define features and target
features = ['State', 'District', 'Variety', 'Min_x0020_Price', 'Max_x0020_Price']
target = 'Modal_x0020_Price'

# Split the data into features and target
X = data[features]
y = data[target]

# Define preprocessor for the pipeline with handle_unknown='ignore'
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Min_x0020_Price', 'Max_x0020_Price']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['State', 'District', 'Variety'])
    ])

# Create a pipeline that first preprocesses the data and then applies a linear regression model
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions
y_pred = pipeline.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Example of making a prediction with new data
new_data = pd.DataFrame({
    'State': ['Kerala'],
    'District': ['Kottayam'],
    'Variety': ['Potato'],
    'Min_x0020_Price': [4400],
    'Max_x0020_Price': [4600]
})

# Predict modal price for new data


