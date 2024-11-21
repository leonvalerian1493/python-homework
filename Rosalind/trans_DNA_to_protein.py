# # RNA Codon Table
# codon_table = {
#     "AUG": "M", "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
#     "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
#     "UAU": "Y", "UAC": "Y", "UGU": "C", "UGC": "C",
#     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
#     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
#     "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
#     "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
#     "AUU": "I", "AUC": "I", "AUA": "I", "GUU": "V", "GUC": "V",
#     "GUA": "V", "GUG": "V", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
#     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAU": "D", "GAC": "D",
#     "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
#     "UAA": "Stop", "UAG": "Stop", "UGA": "Stop"
# }

# def translate_rna_to_protein(rna):
#     protein = []
#     # Iterate through RNA string in chunks of 3 (codons)
#     for i in range(0, len(rna), 3):
#         codon = rna[i:i+3]
#         amino_acid = codon_table.get(codon, "")
#         if amino_acid == "Stop":
#             break
#         if amino_acid:  # Ignore empty or invalid codons
#             protein.append(amino_acid)
#     return "".join(protein)

# # Sample dataset
# rna_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

# # Translate RNA to Protein
# protein_string = translate_rna_to_protein(rna_string)
# print(protein_string)
