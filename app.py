import random

print("🚀 AI Active Learning System Running...")

# Simulated dataset (unlabeled pool)
data = list(range(1000))
labeled = []

# Labeling budget
budget = 20

print(f"Initial unlabeled data size: {len(data)}")
print(f"Labeling budget: {budget}")

def uncertainty_sampling(dataset):
    """
    Simulated uncertainty:
    Here we randomly select, but in real systems
    this would use model prediction confidence.
    """
    return random.choice(dataset)

for i in range(budget):
    sample = uncertainty_sampling(data)
    labeled.append(sample)
    data.remove(sample)
    print(f"Step {i+1}: Selected sample -> {sample}")

print("\n✅ Active Learning Completed")
print("Total labeled samples:", len(labeled))
print("Remaining unlabeled samples:", len(data))
