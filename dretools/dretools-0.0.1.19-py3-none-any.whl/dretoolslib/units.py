from pysam import AlignmentFile
from dretoolslib.parsers import BED
from dretoolslib.parsers import generate_snvs
from dretoolslib.io import max_editing, alignment_parameters
from dretoolslib.shared import impute_strand, is_strand_value_legal, get_refernce_and_alt_characters

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


def ecpm_sample_wise(parser):
    """ Calculate ECPM for an entire sample.

    """
    # @TODO: Move the old ECPM code from stats to here.
    pass


def calculate_aei(parser):
    """ Calculate AEI (ALU Editing Index)

    AEI is a unit developed by Paz-Yaacov N., el all 2015 that measures editing within editing sites.

    https://www.ncbi.nlm.nih.gov/pubmed/26440895
    :param parser:
    :return:
    """

    max_editing(parser)
    parser.add_argument("--name", type=str, default="AEI")
    parser.add_argument("--vcf", type=str)
    parser.add_argument("--genome", type=str, help='')
    parser.add_argument("--regions", type=str, default=None)

    # Adds args.alignment and args.min_qscore
    alignment_parameters(parser)

    args = parser.parse_args()

    from pysam import AlignmentFile
    from dretoolslib.parsers import FASTA
    from dretoolslib.parsers import VCFIntervalTree
    from dretoolslib.parsers import SNVInRegion
    from dretoolslib.shared import passes_min_coverage, passes_min_editing, get_strand, \
        base_transition_tuples_and_titles, passes_max_percent_editing, get_edited_character
    from numpy import average

    bed_obj = BED(args.regions)
    alignment_obj = AlignmentFile(args.alignment, "rb")
    fasta_obj = FASTA(args.genome)
    vcf_itree = VCFIntervalTree(args.vcf, 1, 1, 1.0)
    # Iterate over given repetative elements.
    ref_and_alt_count_list = []
    expression = []

    Editable_Area = 0
    Average_Depth = 0
    Total_Ref_Bases = 0  
    Total_Alt_Bases = 0

    for record in bed_obj.yield_lines():
        # es_in_region = vcf_itree.get_snvs_in_range(record.chromosome, record.strand, record.start, record.end)
        # Count the number of aligned reads overlapping the repeat region.
        #aligned_read_cnt = alignment_obj.count(record.chromosome, record.start, record.end)
        #if aligned_read_cnt > 0:

        strand = record.strand
        if not is_strand_value_legal(strand):
            # Impute strand

            # Find all known editing sites in region.
            es_in_region = vcf_itree.get_snvs_in_range(record.chromosome, record.start, record.end)

            if len(es_in_region) > 0:
                es_set = set([tmp_interval[0] for tmp_interval in es_in_region])
                snvs_in_region = SNVInRegion(es_in_region)
                # Determine the character to count i.e. G for positive strand and C for negative strand.
                # If strand data is not available use the counts transitions in the region to guess the strand.
                alt_count = snvs_in_region.get_alt_count()
                strand = impute_strand(alt_count["A>G"], alt_count["T>C"])

        # @TODO: Allow for other strand formats using a function in BED class.
        reference_base, alternative_base = get_refernce_and_alt_characters(strand)
        
        if reference_base is not None: 
            # Get the location of all adenosines within the region.
            # Bed files should be zero-based (the same as pysam regions) so no need to adjust start and stop.
            countable_positions = fasta_obj.find_countable_character_positions(
                record.chromosome, record.start, record.end, reference_base)

            for position in countable_positions:

                # VCF files are 1-based so adjust stop position.
                read_base_counts = alignment_obj.count_coverage(
                    record.chromosome,
                    position,
                    position + 1,
                    quality_threshold=args.min_qscore,
                    read_callback='all')
                
                tmp_ref_bases, tmp_alt_bases = __get_ref_and_alt_counts(reference_base, read_base_counts)
                 
                if tmp_ref_bases > 0:
                    Editable_Area += 1
                    Total_Ref_Bases += tmp_ref_bases
                    Total_Alt_Bases += tmp_alt_bases
                     
                    editing_ratio = tmp_alt_bases/float(tmp_ref_bases)
                    coverage = float(tmp_ref_bases+tmp_alt_bases)
                    ref_and_alt_count_list.append(editing_ratio)
                    expression.append(coverage)
     
    #Sample_Name   Editable_Area    Average_Depth    Total_Ref_Bases    Total_Alt_Bases    EPK
    #SRR5048072    180210           6                979203             177582             181.3
    AEI = average(ref_and_alt_count_list, weights=expression)
    Average_Depth = (Total_Ref_Bases + Total_Alt_Bases) / Editable_Area
    print("\t".join(
     [
       "Sample_Name",
       "Editable_Area", 
       "Average_Depth", 
       "Total_Ref_Bases", 
       "Total_Alt_Bases", 
       "EPK"
    ]
    ))
 
    out_list = [args.name, Editable_Area, Average_Depth, Total_Ref_Bases, Total_Alt_Bases, AEI]
    out_str = [str(s) for s in out_list]
    print( '\t'.join( out_str))
    

def epk_sample_wise(parser):
    """ Calculate the editing-per-kilobase (EPK) for a sample.

    This function calculates the editing-per-kilobase (EPK) of an entire sample, which can be used to describe the
    global-editing-rate of the sample. Representing the global-editing-rate in EPK helps to reduce
    sample-biases, such as differing library sizes.

    Warning: Calculating the EPK of large libraries make take a long time.

    Examples:
        Note: This function assumes that and index (ending in .bai) file accompanies the bam files.
              Indexes can be calculated with 'samtools index samples.bam'

    # ----------------------------------------------------------------------------------------------------------
    # Sample input files

    head -n 5 consensus_sites.vcf
    #Chromosome    Pos    ID    Ref    Alt Score    Strand    Observations
    19  56379264   .    A    G    .    .    6
    6   149725422  .    T    C    .    .    6
    3   40537447   .    A    G    .    .    3
    19  3648221    .    T    C    .    .    5


    # ----------------------------------------------------------------------------------------------------------
    # Find the global-editing-rate of a sample in EPK

    dretools sample-epk            \\
        --vcf consensus_sites.vcf  \\
        --alignment BAM/SRR3091833.ex.bam
    #Sample_Name    Editable_Area    Average_Depth    Total_Ref_Bases    Total_Alt_Bases    EPK
    BAM/SRR3091833.ex.bam    87    8    692    43    62.1387283


    # ----------------------------------------------------------------------------------------------------------
    # Modify the sample name

    dretools sample-epk            \\
        --name Control_1           \\
        --vcf consensus_sites.vcf  \\
        --alignment BAM/SRR3091833.ex.bam
    #Sample_Name    Editable_Area    Average_Depth    Total_Ref_Bases    Total_Alt_Bases    EPK
    Control_1    87    8    692    43    62.1387283

    # ----------------------------------------------------------------------------------------------------------

    """

    max_editing(parser)
    parser.add_argument("--name", type=str, default=None)
    parser.add_argument("--vcf", type=str)
    # Adds args.alignment and args.min_qscore
    alignment_parameters(parser)

    args = parser.parse_args()

    from pysam import AlignmentFile

    alignment_obj = AlignmentFile(args.alignment, "rb")
    max_editing_ratio = args.max_editing
    name = args.name
    if name is None:
        name = args.alignment

    total_ref_read_bases = 0
    total_alt_read_bases = 0
    editable_area_count = 0
    depth_cnt = 0

    # The coverage is computed per-base [ACGT].
    for site in generate_snvs(args.vcf):

        pos = int(site.position)

        # Returned in the order of A, C, G, T.
        read_base_counts = alignment_obj.count_coverage(
            site.chromosome, pos, pos + 1, quality_threshold=args.min_qscore, read_callback='all')

        tmp_ref_bases, tmp_alt_bases = __get_ref_and_alt_counts(site.reference, read_base_counts)

        # Check to ensure bases pass.
        tmp_total_coverage = tmp_ref_bases + tmp_alt_bases
        
        try: 
            tmp_ratio = tmp_alt_bases/float(tmp_total_coverage)
        except ZeroDivisionError:
            tmp_ratio = 0
         
        # Ensure editing is under max edited ratio.
        if tmp_total_coverage > 0 and tmp_alt_bases/float(tmp_total_coverage) < max_editing_ratio:

            # Used to calculate EPK.
            total_ref_read_bases += tmp_ref_bases
            total_alt_read_bases += tmp_alt_bases

            # Used for other purposes.
            editable_area_count += 1
            depth_cnt += tmp_total_coverage

    epk_str = str(round(__calc_epk(total_ref_read_bases, total_alt_read_bases), 5))
    editable_area_count_str = str(editable_area_count)
    try: 
        average_depth_str = str(round(depth_cnt / float(editable_area_count)))
    except ZeroDivisionError: 
        average_depth_str = 0
    
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


def epk_region_wise(parser):
    """ Calculate the editing-per-kilobase (EPK) for transcriptomic regions.

    This function calculates the editing-per-kilobase (EPK) user defined transcriptomic regions within a sample.
    Here we define transcriptomic regions as any region covered by reads with a start and stop position. This is
    designed for use with editing islands, but can be used for any region defined by a bed file. However, it is
    recommended to keep these small, as per-site read coverage becomes increasingly variable with increased size.
    Representing the global-editing-rate in EPK helps to reduce sample-biases, such as differing library sizes.

    Warning: Calculating the EPK of large libraries make take a long time.

    Examples:
        Note: This function assumes that and index (ending in .bai) file accompanies the bam files.
              Indexes can be calculated with 'samtools index sample.bam'

    # ----------------------------------------------------------------------------------------------------------
    # Sample input files

    head -n 5 consensus_sites.vcf
    #Chromosome    Pos    ID    Ref    Alt Score    Strand    Observations
    19  56379264   .    A    G    .    .    6
    6   149725422  .    T    C    .    .    6
    3   40537447   .    A    G    .    .    3
    19  3648221    .    T    C    .    .    5

    head -n 5 islands.bed
    #Chromosome    Start    End    ID    Score    Strand    Length    Number_of_Sites    Density
    2    128192920  128193033   ub5Kpx5pky615pmsdq4PiQ    .    +    113    7    0.06195
    7    38723547   38723651    kluKgmv4-KKrQsRMYX_iCA    .    -    104    6    0.05769
    6    149725405  149725553   kt31w8egfUS3NGIlr1dTeg    .    -    148    10   0.06757
    19   3648149    3648239     SUz1q7g3dUYHVjlhFK4ZAg    .    -    90    8     0.08889

    # ----------------------------------------------------------------------------------------------------------
    # Finding the editing intensity with editing islands

    dretools region-epk            \\
        --vcf consensus_sites.vcf  \\
        --regions islands.bed      \\
        --alignment BAM/SRR3091828.ex.bam  > SRR3091828.island_epk.tsv
    #Region_ID    Editable_Area    Average_Depth    Total_Ref_Bases    Total_Alt_Bases    EPK   Sample_Name
    ub5Kpx5pky615pmsdq4PiQ    4    7    20    9    450.0     Control_1
    kluKgmv4-KKrQsRMYX_iCA    4    10   27    14   518.5185  Control_1
    kt31w8egfUS3NGIlr1dTeg    3    8    11    12   1090.909  Control_1
    SUz1q7g3dUYHVjlhFK4ZAg    3    5    8     8    1000.0    Control_1
    Z1kllXDbos-rNv9UTjIXzA    2    10   14    7    500.0     Control_1

    # ----------------------------------------------------------------------------------------------------------
    # Add an optional name

    # This is useful when planning to import tables into R or Pandas.
    dretools region-epk            \\
        --name                     \\
        --vcf consensus_sites.vcf  \\
        --regions islands.bed      \\
        --alignment BAM/SRR3091828.ex.bam  > SRR3091828.island_epk.tsv
    #Region_ID    Editable_Area    Average_Depth    Total_Ref_Bases    Total_Alt_Bases    EPK
    ub5Kpx5pky615pmsdq4PiQ    4    7    20    9    450.0
    kluKgmv4-KKrQsRMYX_iCA    4    10   27    14   518.5185185
    kt31w8egfUS3NGIlr1dTeg    3    8    11    12   1090.9090909
    SUz1q7g3dUYHVjlhFK4ZAg    3    5    8     8    1000.0
    Z1kllXDbos-rNv9UTjIXzA    2    10   14    7    500.0

    # ----------------------------------------------------------------------------------------------------------
    """

    max_editing(parser)

    parser.add_argument(
        "--name", type=str, default=None
    )

    parser.add_argument(
        "--vcf",
        type=str,
        help="")

    parser.add_argument(
        "--regions",
        type=str,
        help="")

    # Adds args.alignment and args.min_qscore
    alignment_parameters(parser, nargs="?")

    args = parser.parse_args()

    from dretoolslib.parsers import VCFIntervalTree

    bed_path = args.regions
    alignment_path = args.alignment
    max_editing_ratio = args.max_editing
    name = args.name

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
    titles = [
            "#Region_ID",
            "Editable_Area",
            "Average_Depth",
            "Total_Ref_Bases",
            "Total_Alt_Bases",
            "EPK"
        ]
    if name is not None:
        titles.append("Sample_Name")
    print("\t".join(titles))

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
            read_base_counts = alignment_obj.count_coverage(
                record.chromosome, start, end, quality_threshold=args.min_qscore, read_callback='all')

            # A tuple of the counts of (reference base, alternative base).
            tmp_ref_bases, tmp_alt_bases = __get_ref_and_alt_counts(reference_base, read_base_counts)

            # Check to ensure bases pass.
            tmp_total_coverage = tmp_ref_bases + tmp_alt_bases
            
            # Ensure editing is under max edited ratio.
            try:
                tmp_editing_ratio = tmp_alt_bases / float(tmp_total_coverage)
            except ZeroDivisionError:
                tmp_editing_ratio = 0
             
            if tmp_total_coverage > 0 and tmp_editing_ratio < max_editing_ratio:
                # Used to calculate EPK.
                total_ref_read_bases += tmp_ref_bases
                total_alt_read_bases += tmp_alt_bases

                # Used for other purposes.
                editable_area_count += 1
                depth_cnt += tmp_total_coverage

        epk_str = str(round(__calc_epk(total_ref_read_bases, total_alt_read_bases), 5))

        editable_area_count_str = str(editable_area_count)
        try:
            average_depth_str = str(round(depth_cnt / float(editable_area_count)))
        except ZeroDivisionError:
            average_depth_str = "0"

        out_data = [
            record.name,
            editable_area_count_str,
            average_depth_str,
            str(total_ref_read_bases),
            str(total_alt_read_bases),
            epk_str
        ]

        if name is not None:
            out_data.append(name)

        print("\t".join(out_data))


def epk_site_wise(parser):
    """ Calculate the editing-per-kilobase (EPK) for editing sites.

    This function calculates the editing-per-kilobase (EPK) for locations with known editing sites within a sample.
    Representing the global-editing-rate in EPK helps to reduce sample-biases, such as differing library sizes.

    Warning: Calculating the EPK of large libraries make take a long time.

    Examples:
        Note: This function assumes that and index (ending in .bai) file accompanies the bam files.
              Indexes can be calculated with 'samtools index samples.bam'

    # ----------------------------------------------------------------------------------------------------------
    # Sample input files

    head -n 5 consensus_sites.vcf
    #Chromosome    Pos    ID    Ref    Alt Score    Strand    Observations
    19  56379264   .    A    G    .    .    6
    6   149725422  .    T    C    .    .    6
    3   40537447   .    A    G    .    .    3
    19  3648221    .    T    C    .    .    5


    # ----------------------------------------------------------------------------------------------------------
    # Calculate the EPK for locations of known editing sites

    dretools edsite-epk   \\
        --vcf merged.vcf  \\
        --alignment BAM/SRR3091833.ex.bam
    #Name    Area    Depth    Ref_Bases    Alt_Bases    EPK
    19:56379264   1    9    3    6    2000.0
    6:149725422   1    8    2    6    3000.0
    3:40537447    0    0    0    0    0
    19:3648221    0    0    0    0    0

    #  ----------------------------------------------------------------------------------------------------------
    # Add an optional name

    # This is useful when planning to import tables into R or Pandas.
    dretools edsite-epk   \\
        --name Control_1  \\
        --vcf merged.vcf  \\
        --alignment BAM/SRR3091833.ex.bam
    #Site_Location   Area   Depth   Ref_Bases   Alt_Bases   EPK   Sample_Name
    19:56379264  1   9   3   6   2000.0 Control_1
    6:149725422  1   8   2   6   3000.0 Control_1
    3:40537447   0   0   0   0   0      Control_1
    19:3648221   0   0   0   0   0      Control_1

    # ----------------------------------------------------------------------------------------------------------
    """

    max_editing(parser)
    parser.add_argument("--name", type=str, default=None)
    parser.add_argument("--vcf", type=str)
    # Adds args.alignment and args.min_qscore
    alignment_parameters(parser)

    args = parser.parse_args()

    from pysam import AlignmentFile

    alignment_obj = AlignmentFile(args.alignment, "rb")
    name = args.name
    max_editing_ratio = args.max_editing

    titles = [
            "#Site_Location",
            "Area",
            "Depth",
            "Ref_Bases",
            "Alt_Bases",
            "EPK"
        ]

    if name is not None:
        titles.append("Sample_Name")

    print("\t".join(titles))

    # The coverage is computed per-base [ACGT].
    for site in generate_snvs(args.vcf):
        total_ref_read_bases = 0
        total_alt_read_bases = 0
        editable_area_count = 0
        depth_cnt = 0

        pos = int(site.position)

        # Returned in the order of A, C, G, T.
        read_base_counts = alignment_obj.count_coverage(
            site.chromosome, pos, pos + 1, quality_threshold=args.min_qscore, read_callback='all')

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

        epk_str = str(round(__calc_epk(total_ref_read_bases, total_alt_read_bases), 5))
        editable_area_count_str = str(editable_area_count)

        try:
            average_depth_str = str(round(depth_cnt / float(editable_area_count)))
        except ZeroDivisionError:
            average_depth_str = "0"

        out_data = [
            site.chromosome + ":" + str(pos),
            editable_area_count_str,
            average_depth_str,
            str(total_ref_read_bases),
            str(total_alt_read_bases),
            epk_str,

        ]
        if name is not None:
            out_data.append(name)

        print("\t".join(out_data))
