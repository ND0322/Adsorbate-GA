from ase.ga.data import DataConnection, PrepareDB

# Instantiate the db
db_name = "/home/nathan/Adsorbate-GA/ridge_Ni110Pt37_ads.db"

# Connect to the db
db = DataConnection(db_name)

best_id, best_fitness = db.get_best_candidate()

print(best_id, best_fitness)