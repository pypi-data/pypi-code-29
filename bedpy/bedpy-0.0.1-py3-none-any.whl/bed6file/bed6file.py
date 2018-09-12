import os
from sil import Sil
import cnf as CNF
from ..utils.files import filelines, basename_no_ext, linesplit
from ..utils.constants import DEFAULT_SIL_OPTIONS, DELIM, HEADER

class BED6File:
    def __init__(self,
        file,
        input_directory,
        output_directory,
        reference_file
    ):
        self.file             = file
        self.reference_file   = reference_file
        self.input_directory  = input_directory
        self.output_directory = output_directory

    def filter(
        self,
        filters:list,
        output_file:str=None,
        header:bool=HEADER,
        delim:str=DELIM,
        progress_options:dict=DEFAULT_SIL_OPTIONS,
        verbose:bool=True
    ):
        from ..bed6 import BED6

        input_file = os.path.join(self.input_directory, self.file)

        lines_in_input = filelines(input_file)
        if lines_in_input is None: return None

        if verbose:
            sil = Sil(lines_in_input, **progress_options)
            msg = f'''
            Applying user specified filters named:
                "{CNF.pretty_print(filters)}"
            to sequences defined in:
                "{input_file}"
            '''
            print(msg)


        cnf = CNF.group(filters)

        # Define default output filename (self.file_filter1_filter2_...filtern.bed)
        if output_file is None:
            output_file = os.path.join(self.output_directory,
                f'{basename_no_ext(self.file)}{CNF.filename(filters)}.bed')


        with \
        open(input_file, 'r') as input_file_object, \
        open(output_file, 'w') as output_file_object:

            if header:
                output_file_object.write(input_file_object.readline())
                if verbose: sil.tick()

            for line in input_file_object:
                bed = BED6(*linesplit(line, DELIM, NEWLINE))
                if CNF.apply(cnf, bed): output_file_object.write(line)
                if verbose: sil.tick()

        if verbose:
            lines_in_output = filelines(output_file)
            if header: lines_in_output -= 1
            msg = f'''
            Filtering complete.
            {lines_in_output} sequences found.
            {round(lines_in_output/lines_in_input*100,2)}% of starting sequences.
            Results stored in:
                {output_file}
            '''
            print(msg)

        return BED6File(
            os.path.basename(output_file),
            input_directory=self.output_directory,
            output_directory=self.output_directory,
            reference_file=self.reference_file
        )



    def to_fasta(self, output_file:str=None) -> None:
        """
        Calls the external 'fastaFromBed' command (part of the bedtools suite)
        to extract the sequences denoted in <bed_file> and write them out to
        <output_file> as a tsv.
        """
        if output_file is None:
            output_file = os.path.join(self.output_directory,
                f'''{basename_no_ext(self.file)}.fa''')

        command = "fastaFromBed "\
            " -fi {reference_file} "\
            " -bed {bed_file} "\
            " -fo {output_file} "\
            " -s -name -tab".format(
            reference_file=self.reference_file,
            bed_file=os.path.join(self.input_directory, self.file),
            output_file=output_file
        )
        # input (-fi), bed_file (-bed), output (-fo)
        # forced_strandedness (-s), named (-name), and tabbed (-tab)
        os.system(command)
        return output_file

    def pad(
        self,
        len:int,
        output_file:str=None,
        header:bool=HEADER,
        delim:str=DELIM,
        progress_options:dict=DEFAULT_SIL_OPTIONS,
        verbose=True
    ):
        from ..bed6 import BED6
        from ..pbed6 import PBED6
        input_file = os.path.join(self.input_directory, self.file)

        lines_in_input = filelines(input_file)
        if lines_in_input is None: return None

        if verbose:
            sil = Sil(lines_in_input, **progress_options)
            print(f'Randomly padding sequences to {len}')

        if output_file is None:
            output_file = os.path.join(
                self.output_directory,
                f'''{basename_no_ext(self.file)}_pad_{len}.pbed''')


        with \
        open(input_file, 'r') as input_file_object, \
        open(output_file, 'w') as output_file_object:

            if header:
                output_file_object.write(input_file_object.readline())
                if verbose:sil.tick()

            for line in input_file_object:
                bed = BED6(*line.rstrip('\n').split(delim))
                pbed = bed.pad(len)
                output_file_object.write(pbed.as_txt(delim))
                if verbose: sil.tick()

        if verbose:
            lines_in_output = filelines(output_file)
            if header: lines_in_output -= 1
            msg = f'''Padding complete.
            Results stored in:
                {output_file}
            '''
            print(msg)
        return BED6File(
            os.path.basename(output_file),
            input_directory=self.output_directory,
            output_directory=self.output_directory,
            reference_file=self.reference_file
        )
