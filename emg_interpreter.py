import numpy as np

def calculate_rms(signal, window_size=50):
    """Calculates the Root Mean Square (RMS) to detect signal amplitude changes."""
    return np.sqrt(np.convolve(signal**2, np.ones(window_size)/window_size, mode='same'))

def simulate_and_analyze_emg():
    print("--- Running Intelligent Bio-Signal Interpreter ---")
    
    np.random.seed(42)  # For consistent simulation results
    time = np.linspace(0, 1, 1000)
    
    # Simulate realistic EMG data: Rest phase followed by Muscle Activation phase
    rest_signal = np.random.normal(0, 0.1, 1000)
    action_signal = np.random.normal(0, 0.6, 1000)
    full_bio_data = np.concatenate([rest_signal, action_signal])
    
    # Advanced feature extraction using RMS
    rms_envelope = calculate_rms(full_bio_data, window_size=100)
    
    # Threshold detection
    activation_threshold = 0.3
    detected_movements = rms_envelope > activation_threshold
    
    # Performance and biological metrics calculation
    total_activations = np.sum(detected_movements)
    max_amplitude = np.max(np.abs(full_bio_data))
    mean_resting_noise = np.mean(np.abs(rest_signal))
    
    print("Signal Processing Complete.")
    print(f"-> Maximum Signal Amplitude: {max_amplitude:.4f} mV")
    print(f"-> Baseline Resting Noise (Mean): {mean_resting_noise:.4f} mV")
    print(f"-> Active Contraction Duration: {total_activations} samples crossed threshold.")
    
    if total_activations > 0:
        print("-> System Status: Muscle Contraction successfully detected for Bionic control.")
    else:
        print("-> System Status: Muscle is at rest or signal is too weak.")

if __name__ == "__main__":
    simulate_and_analyze_emg()
