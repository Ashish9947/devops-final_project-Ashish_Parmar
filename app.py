import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import gradio as gr

data = pd.read_csv('https://github.com/mbburova/MDS/raw/main/house_prices_small.csv')
tr, te = train_test_split(data)
x_train = tr.drop(['SalePrice'], axis=1)
y_train = tr.SalePrice
x_test = te.drop(['SalePrice'], axis=1)
y_test = te.SalePrice   
transform = ColumnTransformer([('scale', StandardScaler(), ['LotArea', 'YearBuilt']),
                               ('oh', OneHotEncoder(), ['SaleCondition'])], remainder='passthrough')
pipe = Pipeline([('col_transform', transform),
                 ('regression', LinearRegression())])

pipe.fit(x_train, y_train)

def f(LotArea, OverallQual, SaleCondition, YearBuilt):
    d = pd.DataFrame({'LotArea': [LotArea], 'OverallQual': [OverallQual], 'SaleCondition': [SaleCondition], 'YearBuilt': [YearBuilt]})
    return pipe.predict(d)[0]

app = gr.Interface(fn=f, inputs=["text", gr.inputs.Slider(1, 10), gr.Radio(['Normal', 'Abnorml', 'Partial', 'AdjLand', 'Alloca', 'Family']), "text"], outputs="text")
app.launch(debug=True)