from collections import namedtuple
from random import randint, random
from statistics import mean, stdev
from lib.parsers import generate_snvs
from math import floor

FILE_DELIMITER = ","
import warnings
warnings.filterwarnings("ignore")


def make_groups(dict_of_groups, labels=None):
    """
    { "bam": ["bam1,bam2", "bam3,bam4"]
    {
        "group_1": {"vcf":[vcf_1, vcf_2], "bam":[bam_1, bam_2]}
        "group_2": {"vcf":[vcf_3, vcf_4], "bam":[bam_3, bam_4]}
    }

    :param dict_of_groups:
    :return:
    """

    sorted_keys = sorted(dict_of_groups)

    if labels:
        labels = ",".split(FILE_DELIMITER)
    else:
        first_label_groups = len(dict_of_groups[sorted_keys[0]])
        labels = []
        for i in range(1, first_label_groups+1):
            labels.append("Group_%s" % i)

    group_names = []
    for dict_key in sorted(dict_of_groups):
        group_names.append(dict_key)

    print(group_names)

    GroupObj = namedtuple('GroupObj', group_names)

    g = GroupObj(["1", "3"], ["2", "4"])

    groups = []
    for i in range(len(labels)):
        tmp_list = []
        for sorted_key in sorted_keys:
            tmp_list.append(dict_of_groups[sorted_key][i].split(","))

        print(tmp_list)

        groups.append(GroupObj(*tmp_list))
    return groups


def build_grouped_sample_data_structure(list_of_grouped_samples, delimiter=","):
    """ Build an ordered nested data structure of groups with samples files contained within.

    :param list_of_grouped_samples:
    :param delimiter:
    :return:
    """
    return [group.split(delimiter) for group in list_of_grouped_samples]


def site_level_differential_editing_decision_function(group_1, group_2, coverage_1, coverage_2):

    choices = ["YES", "NO", "NO_TEST"]

    return choices[randint(0, 2)], random()


def find_total_area_covered(n, file_name):
    total_area = 0
    for line in open(file_name):
        sl = line.split()
        if sl[0] == "genome" and int(sl[1]) >= n:
            total_area += int(sl[2])
    return total_area


def find_coverage(info):
    return int(info.split("DP=")[-1].split(";")[0])


def normalized_editing(sites, total_area_covered):
    return round((sites * 1.0e6) / total_area_covered, 5)


def resolve_names(names, default_groups):
    """

    :param names:
    :param default_groups:
    :return:
    """
    if names:
        group_names = names[0].split(",")
    else:
        group_names = [str(group_int) for group_int in range(len(default_groups))]
    return group_names


def filter_bases(bases, min_coverage=5):
    """

    :param bases:
    :param min_coverage:
    :param alt_cnt:
    :return:
    """
    group_over_cutoff = []
    group_over_cutoff_alt = []
    total_coverage = 0
    for tmp_sample_name in bases:
        ref_cnt = float(bases[tmp_sample_name][0])
        alt_cnt = float(bases[tmp_sample_name][1])
        total = ref_cnt + alt_cnt
        if total >= min_coverage:  # and alt_cnt >= min_editing
            total_coverage += total
            group_over_cutoff.append(alt_cnt / total)
            group_over_cutoff_alt.append(alt_cnt)

    return group_over_cutoff, total_coverage


def decide_outcome(p_value_1, group_1, p_value_2, group_2, cutoff=0.05):

    if p_value_1 <= 0.05:
        return p_value_1, group_1
    elif p_value_2 <= 0.05:
        return p_value_2, group_2
    else:
        return sorted([p_value_1, p_value_2])[0], "NONS"


def generate_group_pairs(group_list):
    # Make Comparison Groups
    group_pair_list = []

    tmp_list = list(sorted(group_list))
    while tmp_list:
        name_1 = tmp_list.pop(0)
        for name_2 in tmp_list:
            group_pair_list.append((name_1, name_2))

    return group_pair_list


def region_diff(parser):
    """ Check for significant differences in editing within genomic regions among samples.

    :param parser:
    :return:
    """

    from lib.parsers import BED
    from scipy.stats import ttest_ind
    import rpy2.robjects as robjects
    from rpy2.robjects import StrVector, FloatVector
    import rpy2.robjects.packages as rpackages

    from lib.parsers import EditingInSample
    # from import generate_snvs, coverage_depth, find_numbers_of_ref_and_alt_reads
    r_script = """

    df1<-data.frame(
       group=group_ids,
       sampleEPK=sample_epk,
       regionEPK=region_epk,
       regionSize=region_size,
       regionDepth=region_depth
    )

    minVal <- min( df1$regionEPK[df1$regionEPK>0] ) / 2
    df1$regionEPK[df1$regionEPK<=0] <- minVal
    df1$logRegionEPK <-log(df1$regionEPK)
    df1$logSampleEPK <-log(df1$sampleEPK)

    lm1<-lm(logRegionEPK ~ logSampleEPK + regionSize + regionDepth + group, data=df1)
    #lm1<-lm(logRegionEPK ~ logSampleEPK + group, data=df1)

    p_value <- summary(lm1)$coefficients

    """
    parser.add_argument(
        "--regions",
        type=str,
        help="")

    parser.add_argument(
        "--stat-file",
        type=str,
        default=None,
        help="")

    parser.add_argument(
        "--max-coverage-cov",
        type=float,
        default=0.5,
        help="")

    parser.add_argument(
        "--max-depth-cov",
        type=float,
        default=0.5,
        help="")

    parser.add_argument(
        "--min-area",
        type=float,
        default=20,
        help="")

    parser.add_argument(
        "--min-depth",
        type=float,
        default=10,
        help="")

    parser.add_argument(
        "--names",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--sample-epk",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--region-epk",
        nargs='+',
        type=str,
        help="")

    args = parser.parse_args()

    bed_path = args.regions

    sample_epk = build_grouped_sample_data_structure(args.sample_epk)
    region_epk = build_grouped_sample_data_structure(args.region_epk)

    # max_cl = 30
    # Decide what the group names should be.
    # Returns a list of group names.
    # Will be a list of comma separated names provided to the names parameter or a list of integers.
    group_names = resolve_names(args.names, sample_epk)

    tmp_list = [group_int for group_int in range(len(sample_epk))]

    # =========================================================================
    # Make SampleGroups Obj
    # =========================================================================

    groups_dict = {}
    min_samples_in_group = len(group_names[0])

    for group_i in range(len(group_names)):

        number_of_samples = len(sample_epk[group_i])

        if number_of_samples < min_samples_in_group:
            min_samples_in_group = number_of_samples

        for sample_i in range(number_of_samples):
            epk_in_sample = sample_epk[group_i][sample_i]
            epk_in_region = region_epk[group_i][sample_i]

            editing_obj = EditingInSample(epk_in_sample, epk_in_region)

            tmp_group_name = group_names[group_i]
            try:
                groups_dict[tmp_group_name].append(editing_obj)
            except KeyError:
                groups_dict[tmp_group_name] = [editing_obj]

    # Get a a tuple of all possible sets of two groups.
    group_comparisons = generate_group_pairs(group_names)

    bed_obj = BED(bed_path)
    rpvalcnt = 0
    tpvalcnt = 0
    testable = 0
    min_average_depth = args.min_depth
    min_editing_area = args.min_area
    max_coverage_cov = args.max_coverage_cov
    max_depth_cov = args.max_depth_cov

    for record in bed_obj.yield_lines():

        for group_1_name, group_2_name in group_comparisons:

            region_epks, sample_epks, region_size, region_avg_depth, group_ids = [], [], [], [], []
            val_dict = {}

            for tmp_group_name in (group_1_name, group_2_name):
                if tmp_group_name not in val_dict:
                    val_dict[tmp_group_name] = []

                for tmp_sample in groups_dict[tmp_group_name]:

                    tmp_region_depth = tmp_sample.get_region_depth(record.name)

                    if tmp_region_depth > min_average_depth:
                        region_avg_depth.append(tmp_region_depth)
                        group_ids.append(tmp_group_name)
                        sample_epks.append(tmp_sample.get_sample_epk())
                        # Region-wise data.
                        tmp_region_epk = tmp_sample.get_region_epk(record.name)
                        region_epks.append(tmp_sample.get_region_epk(record.name))
                        region_size.append(tmp_sample.get_region_size(record.name))

                        val_dict[tmp_group_name].append(tmp_region_epk)

            # When zero editing is detectable in regions this will cause errors when calculating stddev.
            at_least_one_region_has_editing = sum(region_epks) > 0

            # Make sure we can test at least almost half of the samples.
            min_samples_for_testability = floor(min_samples_in_group/2)
            min_samples_for_testability = 2 if  min_samples_for_testability <= 1 else min_samples_for_testability
            group_1_is_testable = len(val_dict[group_1_name]) > min_samples_for_testability
            group_2_is_testable = len(val_dict[group_2_name]) > min_samples_for_testability

            if at_least_one_region_has_editing and group_1_is_testable and group_2_is_testable:

                area_cov = stdev(region_size)/mean(region_size)
                depth_cov = stdev(region_avg_depth)/mean(region_avg_depth)
                region_max_editing_area = sorted(region_size)[-1]

                if area_cov < max_coverage_cov and min_editing_area < region_max_editing_area and depth_cov < max_depth_cov:

                    testable += 1

                    robjects.globalenv['group_ids'] = StrVector(group_ids)
                    robjects.globalenv['region_depth'] = FloatVector(region_avg_depth)
                    robjects.globalenv['sample_epk'] = FloatVector(sample_epks)
                    robjects.globalenv['region_epk'] = FloatVector(region_epks)
                    robjects.globalenv['region_size'] = FloatVector(region_size)

                    robjects.r(r_script)

                    p_value = robjects.globalenv["p_value"][-1]

                    if p_value < 0.05:
                        rpvalcnt += 1

                    g1_mean = mean(val_dict[group_1_name])
                    g2_mean = mean(val_dict[group_2_name])

                    ttest_results = ttest_ind(val_dict[group_1_name], val_dict[group_2_name])
                    if ttest_results[1] < 0.05:
                        tpvalcnt += 1

                    print(
                        "\t".join(
                         [
                             group_1_name,
                             group_2_name,
                             record.name,
                             record.chromosome+":"+str(record.start)+"-"+str(record.end),
                             str(round(g1_mean, 2)),
                             str(round(g2_mean, 2)),
                             str(round(p_value, 7)),
                             str(round(ttest_results[1], 7))
                          ]
                        )
                    )


def editing_site_diff(parser):
    """ Check for significant differences in editing of individual sites among samples.

    Sample_A1,Sample_A2  Sample_B1,Sample_B2  Sample_C1,Sample_C2

    """

    from lib.parsers import BED
    from scipy.stats import ttest_ind
    import rpy2.robjects as robjects
    from rpy2.robjects import StrVector, FloatVector
    # import rpy2.robjects.packages as rpackages
    from lib.parsers import EditingInSample

    # from import generate_snvs, coverage_depth, find_numbers_of_ref_and_alt_reads
    r_script = """

    df1<-data.frame(
       group=group_ids,
       sampleEPK=sample_epk,
       regionEPK=region_epk,
       regionSize=region_size,
       regionDepth=region_depth
    )

    minVal <- min( df1$regionEPK[df1$regionEPK>0] ) / 2
    df1$regionEPK[df1$regionEPK<=0] <- minVal
    df1$logRegionEPK <-log(df1$regionEPK)
    df1$logSampleEPK <-log(df1$sampleEPK)

    lm1<-lm(logRegionEPK ~ logSampleEPK + regionSize + regionDepth + group, data=df1)

    p_value <- summary(lm1)$coefficients

    """

    # shared_params(parser, gtf=False, editing_islands=False, bed=True, genome=True)

    parser.add_argument(
        "--names",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--min-depth",
        type=float,
        default=10,
        help="")

    parser.add_argument(
        "--sample-epk",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--vcf",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--max-coverage-cov",
        type=float,
        default=0.50,
        help="")

    args = parser.parse_args()

    # alignment_groups = args.alignment
    # vcf_groups = args.vcf
    # coverage_groups = args.coverage

    sample_epk = build_grouped_sample_data_structure(args.sample_epk)
    vcf_edited = build_grouped_sample_data_structure(args.vcf)

    # vcf_groups = build_grouped_sample_data_structure(vcf_groups)
    # coverage_groups = build_grouped_sample_data_structure(coverage_groups)
    # alignment_groups = build_grouped_sample_data_structure(alignment_groups)

    # min_coverage = int(args.min_coverage)
    # min_editing = int(args.min_editing)
    # max_cov = float(args.max_editing)
    # max_depth = determine_aggregation_depth(min_editing)
    # reference_genome = Fastafile(args.genome)

    # max_cl = 30

    # Decide what the group names should be.
    # Returns a list of group names.
    # Will be a list of comma separated names provided to the names parameter or a list of integers.
    group_names = resolve_names(args.names, sample_epk)

    tmp_list = [group_int for group_int in range(len(sample_epk))]

    # =========================================================================
    # Make SampleGroups Obj
    # =========================================================================

    groups_dict = {}
    min_samples_in_group = len(group_names[0])

    for group_i in range(len(group_names)):

        number_of_samples = len(sample_epk[group_i])

        if number_of_samples < min_samples_in_group:
            min_samples_in_group = number_of_samples

        for sample_i in range(number_of_samples):

            epk_in_sample = sample_epk[group_i][sample_i]
            epk_in_site = vcf_edited[group_i][sample_i]

            editing_obj = EditingInSample(epk_in_sample, region_epk_file=None, vcf_file=epk_in_site)

            tmp_group_name = group_names[group_i]
            try:
                groups_dict[tmp_group_name].append(editing_obj)
            except KeyError:
                groups_dict[tmp_group_name] = [editing_obj]

    group_comparisons = generate_group_pairs(group_names)

    # bed_obj = BED(bed_path)

    name_list = {}
    for tmp_group_name in group_names: # group_comparisons:
        for tmp_sample in groups_dict[tmp_group_name]:
            for tmp_record_name, tmp_record in tmp_sample.yield_editing_sites():
                try:
                    name_list[tmp_record_name] += 1
                except KeyError:
                    name_list[tmp_record_name] = 1

    rpvalcnt = 0
    tpvalcnt = 0
    testable = 0
    for record in name_list:

        for group_1_name, group_2_name in group_comparisons:
            region_epks = []
            sample_epks = []
            region_size = []
            region_avg_depth = []
            group_ids = []
            val_dict = {}

            for tmp_group_name in (group_1_name, group_2_name):

                if tmp_group_name not in val_dict:
                    val_dict[tmp_group_name] = []

                for tmp_sample in groups_dict[tmp_group_name]:

                    tmp_avg_depth = tmp_sample.get_site_depth(record)
                    if tmp_avg_depth > args.min_depth:
                        region_avg_depth.append(tmp_avg_depth)

                        group_ids.append(tmp_group_name)
                        sample_epks.append(tmp_sample.get_sample_epk())
                        region_size.append(1.0)

                        # Region-wise data.
                        tmp_region_epk = tmp_sample.get_site_epk(record)
                        region_epks.append(tmp_region_epk)
                        val_dict[tmp_group_name].append(tmp_region_epk)

            min_s = floor(min_samples_in_group/2)
            if len(val_dict[group_1_name]) > min_s and len(val_dict[group_2_name]) > min_s:

                cov_cutoff = args.max_coverage_cov
                max_depth_cov = args.max_coverage_cov

                if sum(region_epks) > 0:
                    area_cov = stdev(region_size) / mean(region_size)
                    depth_cov = stdev(region_avg_depth) / mean(region_avg_depth)

                    if area_cov < cov_cutoff and depth_cov < max_depth_cov:
                        testable += 1

                        robjects.globalenv['group_ids'] = StrVector(group_ids)
                        robjects.globalenv['sample_epk'] = FloatVector(sample_epks)

                        robjects.globalenv['region_epk'] = FloatVector(region_epks)
                        robjects.globalenv['region_size'] = FloatVector(region_size)
                        robjects.globalenv['region_depth'] = FloatVector(region_avg_depth)

                        robjects.r(r_script)

                        p_value = robjects.globalenv["p_value"][-1]
                        if p_value < 0.05:
                            rpvalcnt += 1

                        t_test_results = ttest_ind(val_dict[group_1_name], val_dict[group_2_name])
                        if t_test_results[1] < 0.05:
                            tpvalcnt += 1

                        g1_mean = mean(val_dict[group_1_name])
                        g2_mean = mean(val_dict[group_2_name])

                        print(
                            "\t".join(
                                [
                                    group_1_name,
                                    group_2_name,
                                    record,
                                    record,
                                    str(round(g1_mean, 2)),
                                    str(round(g2_mean, 2)),
                                    str(round(p_value, 7)),
                                    str(round(t_test_results[1], 7))
                                ]
                            )
                        )


def es_diff_diff(parser):
    """ Check for significant differences in editing within genomic regions among samples.

    :param parser:
    :return:
    """

    from lib.parsers import BED
    from scipy.stats import ttest_ind
    import rpy2.robjects as robjects
    from rpy2.robjects import StrVector, FloatVector
    import rpy2.robjects.packages as rpackages

    from lib.parsers import EditingInSample
    # from import generate_snvs, coverage_depth, find_numbers_of_ref_and_alt_reads
    r_script = """

    df1<-data.frame(
       group=group_ids,
       sampleEPK=sample_epk,
       regionEPK=region_epk,
       regionSize=region_size,
       regionDepth=region_depth
    )

    minVal <- min( df1$regionEPK[df1$regionEPK>0] ) / 2
    df1$regionEPK[df1$regionEPK<=0] <- minVal
    df1$logRegionEPK <-log(df1$regionEPK)
    df1$logSampleEPK <-log(df1$sampleEPK)

    lm1<-lm(logRegionEPK ~ logSampleEPK + regionSize + regionDepth + group, data=df1)
    #lm1<-lm(logRegionEPK ~ logSampleEPK + group, data=df1)

    p_value <- summary(lm1)$coefficients

    """
    parser.add_argument(
        "--sites",
        type=str,
        help="")

    parser.add_argument(
        "--stat-file",
        type=str,
        default=None,
        help="")

    parser.add_argument(
        "--max-coverage-cov",
        type=float,
        default=0.5,
        help="")

    parser.add_argument(
        "--max-depth-cov",
        type=float,
        default=0.5,
        help="")

    parser.add_argument(
        "--min-area",
        type=float,
        default=20,
        help="")

    parser.add_argument(
        "--min-depth",
        type=float,
        default=10,
        help="")

    parser.add_argument(
        "--names",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--sample-epk",
        nargs='+',
        type=str,
        help="")

    parser.add_argument(
        "--site-epk",
        nargs='+',
        type=str,
        help="")

    args = parser.parse_args()

    bed_path = args.sites

    sample_epk = build_grouped_sample_data_structure(args.sample_epk)
    region_epk = build_grouped_sample_data_structure(args.site_epk)

    # max_cl = 30
    # Decide what the group names should be.
    # Returns a list of group names.
    # Will be a list of comma separated names provided to the names parameter or a list of integers.
    group_names = resolve_names(args.names, sample_epk)

    tmp_list = [group_int for group_int in range(len(sample_epk))]

    # =========================================================================
    # Make SampleGroups Obj
    # =========================================================================

    groups_dict = {}
    min_samples_in_group = len(group_names[0])

    for group_i in range(len(group_names)):

        number_of_samples = len(sample_epk[group_i])

        if number_of_samples < min_samples_in_group:
            min_samples_in_group = number_of_samples

        for sample_i in range(number_of_samples):
            epk_in_sample = sample_epk[group_i][sample_i]
            epk_in_region = region_epk[group_i][sample_i]

            editing_obj = EditingInSample(epk_in_sample, epk_in_region)

            tmp_group_name = group_names[group_i]
            try:
                groups_dict[tmp_group_name].append(editing_obj)
            except KeyError:
                groups_dict[tmp_group_name] = [editing_obj]

    # Get a a tuple of all possible sets of two groups.
    group_comparisons = generate_group_pairs(group_names)

    bed_obj = BED(bed_path)


    rpvalcnt = 0
    tpvalcnt = 0
    testable = 0
    min_average_depth = args.min_depth
    min_editing_area = args.min_area
    max_coverage_cov = args.max_coverage_cov
    max_depth_cov = args.max_depth_cov

    for record in generate_snvs(bed_path, min_coverage=None, min_editing=None, max_editing=None):

        record_name = record.chromosome+":"+record.position

        for group_1_name, group_2_name in group_comparisons:

            region_epks, sample_epks, region_size, region_avg_depth, group_ids = [], [], [], [], []
            val_dict = {}

            for tmp_group_name in (group_1_name, group_2_name):

                if tmp_group_name not in val_dict:
                    val_dict[tmp_group_name] = []

                for tmp_sample in groups_dict[tmp_group_name]:

                    tmp_region_depth = tmp_sample.get_region_depth(record_name)

                    if tmp_region_depth > min_average_depth:

                        region_avg_depth.append(tmp_region_depth)
                        group_ids.append(tmp_group_name)
                        sample_epks.append(tmp_sample.get_sample_epk())

                        # Region-wise data.
                        tmp_region_epk = tmp_sample.get_region_epk(record_name)
                        region_epks.append(tmp_sample.get_region_epk(record_name))
                        region_size.append(tmp_sample.get_region_size(record_name))

                        val_dict[tmp_group_name].append(tmp_region_epk)

            # When zero editing is detectable in regions this will cause errors when calculating stddev.
            at_least_one_region_has_editing = sum(region_epks) > 0

            # Make sure we can test at least almost half of the samples.
            min_samples_for_testability = floor(min_samples_in_group/2)
            min_samples_for_testability = 2 if min_samples_for_testability <= 1 else min_samples_for_testability
            group_1_is_testable = len(val_dict[group_1_name]) > min_samples_for_testability
            group_2_is_testable = len(val_dict[group_2_name]) > min_samples_for_testability

            if at_least_one_region_has_editing and group_1_is_testable and group_2_is_testable:

                area_cov = stdev(region_size)/mean(region_size)
                depth_cov = stdev(region_avg_depth)/mean(region_avg_depth)
                region_max_editing_area = sorted(region_size)[-1]

                if area_cov < max_coverage_cov and depth_cov < max_depth_cov:

                    testable += 1


                    robjects.globalenv['group_ids'] = StrVector(group_ids)
                    robjects.globalenv['region_depth'] = FloatVector(region_avg_depth)
                    robjects.globalenv['sample_epk'] = FloatVector(sample_epks)
                    robjects.globalenv['region_epk'] = FloatVector(region_epks)
                    robjects.globalenv['region_size'] = FloatVector(region_size)

                    robjects.r(r_script)

                    p_value = robjects.globalenv["p_value"][-1]

                    if p_value < 0.05:
                        rpvalcnt += 1

                    g1_mean = mean(val_dict[group_1_name])
                    g2_mean = mean(val_dict[group_2_name])

                    ttest_results = ttest_ind(val_dict[group_1_name], val_dict[group_2_name])
                    if ttest_results[1] < 0.05:
                        tpvalcnt += 1

                    print(
                        "\t".join(
                         [
                             group_1_name,
                             group_2_name,
                             record_name,
                             record_name,
                             str(round(g1_mean, 2)),
                             str(round(g2_mean, 2)),
                             str(round(p_value, 7)),
                             str(round(ttest_results[1], 7))
                          ]
                        )
                    )

