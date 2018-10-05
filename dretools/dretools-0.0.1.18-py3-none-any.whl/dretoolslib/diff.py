from collections import namedtuple
from random import randint, random
from statistics import mean, stdev
from dretoolslib.parsers import generate_snvs
from math import floor
from scipy.stats import mannwhitneyu, ks_2samp, kruskal

FILE_DELIMITER = ","
import warnings
warnings.filterwarnings("ignore")

region_help = "Regions to test for differential editing. Must be in BED6 format."

site_help = "Sires to test for differential editing. Must be in VCF format."

max_ca_cov_help_txt = "The maximum allowed variation (coefficient-of-variation) in coverage area for a test to occur."

max_cd_cov_help_txt = "The maximum allowed variation (coefficient-of-variation) " \
                      "in average coverage depth for a test to occur."

min_region_len_help_txt = "The minimum allowed length of a region in nucleotides for testing to occur."

min_depth_help_txt = "The minimum allowed length of a region in nucleotides for testing to occur."

names = "The names of the groups being tested for differential editing. Must be comma delimited."

sample_groups_and_sample_help_txt = "Sample-wise EPK files passed with groups delimited by spaces and samples " \
                                    "delimited by commas."

region_groups_and_sample_help_txt = "Region-wise EPK files passed with groups delimited by spaces and samples " \
                                    "delimited by commas."

edsite_groups_and_sample_help_txt = "Site-wise EPK files passed with groups delimited by spaces and samples " \
                                    "delimited by commas."


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


# @TODO: Add functions for calculating tissue-specificty


def correct_pvalues_for_multiple_testing(pvalues, correction_type = "Benjamini-Hochberg"):                
    """                                                                                                   
    consistent with R - print correct_pvalues_for_multiple_testing([0.0, 0.01, 0.029, 0.03, 0.031, 0.05, 0.069, 0.07, 0.071, 0.09, 0.1]) 
    """
    from numpy import array, empty                                                                        
    pvalues = array(pvalues)
    n = int(pvalues.shape[0])
    new_pvalues = empty(n)

    if correction_type == "Bonferroni":                                                                   
        new_pvalues = n * pvalues
    elif correction_type == "Bonferroni-Holm":                                                            
        values = [ (pvalue, i) for i, pvalue in enumerate(pvalues) ]                                      
        values.sort()
        for rank, vals in enumerate(values):                                                              
            pvalue, i = vals
            new_pvalues[i] = (n-rank) * pvalue                                                            
    elif correction_type == "Benjamini-Hochberg":                                                         
        values = [ (pvalue, i) for i, pvalue in enumerate(pvalues) ]                                      
        values.sort()
        values.reverse()                                                                                  
        new_values = []
        for i, vals in enumerate(values):                                                                 
            rank = n - i
            pvalue, index = vals                                                                          
            new_values.append((n/rank) * pvalue)                                                          
        for i in range(0, int(n)-1):
            if new_values[i] < new_values[i+1]:                                                           
                new_values[i+1] = new_values[i]                                                           
        for i, vals in enumerate(values):
            pvalue, index = vals
            new_pvalues[index] = new_values[i]                                                                                                                  
    return new_pvalues


def region_diff(parser):
    """ Test for differentially edited transcriptomic regions.

    This operation tests a user defined list of transcriptomic regions for differential editing Testing requires two or
    more groups and each group should have three or more samples. Regions should be passed in BED6 format. This
    operation was designed for used with editing islands, but can likely also be used for other small transcriptomic
    features such as 5-prime untranslated regions.

    BED6 format: https://ensembl.org/info/website/upload/bed.html

    Example:
    dretools region-diff        \\
        --regions  islands.bed  \\
        --names    scrRNA,siRNA \\
        --sample-epk            \\
        SRR3091828.sample_EPK.tsv,SRR3091829.sample_EPK.tsv,SRR3091830.sample_EPK.tsv \\
        SRR3091831.sample_EPK.tsv,SRR3091832.sample_EPK.tsv,SRR3091833.sample_EPK.tsv \\
        --region-epk                                                                  \\
        SRR3091828.island_EPK.tsv,SRR3091829.island_EPK.tsv,SRR3091830.island_EPK.tsv \\
        SRR3091831.island_EPK.tsv,SRR3091832.island_EPK.tsv,SRR3091833.island_EPK.tsv \\
        > huvec_diff_islands.tsv

    head -n 5 huvec_diff_islands.tsv
    #Group_1   Group_2  Region_ID  Region_Location  G1_Mean    G2_Mean    LM_pvalue   ttest_pvalue
    scrRNA siRNA  o8VlZXoG8W0HRXSQ1Llp_g  7:55455209-55456608 71.18   6.71   0.669807  0.000341
    scrRNA siRNA  Pbxi6lyFWlZS6EOIeeEwIw  7:55457301-55458649 94.33   9.37   0.86684   0.000717
    scrRNA siRNA  GkDUWP_wCDmvFSC0Q1HHng  7:38723463-38723685 233.79  43.52  0.026463  0.000901
    scrRNA siRNA  Ydr7oqC_zTa_3EwNHYi7qw  7:38724619-38724988 82.43   34.55  0.673315  0.071776
    scrRNA siRNA  OokpaC7sFKK7PAfnUDBSgw  4:2938296-2938760   46.94   13.3   0.888164  0.011983

    """

    from dretoolslib.parsers import BED
    from scipy.stats import ttest_ind
    import rpy2.robjects as robjects
    from rpy2.robjects import StrVector, FloatVector
    from dretoolslib.parsers import EditingInSample

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
        required=True,
        help=region_help)

    parser.add_argument(
        "--max-coverage-cov",
        type=float, default=0.5,
        help=max_ca_cov_help_txt)

    parser.add_argument(
        "--max-depth-cov",
        type=float, default=0.5,
        help=max_cd_cov_help_txt)

    parser.add_argument(
        "--min-area",
        type=float,
        default=20,
        help=min_region_len_help_txt)

    parser.add_argument(
        "--min-depth",
        type=float,
        default=10,
        help=min_depth_help_txt)

    parser.add_argument(
        "--names",
        nargs='+',
        type=str,
        help=names)

    parser.add_argument(
        "--sample-epk",
        nargs='+',
        type=str,
        help=sample_groups_and_sample_help_txt)

    parser.add_argument(
        "--region-epk",
        nargs='+',
        type=str,
        help=region_groups_and_sample_help_txt)

    args = parser.parse_args()

    bed_path = args.regions

    sample_epk = build_grouped_sample_data_structure(args.sample_epk)
    region_epk = build_grouped_sample_data_structure(args.region_epk)


    lm_pvals = []
    ttest_pvals = []
    mv_pvals = []
    kruskal_pvals = []
    data_vals = []

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

    print(
        "\t".join(
            [
                "#Group_1",
                "Group_2",
                "Record_Name",
                "Group_1_Mean",
                "Group_2_Mean",
                "LM_pvalue",
                "ttest_pvalue"
            ]
        )
    )

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
            min_samples_for_testability = 2 if min_samples_for_testability <= 1 else min_samples_for_testability
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
                    lm_pvals.append(p_value)

                    #if p_value < 0.05:
                    #    rpvalcnt += 1
                    ttest_results = ttest_ind(val_dict[group_1_name], val_dict[group_2_name])
                    ttest_pvals.append(ttest_results[1])

                    #if ttest_results[1] < 0.05:
                    #    tpvalcnt += 1
                    kruskal_test = kruskal(val_dict[group_1_name], val_dict[group_2_name])
                    mv_pvals.append(kruskal_test.pvalue)

                    mw_test = mannwhitneyu(val_dict[group_1_name], val_dict[group_2_name], alternative='two-sided')
                    kruskal_pvals.append(mw_test.pvalue)

                    g1_mean = mean(val_dict[group_1_name])
                    g2_mean = mean(val_dict[group_2_name])

                    data_vals.append(
                        "\t".join(
                            [
                                group_1_name, group_2_name, record.name,
                                record.chromosome + ":" + str(record.start) + "-" + str(record.end),
                                str(round(g1_mean, 2)), str(round(g2_mean, 2)),

                            ]
                        )
                    )

    corrected_lm_pvals = correct_pvalues_for_multiple_testing(lm_pvals)
    corrected_ttest_pvals = correct_pvalues_for_multiple_testing(ttest_pvals)
    corrected_mv_pvals = correct_pvalues_for_multiple_testing(mv_pvals)
    corrected_kruskal_pvals = correct_pvalues_for_multiple_testing(kruskal_pvals)

    for i in range(len(data_vals)):

        tmp_pvals = [
            lm_pvals[i], corrected_lm_pvals[i],
            ttest_pvals[i], corrected_ttest_pvals[i],
            mv_pvals[i], corrected_mv_pvals[i],
            kruskal_pvals[i], corrected_kruskal_pvals[i]
        ]
        str_vals = [str(round(tmp_pval, 7)) for tmp_pval in tmp_pvals]

        print(data_vals[i] + "\t" + "\t".join(str_vals))




'''
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
                             str(round(ttest_results[1], 7)),
                             str(round(kruskal_test.pvalue, 7)),
                             str(round(mw_test.pvalue, 7))
                          ]
                        )
                    )
'''

def editing_site_diff(parser):
    """ Test for differentially edited editing sites.

    This operation tests a user defined list of editing sites for differential editing. Testing requires two or
    more groups and each group should have three or more samples. Editing sites should be passed in VCF format.

    Example:
    dretools edsite-diff            \\
        --max-depth-cov 5.0         \\
        --min-depth 2               \\
        --names scrRNA,siRNA        \\
        --sites consensus_sites.vcf \\
        --sample-epk                \\
        SRR3091828.sample_epk.tsv,SRR3091829.sample_epk.tsv,SRR3091830.sample_epk.tsv \\
        SRR3091831.sample_epk.tsv,SRR3091832.sample_epk.tsv,SRR3091833.sample_epk.tsv \\
        --site-epk                                                                    \\
        SRR3091828.edsite_epk.tsv,SRR3091829.edsite_epk.tsv,SRR3091830.edsite_epk.tsv \\
        SRR3091831.edsite_epk.tsv,SRR3091832.edsite_epk.tsv,SRR3091833.edsite_epk.tsv \\
        > diff_sites.tsv

    cat diff_sites.tsv
    #Group_1   Group_2    Site G1_Mean    G2_Mean    LM_pvalue   ttest_pvalue
    scrRNA  siRNA   19:3648162  5888.89 988.89  0.8901652   0.2124562
    scrRNA  siRNA   19:3648201  875.0   711.11  0.9014737   0.7141435
    """
    from scipy.stats import ttest_ind
    import rpy2.robjects as robjects
    from rpy2.robjects import StrVector, FloatVector
    from dretoolslib.parsers import EditingInSample

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
        required=True,
        help=site_help)

    parser.add_argument(
        "--max-coverage-cov",
        type=float,
        default=0.5,
        help=max_ca_cov_help_txt)

    parser.add_argument(
        "--max-depth-cov",
        type=float,
        default=0.5,
        help=max_cd_cov_help_txt)

    parser.add_argument(
        "--min-area",
        type=float,
        default=20,
        help=min_region_len_help_txt)

    parser.add_argument(
        "--min-depth",
        type=float,
        default=10,
        help=min_depth_help_txt)

    parser.add_argument(
        "--names",
        nargs='+',
        type=str,
        help=names)

    parser.add_argument(
        "--sample-epk",
        nargs='+',
        type=str,
        help=sample_groups_and_sample_help_txt)

    parser.add_argument(
        "--site-epk",
        nargs='+',
        type=str,
        help=edsite_groups_and_sample_help_txt)

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

    rpvalcnt = 0
    tpvalcnt = 0
    testable = 0
    min_average_depth = args.min_depth
    max_coverage_cov = args.max_coverage_cov
    max_depth_cov = args.max_depth_cov

    print(
        "\t".join(
            [
                "#Group_1",
                "Group_2",
                "Record_Name",
                "Group_1_Mean",
                "Group_2_Mean",
                "LM_pvalue",
                "ttest_pvalue"
            ]
        )
    )

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
                             str(round(g1_mean, 2)),
                             str(round(g2_mean, 2)),
                             str(round(p_value, 7)),
                             str(round(ttest_results[1], 7))
                          ]
                        )
                    )
            '''
            else:
                print(
                    "\t".join(
                        [
                            group_1_name,
                            group_2_name,
                            record_name,
                            record_name,
                            "NO_TEST",
                            "NO_TEST",
                            "NO_TEST",
                            "NO_TEST"
                        ]
                    )
                )
            '''
