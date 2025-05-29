import re
import matplotlib.pyplot as plt
import numpy as np

# Path to your log file
log_file = "logs/beam_search_bleu/bleu_scores.txt"

beam_sizes = []
bleu_scores = []
generation_times = [] 

current_beam = None

with open(log_file, "r", encoding="utf-8") as f:
    for line in f:
        # Find beam size
        beam_match = re.match(r'Beam size:\s*(\d+)', line)
        if beam_match:
            current_beam = int(beam_match.group(1))
            continue

        # Find BLEU score
        bleu_match = re.search(r'"score":\s*([\d.]+)', line)
        if bleu_match and current_beam is not None:
            bleu = float(bleu_match.group(1))
            beam_sizes.append(current_beam)
            bleu_scores.append(bleu)

# ===========================
# Manually copied generation times from my console
generation_times = [9.77, 87.77, 376.47, 505.44, 638.45, 731.15, 988.14, 860.6, 1099.16, 1670.74]

# ===========================
# Plot BLEU scores
# ===========================
plt.figure(figsize=(10, 6))
plt.plot(beam_sizes, bleu_scores, marker="o", label="BLEU Score")
plt.xlabel("Beam Size")
plt.ylabel("BLEU Score")
plt.title("BLEU Score vs. Beam Size")
plt.grid(True)
plt.legend()
plt.savefig("bleu_vs_beam.png", dpi=300)
plt.close()

# ===========================
# Plot Generation Time
# ===========================
plt.figure(figsize=(10, 6))
plt.plot(beam_sizes, generation_times, marker="o", color="orange", label="Generation Time (sec)")
plt.xlabel("Beam Size")
plt.ylabel("Generation Time (seconds)")
plt.title("Generation Time vs. Beam Size")
plt.grid(True)
plt.legend()
plt.savefig("time_vs_beam.png", dpi=300)
plt.close()

print("Plots saved: 'bleu_vs_beam.png' and 'time_vs_beam.png'")
