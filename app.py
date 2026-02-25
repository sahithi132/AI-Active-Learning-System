import random

print("AI Active Learning System Running...")

data = list(range(1000))
labeled = []

budget = 10

for i in range(budget):
    sample = random.choice(data)
    labeled.append(sample)
    data.remove(sample)

print("Selected samples:", labeled)
print("Remaining unlabeled data:", len(data))
