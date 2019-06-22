from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO
import pandas as pd

def get_protein_composition(sequence):
	protein_analysis = ProteinAnalysis(sequence)
	return protein_analysis.get_amino_acids_percent()

cyt_proteins = SeqIO.parse(open("data/cyt_proteins.fasta"), 'fasta')
mem_proteins = SeqIO.parse(open("data/mem_proteins.fasta"), 'fasta')

dataset_raw = []

for protein in cyt_proteins:
	protein_data = get_protein_composition(str(protein.seq))
	protein_data['mem'] = False
	dataset_raw.append(protein_data)

for protein in mem_proteins:
	protein_data = get_protein_composition(str(protein.seq))
	protein_data['mem'] = True
	dataset_raw.append(protein_data)

pd.DataFrame(dataset_raw).to_csv("data/dataset.csv", index=False)
