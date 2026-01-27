# Installation : pip install wilds
from wilds import get_dataset

# 1. Télécharger le dataset (ça gère tout tout seul)
# Cela va télécharger les données dans le dossier "data"
dataset = get_dataset(dataset="camelyon17", download=True, root_dir="../data")

# 2. Vérifier ce qu'on a
print("Nombre de patchs:", len(dataset))