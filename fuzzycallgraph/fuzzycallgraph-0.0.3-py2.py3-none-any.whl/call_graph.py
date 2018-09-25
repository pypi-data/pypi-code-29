from collections import namedtuple
import sys
from typing import Iterable, Tuple, List, Set


class Function(namedtuple('Function', 'name signature body')):
    def calls(self, other_fn) -> bool:
        return other_fn.name in self.body
    
    def __repr__(self):
        return f"{self.name} :: {self.signature[self.signature.index('('):].rstrip()[:-1]}"


Signature = str
Name = str
Body = str


def dependencies(f: Function, possible_dependencies: Set[Function]) -> Set[Function]:
    return {
        g for
        g in possible_dependencies
        if f.calls(g) 
    }


def dependents(f: Function, possible_dependents: Set[Function]) -> Set[Function]:
    return {
        g for
        g in possible_dependents
        if g.calls(f)
    }


def fn_name(line: str) -> str:
    return line[line.index(' ') + 1 : line.index('(')]


# Nodes
# TODO - regex
def parse_names(signatures: List[Signature]) -> List[Name]:
    for s in signatures:
        assert s.startswith('def'), f'ERROR: not a signature: "{s}"'

    return list(map(fn_name, signatures))
    

def parse_signatures(lines: List[str]) -> List[Signature]:
    return [
        line
        for line in lines
        if line.startswith('def')
    ]


def parse_function(lines: List[str], start=0) -> Tuple[Body, int]:
    assert start < len(lines), f'Line number {start} out of bounds'

    i = start
    
    while not lines[i].startswith('def'):
        i += 1
        
    j = i + 1

    while j < len(lines) and not lines[j].startswith('def'):
        j += 1
    
    next_function = lines[i:j]
    return next_function, j
    

# One requirement for edges    
def parse_bodies(lines: List[str]) -> List[Body]:
    i = 0
    bodies = []
    while len(lines) > i:
        fn_body, i = parse_function(lines, i)
        bodies.append(''.join(fn_body[1:]))
    return bodies
    
  
def parse_functions(pathname: str):
    import sys

    with open(pathname) as fp:
        source_code = fp.readlines()

    signatures: List[Signature] = parse_signatures(source_code)

    names: List[Name] = parse_names(signatures)

    bodies: List[Body] = parse_bodies(source_code)

    fs: List[Function] = [ 
        Function(signature=s, name=n, body=b) 
        for s, n, b in zip(signatures, names, bodies)
    ]
    return fs

def generate_call_graph(pathname: str):
    all_functions: List[Function] = parse_functions(pathname)

    edges = [ 
        f'  {fn.name} -> {g.name};' 
        for fn in all_functions 
        for g in dependencies(fn, all_functions)
    ]
    print('digraph G {')
    for edge in edges: 
        print(edge)
    print('}')


def main():
    generate_call_graph(sys.argv[1])

if __name__ == '__main__':
    draw(sys.argv[1]) # ...no?
