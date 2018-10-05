from dretoolslib.parsers import generate_snvs
from dretoolslib.io import shared_params
from dretoolslib.io import island_params


def get_dict_of_merged_positions(file_list, store_variants=False):
    """

    :param file_list:
    :param store_variants:
    :return:
    """
    merged_dict = {}
    for vcf_file in file_list:
        for chrom, pos, id, ref, alt, qual, fil, info in generate_snvs(vcf_file):

            site_key = (chrom, pos, ref, alt)

            if store_variants:
                try:
                    merged_dict[site_key].append(vcf_file)
                except KeyError:
                    merged_dict[site_key] = [vcf_file]
            else:
                try:
                    merged_dict[site_key] += 1
                except KeyError:
                    merged_dict[site_key] = 1

    return merged_dict


def merge_editing_sites(parser):
    """ Merge two or more files containing editing sites.

    This function merges two of more VCF files containing editing sites. It is meant for creating consensus sets of
    editing sites that can be used for calculating EPK or predicting the locations of editing islands. Further, in
    addition to simply creating a unique set various filters are available to control things such as the number of
    edited bases for consideration as an editing site or the minimum number of samples a site must be observed in-order
    to be included in the consensus set.

    Examples:

    cat sample1.vcf
    1	20649498	.	T	C	31.77	.	AC=1;DP=12;	GT:AD:DP:GQ:PL	0/1:6,6:12:60:60,0,272
    1	20649504	.	T	C	31.77	.	AC=1;DP=12;	GT:AD:DP:GQ:PL	0/1:6,6:12:60:60,0,272
    1	20649529	.	T	C	157.77	.	AC=1;DP=14;	GT:AD:DP:GQ:PL	0/1:7,7:11:71:186,0,71
    1	20649581	.	T	C	96.82	.	AC=1;DP=16;	GT:AD:DP:GQ:PL	0/1:8,8:5:19:125,0,19

    cat sample2.vcf
    1	20649498	.	T	C	31.77	.	AC=1;DP=10;	GT:AD:DP:GQ:PL	0/1:5,5:14:60:60,0,272
    1	20649507	.	T	C	31.77	.	AC=1;DP=12;	GT:AD:DP:GQ:PL	0/1:6,6:12:60:60,0,272
    1	20649529	.	T	C	157.77	.	AC=1;DP=12;	GT:AD:DP:GQ:PL	0/1:4,8:11:71:186,0,71
    1	20649581	.	T	C	96.82	.	AC=1;DP=8;	GT:AD:DP:GQ:PL	0/1:6,2:5:19:125,0,19

    -------------------------------------------------------------------------------------------------------------------
    # Require that an editing site be seen in at least three samples to be included in the consensus set.
    # Here sites 1:20649504 and 1:20649507 are exclude at each is only present once.
    dretools edsite-merge \\
        --min-samples  2  \\
        --vcf sample1.vcf sample2.vcf > consensus_sites.vcf

    #Chromosome	Position	ID	Ref	Alt	Qual	Fil	Sample_cnt
    1	20649498	.	T	C	.	.	2
    1	20649529	.	T	C	.	.	2
    1	20649581	.	T	C	.	.	2

    -------------------------------------------------------------------------------------------------------------------
    # Increase the cutoffs that exclude sites without sufficient read coverage or edited bases.
    # Here site in addition to sites, 1:20649504 and 1:20649507, site 1:20649529 is excluded as it is below the
    # minimum read coverage in sample2.vec. Similarly, site 1:20649581 is excluded as the number of editing bases
    # is below the cutoff in sample2.vec.
    dretools edsite-merge \\
        --min-samples  2  \\
        --min-coverage 5  \\
        --min-editing  3  \\
        --vcf sample1.vcf sample2.vcf
    #chromosome	position	id	ref	alt	qual	fil	sample_cnt
    1	20649529	.	T	C	.	.	2
    1	20649498	.	T	C	.	.	2

    """

    shared_params(parser, coverage=False, editing_islands=False, names=False, genome=False, gtf=False, alignment=False)

    default_min_samples = 1
    min_samples_help_text = "Site must be found in N or more samples. (Default %s)" % default_min_samples

    parser.add_argument(
        "--min-samples",
        type=int,
        default=default_min_samples,
        help=min_samples_help_text
    )

    args = parser.parse_args()

    min_cov = args.min_coverage
    min_ed = args.min_editing
    max_ed = args.max_editing
    vcf_list = args.vcf
    # @TODO: add store_variants
    merged_dict = {}
    cnt_dict = {}

    print("\t".join([
                "#Chromosome",
                "Position",
                "ID",
                "Ref",
                "Alt",
                "Qual",
                "Fil",
                "Info"
            ]
        )
    )

    for vcf_file_name in vcf_list:
        for site in generate_snvs(vcf_file_name, min_coverage=min_cov, min_editing=min_ed, max_editing=max_ed):

            site_key = (site.chromosome, site.position, site.reference, site.alteration)

            try:
                merged_dict[site_key] += 1
            except KeyError:
                merged_dict[site_key] = 1

            ratio = round(site.alt_cnt/site.ref_cnt, 5)
            try:
                cnt_dict[site_key][0] += site.ref_cnt
                cnt_dict[site_key][1] += site.alt_cnt
                cnt_dict[site_key][2] += ratio
            except KeyError:
                cnt_dict[site_key] = [site.ref_cnt, site.alt_cnt, ratio]

    for dict_key in sorted(merged_dict):
        chrom, pos, ref, alt = dict_key

        if merged_dict[dict_key] >= args.min_samples:
            sample_cnt = float(merged_dict[dict_key])
            dp = round((cnt_dict[dict_key][0] + cnt_dict[dict_key][1])/sample_cnt)
            avg_ref_cnt = round(cnt_dict[dict_key][0] / sample_cnt, 1)
            avg_alt_cnt = round(cnt_dict[dict_key][1] / sample_cnt, 1)
            avg_epk = round(cnt_dict[dict_key][2] / sample_cnt, 4)

            info = "DP=%s;SampleCnt=%s;AvgAltRefRatio=%s;AvgRefAltCnt=%s,%s;" % (
                dp, merged_dict[dict_key], avg_epk, avg_ref_cnt, avg_alt_cnt)

            id, qual, fil = ".", ".", "."

            print("\t".join([chrom, pos, id, ref, alt, qual, fil, info]))


def find_islands(parser):
    """ Find editing islands within one or more files containing editing sites.

    Overview:
    RNA editing has been described to happen in clusters in numerous publications [1]. To study this phenomena, we
    created an algorithm to detect these clusters of editing sites, or editing islands, and included it in our recently
    published RNA editing detection tool, RNAEditor [2]. However, predicting the locations of editing islands using
    consensus sets of editing sites is also of interest. To meet this need we have implemented the editing island
    prediction algorithm in DRETools.
    Usage Notes:
    The two main considerations when predicting editing islands are the epsilon and min-points arguments. These
    arguments control the behavior of the DBSCAN algorithm. We tested silhouette coefficient with a grid search in
    the RNAEditor manuscript and found epsilon=50 and min-points=5 yielded the lowest silhouette coefficient. Further,
    the average editing island length during testing was 89.3 ± 30.9 bp. This is interesting as this is close the size
    of intramolecular imperfect duplexes that form between Alu element and its inverted-repeat [3], which is the most
    commonly edited type of transcriptomic feature.
    References:
    [1] Bazak, Lily, et al. "A-to-I RNA editing occurs at over a hundred million genomic sites,
        located in a majority of human genes." Genome research 24.3 (2014): 365-376.
    [2] John, David, et al. "RNAEditor: easy detection of RNA editing events and the introduction of editing islands."
        Briefings in bioinformatics 18.6 (2016): 993-1001.
    [3] Elbarbary, Reyad A., Bronwyn A. Lucas, and Lynne E. Maquat. "Retrotransposons as regulators of gene expression."
        Science 351.6274 (2016): aac7247.

    Example:
    cat test.vcf
    1 2277250 . A G . . DP=13;Dels=0.0; GT:AD:DP:GQ:PL  1/1:7,7:12:3:35,3,0
    1 2277259 . A G . . DP=7;Dels=0.0;  GT:AD:DP:GQ:PL  1/1:7,7:9:3:35,3,0
    1 2277264 . A G . . DP=7;Dels=0.0;  GT:AD:DP:GQ:PL  1/1:7,7:9:3:35,3,0
    1 2277274 . A G . . DP=11;Dels=0.0; GT:AD:DP:GQ:PL  1/1:7,7:11:3:35,3,0
    1 2277284 . A G . . DP=7;Dels=0.0;  GT:AD:DP:GQ:PL  1/1:7,7:17:3:35,3,0
    1 2277294 . A G . . DP=14;Dels=0.0; GT:AD:DP:GQ:PL  1/1:7,7:14:3:35,3,0
    1 2277318 . A G . . DP=15;Dels=0.0; GT:AD:DP:GQ:PL  1/1:8,8:15:3:35,3,0
    1 2277330 . A G . . DP=11;Dels=0.0; GT:AD:DP:GQ:PL  1/1:6,6:11:3:35,3,0

    dretools find-islands --vcf test.vcf
    #Chromosome Start End ID Score Strand Length Number_of_Sites Density
    1 2277247 2277334 MZlCCKc5Pv5JbgV6Xf0GWA . + 87 8 0.09195

    """

    from sklearn.cluster import DBSCAN
    from base64 import urlsafe_b64encode
    from hashlib import md5
    from dretoolslib.io import vcf_params

    # Get the common commands for VCF file input.
    vcf_params(parser)

    default_epsilon = 50
    default_min_points = 5
    default_min_island_length = default_min_points * 2
    default_pad_len = 3

    # Make help text strings
    epsilon_help_text = """
 Maximum distance between two sites to considered in the same neighborhood. (Default: %s)

    """ % default_epsilon

    min_points_help_text = """ Minimum samples for a neighborhood to be considered a core point. (Default: %s)

    """ % default_min_points

    default_pad_len_text = """ Expand islands start and end bounds by a given integer. (Default: %s)

    """ % default_pad_len

    min_island_length_help_text = """ Minimum editing island length. %s

    """ % default_min_island_length

    # Values relating to DBSCAN
    parser.add_argument(
        '--epsilon',
        type=float,
        default=default_epsilon,
        help=epsilon_help_text
    )
    parser.add_argument(
        '--min-points',
        type=int,
        default=default_min_points,
        help=min_points_help_text
    )

    # Values controlling output after prediction has taken place.
    parser.add_argument(
        '--pad-length',
        type=float,
        default=default_pad_len,
        help=default_pad_len_text
    )
    parser.add_argument(
        "--min-length",
        type=int,
        default=default_min_island_length,
        help=min_island_length_help_text
    )

    args = parser.parse_args()

    # Sort by chromosome, what about strand?
    chromosome_dict = {"+": {}, "-": {}}

    min_cov = args.min_coverage
    min_ed = args.min_editing
    max_ed = args.max_editing

    pad_len = int(args.pad_length)

    for vcf_name in args.vcf:
        for site in generate_snvs(vcf_name, min_coverage=min_cov, min_editing=min_ed, max_editing=max_ed):
            strand = "+" if site.reference == "A" else "-"
            position = int(site.position)

            try:
                try:
                    chromosome_dict[strand][site.chromosome][position] += 1
                except KeyError:
                    chromosome_dict[strand][site.chromosome][position] = 1
            except KeyError:
                chromosome_dict[strand].update({site.chromosome: {position: 1}})

    print("\t".join([
                "#Chromosome",
                "Start",
                "End",
                "ID",
                "Score",
                "Strand",
                "Length",
                "Number_of_Sites",
                "Density"
            ]
        )
    )

    for strand in sorted(chromosome_dict):
        for chromosome in sorted(chromosome_dict[strand]):

            pos_dict = set(chromosome_dict[strand][chromosome])

            number_of_unique_editing_sites = len(pos_dict)

            pos_list = [[p] for p in sorted(pos_dict)]

            if number_of_unique_editing_sites > args.min_points:

                db = DBSCAN(eps=args.epsilon, min_samples=args.min_points).fit(pos_list)

                island_dict = {}  # Make lists of bounds
                for i in range(number_of_unique_editing_sites):
                    if db.labels_[i] >= 0:
                        try:
                            island_dict[db.labels_[i]].append(pos_list[i])
                        except KeyError:
                            island_dict[db.labels_[i]] = [pos_list[i]]

                for label in range(len(island_dict)):
                        sites_in_island = sorted(island_dict[label])
                        island_start = sites_in_island[0][0] - pad_len
                        island_end = sites_in_island[-1][0] + 1 + pad_len
                        island_length = island_end - island_start
                        number_of_sites_in_island = len(sites_in_island)

                        if island_length >= args.min_length:
                            hstr = chromosome + strand + str(island_start) + str(island_end)
                            md5_digest = md5(hstr.encode('utf-8')).digest()

                            print("\t".join([
                                chromosome,
                                str(island_start),
                                str(island_end),
                                urlsafe_b64encode(md5_digest)[:-2].decode('utf-8'),
                                ".",                                                           # score
                                strand,
                                str(island_length),                                            # length of island
                                str(number_of_sites_in_island),                                # # sites in island
                                str(round(number_of_sites_in_island/float(island_length), 5))  # density
                            ]))


