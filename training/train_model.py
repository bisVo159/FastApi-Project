import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from training.train_utils import DATA_FILE_PATH, MODEL_DIR, MODEL_PATH

df=(pd
    .read_csv(DATA_FILE_PATH)
    .drop(columns=['name','model','edition'])
    .drop_duplicates()
)

X=df.drop(columns=['selling_price'])
y=df.selling_price.copy()

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

num_cols=X.select_dtypes(include=['int64','float64']).columns.to_list()
cat_cols=X.select_dtypes(include=['O']).columns.to_list()

num_pipeline=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='median')),
    ('scaler',StandardScaler())
])
cat_pipeline=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='constant',fill_value='missing')),
    ('onehot',OneHotEncoder(handle_unknown='ignore',sparse_output=False))
])

preprocessor=ColumnTransformer(transformers=[
    ('num',num_pipeline,num_cols),
    ('cat',cat_pipeline,cat_cols)
])
model=Pipeline(steps=[
    ('preprocessor',preprocessor),
    ('regressor',RandomForestRegressor(n_estimators=10,max_depth=5,random_state=42))
])

model.fit(X_train,y_train)

if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)
joblib.dump(model,MODEL_PATH)
print(f'Model saved to {MODEL_PATH}')
