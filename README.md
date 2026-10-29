# Bioinformatics & Technical Bionics Projects

Welcome to my repository dedicated to technical bionics and bioinformatics algorithms. This project implements structural DNA alignment and biological signal processing tools using Python.

## 🧬 Project Structure

The repository contains the following core components:

*   **`dna_alignment.py`**: A molecular sequence alignment engine. It features dynamic mutation tracking and scoring matrix generation (inspired by the Needleman-Wunsch algorithm) to evaluate similarity between genetic sequences.
*   **`emg_interpreter.py`**: A framework designed for processing and interpreting Electromyography (EMG) signals to bridge biological muscle activity with bionic applications.

## 🚀 Features implemented

### 1. DNA Sequence Analysis
*   **Mutation Spotting**: Scans sequences of equal length to locate precise nucleic acid substitutions.
*   **Dynamic Matrix Initialization**: Generates flexible zero-matrices calibrated with custom dimension scaling (+1 for gap factoring).
*   **Alignment Scoring**: Computes match awards, mismatch penalties, and gap costs across an optimal scoring matrix grid.

### 2. Bionic Signal Processing
*   Modular setup for parsing electrical biosignals to decode physical muscle movements.

## 🛠️ How to Run Locally

To test these scripts on your local machine, make sure you have Python installed, then run:

```bash
python dna_alignment.py
```

## 📝 Future Scope
*   Implement full global/local alignment traceback paths.
*   Integrate real-time digital filtering for raw EMG signal visualization.
