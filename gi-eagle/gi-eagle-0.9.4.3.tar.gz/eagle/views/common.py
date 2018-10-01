from base64 import b64encode
from datetime import date
import glob
from io import BytesIO
import os
import uuid

import h5py

try:
    import matplotlib

    matplotlib.use('Agg')
    from matplotlib import pyplot, patches, lines
    NO_MATPLOTLIB=False
except ImportError:
    NO_MATPLOTLIB=True

from eagle.application import app
from eagle.core.wrap.sample import Sample

SNP_PATH = app.config["SNP_PATH"]
GROUP_PATH = app.config["GROUP_PATH"]
BAM_PATH = app.config["BAM_PATH"]


def __h5files__(path):
    '''return sorted h5 files in a path'''
    files = [f.rsplit("/", 1)[-1][:-3]
             for f in glob.iglob(os.path.join(path, "*.h5"))]
    return sorted(files)


def __txtfiles__(path):
    '''return sorted txt files in a path'''
    files = [f.rsplit("/", 1)[-1][:-4]
         for f in glob.iglob(os.path.join(path, "*.txt"))]
    return sorted(files)


def available_samples(project_filter=True):
    '''return all available sample names'''
    return __h5files__(SNP_PATH)


def available_sample_objects(project_filter=True):
    '''return all available samples as Sample objects'''
    return [Sample(sample_filename(s)) for s in available_samples()]


def available_group_samples(group):
    samples = open(group).readline().split()
    return samples


def available_groups(project_filter=True):
    '''return all available groups'''
    return __txtfiles__(GROUP_PATH)


def sample_filename(sample):
    '''return the filename to a given sample'''
    return os.path.join(SNP_PATH, sample + ".h5")


def group_filename(group):
    '''return the filename to a given sample'''
    return os.path.join(GROUP_PATH, group + ".txt")


def bam_filename(sample):
    '''return the bam filename to a given sample'''
    return os.path.join(BAM_PATH, sample + ".bam")


def available_chromosomes():
    '''return the chromosomes of all samples'''
    chromosomes = []
    for sample_name in available_samples():
        sample_path = sample_filename(sample_name)
        sample = h5py.File(sample_path, 'r')
        for chrom in sample:
            if chrom not in chromosomes:
                chromosomes.append(chrom)
    return chromosomes


def generate_box_plot(samples, hetcounts, homcounts, bothcounts):
    '''
    generates a boxplot png which shows the homozygot and heterozygot count for each sample.
    Returns the Bytes for the png image.
    '''
    if NO_MATPLOTLIB:
        return
    ax = pyplot.subplot(111, frameon=False)

    if len(samples) == 1:  # Matplotlib has some very strange quirks
        homcounts = list(homcounts.values())
        hetcounts = list(hetcounts.values())
        bothcounts = list(bothcounts.values())
        pyplot.bar([0], homcounts, 0.35, color='#f04124')
        pyplot.bar([0], bothcounts, 0.35, color='#00A000', bottom=bothcounts[0])
        pyplot.bar([0], hetcounts, 0.35, color='k', bottom=bothcounts[0] + homcounts[0])
        pyplot.xticks([0], samples)
    else:
        pyplot.bar(range(len(samples)), homcounts.values(), 0.35, color='#f04124')
        pyplot.bar(
            range(len(samples)),
            bothcounts.values(),
            0.35,
            color='#00A000',
            bottom=list(homcounts.values())
        )
        pyplot.bar(
            range(len(samples)),
            hetcounts.values(),
            0.35,
            color='k',
            bottom=[x + y for (x, y) in zip(homcounts.values(), bothcounts.values())]
        )

        pyplot.xticks(range(len(samples)), samples, rotation=90)

    red_patch = patches.Patch(color='#f04124')
    black_patch = patches.Patch(color='black')
    green_patch = patches.Patch(color='green')

    ax.legend(handles=[black_patch, red_patch, green_patch],
              labels=["Heterozygot", "Homozygot", "Both"], loc='upper right')

    raw_data = BytesIO()
    pyplot.savefig(raw_data, dpi='figure', bbox_inches='tight', pad_inches=0, format='png')
    raw_data.seek(0)
    image_as_bytes = raw_data.read()
    raw_data.close()
    pyplot.close()

    return image_as_bytes

def generate_vcf(results, cases, usehg19=False):
    vcf_string = """##fileformat=VCFv4.0
##fileDate=%s
##source=eagle
##reference=%s
##phasing=partial
##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of Samples With Data">
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
##INFO=<ID=AF,Number=.,Type=Float,Description="Allele Frequency">
##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele">
##INFO=<ID=DB,Number=0,Type=Flag,Description="dbSNP membership, build 129">
##INFO=<ID=H2,Number=0,Type=Flag,Description="HapMap2 membership">
##FILTER=<ID=q10,Description="Quality below 10">
##FILTER=<ID=s50,Description="Less than 50%% of samples have data">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality">
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t""" % \
                 (date.today().strftime('%Y%m%d'), "hg19" if usehg19 else "hg38")
    vcf_string += "\t".join(cases)
    vcf_string += "\n"
    rows = []
    for r in results:
        row = [str(s) for s in [r["chrom"][3:],
                                r["position"],
                                ".",
                                r["ref"] if r["ref"] in "ACGT" else "N",
                                "ACGT"[r["typ"]] if r["typ"] < 4 else ".",
                                r["maxqual"],
                                ".",
                                ".",
                                "GT:GQ"]]
        for sample in cases:
            GT_string = "./."
            GQ_string = "."
            if sample in r['samples']:
                GT_string = "0/1" if r['heterozygot'][sample] \
                    else "1/1" if r["typ"] < 4 else "0/0"
                GQ_string = str(r['qual'][sample])
            row.append("%s:%s" % (GT_string, GQ_string))
        rows.append("\t".join(row))
    vcf_string += "\n".join(rows)
    # vcf_string += results[0]
    return vcf_string


def generate_homozygot_data(cases, results):
    cases_list = sorted([os.path.splitext(os.path.basename(case))[0] for case in cases])
    homhetdata = {}
    homhetcount_samples = {}
    homhetcount_samples['het'] = {case: 0 for case in cases_list}
    homhetcount_samples['hom'] = {case: 0 for case in cases_list}
    homhetcount_samples['both'] = {case: 0 for case in cases_list}

    for r in results:
        for bgene in r.symbols:
            gene = bgene.decode('utf-8')
            if gene not in homhetdata.keys():
                homhetdata[gene] = {}
            for case in r.samples:
                homhet = 'het' if r.heterozygot[case] else 'hom'
                if case not in homhetdata[gene]:
                    homhetdata[gene][case] = homhet
                    homhetcount_samples[homhet][case] += 1
                else:
                    if homhetdata[gene][case] == homhet or homhetdata[gene][case] == 'both':
                        continue
                    homhetcount_samples[homhetdata[gene][case]][case] -= 1
                    homhetcount_samples['both'][case] += 1
                    homhetdata[gene][case] = 'both'

    if NO_MATPLOTLIB:
        barchart = None
    else:
        barchart = b64encode(generate_box_plot(
            samples=cases_list,
            hetcounts=homhetcount_samples['het'],
            homcounts=homhetcount_samples['hom'],
            bothcounts=homhetcount_samples['both']
        )).decode('utf-8')

    return cases_list, homhetdata, barchart

class Query():
    pass


def parse_request(request):
    q = Query()
    q.case = request.form.getlist('case')
    q.chromosomes = request.form.getlist('chromosomes')
    q.control = request.form.getlist('control')
    q.effects = sum(request.form.getlist('effects', type=int))
    q.min_qual = request.form.get('minquality', type=int)
    q.min_mapping_qual = request.form.get('minmappingquality', type=int)
    q.min_samples_per_gene = request.form.get('samplespergene', type=int)
    q.min_samples_per_variant = request.form.get('samplespervariant', type=int)
    q.min_variants_per_gene = request.form.get('variantspergene', type=int)
    q.min_variant_length = request.form.get('minlength', type=int)
    q.max_variant_length = request.form.get('maxlength', type=float)
    q.search_all = request.form.get('searchall', type=bool)
    q.case_groups = request.form.getlist('case_group')
    q.control_groups = request.form.getlist('control_group')
    q.usehg19 = request.form.get('usehg19', type=bool) is True
    q.ignore_heterozygosity = \
        request.form.get('ignore_heterozygosity', type=bool) is True
    q.insertion = request.form.get('insertion', type=bool) is True
    q.inversion = request.form.get('invariant', type=bool) is True
    q.deletion = request.form.get('deletion', type=bool) is True
    q.dbsnp = request.form.get("dbsnp")
    q.uuid = uuid.uuid4()

    # genes
    genes = request.form.getlist('genes')
    if genes and not q.search_all:
        q.genes = map(lambda x: x.strip(),
                      request.form.getlist('genes')[0].split("\n"))
    else:
        q.genes = []

    q.index = request.form.get('sample')
    q.parent1 = request.form.get('parent1')
    q.parent2 = request.form.get('parent2')

    return q
