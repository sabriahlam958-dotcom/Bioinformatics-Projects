def initialize_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([0] * cols)
    return matrix

def score_alignment(seq1, seq2):
    MATCH = 1
    MISMATCH = -1
    GAP = -2
    
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    matrix = initialize_matrix(rows, cols)
    
    for i in range(rows):
        matrix[i][0] = i * GAP
    for j in range(cols):
        matrix[0][j] = j * GAP
        
    for i in range(1, rows):
        for j in range(1, cols):
            if seq1[i-1] == seq2[j-1]:
                diagonal_score = matrix[i-1][j-1] + MATCH
            else:
                diagonal_score = matrix[i-1][j-1] + MISMATCH
                
            up_score = matrix[i-1][j] + GAP
            left_score = matrix[i][j-1] + GAP
            
            matrix[i][j] = max(diagonal_score, up_score, left_score)
            
    return matrix

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
    print("-" * 50)
    
    print("Generating DNA Alignment Scoring Matrix...")
    scoring_matrix = score_alignment("ATCG", "ATG")
    
    print("\nSample Matrix for (ATCG) vs (ATG):")
    for row in scoring_matrix:
        print(row)
