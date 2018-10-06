from dretoolslib.parsers import generate_snvs
from dretoolslib.io import shared_params
from dretoolslib.shared import passes_min_coverage, passes_min_editing, get_strand, base_transition_tuples_and_titles, passes_max_percent_editing, get_edited_character
from dretoolslib.parsers import BED, get_coverage_total_area_covered
from dretoolslib.parsers import GenomicIntervalTree, BedIntervalTree, find_total_area_covered
from numpy import average, var, std
from pysam import Fastafile
from pysam import AlignmentFile
from statistics import mean
from dretoolslib.parsers import SNVInRegion


def sample(vcf_list, coverage=None, names=None, gtf=None, islands=None, min_coverage=None, min_editing=None, max_editing=None):
    """

    :param vcf_list:
    :param coverage:
    :param names:
    :param gtf:
    :param islands:
    :param min_coverage:
    :param min_editing:
    :param max_editing:
    :return:
    """
    from dretoolslib.parsers import normalized_editing

    # =========================
    # Set up data structures
    # =========================
    # First we need to know if we will be differentiating between Adar1 and Adar2 sites
    island_interval_tree = None
    if islands:
        # Create an interval tree from editing islands and use it to discriminate Adar1 from Adar2 sites.
        island_interval_tree = BedIntervalTree()
        island_interval_tree.add_islands_from_file(islands)

    # Base output columns.
    titles = ["Sample", "ESs"]

    coverage_list = []
    if coverage:
        coverage_list = coverage
        titles.append("Area_Covered")

    # Generate data structures for Base counting.
    transition_tuple_titles, transition_tuple_list = base_transition_tuples_and_titles()

    titles += transition_tuple_titles  # A>C A>G ...
    # If discriminate Adar1 from Adar2 we need additional columns
    if islands:
        titles += ["A1_" + title for title in transition_tuple_titles]  # A>C A>G ...
        titles += ["A2_" + title for title in transition_tuple_titles]  # A>C A>G ...

    names_dict = {}
    if names:
        names_list = names
        if type(names_list) != list:
            names_list = names_list.split(",")

        assert len(names_list) == len(vcf_list)
        # For finding aliases given by names flag.
        for i in range(len(names_list)):
            names_dict[vcf_list[i]] = names_list[i]

    genomic_features = None
    if gtf:
        # Initialize variables for various columns.
        # Build interval tree for fast position searches. This can take some time so report to users.
        # print("Generating interval tree ......", end=" ",  flush=True)
        interval_tree = GenomicIntervalTree(gtf)
        genomic_features = interval_tree.genomic_features

        ge_title = ["ES_" + s for s in genomic_features]
        titles += ge_title
        if islands:
            titles += ["A1_" + title for title in ge_title]
            titles += ["A2_" + title for title in ge_title]

        # Make variables for holding row information.
        features_dict = {t: 0 for t in genomic_features}

    # First print the titles.
    out_lines = ["\t".join(titles)]

    # Run name check i.e. name should have unique intersect greater than other names with paired values.
    # =============================================================================================
    # Parse VCF files
    # =============================================================================================
    for i in range(len(vcf_list)):
        # Hold all unique sites in each VCF in a dict
        # snv_dict = 0
        total_sites = 0
        # Make variables for holding row information.
        if gtf:
            features_dict = {t: 0 for t in genomic_features}
            if islands:
                adar1_features_dict = {t: 0 for t in genomic_features}
                adar2_features_dict = {t: 0 for t in genomic_features}

        tmp_transition_dict = {t: 0 for t in transition_tuple_list}
        if islands:
            tmp_adar1_transition_dict = {t: 0 for t in transition_tuple_list}
            tmp_adar2_transition_dict = {t: 0 for t in transition_tuple_list}

        # The row id are the file name, unless a name data structure is passed.
        name = vcf_list[i]
        if names:
            name = names_dict[vcf_list[i]]

        # If a coverage file is present find coverage.
        total_area_covered = None
        if coverage:
            total_area_covered = float(find_total_area_covered(min_coverage, coverage_list[i]))
            area_covered_dict = get_coverage_total_area_covered(min_coverage, coverage_list[i])

        vcf_coverage_dict = {}

        for snv in generate_snvs(vcf_list[i], min_coverage=min_coverage, min_editing=min_editing, max_editing=max_editing):
            # Find coverage

            strand = "+" if snv.reference == "A" else "-"
            transition_tuple = (snv.reference, snv.alteration)

            try:
                vcf_coverage_dict[snv.ref_cnt + snv.alt_cnt] += 1
            except KeyError:
                vcf_coverage_dict[snv.ref_cnt + snv.alt_cnt] = 1

            total_sites += 1
            # try:
            #    # Ignore
            #    snv_dict[site_key].add(name)
            # except KeyError:
            #     snv_dict[site_key] = set(name)
            # Count transitions i.e. A>G and C>T
            try:
                tmp_transition_dict[transition_tuple] += 1
                if islands:
                    if island_interval_tree.location_is_in_interval(snv.chromosome, int(snv.position)):
                        tmp_adar1_transition_dict[transition_tuple] += 1
                    else:
                        tmp_adar2_transition_dict[transition_tuple] += 1
            except KeyError:
                print("Warning: Bases %s and/or %s not included in base dict." % transition_tuple)

            # Count occurrences in locations
            # First find overlapping genes.
            if gtf:

                features = interval_tree.get_features_overlapping_position(snv.chromosome, int(snv.position), strand)

                if islands:
                    is_in_island = island_interval_tree.location_is_in_interval(snv.chromosome, int(snv.position))
                    for feature in features:
                        if is_in_island:
                            adar1_features_dict[feature] += 1
                        else:
                            adar2_features_dict[feature] += 1
                else:
                    for feature in features:
                        features_dict[feature] += 1

        # =============================================================================================
        # Build output.
        # =============================================================================================
        # Number of sites
        # total_sites = snv_cnt
        out_list = [name, str(total_sites)]

        if coverage:
            coverage_ratios_list = []
            weights_list = []

            for cov_level in vcf_coverage_dict:
                coverage_ratios_list.append(vcf_coverage_dict[cov_level] / area_covered_dict[cov_level])
                weights_list.append(area_covered_dict[cov_level]/total_area_covered)

            try:
                weighted_average = average(coverage_ratios_list, weights=weights_list)*1e6
            except ZeroDivisionError:
                weighted_average = 0

            normalized_site_count = normalized_editing(total_sites, total_area_covered)
            out_list += [str(total_area_covered), str(normalized_site_count), str(weighted_average)]

        out_list += [str(tmp_transition_dict[i]) for i in transition_tuple_list]
        if islands:
            out_list += [str(tmp_adar1_transition_dict[i]) for i in transition_tuple_list]
            out_list += [str(tmp_adar2_transition_dict[i]) for i in transition_tuple_list]

        if gtf:
            out_list += [str(features_dict[i]) for i in genomic_features]
            if islands:
                out_list += [str(adar1_features_dict[i]) for i in genomic_features]
                out_list += [str(adar2_features_dict[i]) for i in genomic_features]

        out_lines.append("\t".join(out_list))

    return out_lines




def count_edited_and_nonedited_bases_in_region(
        aligned_reads, chromosome, start, end, comp_count_char, count_char_position_set=set(), es_set=set()):
    """

    :param aligned_reads:
    :param chromosome:
    :param start:
    :param end:
    :param comp_count_char:
    :param count_char_position_set:
    :param es_set:
    :return:
    """

    cout_pos_dict = {}
    count_edited_bases = {}
    total_editable_but_not_edited = 0
    total_edited_bases = 0
    base_count_list = []
    edited_base_count_list = []
    a = []
    for read in aligned_reads.fetch(chromosome, start, end):
        for i in range(len(read.query_sequence)):
            tmp_edited_bases = 0
            tmp_all_bases = 0
            if read.pos + i in count_char_position_set:
                read_base = read.query_sequence[i]

                add_int = 0
                if read_base == comp_count_char and read.pos + i in es_set:
                    add_int = 1

                try:
                    count_edited_bases[read.pos + i] += add_int
                except KeyError:
                    count_edited_bases[read.pos + i] = add_int

                try:
                    cout_pos_dict[read.pos + i] += 1
                except KeyError:
                    cout_pos_dict[read.pos + i] = 1

    return cout_pos_dict, count_edited_bases


def get_set_of_positions_matching_character_from_sequence(sequence, count_char, start):
    """

    :param sequence:
    :param count_char:
    :param start:
    :return:
    """
    count_char_position_set = set()
    for i in range(len(sequence)):
        if sequence[i] == count_char:
            tmp_full_location = start + i
            count_char_position_set.add(tmp_full_location)

    return count_char_position_set


def find_countable_character_positions(reference_genome, chromosome, start, end, count_char):
    """

    :param reference_genome:
    :param chromosome:
    :param start:
    :param end:
    :param count_char:
    :return:
    """
    # Next get the reference sequence
    sequence = reference_genome.fetch(chromosome, start, end)
    # Make a list of all editable positions i.e. locations of all A or C in region depending on strand.
    # Here we use a set as we will iterate over reads in the next step checking to see if the site is
    # included in the positions to check list.
    return get_set_of_positions_matching_character_from_sequence(sequence, count_char, start)


def get_genome(genome_path):
    """

    :return:
    """
    if genome_path:
        return Fastafile(genome_path)
    return None


def get_gtf_interval_tree(gtf_path):
    """

    :param gtf_path:
    :return:
    """

    genomic_features = []
    interval_tree = None
    if gtf_path:
        gtf = gtf_path
        interval_tree = GenomicIntervalTree(gtf)
        genomic_features = interval_tree.genomic_features
        return gtf, interval_tree, genomic_features


def get_alignment(alignment_path):
    """

    :param alignment_path:
    :return:
    """
    # aligned_reads = None
    if alignment_path:
        return AlignmentFile(alignment_path[0], "rb")
    return None


def get_count_dicts_of_editing_at_editable_positions(aligned_reads, count_char_position_set, chromosome, start, end, count_char, es_set):
    """ Returns two dictionaries the first contains the counts of the coverage at the editable positions.
    The second contains the counts of edited bases at each position.

    In this context "editable" means a site which has the minimum read depth and is a base that could be edited (i.e.
    A for positive strands and T for negative strands).

    :param aligned_reads:
    :param count_char_position_set:
    :param chromosome:
    :param start:
    :param end:
    :param count_char:
    :param es_set:
    :return: count_edited_bases - The read depth at all editable positions.
    :return: cout_pos_dict - The number of edited bases at all editable positions.
    """

    cout_pos_dict = {}
    count_edited_bases = {}
    for read in aligned_reads.fetch(chromosome, start, end):
        if not read.is_duplicate:
            for i in range(len(read.query_sequence)):
                tmp_global_pos = read.pos + i

                if tmp_global_pos in count_char_position_set:
                    read_base = read.query_sequence[i]
                    add_int = 0
                    # if read_base == count_char:
                    if read_base == count_char and tmp_global_pos in es_set:
                        add_int = 1

                    try:
                        count_edited_bases[tmp_global_pos] += add_int
                    except KeyError:
                        count_edited_bases[tmp_global_pos] = add_int

                    try:
                        cout_pos_dict[tmp_global_pos] += 1
                    except KeyError:
                        cout_pos_dict[tmp_global_pos] = 1

    return count_edited_bases, cout_pos_dict


def get_mean(values_list):
    """

    :return:
    """
    list_len = len(values_list)
    if list_len > 1:
        return mean(values_list)
    elif list_len == 1:
        return values_list[0]
    else:
        return 0


def get_ref_and_alt_cnts(reference_base, read_base_counts):
    """

    :param reference_base:
    :param read_base_counts:
    :return:
    """
    tmp_total_ref_read_bases, tmp_total_alt_read_bases = 0, 0
    if reference_base == "A":
        tmp_total_ref_read_bases += read_base_counts[0][0]
        tmp_total_alt_read_bases += read_base_counts[2][0]
    elif reference_base == "T":
        tmp_total_ref_read_bases += read_base_counts[3][0]
        tmp_total_alt_read_bases += read_base_counts[1][0]
    else:
        print("ERROR: Read base %s is not editable. " % (reference_base,))
        exit()
    return tmp_total_ref_read_bases, tmp_total_alt_read_bases


def sample_wise_overall_editing(parser):
    """ Calculate the editing per kilo-read-base
    """

    def split_list(the_list, chunk_size):
        result_list = []
        while the_list:
            result_list.append(the_list[:chunk_size])
            the_list = the_list[chunk_size:]
        return result_list

    parser.add_argument("--vcf", type=str)
    parser.add_argument("--alignment", type=str)

    args = parser.parse_args()

    from pysam import AlignmentFile

    alignment_obj = AlignmentFile(args.alignment, "rb")

    total_ref_read_bases = 0
    total_alt_read_bases = 0

    #  The coverage is computed per-base [ACGT].
    for site in generate_snvs(args.vcf):

        pos = int(site.position)

        # Returned in the order of A, C, G, T.
        read_base_counts = alignment_obj.count_coverage(site.chromosome, pos, pos + 1)

        # if site.reference == "A":
        #    total_ref_read_bases += read_base_counts[0][0]
        #    total_alt_read_bases += read_base_counts[2][0]
        # elif site.reference == "T":
        #    total_ref_read_bases += read_base_counts[3][0]
        #    total_alt_read_bases += read_base_counts[1][0]
        # else:
        #    print("ERROR: Read base %s at %s:%s" % (site.reference, site.chromosome, site.position))

        tmp_bases = get_ref_and_alt_cnts(site.reference, read_base_counts)
        total_ref_read_bases += tmp_bases[0]
        total_alt_read_bases += tmp_bases[1]

    overall_editing = str(round(total_alt_read_bases/float(total_ref_read_bases), 10))

    print("\t".join([str(total_ref_read_bases), str(total_alt_read_bases), overall_editing]))


def region_wise_overall_editing(parser):
    """

    :param parser:
    :return:
    """

    # shared_params(parser, coverage=False, editing_islands=False, names=False, bed=True, genome=False)

    parser.add_argument(
        "--vcf",
        type=str,
        help="")

    parser.add_argument(
        "--regions",
        type=str,
        help="")

    parser.add_argument(
        "--alignment",
        type=str,
        help="")

    args = parser.parse_args()

    from dretoolslib.parsers import VCFIntervalTree

    bed_path = args.regions
    alignment_path = args.alignment

    alignment_obj = AlignmentFile(alignment_path, "rb")

    # Make GTF parser obj to iterate over genomic locations.
    bed_obj = BED(bed_path)

    # ========================================================================
    # Parse VCF file into interval tree so that all editing sites within
    # a genomic location can be rapidly queried.
    # ========================================================================
    # Build interval tree from all VCF files.
    # Make interval tree of vcf locations.

    vcf_itree = VCFIntervalTree(args.vcf)

    # Print titles.
    print("\t".join(
        [
            "chromosome",
            "start",
            "end",
            "name",
            "strand",
            "total_reference_read_bases",
            "total_alternative_read_bases",
            "overall_editing"
        ]
    ))

    for record in bed_obj.yield_lines():

        es_in_region = vcf_itree.get_snvs_in_range(record.chromosome, record.strand, record.start, record.end)

        total_ref_read_bases = 0
        total_alt_read_bases = 0

        for es in es_in_region:
            # es is an interval object containing records like.
            # Interval(43021013, 43021014, ('sites.vcf', 'A', 'G', -1, -1))
            start, end, metadata = es
            reference_base = metadata[1]

            # returns tuple of arrays like (array('L', [0]), array('L', [0]), array('L', [0]), array('L', [0]))
            # always in order of A, C, G, T
            read_base_counts = alignment_obj.count_coverage(record.chromosome, start, end)

            # A tuple of the counts of (reference base, alternative base).
            tmp_bases = get_ref_and_alt_cnts(reference_base, read_base_counts)

            total_ref_read_bases += tmp_bases[0]
            total_alt_read_bases += tmp_bases[1]

        try:
            overall_editing = str(round(total_alt_read_bases / float(total_ref_read_bases), 10))
        except ZeroDivisionError:
            overall_editing = "0"

        print("\t".join(
            [
                record.chromosome,
                str(record.start),
                str(record.end),
                record.name,
                record.strand,
                str(total_ref_read_bases),
                str(total_alt_read_bases),
                overall_editing
            ]
        ))


def genomic_region(parser):
    """ Calculate region-wise information about the editing within a sample.

    The output of this function depends on the data passed to it via command line.
    The following data will always be printed for each VCF file passed:
    1. name          - The name of the region.
    2. region_len    - The length of the region.
    3. editable_area - The number of bases in the region with enough coverage for editing detection.
    4. total_ES      - The total number of editing sites in the region.
    5. A>G           - The number of editing sites coming from the positive strand.
    6. T>C           - The number of editing sites coming from the negative strand.
    7. REI           - The relative editing intensity of the region.

    If a gtf file is passed the following information will also be printed for each line.
    intergenic
    exon
    intron
    three_prime_utr
    five_prime_utr

    nretools grstat                           \\
     --genome    organism.primary_assembly.fa \\
     --gtf       organism.gtf                 \\
     --bed       organism.gtf.bed             \\
     --vcf       sample.editing_sites.vcf     \\
    --alignment  sample.noDup.realigned.recalibrated.bam
    """

    shared_params(parser, coverage=False, editing_islands=False, names=False, bed=True)

    parser.add_argument("--ref-vcf", type=str, default="")

    args = parser.parse_args()

    from dretoolslib.parsers import VCFIntervalTree

    # ========================================================================
    # Initialize data structures.
    # ========================================================================

    min_coverage = args.min_coverage
    min_editing = args.min_editing
    max_percent_coverage = args.max_editing
    genome_path = args.genome
    bed_path = args.bed
    alignment_path = args.alignment

    # If path is None return None, else return Fasta object.
    genome = get_genome(genome_path)

    genomic_features = []
    interval_tree = None
    if args.gtf:
        gtf = args.gtf
        interval_tree = GenomicIntervalTree(gtf)
        genomic_features = interval_tree.genomic_features

    aligned_reads = get_alignment(alignment_path)

    # Make GTF parser obj to iterate over genomic locations.
    bed_obj = BED(bed_path)

    # ========================================================================
    # Parse VCF file into interval tree so that all editing sites within
    # a genomic location can be rapidly queried.
    # ========================================================================
    # Build interval tree from all VCF files.
    # Make interval tree of vcf locations.
    vcf_itree = VCFIntervalTree(args.vcf[0], min_coverage, min_editing, max_percent_coverage)

    if args.ref_vcf:
        ref_vcf_itree = VCFIntervalTree(args.ref_vcf)

    # ========================================================================
    # Print titles.
    # ========================================================================
    titles = [
        "#name",
        "location",
        "region_len",
        "editable_area",
        "average_coverage_depth",
        "coverage_depth_std",
        "total_ES",
        "total_edited_reads",
        "A>G",
        "T>C",
    ] + genomic_features
    print("\t".join(titles))

    # ========================================================================
    # Iterate over all give genomic locations.
    # ========================================================================
    for record in bed_obj.yield_lines():
        total_edited_bases = 0
        total_editable_but_not_edited = 0
        mean_coverage_depth = 0
        features_dict = {}
        bases_passing_cutoff = 0
        coverage_depth_std = 0
        epk_total_ref_read_bases = 0
        epk = 0
        epk_total_alt_read_bases = 0
        REI = 0
        # Get all SNVs falling within gene.
        # Will return something like
        # {Interval(155054801, 155054802, ('VCF/SRR1539273.all_editing_sites.vcf', 'A', 'G', 2, 2))}
        es_in_region = vcf_itree.get_snvs_in_range(record.chromosome, record.strand, record.start, record.end)

        es_set = set([tmp_interval[0] for tmp_interval in es_in_region])
        snvs_in_region = SNVInRegion(es_in_region)
        # Get a dictionary of editing site counts.
        # alt_count = snvs_in_region.get_alt_count()
        # Find the max number of locations where editing could be detected.
        # position_set = snvs_in_region.get_position_set()
        # Create a dictionary of genomic features to hold counts.
        if args.gtf:
            features_dict = {t: 0 for t in genomic_features}
            for var_pos in es_set:
                fc = interval_tree.get_features_overlapping_position(record.chromosome, var_pos, record.strand)
                for f in fc:
                    features_dict[f] += 1

        # Count the number of SNVs. If none are present we don't even need to calculate other values.
        editing_sites_in_region_cnt = len(es_in_region)

        # if True:  # editing_sites_in_region_cnt > 0:
        if editing_sites_in_region_cnt > 1:
            # ===============================================================
            # Collect data from the VCF information.
            # 1. A dictionary keeping track of all SNVs in the genomic region.
            # 2. The sum of Alt and Ref bases at editing sites.
            # ===============================================================

            # Calc EPK ----------------------------------------------------------------------
            ref_es_in_region = vcf_itree.get_snvs_in_range(record.chromosome, record.strand, record.start, record.end)

            epk_total_ref_read_bases = 0
            epk_total_alt_read_bases = 0
            coverage_depth_list = []
            for es in ref_es_in_region:
                # es is an interval object containing records like.
                # Interval(43021013, 43021014, ('sites.vcf', 'A', 'G', -1, -1))
                start, end, metadata = es
                reference_base = metadata[1]

                # returns tuple of arrays like (array('L', [0]), array('L', [0]), array('L', [0]), array('L', [0]))
                # always in order of A, C, G, T
                read_base_counts = aligned_reads.count_coverage(record.chromosome, start, end)

                # A tuple of the counts of (reference base, alternative base).
                tmp_bases = get_ref_and_alt_cnts(reference_base, read_base_counts)

                epk_total_ref_read_bases += tmp_bases[0]
                epk_total_alt_read_bases += tmp_bases[1]
                coverage_depth_list.append(tmp_bases[0]+tmp_bases[1])
            # --------------------------------------------------------------------------------------------
            # if len(coverage_depth_list) > 0
            mean_coverage_depth = get_mean(coverage_depth_list)
            coverage_depth_std = std(coverage_depth_list)

            try:
                epk = str(round( (epk_total_alt_read_bases * 1000 ) / float(epk_total_ref_read_bases), 5))
            except ZeroDivisionError:
                epk = "0"

            if genome and len(es_set) > 0:

                # Determine the character to count i.e. G for positive strand and C for negative strand.
                # If strand data is not available use the counts transitions in the region to guess the strand.
                alt_count = snvs_in_region.get_alt_count()
                count_char = get_edited_character(record.strand, alt_count["A>G"], alt_count["T>C"])

                # Make a list of all editable positions i.e. locations of all A or C in region depending on strand.
                # Here we use a set as we will iterate over reads in the next step checking to see if the site is
                # included in the positions to check list.

                count_char_position_set = find_countable_character_positions(
                    genome, record.chromosome, record.start, record.end, count_char)

                # mean_coverage_depth = []
                editable_area = 0
                # Count the number of alternative bases that could be editing and the number of
                # unedited reference bases for each location in which editing could be detected.
                cout_pos_dict = {}
                count_edited_bases = {}

                count_edited_bases, cout_pos_dict = get_count_dicts_of_editing_at_editable_positions(
                    aligned_reads, count_char_position_set, record.chromosome, record.start, record.end,
                    count_char, es_set)

                bases_passing_cutoff = 0
                editing_sites_in_region_cnt = 0
                total_edited_bases = 0
                all_passing_bases = 0
                coverage_depth_list = []
                for el in cout_pos_dict:
                    if passes_min_coverage(cout_pos_dict[el], min_coverage):

                        tmp_ref = cout_pos_dict[el] - count_edited_bases[el]
                        total_editable_but_not_edited += tmp_ref

                        coverage_depth_list.append(cout_pos_dict[el])
                        bases_passing_cutoff += 1
                        all_passing_bases += cout_pos_dict[el]

                        over_min_editing = passes_min_editing(count_edited_bases[el], min_editing)
                        under_min_ratio = passes_max_percent_editing(tmp_ref, count_edited_bases[el],
                                                                     max_percent_coverage)
                        if over_min_editing and under_min_ratio:
                            #    editing_sites_in_region_cnt += 1
                            total_edited_bases += count_edited_bases[el]

                mean_coverage_depth = get_mean(coverage_depth_list)
                coverage_depth_std = round(std(coverage_depth_list))

                if bases_passing_cutoff > 0:
                    try:
                         REI = total_edited_bases / total_editable_but_not_edited
                    except ZeroDivisionError:
                         REI = total_edited_bases

        # If a a gtf file is not passed genomic_features will be an empty list.
        feature_list = []
        for region_type in genomic_features:
            feature_list.append(str(features_dict[region_type]) if region_type in features_dict else "0")

        genomic_region_list = [
            str(record.name),                                                          # 0
            record.chromosome+record.strand+str(record.start)+"-"+str(record.end),     # 1
            str(record.end - record.start),                                            # 2
            str(bases_passing_cutoff),                                                 # 5
            str(round(mean_coverage_depth)),                                           # 3
            str(coverage_depth_std),                                                   # 4
            str(len(es_set)),                           # str(editing_sites_in_region_cnt),
            str(total_edited_bases),                    # str(editing_sites_in_region_cnt),
            str(snvs_in_region.unique_alt_cnt["A>G"]),  # str(alt_count["A>G"]),
            str(snvs_in_region.unique_alt_cnt["T>C"]),  # str(alt_count["T>C"]),
        ]

        genomic_region_list += feature_list

        print("\t".join(genomic_region_list))


def get_bases_at_site(alignment_obj, chromosome, position):
    """

    So to convert INS from 0 to 1-based system:
    start = start + 1; end = end + 1
    and to convert INS from 1 to 0-based system:
    start = start - 1; end = end - 1

    :param alignment_obj:
    :param chromosome:
    :param position:
    :return:
    """
    # multiple_iterators=True
    position = int(position)
    read_list = alignment_obj.pileup(chromosome, position, position + 1)
    base_list = []
    for pileupcolumn in read_list:
        if pileupcolumn.pos == position:
            for pileupread in pileupcolumn.pileups:
                if not pileupread.is_del and not pileupread.is_refskip: # and not pileupread.is_duplicate
                    # if not pileupread.is_del and not pileupread.is_refskip :
                    base_list.append(pileupread.alignment.query_sequence[pileupread.query_position])

    return base_list


def get_bases_at_site_fetch(alignment_obj, chromosome, position, reference_base, alternative_base):
    """

    So to convert INS from 0 to 1-based system:
    start = start + 1; end = end + 1
    and to convert INS from 1 to 0-based system:
    start = start - 1; end = end - 1

    :param alignment_obj:
    :param chromosome:
    :param position:
    :return:
    """
    position = int(position)
    # read_list = alignment_obj.pileup(chromosome, position, position + 1)
    base_list = []

    # count_coverage
    counts = alignment_obj.count_coverage(chromosome,  position, position + 1)
    base_list = []
    print(counts[0][0])
    '''
    # for read in alignment_obj.fetch(chromosome,  position, position + 1, multiple_iterators=True):
        print(read.__dict__)
        if not read.is_duplicate:
            for i in range(len(read.query_sequence)):
                tmp_global_pos = read.pos + i
    '''
    return base_list


def editing_site(parser):
    """ Calculate site-wise information about the editing within a sample.

    The output of this function depends on the data passed to it via command line.
    The following data will always be printed for each VCF file passed:
    1. position     - The location of the editing site.
    2. transition   - The type of transition the editing site is created from.
    3. edited_bases - The number of alternative bases that match the transition type.
    4. total_bases  - The total number of editing sites in the region.
    5. edited_ratio - The number of editing sites coming from the positive strand.

    If a bed file of regions is passed the following information will also be printed for each line.
    6. Overlapping region ID.

    !Important!
    If an alignment file is passed the behavior of the program will change.
    When an alignment file is passed the all positions listed in the VCF file will be considered and
    the alignment file will be used to determine the coverage at a given site.
    This can be useful in scenarios such as creating consensus VCF files and finding instances where a
    site is covered but there is no editing present.

    Example 1:
    nretools edsite-stats               \\
        --vcf sample.editing_sites.vcf  \\

    Example 2:
    nretools edsite-stats                  \\
        --vcf     sample.editing_sites.vcf \\
        --regions organism.genes.bed

    Example 3:
    nretools edsite-stats                    \\
        --vcf       sample.editing_sites.vcf \\
        --alignment sample.bam

    """

    shared_params(parser, gtf=False, coverage=False, names=True, genome=False, editing_islands=False, region=True)

    args = parser.parse_args()

    from pysam import AlignmentFile

    titles = [
        "#position",
        "transition",
        "edited_bases",
        "total_bases",
        "edited_ratio"
    ]

    min_cov = args.min_coverage
    min_ed = args.min_editing
    max_ed = args.max_editing
    regions_file = args.region

    # name_list = args.names
    vcf_list = args.vcf
    alignment_list = args.alignment

    if args.alignment:
        min_cov = None
        min_ed = None
        max_ed = None

    # Make GTF parser obj to iterate over genomic locations.
    # First we need to know if we will be differentiating between Adar1 and Adar2 sites

    island_interval_tree = None
    if regions_file:
        # Create an interval tree from editing islands and use it to discriminate Adar1 from Adar2 sites.
        island_interval_tree = BedIntervalTree()
        island_interval_tree.add_islands_from_file_with_names(regions_file)
        titles.append("region_ID")

    print("\t".join(titles))

    for file_number in range(len(vcf_list)):

        vcf_file_name = args.vcf[file_number]

        aligned_reads = None
        if alignment_list:
            aligned_reads = AlignmentFile(alignment_list[file_number], "rb")

        # name = ""
        # if name_list:
        #     name = name_list[file_number]

        for site in generate_snvs(vcf_file_name, min_coverage=min_cov, min_editing=min_ed, max_editing=max_ed):

            if aligned_reads:
                bases = get_bases_at_site(aligned_reads, site.chromosome, site.position)
                ref_cnt = bases.count(site.reference)
                alt_cnt = bases.count(site.alteration)
            else:
                ref_cnt = site.ref_cnt
                alt_cnt = site.alt_cnt

            total_coverage = ref_cnt + alt_cnt

            out_list = []
            # if name is not None:
            #    out_list.append(name)

            region_ids_list = []
            if regions_file:
                region_ids_list = island_interval_tree.location_is_in_interval_with_names(
                    site.chromosome, site.position)

            try:
                ratio = str(round(alt_cnt / float(total_coverage), 5))
            except ZeroDivisionError:
                ratio = "0"

            out_list += [
                site.chromosome + ":" + str(site.position),
                site.reference+">"+site.alteration,
                str(alt_cnt), str(total_coverage), ratio
            ]

            if region_ids_list:
                out_list.append(region_ids_list[0])
            else:
                out_list.append("None")

            print("\t".join(out_list))


def sample_cli(parser):
    """ Calculate sample-wise information about the editing in a set of samples.

    The output of this function depends on the data passed to it via command line.
    The following data will always be printed for each VCF file passed:

    1. Sample - The name of the file
    2. ESs    - The number of editing sites detected in the sample.
    3-14.     - A>C A>G A>T C>A C>G C>T G>A G>C G>T T>A T>C T>G (The possible transitions in alphabetical order).

    Aside from the basic data a GTF file containing gene structure annotations many also be passed.
    If a GTF file is passed types the number of editing sites in the following features will be included.
    15. Intergenic Regions
    16. Exons
    17. Introns
    18. Three Prime UTRs.
    19. Five Prime UTRs.


    Examples:

    # ----------------------------------------------------------------------------------------------------------
    # Sample input files

    head -n 5 consensus_sites.vcf
    #Chromosome    Pos    ID    Ref    Alt Score    Strand    Observations
    19  56379264   .    A    G    .    .    6
    6   149725422  .    T    C    .    .    6
    3   40537447   .    A    G    .    .    3
    19  3648221    .    T    C    .    .    5

    # ----------------------------------------------------------------------------------------------------------
    # Calculate basic stats regarding a sample

    nretools sample-stats                                    \\
        --gtf   Homo_sapiens.GRCh38.90.gtf                   \\
        --names SRR2087305 SRR1998058 SRR2087291             \\
        --vcf   SRR2087305.vcf SRR1998058.vcf SRR2087291.vcf \\
        --bam   SRR2087305.coverage.tsv SRR1998058.coverage.tsv SRR2087291.coverage.tsv

    """

    shared_params(parser)

    args = parser.parse_args()

    out_lines = sample(
        args.vcf,
        coverage=args.coverage,
        names=args.names,
        gtf=args.gtf,
        islands=args.islands,
        min_coverage=args.min_coverage,
        min_editing=args.min_editing,
        max_editing=args.max_editing
    )

    print("\n".join(out_lines))
