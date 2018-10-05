"""
This file controls which input names call which functions.
"""
from collections import OrderedDict
from . import stats, diff, merge, units

version = "0.0.1.18"
# python3 setup.py sdist bdist_wheel ; twine upload --repository-url https://upload.pypi.org/legacy/   dist/dretools-0.0.1.17*

operations_dict = OrderedDict()
# Unit
operations_dict["Units"] = OrderedDict()
operations_dict["Units"]["sample-epk"] = units.epk_sample_wise
operations_dict["Units"]["sample-aei"] = units.calculate_aei

operations_dict["Units"]["region-epk"] = units.epk_region_wise
operations_dict["Units"]["edsite-epk"] = units.epk_site_wise

# Differential Editing
operations_dict["Differential Editing"] = OrderedDict()
operations_dict["Differential Editing"]["region-diff"] = diff.region_diff
operations_dict["Differential Editing"]["edsite-diff"] = diff.editing_site_diff

# Stats
operations_dict["Stats"] = OrderedDict()
operations_dict["Stats"]["sample-stats"] = stats.sample_cli
operations_dict["Stats"]["region-stats"] = stats.genomic_region
operations_dict["Stats"]["edsite-stats"] = stats.editing_site

# Merge
operations_dict["Merge"] = OrderedDict()
operations_dict["Merge"]["find-islands"] = merge.find_islands
operations_dict["Merge"]["edsite-merge"] = merge.merge_editing_sites
