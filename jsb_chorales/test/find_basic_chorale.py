import csv
import numpy as np
from pathlib import Path

test_dir = Path("/Users/yasinsensoy/Desktop/ex05/jsb_chorales/test")
results = []

for f in sorted(test_dir.glob("*.csv")):
    chorale = []
    with open(f) as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            chorale.append([int(n) for n in row])
    
    arr = np.array(chorale)
    unique = len(np.unique(arr))
    results.append((f.name, len(chorale), unique))

# Uzunluğa göre sırala
results.sort(key=lambda x: x[1])

print(f"{'Dosya':<25} {'Adım':>6} {'Unique Nota':>12}")
print("-" * 45)
for name, steps, unique in results[:10]:
    print(f"{name:<25} {steps:>6} {unique:>12}")
