import sys
import math
import re
import os

class Atom(list):
    def __init__(self, name, num, x, y, z):
        self.name = name
        self.num = num
        self.extend([x, y, z])

class Residue(list):
    def __init__(self, name, num, atoms):
        self.name = name
        self.num = num
        self.extend(atoms)

    def atom(self, name):
        for atom in self:
            if atom.name == name:
                return atom
        print "Couldn't find atom '%s'" % name
        write_residue(r)
        quit()

class Chain(list):
    def __init__(self, name, residues):
        self.name = name
        self.extend(residues)

    def residue(self, n):
        for r in self:
            if r.num == n:
                return r
        print "Couldn't find residue %d in chain %s" % (n, self.name)
        quit()

class Model(list):
    def __init__(self, num, chains):
        self.num = num
        self.extend(chains)

    def residue(self, n):
        for c in self:
            for r in c:
                if r.num == n:
                    return r
        print "Couldn't find residue %d" % n
        quit()

class Structure(list):
    def __init__(self, name, models):
        self.name = name
        self.extend(models)

    def model(self, n):
        for m in self:
            if m.num == n:
                return m
        print "Couldn't find Model %d" % n
        quit()

class ParsedLine:
    def __init__(self, line):
        self.atom_name = line[12:16].strip()
        self.res_name = line[17:20].strip()
        self.chain_name = line[20:22].strip()
        self.atom_num = int(line[6:11].strip())
        self.res_num = int(line[22:26].strip())
        self.x = float(line[30:38].strip())
        self.y = float(line[38:46].strip())
        self.z = float(line[46:54].strip())

class PdbParser:
    def __init__(self, file_name):
        self.atoms = []
        self.residues = []
        self.chains = []
        self.models = []
        self.oline = ''
        self.model_num = 1
        i = 0
        for line in open(file_name):
            if (line[0:4] == "ATOM"):
                line = ParsedLine(line)
                if i > 0:
                    if line.chain_name != self.oline.chain_name:
                        self.add_chain()
                    elif line.res_num != self.oline.res_num or line.res_name != self.oline.res_name:
                        self.add_residue()
                self.atoms.append(Atom(line.atom_name, line.atom_num, line.x, line.y, line.z))
                self.oline = line
                i += 1
            elif line[0:5] == "MODEL":
                self.add_model()
                g = re.split('\s+', line)
                if len(g) >= 2:
                    try:
                        self.model_num = int(g[1])
                    except ValueError:
                        pass
            elif line[0:6] == "ENDMDL":
                self.add_model()
            elif line[0:3] == "TER":
                self.add_chain()
        self.add_model()
        self.structure = Structure(os.path.splitext(file_name)[0], self.models)

    def add_residue(self):
        if len(self.atoms) > 0:
            self.residues.append(Residue(self.oline.res_name, self.oline.res_num, self.atoms))
            self.atoms = []

    def add_chain(self):
        self.add_residue()
        if len(self.residues) > 0:
            self.chains.append(Chain(self.oline.chain_name, self.residues))
            self.residues = []

    def add_model(self):
        self.add_chain()
        if len(self.chains) > 0:
            self.models.append(Model(self.model_num, self.chains))
            self.chains = []
            self.model_num += 1

def write_structure(structure, f = sys.stdout):
    model_index = 0
    for model in structure:
        f.write("MODEL%6d\n" % (model_index + 1,))
        write_model(model, f)
        f.write("ENDMDL\n")
        model_index += 1
    f.write("END\n")

def write_model(model, f = sys.stdout):
    atom_index = 0
    for chain in model:
        for residue in chain:
            for atom in residue:
                f.write("ATOM%7i  %-4s%3s%2s%4i%12.3lf%8.3lf%8.3lf%6.2f%6.2f%12c  \n" % \
                    (atom_index+1, atom.name , residue.name , chain.name , residue.num, atom[0], atom[1], atom[2] , 1.00 , 0.00, atom.name[0]))
                atom_index += 1

def write_residue(residue):
    num_atom = 1
    for atom in residue:
        print "ATOM%7i  %-4s%3s%2s%4i%12.3lf%8.3lf%8.3lf%6.2f%6.2f%12c  \n" % \
            (num_atom, atom.name , residue.name , chain.name , residue.num, atom[0], atom[1], atom[2] , 1.00 , 0.00, atom.name[0]),
    num_atom += 1
 
