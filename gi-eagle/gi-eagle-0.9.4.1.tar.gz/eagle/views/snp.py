"""
SNP query page
"""
from base64 import b64encode
import os

from flask import render_template, request

from eagle.application import app
from eagle.core import snps
from eagle.core.effectenum import EffectNames, exon_effects

from eagle.views.common import sample_filename, group_filename,\
    available_groups, available_sample_objects, parse_request,\
    available_group_samples, generate_homozygot_data, generate_vcf


@app.template_filter()
def diseases(samples):
    '''return the disease of a sample'''
    return set([sample.disease for sample in samples])


def samples_by_diseases(diseases):
    '''return all samples affected by one of the given diseases'''
    samples = [sample_filename(s.basename) for s in available_sample_objects()
               if '@' + s.disease in diseases]
    for disease in diseases:
        if not disease.startswith('@'):
            file_path = group_filename(disease)
            group_samples = available_group_samples(file_path)
            samples += [sample_filename(sample) for sample in group_samples]
    return samples





@app.route('/snp', methods=['GET', 'POST'])
def snp():
    if request.method != 'POST':
        return render_template(
            "snp_query.html",
            available_samples=available_sample_objects(),
            available_groups=available_groups(),
            EffectNames=EffectNames,
            exon_effects=exon_effects,
        )

    # parse the request parameters
    q = parse_request(request)

    # building case filenames
    cases = [sample_filename(c) for c in q.case]
    cases.extend(samples_by_diseases(q.case_groups))
    cases = set(cases)

    # building control filenames
    controls = [sample_filename(c) for c in q.control]
    controls.extend(samples_by_diseases(q.control_groups))
    controls = set(controls)

    results = snps.run(
        cases,
        controls,
        q.effects,
        q.min_qual,
        q.min_samples_per_gene,
        q.min_samples_per_variant,
        q.min_variants_per_gene,
        q.genes,
        ignore_heterozygosity=q.ignore_heterozygosity,
        usehg19=q.usehg19,
        dbsnp=q.dbsnp,
        min_alt_mapping_qual=q.min_mapping_qual,
    )


    cases_list, homhetdata, barchart = generate_homozygot_data(cases, results)

    vcf = b64encode(generate_vcf(results, cases_list, q.usehg19).encode()).decode()




    return render_template('snp_results.html', title="SNP", results=results,
                           vcf=vcf, query=q, caseslist=cases_list,
                           homhetdata=homhetdata, barchart=barchart)
