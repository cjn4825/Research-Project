import matplotlib.pyplot as plt
import numpy as np

securityTools = [
    "CrowdStrike Falcon",
    "SentinelOne",
    "Defender XDR",
    "Avast Free AV",
    "Bitdefender AV",
    "Defender AV"
]

socRequirement = [3, 3, 2, 1, 1, 1]
tuning = [3, 3, 2, 1, 2, 2]
detectionApproach = [3, 3, 3, 1, 2, 1]
updateFrequency = [3, 3, 3, 2, 2, 2]

complexity = np.array(socRequirement) + np.array(tuning)+ np.array(detectionApproach) + np.array(updateFrequency)
adaptability = np.array(detectionApproach) + np.array(tuning)  + np.array(updateFrequency)
effectiveness = np.array(detectionApproach) + np.array(updateFrequency)

def normalize(a):
    return (a - np.min(a)) / (np.max(a) - np.min(a))

complexityScore = normalize(complexity)
effectivenessScore = normalize(effectiveness)
adaptabilityScore = normalize(adaptability)

numTools = len(securityTools)
x = np.arange(numTools)

fig, ax = plt.subplots(figsize=(14.44, 6.73))
barWidth = 0.2

ax.bar(x - 1.5*barWidth, socRequirement, barWidth, label='SOC Requirement')
ax.bar(x - 0.5*barWidth, tuning, barWidth, label='Tuning Requirement')
ax.bar(x + 0.5*barWidth, detectionApproach, barWidth, label='Detection Approach')
ax.bar(x + 1.5*barWidth, updateFrequency, barWidth, label='Update Frequency')

ax.set_ylabel('Score (1-3)')
ax.set_title('Security Tool Metrics')
ax.set_xticks(x)
ax.set_xticklabels(securityTools, rotation=45, ha='right')
ax.legend()
plt.tight_layout()

plt.savefig("data.png", dpi=300)
print("   complexity: ", complexityScore)
print(" adaptability: ", adaptabilityScore)
print("effectiveness: ", effectivenessScore)
