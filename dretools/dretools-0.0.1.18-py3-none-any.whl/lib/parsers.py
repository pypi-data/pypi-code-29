from intervaltree import IntervalTree
from collections import namedtuple
from lib.shared import passes_min_coverage, passes_min_editing, passes_max_percent_editing
from pysam import AlignmentFile

comments_and_title_char = "#"


def find_coverage(info):
    return int(info.split("DP=")[-1].split(";")[0])


def coverage_depth(info):
    return int(info.split("DP=")[-1].split(";")[0])


def normalized_editing(sites, total_area_covered):
    return round((sites * 1.0e6) / total_area_covered, 5)


def find_total_area_covered(n, file_name):
    total_area = 0
    for line in open(file_name):
        sl = line.split()
        if sl[0] == "genome" and int(sl[1]) >= n:
            total_area += int(sl[2])
    return total_area


def get_coverage_total_area_covered(n, file_name):
    area_dict = {}
    for line in open(file_name):
        sl = line.split()
        coverage_level = int(sl[1])
        area_covered = int(sl[2])
        if sl[0] == "genome" and int(sl[1]) >= n:
            area_dict[coverage_level] = area_covered
    return area_dict


def find_numbers_of_ref_and_alt_reads(info):
    """ Find the number reference and alternative bases described in a vcf file line.

    :param info: The info section of a VCF line. I.E. the final few columns with attributes and other data.
    Should look something like this:
        ABHom=1.00;AC=2;...QD=18.37;SOR=2.303       GT:AD:DP:GQ:PL  1/1:0,2:2:6:64,6,0

    :return: (int, int) a tuple containing the counts of reference and alternative bases.
    """

    if "BaseCounts=" in info:
        A, C, G, T = [int(i) for i in info.split("BaseCounts=")[-1].split(";")[0].split(",")]

        if A+G > C+T:
            ref, alt = str(A), str(G)
        else:
            ref, alt = str(C), str(T)
        # This version includes all bases in ref count.
        # ref -= alt
    else:
        try:
            ref, alt = info.split()[-1].split(":")[1].split(",")
        except ValueError:
            print(info)
            print(info.split()[-1].split(":")[1].split(","))
            exit()

    return int(ref), int(alt)


def yield_bed_lines(bed_file):
    from collections import namedtuple

    bed_record = namedtuple('GFFRecord', [
        "chromosome",
        "start",
        "end",
        "name",
        "score",
        "strand"
    ])

    title_flag = True

    with open(bed_file) as bed_file_obj:

        for line in bed_file_obj:

            sl = line.split()

            chromosome = sl[0]
            try:
                start = int(sl[1])
                end = int(sl[2])

                try:
                    name = sl[3]
                except IndexError:
                    name = "."

                try:
                    score = sl[4]
                except IndexError:
                    score = "."

                try:
                    strand = sl[5]
                except IndexError:
                    strand = "."

                yield bed_record(chromosome, start, end, name, score, strand)

            except ValueError:
                if not title_flag:
                    assert False, "ValueError"
                title_flag = False


class GroupsManager:

    def __init__(self):
        pass

    def add_vcf_groups(self, input_string):
        # Check if other groups have been added
        pass

    def add_bam_groups(self, input_string):
        pass

    def find_group_of_file(self, file_name):
        pass


class BED:

    def __init__(self, bed_file):
        self.file_location = bed_file
        self.BEDRecord = namedtuple('BEDRecord', ["chromosome", "start", "end", "name", "score", "strand"])

    def yield_lines(self):
        title_flag = True

        with open(self.file_location) as bed_obj:
            for line in bed_obj:
                sl = line.split()
                try:

                    chromosome = sl[0]
                    start = int(sl[1])
                    end = int(sl[2])
                    name = sl[3]
                    score = sl[4]
                    strand = sl[5]

                    # Convert to 1 based counts as we will be searching with VCF files.
                    end = end + 1 if start - end == 0 else end

                    yield self.BEDRecord(chromosome, start, end, name, score, strand)

                except ValueError:
                    if not title_flag:
                        assert False, "ValueError"
                    title_flag = False


class GFF:

    def __init__(self, gff_file, attribute_format="Ensembl"):

        self.file_location = gff_file
        self.attribute_format = attribute_format
        # @TODO: Add more formats and use UGAs if no reference not supported.
        if attribute_format == "Ensembl":
            self.gene_id_regex = 'gene_id "'
            self.gene_name_regex = 'gene_name "'
            self.tran_id_regex = 'transcript_id "'
            self.exon_id_regex = 'exon_id "'
        else:
            self.gene_id_regex = 'gene_id "'
            self.gene_name_regex = 'gene_name "'
            self.tran_id_regex = 'transcript_id "'
            self.exon_id_regex = 'exon_id "'
        # "frame", "attribute",

        GFFRecord = namedtuple('GFFRecord', [
            "chromosome", "source", "feature", "start", "end", "strand",
            "gene_id", "gene_name", "tran_id", "exon_id"
        ])
        self.GFFRecord = GFFRecord

    def yield_lines(self):
        with open(self.file_location) as gff_obj:
            for line in gff_obj:
                if line[0] != "#":
                    sl = line.split()
                    chromosome = sl[0]
                    source = sl[1]
                    feature = sl[2]
                    start = int(sl[3])
                    end = int(sl[4])
                    strand = sl[6]
                    # frame = sl[5 or 7?]
                    attribute = " ".join(sl[6:])

                    gene_id = self.get_gene_id(attribute)
                    gene_name = self.get_gene_name(attribute)

                    tran_id = self.get_transcript_id(attribute)
                    exon_id = self.get_exon_id(attribute, chromosome, strand, start, end)

                    # Convert to 1 based counts as we will be searching with VCF files.
                    end = end + 1 if start - end == 0 else end

                    yield self.GFFRecord(chromosome, source, feature, start, end, strand, gene_id, gene_name, tran_id, exon_id)

    def get_gene_id(self, attributes):
        return attributes.split(self.gene_id_regex)[-1].split('";')[0] if self.gene_id_regex in attributes else None

    def get_gene_name(self, attributes):
        return attributes.split(self.gene_name_regex)[-1].split('";')[0] if self.gene_name_regex in attributes else None

    def get_transcript_id(self, attributes):
        return attributes.split(self.tran_id_regex)[-1].split('";')[0] if self.tran_id_regex in attributes else None

    def get_exon_id(self, attributes, chromosome, strand, start, end):

        if self.exon_id_regex in attributes:
            return attributes.split(self.exon_id_regex)[-1].split('";')[0]
        else:
            return "%s%s:%s-%s" % (strand, chromosome, start, end)

# gene_coverage_cnt_dict[record.chromosome][record.start:record.end] = None
# for s in self.gene_tree_dict:


class GenomicIntervalTree:
    """

    """

    def __init__(self, gtf_file):

        from intervaltree import IntervalTree
        # Here we build two tree dictionaries. The purpose of these is so that we can differentiate between
        # between reads falling in exons and those falling in intergenic space. The problem is that intergenic
        # space is not annotated so falling within the bounds of a gene and not an exonic feature
        # Finally we use dictionaries to differentiate between chromosome and strand.
        self.gene_tree_dict = {"+": dict(), "-": dict()}
        self.exon_tree_dict = {"+": dict(), "-": dict()}
        self.total_area_covered_by_genes = 0
        self.total_intergenic_area = 0
        self.total_intronic_are = 0
        self.total_area_covered_by_exons = 0
        self.total_area_covered_by_3utr = 0
        self.total_area_covered_by_5utr = 0
        gene_coverage_cnt_dict = {}
        exonic_feature_bounds_dict = {}

        intergenic = "intergenic"
        exon = "exon"
        intron = "intron"
        three_prime_utr = "three_prime_utr"
        five_prime_utr = "five_prime_utr"

        self.genomic_features = [intergenic, exon, intron, three_prime_utr, five_prime_utr]
        self.exonic_feature_set = {exon, five_prime_utr, three_prime_utr}
        self.feature_set_lens = {k: 0 for k in self.genomic_features}

        unique_exon_lens = []
        unique_five_prime_lens = []
        unique_three_prime_lens = []

        # exonic_feature_set_lens = {f: 0 for f in exonic_feature_bounds_dict}
        # exonic_feature_set_bound_sets = {"exon": set(), "five_prime_utr": set(), "three_prime_utr": set()}
        # exonic_feature_dict = {}
        # exon_set = set()
        # five_prime_utr_set = set()
        # three_prime_utr_set = set()
        gff_obj = GFF(gtf_file)
        # Record is a line in a GFF or GTF file.
        for record in gff_obj.yield_lines():
            if record.chromosome not in self.gene_tree_dict[record.strand]:
                self.gene_tree_dict[record.strand][record.chromosome] = IntervalTree()
                self.exon_tree_dict[record.strand][record.chromosome] = IntervalTree()
                gene_coverage_cnt_dict[record.chromosome] = IntervalTree()

            if record.feature == "gene":
                # self.total_area_covered_by_genes += record.start - record.end
                self.gene_tree_dict[record.strand][record.chromosome][record.start:record.end] = record.gene_id
                gene_coverage_cnt_dict[record.chromosome][record.start:record.end] = None

            elif record.feature in self.exonic_feature_set:
                # Get all unique exonic annotations, exons will occur multiple times unlike genes and transcripts.
                location_tuple = (record.strand, record.chromosome, record.start, record.end)
                annotation = (record.feature, record.gene_id, record.tran_id, record.exon_id)
                try:
                    exonic_feature_bounds_dict[location_tuple].add(annotation)
                except KeyError:
                    # {(annotation,)} Will not work
                    # annotation = (record.feature, record.gene_id, record.tran_id, record.exon_id, "!!!")

                    exonic_feature_bounds_dict[location_tuple] = set()
                    exonic_feature_bounds_dict[location_tuple].add(annotation)

        # Add unique exonic features to dictionary of strand chromosome and interval trees.
        for location_key, annotation_values in exonic_feature_bounds_dict.items():

            location_length = location_key[3] - location_key[2]
            tmp_location_types = set()
            for tmp_annotation in annotation_values:
                # tmp_feature = tmp_annotation[0]
                tmp_location_types.add(tmp_annotation[0])  # tmp_feature

                # exonic_feature_set_lens[tmp_feature] += 1

            if exon in tmp_location_types:
                unique_exon_lens.append(location_length)
            if three_prime_utr in tmp_location_types:
                unique_three_prime_lens.append(location_length)
            if five_prime_utr in tmp_location_types:
                unique_five_prime_lens.append(location_length)

            strand, chromosome, start, end = location_key
            self.exon_tree_dict[strand][chromosome][start:end] = annotation_values

        for c in gene_coverage_cnt_dict:
            gene_coverage_cnt_dict[c].merge_overlaps()
            for o in gene_coverage_cnt_dict[c]:
                self.total_area_covered_by_genes += o[1] - o[0]

        # chr 1 248956422
        self.total_intergenic_area = 3099411205 - self.total_area_covered_by_genes
        self.total_area_covered_by_exons = sum(unique_exon_lens)
        self.total_area_covered_by_3utr = sum(unique_three_prime_lens)
        self.total_area_covered_by_5utr = sum(unique_five_prime_lens)
        intron_area = self.total_area_covered_by_genes - self.total_area_covered_by_exons

        self.feature_set_lens[intergenic] = 248956422 - self.total_area_covered_by_genes
        self.feature_set_lens[exon] = self.total_area_covered_by_exons
        self.feature_set_lens[intron] = intron_area
        self.feature_set_lens[three_prime_utr] = self.total_area_covered_by_3utr
        self.feature_set_lens[five_prime_utr] = self.total_area_covered_by_5utr

    def get_genes_overlapping_position(self, chromosome, position, strand):
        """
        :param chromosome:
        :param position:
        :param strand:
        :return:
        """
        if chromosome in self.gene_tree_dict[strand]:
            return sorted(self.gene_tree_dict[strand][chromosome][position])
        else:
            return []

    def get_features_overlapping_position(self, chromosome, position, strand):
        """
        exon, intron, three_prime, five_prime, intergenic
        :param chromosome:
        :param position:
        :param strand:
        :return:
        """

        # First does this feature overlap a gene
        gene_set_list = self.get_genes_overlapping_position(chromosome, position, strand)

        overlapping_regions = []
        if gene_set_list:
            spliced_features = self.get_spliced_features_overlapping_position(chromosome, position, strand)
            if spliced_features:
                for region in spliced_features:
                    overlapping_regions += list(set(r[0] for r in region[-1]))
            else:
                overlapping_regions.append("intron")
        else:
            return ["intergenic"]

        return overlapping_regions

    def get_spliced_features_overlapping_position(self, chromosome, position, strand):

        if chromosome in self.exon_tree_dict[strand]:
            return sorted(self.exon_tree_dict[strand][chromosome][position])
        else:
            return []

    def get_spliced_features_overlapping_range(self, chromosome, start, end, strand):

        if chromosome in self.exon_tree_dict[strand]:
            return sorted(self.exon_tree_dict[strand][chromosome][start:end])
        else:
            return []

    def get_count_of_overlapping_features(self, chromosome, position, strand):
        pass


class BedIntervalTree:

    def __init__(self):
        self.interval_tree = dict()
        self.columns_titles = False

    def add_island(self, chromosome, start, end):

        start = int(start)
        end = int(end)

        try:
            self.interval_tree[chromosome][start:end] = True
        except KeyError:
            self.interval_tree[chromosome] = IntervalTree()
            self.interval_tree[chromosome][start:end] = True

    def add_islands_from_file(self, bed_file):
        with open(bed_file) as bed_obj:
            for line in bed_obj:
                if line[0] != "#":
                    sl = line.split()
                    chromosome, start, end = sl[0], sl[1], sl[2]
                    self.add_island(chromosome, start, end)

    def location_is_in_interval(self, chromosome, position):
        if chromosome in self.interval_tree:
            if self.interval_tree[chromosome].overlaps(position):
                return True
        return False

    def location_is_in_interval_with_names(self, chromosome, position):
        position = int(position)
        if chromosome in self.interval_tree:
            if self.interval_tree[chromosome].overlaps(position):
                region_id_list = [i[-1] for i in self.interval_tree[chromosome][position]]
                return region_id_list
        return []

    def add_islands_with_names(self, chromosome, start, end, region_id):

        try:
            start = int(start)
            end = int(end)

            try:
                self.interval_tree[chromosome][start:end] = region_id
            except KeyError:
                self.interval_tree[chromosome] = IntervalTree()
                self.interval_tree[chromosome][start:end] = region_id
        except ValueError:
            if self.columns_titles:
                exit("ValueError")
            self.columns_titles = True

    def add_islands_from_file_with_names(self, bed_file):
        with open(bed_file) as bed_obj:
            for line in bed_obj:
                sl = line.split()
                chromosome, start, end, name = sl[0], sl[1], sl[2], sl[3]
                self.add_islands_with_names(chromosome, start, end, name)


vcf_tuple = namedtuple('vcf', [
    "chromosome", "position", "id", "reference", "alteration", "quality", "filter", "ref_cnt", "alt_cnt", "info"])


def generate_snvs(vcf_file, min_coverage=None, min_editing=None, max_editing=None):
    """

    :param vcf_file:
    :param min_coverage:
    :param min_editing:
    :param max_editing:
    :return:
    """
    with open(vcf_file) as vf_obj:

        for line in vf_obj:
            if line[0] != "#":

                sl = line.split()
                chromosome = sl[0]  # @TODO: Run chromosome checks
                position = sl[1]
                id = sl[2]  # For annotated SNPs
                reference = sl[3]
                alteration = sl[4]  # phred-scaled quality score for the assertion made in ALT

                try:
                    quality = sl[5]
                except IndexError:
                    quality = "."

                try:
                    filter = sl[6]
                except IndexError:
                    filter = "."

                try:
                    info = "\t".join(sl[6:])
                except IndexError:
                    info = "."
                try:
                    ref_cnt, alt_cnt = find_numbers_of_ref_and_alt_reads(info)
                except IndexError:
                    ref_cnt, alt_cnt = -1, -1

                over_min_editing = True
                over_min_coverage = True
                under_max_percent_editing = True

                if min_coverage is not None:
                    over_min_editing = passes_min_editing(alt_cnt, min_editing)
                if min_editing is not None:
                    over_min_coverage = passes_min_coverage(ref_cnt + alt_cnt, min_coverage)
                if max_editing is not None:
                    under_max_percent_editing = passes_max_percent_editing(ref_cnt, alt_cnt, max_editing)

                if over_min_editing and over_min_coverage and under_max_percent_editing:
                    yield vcf_tuple(chromosome, position, id, reference, alteration, quality, filter, ref_cnt, alt_cnt, info)


class VCFIntervalTree:

    def __init__(self, vcf_file=None, min_coverage=None, min_editing=None, max_percent_coverage=None):
        """
        min_coverage=5, min_editing=3, max_percent_coverage=0.99
        """
        self.SNV_dict = {"+": dict(), "-": dict()}
        self.add_vcf_file(vcf_file, min_coverage, min_editing, max_percent_coverage)

    def add_vcf_file(self, file_name, min_coverage=None, min_editing=None, max_percent_coverage=None):
        """

        :return:
        """
        for snv in generate_snvs(file_name, min_coverage=min_coverage, min_editing=min_editing,
                                 max_editing=max_percent_coverage):
            strand = "+" if snv.reference == "A" else "-"
            data = (file_name, snv.reference, snv.alteration, snv.ref_cnt, snv.alt_cnt)
            self.add_snv(strand, snv.chromosome, snv.position, data)

    def add_snv(self, strand, chromosome, position, data):
        """

        :param chromosome:
        :param strand:
        :param position:
        :param reference:
        :param alteration:
        :return:
        """
        # reference, alteration
        # print([type(i)])
        position = int(position)
        #print(type(strand), type(chromosome), type(), type(data))
        try:
            self.SNV_dict[strand][chromosome][position:position+1] = data
        except KeyError:
            self.SNV_dict[strand][chromosome] = IntervalTree()
            self.SNV_dict[strand][chromosome][position:position+1] = data

    def get_snvs_in_range(self, chromosome, strand, start, stop):
        """

        :param chromosome:
        :param strand:
        :param start:
        :param stop:
        :return:
        """
        try:
            snvs_dict = self.SNV_dict[strand][chromosome][start:stop]
        except KeyError:
            snvs_dict = {}

        return snvs_dict


class VCF:

    def __init__(self, file_name, min_editing, min_coverage, max_percent_coverage=0):

        self.file_name = file_name
        self.min_editing = min_editing
        self.min_coverage = min_coverage
        self.max_percent_coverage = max_percent_coverage
        self.editing_sites = []
        self.site_location_dict = None
        self.position_and_chars_set = set()

        self.editing_sites_coverage_dict = None
        self.coverage_count_dict = 0
        self.VCFRecord = namedtuple('VCFRecord', [
            "chromosome", "position", "id", "ref", "alt", "depth", "ref_base_cnt", "alt_base_cnt"
        ])

    def parse_editing_sites(self):
        """ Parse all editing sites in a file.
        """
        self.editing_sites_coverage_dict = {}
        self.coverage_count_dict = {}
        self.site_location_dict = {}

        # def generate_snvs(vcf_file, min_coverage=None, min_editing=None, max_editing=None):

        for snv in generate_snvs(self.file_name, min_coverage=self.min_coverage, min_editing=self.min_editing,
                                 max_editing=self.max_percent_coverage):
            # chromosome, position, id, ref, alt, qual, fil, info
            # ref_cnt, alt_cnt = find_numbers_of_ref_and_alt_reads(snv.info)
            depth = snv.ref_cnt + snv.alt_cnt

            over_min_editing = passes_min_editing(snv.alt_cnt, self.min_editing)
            over_min_coverage = passes_min_coverage(depth, self.min_coverage)
            under_max_percent_editing = passes_max_percent_editing(snv.ref_cnt, snv.alt_cnt, self.max_percent_coverage)

            if over_min_editing and over_min_coverage and under_max_percent_editing:
                vcf_record = self.VCFRecord(
                    snv.chromosome, snv.position, id, snv.reference, snv.alteration, depth, snv.ref_cnt, snv.alt_cnt)

                # Add to main list
                self.editing_sites.append(vcf_record)

                self.site_location_dict[(str(snv.chromosome), int(snv.position))] = vcf_record

                self.position_and_chars_set.add((snv.chromosome, snv.position, snv.reference, snv.alteration))

                # Make a dictionary of editing sites covered by N depth.
                # Using the same object that is being placed in the list to keep memory low.
                try:
                    self.editing_sites_coverage_dict[depth].append(vcf_record)
                    self.coverage_count_dict[depth] += 1
                except KeyError:
                    self.coverage_count_dict[depth] = 1
                    self.editing_sites_coverage_dict[depth] = [vcf_record]

    def get_editing_sites_covered_by_n_reads(self, n):
        return self.coverage_count_dict[n]

    def in_editing_site_tuple_set(self, chromosome, position):
        """
        :return:
        """

        if self.site_location_dict is None:
            self.parse_editing_sites()

        position = int(position)

        if (chromosome, position) in self.site_location_dict:
            return self.site_location_dict[(chromosome, position)]
        else:
            return []

    def get_editing_site_tuple_set(self):
        if self.site_location_dict is None:
            self.parse_editing_sites()
        return self.position_and_chars_set

    def editing_site_coverage_levels(self):
        """ Return the set of all coverage levels.

        :return:
        """
        # If the VCF file has not been parsed, do that now.
        if self.editing_sites_coverage_dict is None:
            self.parse_editing_sites()

        return set(self.editing_sites_coverage_dict)

    def get_editing_sites_coverage_dict(self):
        return self.coverage_count_dict


class Coverage:

    def __init__(self, file_name, min_coverage, max_coverage):

        self.file_name = file_name
        self.min_coverage = min_coverage
        self.max_coverage = max_coverage
        self.coverage_area_dict = dict()

        with open(file_name) as coverage_file:
            for line in coverage_file:
                sl = line.split()
                coverage_level = int(sl[1])
                area_coverage = int(sl[2])

                if sl[0] == "genome" and coverage_level >= min_coverage:

                    # The the coverage level is above the max level bin into max_coverage.
                    coverage_level = max_coverage if coverage_level > max_coverage else coverage_level

                    try:
                        self.coverage_area_dict[coverage_level] += area_coverage
                    except KeyError:
                        self.coverage_area_dict[coverage_level] = area_coverage

    def yield_sorted_coverage_level_and_areas(self):
        for level in sorted(self.coverage_area_dict):
            yield level, self.coverage_area_dict[level]

    def get_coverage_dict(self):
        return self.coverage_area_dict

    def get_area_covered_by_n_reads(self, coverage_level):
        return self.coverage_area_dict[coverage_level]


class EditingSample:

    def __init__(self, vcf_file=None, coverage_file=None, alignment_file=None, min_editing=None, min_coverage=None,
                 max_percent_coverage=0, max_coverage=None, name=None):

        #if name is None:
        #    self.name = vcf_file
        self.name = name

        self.vcf_obj = None
        if vcf_file:
            self.add_editing_sites(vcf_file, min_editing, min_coverage, max_percent_coverage)

        self.coverage_obj = None
        if coverage_file:
            self.add_coverage(vcf_file, min_coverage)

        self.alignment_obj = None
        if alignment_file:
            self.add_alignment_file(alignment_file)

        self.min_editing = min_editing
        self.min_coverage = min_coverage
        self.max_coverage = max_coverage
        self.max_percent_coverage = max_percent_coverage

    def get_name(self):
        if self.name is None:
            return self.vcf_obj.file_name
        else:
            return self.name

    def add_alignment_file(self, file_name):
        """

        :param file_name:
        :return:
        """
        self.alignment_obj = AlignmentFile(file_name, "rb")

    def get_ref_and_alt_bases_at_site(self, chromosome, position, ref_char, alt_char):

        assert self.alignment_obj is not None
        ref_cnt, alt_cnt, other_cnt = 0, 0, 0
        position = int(position)
        for read in self.alignment_obj.fetch(chromosome, position, position + 1):
            for i in range(len(read.query_sequence)):
                if read.pos + i == position:

                    read_base = read.query_sequence[i]

                    if read_base == ref_char:
                        ref_cnt += 1
                    elif read_base == alt_char:
                        alt_cnt += 1
                    else:
                        other_cnt += 1

        return ref_cnt, alt_cnt, other_cnt

    def get_number_of_edited_and_nonedited_bases_at(self, chromosome, position, ref_char, alt_char):
        """ Return
        self.vcf_obj.get_editing_sites_coverage_dict

        :param chromosome:
        :param position:
        :return: edited bases, non-edited bases
        """
        position = int(position)
        vcf_record = self.vcf_obj.in_editing_site_tuple_set(chromosome, position)

        if vcf_record:
            return vcf_record.alt_base_cnt, vcf_record.ref_base_cnt
        else:
            # Get data from bam files.
            ref_cnt, alt_cnt, other_cnt = self.get_ref_and_alt_bases_at_site(chromosome, position, ref_char, alt_char)
            return ref_cnt, alt_cnt

    def get_file_name(self):
        return self.vcf_obj.file_name

    def get_area_covered_by_n_reads(self, n):
        return self.coverage_obj.get_area_covered_by_n_reads(n)

    def get_editing_sites_covered_by_n_reads(self, n):
        return self.vcf_obj.get_editing_sites_covered_by_n_reads(n)

    def add_editing_sites(self, vcf_file_name, min_editing, min_coverage, max_percent_coverage):
        self.vcf_obj = VCF(vcf_file_name, min_editing, min_coverage, max_percent_coverage)

    def get_editing_sites(self):
        return self.vcf_obj.get_editing_site_tuple_set()

    def add_coverage(self, coverage_file_name, min_coverage=None, max_coverage=None):

        if min_coverage is None:
            min_coverage = self.min_coverage

        if max_coverage is None:
            max_coverage = self.max_coverage

        self.coverage_obj = Coverage(coverage_file_name, min_coverage, max_coverage)

    def get_vcf_coverage_level_set(self):
        """ Get the unique set of level of coverage for editing site in the sample.

        :return:
        """
        return self.vcf_obj.editing_site_coverage_levels()

    def get_binned_coverage_cnt(self, coverage_bins):
        """

        :param coverage_bins:
        :return:
        """
        coverage_bins = list(sorted(coverage_bins))
        current_bin = coverage_bins.pop(0)
        coverage_dict = self.coverage_obj.get_coverage_dict()

        out_bins = {}
        for coverage_level in sorted(coverage_dict):
            # If the coverage level is greater than or equal to the next bin.
            # Move to the next largest bin.
            if len(coverage_bins) > 0 and coverage_level >= coverage_bins[0]:
                current_bin = coverage_bins.pop(0)

            try:
                out_bins[current_bin] += coverage_dict[coverage_level]
            except KeyError:
                out_bins[current_bin] = coverage_dict[coverage_level]

        return out_bins

    def get_binned_editing_cnt(self, coverage_bins):

        coverage_bins = list(sorted(coverage_bins))

        editing_dict = self.vcf_obj.get_editing_sites_coverage_dict()

        out_bins = {}
        current_bin = coverage_bins.pop(0)

        for coverage_level in sorted(editing_dict):
            # If the coverage level is greater than or equal to the next bin.
            # Move to the next largest bin.

            if len(coverage_bins) > 0 and coverage_level >= coverage_bins[0]:
                current_bin = coverage_bins.pop(0)

            try:
                out_bins[current_bin] += editing_dict[current_bin]
            except KeyError:
                out_bins[current_bin] = editing_dict[current_bin]

        return out_bins


class Group:

    def __init__(self, ):
        """

        :param min_editing:
        :param min_coverage:
        """
        self.group_names_dict = dict()
        # self.min_editing = min_editing
        # self.min_coverage = min_coverage
        # self.max_percent_coverage = max_percent_coverage
        # self.max_coverage = max_coverage
        self.comparison_tuples_list = []
        self.mean_coverage_vals = None
        self.stdev_coverage_vals = None
        self.coverage_bins = None


EPKMeasurement = namedtuple(
    'EPKMeasurement', [

        "editable_area",
        "avg_depth",

        "edited_bases",
        "reference_bases",

        "epk",

    ]
)


def yield_editing_rates(file_name):

    for line in open(file_name):
        if line[0] != "#":
            spln = line.split()

            # 0 Sample_Name
            # 1 Editable_Area
            # 2 Average_Depth
            # 3 Total_Ref_Bases
            # 4 Total_Alt_Bases
            # 5 EPK

            name = spln[0]
            area = spln[1]
            avg_depth = spln[2]
            #std_depth = spln[3]
            #edited_bases = spln[4]
            #ref_bases = spln[5]
            #epk = spln[6]
            ref_bases = spln[3]
            edited_bases = spln[4]
            epk = spln[5]

            yield name, EPKMeasurement(area, avg_depth, edited_bases, ref_bases, epk)


class EditingInSample:

    def __init__(self, sample_epk_file=None, region_epk_file=None, vcf_file=None):

        self.sample_name = None
        self.sample_editing_measurement = None
        if sample_epk_file is not None:
            self.parse_sample_wise_editing_rates(sample_epk_file)

        self.regions_epk_measurement_dict = {}
        if region_epk_file is not None:
            self.parse_region_wise_editing_rates(region_epk_file)

        self.site_epk_measurement_dict = {}
        if vcf_file is not None:
            self.parse_vcf_editing_rates(vcf_file)

    def parse_sample_wise_editing_rates(self, sample_epk_file):
        for name, measurement in yield_editing_rates(sample_epk_file):
            self.sample_name, self.sample_editing_measurement = name, measurement

    def parse_region_wise_editing_rates(self, region_epk_file):
        for region_name, region_measurement in yield_editing_rates(region_epk_file):
            assert region_name not in self.regions_epk_measurement_dict
            self.regions_epk_measurement_dict[region_name] = region_measurement

    def get_sample_epk(self):
        return float(self.sample_editing_measurement.epk)

    # ====================================================
    #                     Editing Sites
    # ====================================================

    def parse_vcf_editing_rates(self, vcf_file):
        for record in generate_snvs(vcf_file):
            tmp_name = "%s:%s-%s" % (record.chromosome, record.position, int(record.position) + 1)
            edited_bases = int(record.alt_cnt)
            ref_bases = int(record.ref_cnt)
            # @TODO: Get the DP= value with regex.
            depth = edited_bases + ref_bases
            epk = (edited_bases*1000)/float(edited_bases + ref_bases)
            self.site_epk_measurement_dict[tmp_name] = EPKMeasurement(1, depth, edited_bases, ref_bases, epk)

    def yield_editing_sites(self):
        for tmp_name in self.site_epk_measurement_dict:
            yield tmp_name, self.site_epk_measurement_dict[tmp_name]

    def get_site_epk(self, region_id):
        tmp_val = 0
        if region_id in self.site_epk_measurement_dict:
            tmp_val = self.site_epk_measurement_dict[region_id].epk
        return float(tmp_val)

    def get_site_depth(self, region_id):
        tmp_val = 0
        if region_id in self.site_epk_measurement_dict:
            tmp_val = self.site_epk_measurement_dict[region_id].avg_depth
        return float(tmp_val)

    # ====================================================
    #                     Regions
    # ====================================================
    def get_region_epk(self, region_id):
        tmp_val = 0
        if region_id in self.regions_epk_measurement_dict:
            tmp_val = self.regions_epk_measurement_dict[region_id].epk
        return float(tmp_val)

    def get_region_depth(self, region_id):
        tmp_val = 0
        if region_id in self.regions_epk_measurement_dict:
            tmp_val = self.regions_epk_measurement_dict[region_id].avg_depth
        return float(tmp_val)

    def get_region_size(self, region_id):
        tmp_val = 0
        if region_id in self.regions_epk_measurement_dict:
            tmp_val = self.regions_epk_measurement_dict[region_id].editable_area
        return float(tmp_val)


'''

nretools grdiff --regions ../huvec_islands_mc4_me2_eps150_pl2_ms4_ml30.bed --names scrRNA,siRNA --sample-epk SRR3091828.sample_EPK.tsv,SRR3091829.sample_EPK.tsv,SRR3091830.sample_EPK.tsv SRR3091831.sample_EPK.tsv,SRR3091832.sample_EPK.tsv,SRR3091833.sample_EPK.tsv --region-epk SRR3091828.island_EPK.tsv,SRR3091829.island_EPK.tsv,SRR3091830.island_EPK.tsv SRR3091831.island_EPK.tsv,SRR3091832.island_EPK.tsv,SRR3091833.island_EPK.tsv

nretools grdiff \
--regions /media/tyler/DATA/Storage/Projects/nretools.bitbucket.io/analysis/All_samples__MinCov5_MinEd2_MinSa5_Eps150.islands.bed \
--names GM12787,K562 \
--vsample-epk  SRR3192396.island_EPK.tsv,SRR3192397.island_EPK.tsv,SRR3192398.island_EPK.tsv,SRR3192399.island_EPK.tsv,SRR3192400.island_EPK.tsv,SRR3192401.island_EPK.tsv,SRR3192402.island_EPK.tsv,SRR3192403.island_EPK.tsv,SRR3192406.island_EPK.tsv,SRR3192407.island_EPK.tsv,SRR3192657.island_EPK.tsv,SRR3192658.island_EPK.tsv,SRR5048071.island_EPK.tsv,SRR5048072.island_EPK.tsv     SRR3192408.sample_EPK.tsv,SRR3192409.sample_EPK.tsv,SRR3192410.sample_EPK.tsv,SRR3192411.sample_EPK.tsv,SRR3192412.sample_EPK.tsv,SRR3192413.sample_EPK.tsv,SRR3192414.sample_EPK.tsv,SRR3192415.sample_EPK.tsv,SRR3192416.sample_EPK.tsv,SRR3192417.sample_EPK.tsv,SRR3192422.sample_EPK.tsv,SRR3192423.sample_EPK.tsv,SRR3192544.sample_EPK.tsv,SRR3192545.sample_EPK.tsv \
--region-epk  SRR3192396.sample_EPK.tsv,SRR3192397.sample_EPK.tsv,SRR3192398.sample_EPK.tsv,SRR3192399.sample_EPK.tsv,SRR3192400.sample_EPK.tsv,SRR3192401.sample_EPK.tsv,SRR3192402.sample_EPK.tsv,SRR3192403.sample_EPK.tsv,SRR3192406.sample_EPK.tsv,SRR3192407.sample_EPK.tsv,SRR3192657.sample_EPK.tsv,SRR3192658.sample_EPK.tsv,SRR5048071.sample_EPK.tsv,SRR5048072.sample_EPK.tsv     SRR3192408.island_EPK.tsv,SRR3192409.island_EPK.tsv,SRR3192410.island_EPK.tsv,SRR3192411.island_EPK.tsv,SRR3192412.island_EPK.tsv,SRR3192413.island_EPK.tsv,SRR3192414.island_EPK.tsv,SRR3192415.island_EPK.tsv,SRR3192416.island_EPK.tsv,SRR3192417.island_EPK.tsv,SRR3192422.island_EPK.tsv,SRR3192423.island_EPK.tsv,SRR3192544.island_EPK.tsv,SRR3192545.island_EPK.tsv
'''


class SampleGroup:

    def __init__(self, min_editing=0, min_coverage=0, max_percent_coverage=0, max_coverage=5000):
        """

        :param min_editing:
        :param min_coverage:
        """
        self.group_names_dict = dict()
        self.min_editing = min_editing
        self.min_coverage = min_coverage
        self.max_percent_coverage = max_percent_coverage
        self.max_coverage = max_coverage
        self.comparison_tuples_list = []
        self.mean_coverage_vals = None
        self.stdev_coverage_vals = None
        self.coverage_bins = None

    def get_all_vcf_sites(self):
        out_set = set()
        for group_name in self.group_names_dict:
            for sample_obj in self.group_names_dict[group_name]:
                next_set = sample_obj.get_editing_sites()
                out_set = out_set.union(next_set)

        return out_set

    def add_group(self, group_name, vcf_file_list, coverage_file_list=None, alignment_file_list=None):

        tmp_editing_sample_list = []
        for i in range(len(vcf_file_list)):

            tmp_sample = EditingSample(
                vcf_file_list[i],
                min_editing=self.min_editing,
                min_coverage=self.min_coverage,
                max_coverage=self.max_coverage,
                max_percent_coverage=self.max_percent_coverage
            )

            if coverage_file_list:
                tmp_sample.add_coverage(coverage_file_list[i])

            if alignment_file_list:
                tmp_sample.add_alignment_file(alignment_file_list[i])

            # Make a list of all samples.
            tmp_editing_sample_list.append(tmp_sample)

        # Add list of samples to the groups dictionary.
        self.group_names_dict[group_name] = tmp_editing_sample_list

    def yield_group_names_and_sample_list(self):
        for group_name in self.group_names_dict:
            yield group_name, self.group_names_dict[group_name]

    def get_samples_in_group(self, group_name):
        return self.group_names_dict[group_name]

    def find_coverage_bins(self):
        """ While test_data we encountered a problem of dropout conditions

        :return:
        """
        coverage_depth_set = None
        for group_name, sample_list in self.yield_group_names_and_sample_list():

            for sample in sample_list:

                if coverage_depth_set is None:
                    coverage_depth_set = sample.get_vcf_coverage_level_set()
                else:
                    # Get the intersection i.e. common values between the two sets.
                    # This is mean to combat dropouts in samples with lower editing rates.
                    coverage_depth_set = coverage_depth_set & sample.get_vcf_coverage_level_set()

        return coverage_depth_set

    def get_group_data(self):
        pass

    def find_average_depth_values(self):

        coverage_bins = self.find_coverage_bins()
        from statistics import mean
        normalized_sample_list = []
        for group_name in self.group_names_dict:
            for sample in self.group_names_dict[group_name]:
                # rint(sample.get_binned_coverage_cnt(coverage_bins))
                normalized_sample_list.append(sample.get_binned_coverage_cnt(coverage_bins))

        mean_coverage_values = {}

        for bin_level in coverage_bins:
            tmp_coverage_levels = []
            for sample in normalized_sample_list:
                tmp_coverage_levels.append(float(sample[bin_level]))

            mean_coverage_values[bin_level] = mean(tmp_coverage_levels)

        return mean_coverage_values

    def find_stdev_depth_values(self):

        coverage_bins = self.find_coverage_bins()
        from statistics import stdev
        normalized_sample_list = []
        for group_name in self.group_names_dict:
            for sample in self.group_names_dict[group_name]:
                # print(sample.get_binned_coverage_cnt(coverage_bins))
                normalized_sample_list.append(sample.get_binned_coverage_cnt(coverage_bins))

        stdev_coverage_values = {}
        for bin_level in coverage_bins:
            tmp_coverage_levels = []
            for sample in normalized_sample_list:
                tmp_coverage_levels.append(float(sample[bin_level]))

            stdev_coverage_values[bin_level] = stdev(tmp_coverage_levels)

        return stdev_coverage_values

    def generate_group_pairs(self):
        # Make Comparison Groups
        tmp_list = list(sorted(self.group_names_dict))
        while tmp_list:
            name_1 = tmp_list.pop(0)
            for name_2 in tmp_list:
                self.comparison_tuples_list.append((name_1, name_2))

    def get_group_comparison_tuples(self):

        if not self.comparison_tuples_list:
            self.generate_group_pairs()

        return self.comparison_tuples_list

    def get_group(self, group_name):
        return self.group_names_dict[group_name]

    def get_coverage_bins(self):

        if self.coverage_bins is None:
            self.coverage_bins = self.find_coverage_bins()
        return self.coverage_bins

    def get_cov_level_EPCMs(self, group_name):

        if self.coverage_bins is None:
            self.coverage_bins = self.find_coverage_bins()

        if self.mean_coverage_vals is None:
            self.mean_coverage_vals = self.find_average_depth_values()

        if self.stdev_coverage_vals is None:
            self.stdev_coverage_vals = self.find_stdev_depth_values()

        out_matrix = []
        for bin in self.coverage_bins:
            tmp_row = []
            for sample in self.group_names_dict[group_name]:
                binned_coverage = sample.get_binned_coverage_cnt(self.coverage_bins)
                binned_editing = sample.get_binned_editing_cnt(self.coverage_bins)
                tmp_row.append(binned_editing[bin]/binned_coverage[bin])
            out_matrix.append(tmp_row)

        return out_matrix

    def get_coverage_at_site_for_group(self, group_name, chromosome, position, ref_char, alt_char):
        """

        :param group_1_name:
        :param chromosome:
        :param position:
        :return: ref_cnt, alt_cnt
        """

        samples_es_cov_tuple_dict = {}
        # Samples - EditingSample
        for sample in self.get_group(group_name):
            counts = sample.get_number_of_edited_and_nonedited_bases_at(chromosome, position, ref_char, alt_char)
            samples_es_cov_tuple_dict[sample.get_name()] = counts
        return samples_es_cov_tuple_dict

    def get_average_area_per_coverage_level(self):

        if self.coverage_bins is None:
            self.coverage_bins = self.find_coverage_bins()

        if self.mean_coverage_vals is None:
            self.mean_coverage_vals = self.find_average_depth_values()

        if self.stdev_coverage_vals is None:
            self.stdev_coverage_vals = self.find_stdev_depth_values()

        total_area = 0
        val_list = []
        for i in self.mean_coverage_vals:
            val_list.append(self.mean_coverage_vals[i])
            total_area += self.mean_coverage_vals[i]

        z = [i/total_area for i in val_list]

        return z

    def get_normalized_editing_values(self, group_name):

        if self.coverage_bins is None:
            self.coverage_bins = self.find_coverage_bins()

        if self.mean_coverage_vals is None:
            self.mean_coverage_vals = self.find_average_depth_values()

        if self.stdev_coverage_vals is None:
            self.stdev_coverage_vals = self.find_stdev_depth_values()

        samples_in_group_normalized_coverage = []
        for sample in self.group_names_dict[group_name]:
            binned_coverage = sample.get_binned_coverage_cnt(self.coverage_bins)
            binned_editing = sample.get_binned_editing_cnt(self.coverage_bins)

            total_normalized_editing = 0
            total_coverage = 0
            for coverage_bin in self.coverage_bins:

                scaling_value = self.mean_coverage_vals[coverage_bin]/binned_coverage[coverage_bin]

                # x = binned_coverage[coverage_bin]
                # mu = self.mean_coverage_vals[coverage_bin]
                # sigma = self.stdev_coverage_vals[coverage_bin]
                # scaling_value = (x - mu)/sigma

                ## @TODO: Make this more sane. We only need to calculate this once.
                total_normalized_editing += binned_editing[coverage_bin] * scaling_value
                total_coverage += self.mean_coverage_vals[coverage_bin]

            samples_in_group_normalized_coverage.append(normalized_editing(total_normalized_editing, total_coverage))

        return samples_in_group_normalized_coverage


