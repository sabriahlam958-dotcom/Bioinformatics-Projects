import numpy as np
import matplotlib.pyplot as plt

def simulate_and_analyze_emg():
    print("--- Running Intelligent Bio-Signal Interpreter ---")
    
    time = np.linspace(0, 1, 1000)
    rest_signal = np.random.normal(0, 0.1, 1000)
    action_signal = np.random.normal(0, 0.6, 1000)
    
    full_bio_data = np.concatenate([rest_signal, action_signal])
    
    activation_threshold = 0.4
    detected_movements = np.abs(full_bio_data) > activation_threshold
    
    total_activations = np.sum(detected_movements)
    print(f"Signal Processing Complete. Detected {total_activations} neural threshold crossings.")

if __name__ == "__main__":
    simulate_and_analyze_emg()
