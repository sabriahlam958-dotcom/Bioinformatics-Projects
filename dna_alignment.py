def analyze_dna(reference_dna, patient_dna):
    if len(reference_dna) != len(patient_dna):
        return 0, ["Error: DNA strands must be of equal length."]
        
    mutations = []
    for i in range(len(reference_dna)):
        if reference_dna[i] != patient_dna[i]:
            mutations.append(f"Pos {i+1}: {reference_dna[i]} -> {patient_dna[i]}")
            
    similarity = ((len(reference_dna) - len(mutations)) / len(reference_dna)) * 100
    return similarity, mutations

if __name__ == "__main__":
    print("--- Running Molecular Mutation & DNA Alignment Engine ---")
    ref_sequence = "ATGCGATCGATCGATCGATCGATC"
    pat_sequence = "ATGGGATCGATCGTTCGATCGATC"
    sim_score, mutation_list = analyze_dna(ref_sequence, pat_sequence)
    print(f"Global Alignment Score (Similarity): {sim_score:.2f}%")
