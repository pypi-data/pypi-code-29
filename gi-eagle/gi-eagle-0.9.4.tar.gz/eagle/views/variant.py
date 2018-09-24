from base64 import b64encode
from collections import namedtuple

from flask import render_template, request

from eagle.application import app
from eagle.core import variant_detail as variant_detail_core
from eagle.core import variant_overlap as variant_overlap_core
from eagle.core import variant_search as variant_search_core
from eagle.core.effectenum import EffectNames
from eagle.views.common import available_samples, sample_filename, \
    generate_homozygot_data, generate_vcf


@app.route('/variant_detail/<chrom>/<position>/<typ>/<sample>',
           methods=['GET', 'POST'])
def variant_detail(chrom, position, typ, sample):
    variants = variant_detail_core.run(sample_filename(sample),
                                       chrom, int(position), typ)
    return render_template("variant.html", variants=variants,
                           EffectNames=EffectNames, chrom=chrom,
                           position=position, typ=typ)


@app.route("/variant_search", methods=['GET', 'POST'])
def variant_search():
    if request.method != "POST":
        return render_template("variant_search_query.html")

    regions = list(map(lambda x: variant_search_core.parse_region(x.strip()),
                       request.form.getlist('regions')[0].split("\n")))

    cases = [sample_filename(s) for s in available_samples()]

    results = variant_search_core.run(cases, regions)
    cases_list, homhetdata, barchart = generate_homozygot_data(available_samples(), results)
    vcf = b64encode(generate_vcf(results, cases_list).encode()).decode()

    return render_template("snp_results.html", title="Variant Search",
                           results=results, caseslist=cases_list,
                           barchart=barchart, homhetdata=homhetdata,
                           vcf=vcf)


@app.route("/variant_overlap", methods=['GET', 'POST'])
def variant_overlap():
    if request.method != "POST":
        return render_template("variant_overlap_query.html",
                               available_samples=available_samples())

    samples = request.form.getlist('samples')
    sample1, sample2, sample3 = samples
    sample_filename_1, sample_filename_2, sample_filename_3 = \
        map(sample_filename, samples)
    result = variant_overlap_core.run(
        sample_filename_1,
        sample_filename_2,
        sample_filename_3,
    )

    return render_template("variant_overlap_results.html", result=result,
                           sample1=sample1, sample2=sample2, sample3=sample3)
