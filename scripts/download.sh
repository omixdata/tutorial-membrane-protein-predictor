wget -O data/cyt_proteins.fasta \
	"https://www.uniprot.org/uniprot/?query=locations%3A%28location%3ASL-0086%29+taxonomy%3Abacteria+AND+reviewed%3Ayes&sort=score&format=fasta"
wget -O data/mem_proteins.fasta \
	"https://www.uniprot.org/uniprot/?query=locations%3A%28location%3A%22Membrane%22%29+taxonomy%3Abacteria+AND+reviewed%3Ayes&sort=score&format=fasta"
