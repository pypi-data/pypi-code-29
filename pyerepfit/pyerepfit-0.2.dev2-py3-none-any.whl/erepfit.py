#!/usr/bin/env python3

import argparse
import os
import sys
import json
import jsonschema
import yaml
import jsonpickle
import numpy as np

from . import evaluator
from .inputdata import ErepfitInput
from .rep_basis import PolynomialRepulsive, BasisRepulsiveModel
from .rep_spline import RepulsivePotenial, Spline4RepulsiveModel
from . import rep_model
from . import utils
from . import equation_solver
import os

from pyerepfit import __version__

def print_header(output_stream):
    print(
"""
===============================================================================

    PyErepfit v{}
    Powered by Chien-Pin Chou

===============================================================================
""".format(__version__), file=output_stream
    )

            
def run_erepfit(options, output_stream=sys.stdout):

    parser = argparse.ArgumentParser()
    parser.add_argument("-y", dest='yaml', help='Parse input as YAML format', action='store_true')
    parser.add_argument("-e", dest='evaluate_only', help='Evaluate the DFTB only', action='store_true')
    parser.add_argument("-f", dest='fitting_only', help='Fitting the repulsive only', action='store_true')
    hasPrint = False
    try:
        import matplotlib.pyplot as plt
        parser.add_argument("-p", dest='print', help='Print the repulsive to eps', action='store_true')
        hasPrint = True
    except:
        pass
    parser.add_argument("-o", dest='output_file', help='Output file', type=str)
    parser.add_argument("input_file_path", help="Input file path")

    opt = parser.parse_args(options)

    if (opt.output_file):
        output_stream = open(opt.output_file, 'w')

    print_header(output_stream)

    print('Reading input schema.', file=output_stream)
    with open(os.path.join(os.path.dirname(__file__), 'erepfit_input_schema.json'), 'r') as f:
        input_schema = json.load(f)

    if (opt.yaml):
        print('Reading input file as YAML', file=output_stream)
        with open(opt.input_file_path, 'r') as f:
            input_file = yaml.load(f)
    else:
        print('Reading input file as JSON', file=output_stream)
        with open(opt.input_file_path, 'r') as f:
            input_file = json.load(f)

    print('Validate input file.', file=output_stream)
    jsonschema.validate(input_file, input_schema)

    erepfit_input = ErepfitInput(input_file)

    erepfit_input.electronic_slater_koster_files.adjust_path(os.path.abspath(os.curdir))

    
    # if only evaluate electronic reference values
    if (opt.evaluate_only or not opt.fitting_only):
        print('Testing DFTB implementation for parameterization...', file=output_stream)
        dftb_path = erepfit_input.options['toolchain']['path']
        if not os.path.isabs(dftb_path):
            dftb_path = os.path.expanduser(dftb_path)
        dftb_path = os.path.expandvars(dftb_path)
        if not os.path.isabs(dftb_path):
            dftb_path = utils.which(dftb_path)

        succ = evaluator.test_dftb_binary(dftb_path)
        if (succ):
            print('  {} => working'.format(dftb_path), file=output_stream)
        else:
            print('  {} => not working'.format(dftb_path), file=output_stream)
            sys.exit(1)
        
        
        evaluator.evaluate(erepfit_input)
        print('\nEvaluate DFTB...done', file=output_stream)

        jsonpickle.set_encoder_options('simplejson', indent=4)
        jsonpickle.set_encoder_options('json', indent=4)
        
        with open('evaluated.json', 'w') as f:
            js = jsonpickle.encode(erepfit_input, unpicklable=False)
            print(js, file=f)
    
    elif (opt.fitting_only or not opt.evaluate_only):

        rep_models = []
        rep_names = []
        poten_type = erepfit_input.options.get("potential_type")
        
        for k, v in erepfit_input.potential_grids.items():
            if (k in erepfit_input.external_repulsive_potentials):
                print('Repulsive {} found in external repulsuive potentials, will not be fitted.'.format(k), file=output_stream)
                continue
            if (poten_type == "polynomial"):
                cutoff = v['knots'][-1]
                model = BasisRepulsiveModel(cutoff, minimal_order=3, order=9, start=v['knots'][0])
            else: 
                model = Spline4RepulsiveModel(v['knots'])
            rep_names.append(k)
            rep_models.append(model)


        collection = rep_model.RepulsiveModelCollection(rep_names, rep_models)

        builder = rep_model.RepulsivePotentialEquationBuilder(erepfit_input)
        builder.build_linear_equations(collection)

        print("", file=output_stream)
        print(collection.description(), file=output_stream)
                
        
        if (poten_type == "polynomial"):
            solver = equation_solver.GeneralSolver()
        else:
            solver = equation_solver.ContinuitySolver(3)
        
        builder.solve(collection, solver)
        builder.print_residuals(output_stream)

        print('Resulting Repulsive Potentials:', file=output_stream)
        output_prefix = erepfit_input.options.get("output_prefix", "./")
        os.makedirs(output_prefix, exist_ok=True)
        for ind in range(len(collection.rep_names)):
            rep_name = collection.rep_names[ind]
            spl_rep = collection.resulting_repulsives[ind]
            reversed_rep_name = '{}-{}'.format(*reversed(rep_name.split('-')))

            with open(os.path.join(output_prefix, '{}.skf'.format(rep_name)), 'w') as fout:
                print(spl_rep, file=fout)
            if (reversed_rep_name != rep_name):
                with open(os.path.join(output_prefix, '{}.skf'.format(reversed_rep_name)), 'w') as fout:
                    print(spl_rep, file=fout)
            
            print(rep_name, file=output_stream)
            print(spl_rep, file=output_stream)

            if (hasPrint and opt.print):
                plt.figure()
                output_fig = os.path.join(output_prefix, '{}.eps'.format(rep_name))
            
                plt.title(rep_name)
                # plt.ylim(-2, 2)

                styles = ['c--', 'r--', 'g--']
                labels = ['Rep. Potential', '1st derivative', '2nd derivative']
                for i in range(3):
                    xs = np.linspace(spl_rep.knots[0]-0.2, spl_rep.knots[-1], num=100)
                    ys = []
                    for r in xs:
                        v = spl_rep.eval(r, i)
                        ys.append(v)
                    if (i==0):
                        maxv = max(ys)
                        minv = min(ys)
                        plt.ylim(min(minv, max(-0.5, -maxv)), maxv)
                    plt.plot(xs, ys, styles[i], linewidth=1, label=labels[i])
                    
                plt.legend(loc='upper right')
                plt.xlabel('Diatomic Distance [a.u.]')
                plt.ylabel('Energy [a.u.]')
                plt.savefig(output_fig, format='eps')

        print('End of pyerepfit Program', file=output_stream)        
    
            

if __name__ == '__main__':

    run_erepfit(sys.argv[1:])



