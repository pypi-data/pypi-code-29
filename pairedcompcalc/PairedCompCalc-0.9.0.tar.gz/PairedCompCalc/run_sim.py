"""Script to simulate paired-comparison experiments with one group of listeners,
and store individual results in files with same structure as real experiments.
Copy this script and use as a template for other simulations.

Data can be generated using either
(1): the Thurstone Case V model, pc_simulator.SubjectThurstone, OR
(2): the Bradley-Terry-Luce model, pc_simulator.SubjectBradley.

NOTE: for now, these methods can only simulate ONE population at a time,
i.e., only ONE group and ONE attribute.
More than one (test_factor, tf_category) pair may be given, but
the population distribution will be the same in all test conditions.
This may be extended in future versions.

*** Version history:
2017-11-20, tested by comparison to MatLab analysis package
2018-07-30, tested with new simulator signature
"""

# ************* generate different groups, test-conditions, attributes in single run?

import numpy as np
from pathlib import Path

# import PairedCompCalc.pc_simulator as pcs
from PairedCompCalc.pc_simulator import PairedCompSimulator
from PairedCompCalc.pc_simulator import SubjectThurstone, SubjectBradley
from PairedCompCalc.pc_data import PairedCompFrame

result_path = Path('../test_sim')

n_systems = 3

attributes = ['SimQual0', 'SimQual1', 'SimQual2']
quality = [[0, -0.5, -1.],
           [0., 0.5, 1.],
           [0., -1., 0.5]]

pcf = PairedCompFrame(attributes=attributes[:1],  # *** can only simulate ONE attribute at a time ******
                      systems=[f'S{i}' for i in range(n_systems)],
                      forced_choice=False,
                      response_labels=['Equal', 'Slightly Better', 'Better', 'Much Better'],
                      test_factors={'SNR': ['Low', 'High']}
                      )

pc = PairedCompSimulator(pcf,
                         quality_mean=quality[0],
                         quality_std=0.3,
                         n_replications=6,
                         lapse_prob=0.)

for (attr, q) in zip(attributes, quality):
    pcf.attributes = [attr]
    pc.quality_mean = q
    attr_path = result_path / attr
    data_path = attr_path / 'Thurstone'
    pc.run(n_subjects=20,
           subject_class=SubjectThurstone,
           result_path=data_path)

    print(f'\n*** True quality parameters for subjects in {data_path}:')
    pc_qual = np.array(pc.quality)
    for q_i in pc_qual:
        print(np.array_str(q_i, precision=3))
    print('Group mean = ', np.array_str(np.mean(pc_qual, axis=0),
                                        precision=3, suppress_small=True))

    data_path = attr_path / 'Bradley'
    pc.run(n_subjects=20,
           subject_class=SubjectBradley,
           result_path=data_path)

    print(f'\n*** True quality parameters for subjects in {data_path}:')
    pc_qual = np.array(pc.quality)
    for q_i in pc_qual:
        print(np.array_str(q_i, precision=3))
    print('Group mean = ', np.array_str(np.mean(pc_qual, axis=0),
                                        precision=3, suppress_small=True))
