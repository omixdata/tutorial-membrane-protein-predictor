from flask import Flask, request, render_template
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("data/model.pickle", "rb"))

def get_protein_composition(sequence):
	protein_analysis = ProteinAnalysis(sequence)
	return protein_analysis.get_amino_acids_percent()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():

    sequence = request.form['sequence']
    protein_data = get_protein_composition(sequence)
    dataframe = pd.DataFrame([protein_data])
    
    prediction = model.predict(dataframe)[0]
    probability = model.predict_proba(dataframe)[0][1]

    if prediction:
        location = "Membrane"
    else:
        location = "Cytoplasm"

    return render_template('index.html', 
                           result={"location": location, 
                                   "probability": probability,
                                   "sequence": sequence})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)