from ase.db import connect
import matplotlib.pyplot as plt

ids = []
e = []

with connect("ridge_Ni110Pt37_ads.db") as db:
    for row in db.select():
        pe = row.key_value_pairs.get('potential_energy')
        if pe is not None:
            ids.append(row.id)
            e.append(pe)

plt.figure(figsize=(8,5))
plt.plot(ids, e, marker='o', linestyle='-', color='tab:blue')
plt.xlabel("generation")
plt.ylabel("Potential energy (eV)")
plt.title("Potential energy of generations of GA")
plt.grid(True)
plt.tight_layout()
plt.show()