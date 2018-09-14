# -*- coding: utf-8 -*-

"""Main module."""
import sys, re
import Bio
from Bio import SeqIO
from BCBio import GFF

fasta_regex = re.compile('\.(fasta|fa|fna|fas|ffa|fra)$', re.IGNORECASE)
genbank_regex = re.compile('\.(genbank|gbk|gb)$', re.IGNORECASE)
gff_regex = re.compile('\.(gff|gff3|gff2)$', re.IGNORECASE)
dupkey_regex = re.compile('\'(.*)\'')

def load_references(reference_files):
    """Returns a list of Biopython SeqRecord objects constructed from the passed 
    list of reference files. Reference files can be in genbank, GFF, or FASTA 
    format. genbank and GFF files may not have sequence information. If they 
    do not, then this method expects the sequence information to be contained
    within a passed FASTA file."""

    if type(reference_files) == str:
        reference_files = [reference_files]

    if type(reference_files) != list:
        raise ValueError("IN: bio_utils.load_references(): "
                         "Expected one positional argument of type "
                         "str or list. Recieved type: {}".format(type(reference_files)))

    file_set = set(reference_files)

    if len(file_set) != len(reference_files):
        raise ValueError("IN: bio_utils.load_references(): "
                         "Some reference files were passed more than once")

# Load FASTA files
    fasta_seq_dict = {}
    fasta_SeqRecords = []

    for FASTA_file in reference_files:

        if re.search(fasta_regex, FASTA_file):
            
            parsed_seq_records = list(SeqIO.parse(FASTA_file, 'fasta'))
            
            if len(parsed_seq_records) == 0:
                
                raise ValueError("IN: bio_utils.load_references(): "
                                 "Biopython package parsed zero FASTA "
                                 "records from file: {}".format(FASTA_file))
            
            else:
                
                fasta_SeqRecords.extend(parsed_seq_records)

    try:
        
        fasta_seq_dict = SeqIO.to_dict(fasta_SeqRecords)

    except ValueError as duplicate_key_error:
        
        m = re.search(dupkey_regex, duplicate_key_error.args[0])
        if m:
            dupkey = m.group(1)
        else:
            dupkey = duplicate_key_error.args[0]
        
        duplicate_key_error.args = ("IN: bio_utils.load_references(): "
                                    "Found FASTA records with the same ID: {}".format(dupkey),)
    
        raise duplicate_key_error
    
    # Load annotated sequences (a.k.a genbank / GFF)
    annotated_SeqRecords = []
    
    for annotated_file in reference_files:

        if re.search(genbank_regex, annotated_file):
            
            parsed_seq_records = list(SeqIO.parse(annotated_file, 'genbank'))
            
            if len(parsed_seq_records) == 0: 
                
                raise ValueError("IN: bio_utils.load_references(): "
                                 "Biopython package parsed zero genbank "
                                 "records from file: {}".format(annotated_file))
            
            else:
                annotated_SeqRecords.extend(parsed_seq_records)

        elif re.search(gff_regex, annotated_file):
            
            in_handle = open(annotated_file)
            
            try:
                
                parsed_seq_records = list(GFF.parse(in_handle))
                in_handle.close()
                
                if len(parsed_seq_records) == 0: 
                    
                    raise ValueError("IN: bio_utils.load_references(): "
                                     "bcbio-gff package parsed zero gff "
                                     "records from file: {}".format(annotated_file))
                
                else:
                    annotated_SeqRecords.extend(parsed_seq_records)

            except Exception as e:
                
                e.args = ("IN: bio_utils.load_references(): GFF reference file ({}) "
                          "failed to be parsed by bcbio-gff package. An exception was "
                          "raised with message: {}".format(annotated_file, e.args[0]),)
                
                raise e

        elif not re.search(fasta_regex, annotated_file):
            raise ValueError("IN: bio_utils.load_references(): Could not identify reference "
                             "file format. Expecting to find file extentions for genbank, GFF, "
                             "or FASTA files. Reference file name: {}".format)

    for annotated_seq_record in annotated_SeqRecords:
        
        if isinstance(annotated_seq_record.seq, Bio.Seq.UnknownSeq):
            
            if len(fasta_SeqRecords) == 0:
                raise ValueError("IN: bio_utils.load_references(): A biopython SeqRecord ({}) "
                                 "was created without any sequence information!".format(annotated_seq_record.id))

            if annotated_seq_record.id in fasta_seq_dict:
                
                if len(annotated_seq_record.seq) == len(fasta_seq_dict[annotated_seq_record.id].seq):
                    # If the sequence records have the same id AND the length of the unknown sequence is equal to the length of the 
                    # sequence found in the dictionary, then it is probably safe to attach this sequence to the current SeqRecord. 
                    # Warning! Doing so can have disaterous consequences if this sequence information is not the exact same 
                    # information that the annotations are based on. Client might want to sanity check the records returned 
                    # from this method.

                    annotated_seq_record.seq = fasta_seq_dict[annotated_seq_record.id].seq
                    
                    for index, fasta_record in list(enumerate(fasta_SeqRecords)):
                        if fasta_record.id == annotated_seq_record.id:
                            fasta_SeqRecords.pop(index)
                            break

                else:
                    raise ValueError("IN: bio_utils.load_references(): SeqRecord {} has an unknown "
                                     "sequence. Found a FASTA record with the same ID, but it's "
                                     "length is not the same as the unknown sequence".format(annotated_seq_record.id))
            else:
                raise ValueError("IN: bio_utils.load_references(): Could not find sequence information for sequence record {}".format(annotated_seq_record.id))

    if len(annotated_SeqRecords) == 0 and len(fasta_SeqRecords) == 0:
        raise ValueError("IN: bio_utils.load_references(): Biopython/BCBio parsed zero sequence "
                         "records from passed reference files: {}".format(", ".join(reference_files)))

    return annotated_SeqRecords + fasta_SeqRecords