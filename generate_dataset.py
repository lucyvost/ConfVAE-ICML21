import rdkit
from rdkit import Chem
import random
import numpy as np
import pickle 

list_to_pickle = []

n_data_points = 100
atom_types = ['C', 'N', 'O']
p = np.random.uniform(-2, 2, (n_data_points,3))
for n in range(n_data_points):
    #generate 3D coordinates randomly
    pos = p[n]

    atomType = random.choice(atom_types)

    fakelig = atomType
    #fakelig += f'.{atomType}'
    molPharmProf = Chem.MolFromSmiles(fakelig)
    
    #Now add the 3d position to each atom
    conf = Chem.Conformer(molPharmProf.GetNumAtoms())
    
    
    conf.SetAtomPosition(0, pos)

    conf.SetId(0)
    molPharmProf.AddConformer(conf)

    list_to_pickle.append(molPharmProf)

    Chem.MolToMolFile(molPharmProf, f'data/{n}.sdf')
with open('small_train_set.pkl', 'wb') as f:  # open a text file
    pickle.dump(list_to_pickle, f) # serialize the list
