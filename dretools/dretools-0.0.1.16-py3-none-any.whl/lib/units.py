from pysam import AlignmentFile
from lib.parsers import BED, get_coverage_total_area_covered
from lib.parsers import generate_snvs


def __get_ref_and_alt_counts(reference_base, read_base_counts):
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


def __calc_epk(total_reference_read_bases, total_alternative_read_bases):
    try:
        epk = (total_alternative_read_bases * 1000) / float(total_reference_read_bases)
    except ZeroDivisionError:
        epk = 0
    return epk


def epk_region_wise(parser):
    """ Find epk for regions.

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

    from lib.parsers import VCFIntervalTree

    bed_path = args.regions
    alignment_path = args.alignment
    max_editing_ratio = 0.99

    alignment_obj = AlignmentFile(alignment_path, "rb")  # alignment_path[0]

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
            "#Sample_Name",
            "Editable_Area",
            "Average_Depth",
            "Total_Ref_Bases",
            "Total_Alt_Bases",
            "EPK"
        ]
    ))

    for record in bed_obj.yield_lines():

        es_in_region = vcf_itree.get_snvs_in_range(record.chromosome, record.strand, record.start, record.end)

        total_ref_read_bases = 0
        total_alt_read_bases = 0
        editable_area_count = 0
        depth_cnt = 0

        for es in es_in_region:
            # es is an interval object containing records like.
            # Interval(43021013, 43021014, ('sites.vcf', 'A', 'G', -1, -1))
            start, end, metadata = es
            reference_base = metadata[1]

            # returns tuple of arrays like (array('L', [0]), array('L', [0]), array('L', [0]), array('L', [0]))
            # always in order of A, C, G, T
            read_base_counts = alignment_obj.count_coverage(record.chromosome, start, end)

            # A tuple of the counts of (reference base, alternative base).
            tmp_ref_bases, tmp_alt_bases = __get_ref_and_alt_counts(reference_base, read_base_counts)

            # Check to ensure bases pass.
            tmp_total_coverage = tmp_ref_bases + tmp_alt_bases

            # Ensure editing is under max edited ratio.
            if tmp_total_coverage > 0 and tmp_alt_bases / float(tmp_total_coverage) < max_editing_ratio:
                # Used to calculate EPK.
                total_ref_read_bases += tmp_ref_bases
                total_alt_read_bases += tmp_alt_bases

                # Used for other purposes.
                editable_area_count += 1
                depth_cnt += tmp_total_coverage

        epk_str = str(round(__calc_epk(total_ref_read_bases, total_alt_read_bases), 7))

        editable_area_count_str = str(editable_area_count)
        try:
            average_depth_str = str(round(depth_cnt / float(editable_area_count)))
        except ZeroDivisionError:
            average_depth_str = "0"

        print(
            "\t".join(
                [
                    record.name,
                    editable_area_count_str,
                    average_depth_str,
                    str(total_ref_read_bases),
                    str(total_alt_read_bases),
                    epk_str
                ]
            )
        )


'''
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
        print("\t".join(
            [
                # record.chromosome,
                # str(record.start),
                # str(record.end),
                record.name,
                # record.strand,
                str(total_ref_read_bases),
                str(total_alt_read_bases),
                epk_str
            ]
        ))
'''


def epk_sample_wise(parser):
    """ Calculate the editing per kilo-read-base
    """

    def split_list(the_list, chunk_size):
        result_list = []
        while the_list:
            result_list.append(the_list[:chunk_size])
            the_list = the_list[chunk_size:]
        return result_list

    parser.add_argument("--name", type=str, default=None)
    parser.add_argument("--vcf", type=str)
    parser.add_argument("--alignment", type=str)

    args = parser.parse_args()

    from pysam import AlignmentFile

    alignment_obj = AlignmentFile(args.alignment, "rb")

    name = args.name
    if name is None:
        name = args.alignment

    total_ref_read_bases = 0
    total_alt_read_bases = 0
    max_editing_ratio = 0.99
    editable_area_count = 0
    depth_cnt = 0

    # The coverage is computed per-base [ACGT].
    for site in generate_snvs(args.vcf):

        pos = int(site.position)

        # Returned in the order of A, C, G, T.
        read_base_counts = alignment_obj.count_coverage(site.chromosome, pos, pos + 1)

        tmp_ref_bases, tmp_alt_bases = __get_ref_and_alt_counts(site.reference, read_base_counts)

        # Check to ensure bases pass.
        tmp_total_coverage = tmp_ref_bases + tmp_alt_bases

        # Ensure editing is under max edited ratio.
        if tmp_total_coverage > 0 and tmp_alt_bases/float(tmp_total_coverage) < max_editing_ratio:

            # Used to calculate EPK.
            total_ref_read_bases += tmp_ref_bases
            total_alt_read_bases += tmp_alt_bases

            # Used for other purposes.
            editable_area_count += 1
            depth_cnt += tmp_total_coverage

    epk_str = str(round(__calc_epk(total_ref_read_bases, total_alt_read_bases), 7))
    editable_area_count_str = str(editable_area_count)
    average_depth_str = str(round(depth_cnt / float(editable_area_count)))

    print("\t".join(
        [
            "#Sample_Name",
            "Editable_Area",
            "Average_Depth",
            "Total_Ref_Bases",
            "Total_Alt_Bases",
            "EPK"
        ]
    ))

    print(
        "\t".join(
            [
                name,
                editable_area_count_str,
                average_depth_str,
                str(total_ref_read_bases),
                str(total_alt_read_bases),
                epk_str
            ]
        )
    )


def epk_site_wise(parser):
    """ Calculate the editing per kilo-read-base
    """

    def split_list(the_list, chunk_size):
        result_list = []
        while the_list:
            result_list.append(the_list[:chunk_size])
            the_list = the_list[chunk_size:]
        return result_list

    # parser.add_argument("--name", type=str, default=None)
    parser.add_argument("--vcf", type=str)
    parser.add_argument("--alignment", type=str)

    args = parser.parse_args()

    from pysam import AlignmentFile

    alignment_obj = AlignmentFile(args.alignment, "rb")

    #name = args.name
    #if name is None:
    #    name = args.alignment

    total_ref_read_bases = 0
    total_alt_read_bases = 0
    max_editing_ratio = 0.99
    editable_area_count = 0
    depth_cnt = 0

    print("\t".join(
        [
            "#Name",
            "Area",
            "Depth",
            "Ref_Bases",
            "Alt_Bases",
            "EPK"
        ]
    ))

    # The coverage is computed per-base [ACGT].
    for site in generate_snvs(args.vcf):
        total_ref_read_bases = 0
        total_alt_read_bases = 0
        editable_area_count = 0
        pos = int(site.position)

        # Returned in the order of A, C, G, T.
        read_base_counts = alignment_obj.count_coverage(site.chromosome, pos, pos + 1)

        tmp_ref_bases, tmp_alt_bases = __get_ref_and_alt_counts(site.reference, read_base_counts)

        # Check to ensure bases pass.
        tmp_total_coverage = tmp_ref_bases + tmp_alt_bases

        # Ensure editing is under max edited ratio.
        if tmp_total_coverage > 0 and tmp_alt_bases/float(tmp_total_coverage) < max_editing_ratio:

            # Used to calculate EPK.
            total_ref_read_bases += tmp_ref_bases
            total_alt_read_bases += tmp_alt_bases

            # Used for other purposes.
            editable_area_count += 1
            depth_cnt += tmp_total_coverage

        epk_str = str(round(__calc_epk(total_ref_read_bases, total_alt_read_bases), 7))
        editable_area_count_str = str(editable_area_count)

        try:
            average_depth_str = str(round(depth_cnt / float(editable_area_count)))
        except ZeroDivisionError:
            average_depth_str = "0"

        print(
            "\t".join(
                [
                    #name,
                    site.chromosome + ":" + str(pos),
                    editable_area_count_str,
                    average_depth_str,
                    str(total_ref_read_bases),
                    str(total_alt_read_bases),
                    epk_str
                ]
            )
        )

