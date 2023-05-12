from flask import Flask, request
import pandas as pd

df = pd.read_csv('./data/diagnoses2019.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is a API service for Minnesota ICD code details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/icd', methods=["GET"])
def preview():
    #R73
        filter_value = request.args.get(icdcode)
        filtered = df[df['principal_diagnosis_code']] == filter_value
        return filtered.to_json(orient="records")

if __name__ == '__main__':
    app.run(debug=True)
