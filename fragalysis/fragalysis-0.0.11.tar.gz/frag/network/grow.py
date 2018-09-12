from .query import get_full_graph
from rdkit import Chem

DATA_DICT = {}
TOT_SET = set()

def iterate(input_smiles,counter,num_iterations):
    global DATA_DICT
    counter += 1
    if counter > num_iterations:
        return
    num_start = Chem.MolFromSmiles(input_smiles).GetNumHeavyAtoms()
    results = get_full_graph(input_smiles, graph_url="neo4j")
    for vector in results:
        for new_smiles in results[vector]:
            diff = Chem.MolFromSmiles(new_smiles).GetNumHeavyAtoms()-num_start
            if new_smiles not in TOT_SET:
                TOT_SET.add(new_smiles)
                DATA_DICT[num_iterations].add(new_smiles)
            iterate(new_smiles,counter,num_iterations)

def grow_smiles(smiles='CC(C)C(=O)Nc1cccc(C#N)c1',num_iterations=10):
    global DATA_DICT
    counter = -1
    for i in range(num_iterations):
        DATA_DICT[i] = set()
    iterate(smiles,counter,num_iterations)
