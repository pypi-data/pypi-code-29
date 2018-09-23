import argparse, pathlib, PyPDF2


def mergepdf(input_dir, output_file, sorted_key):
    """Merge PDF files."""
    lst = list(map(str, pathlib.Path(input_dir).rglob('*.pdf')))
    key = eval(f"lambda s: f'{sorted_key}'") if sorted_key else None
    if key:
        lst = sorted(lst, key=key)
        print(lst)
    try:
        merger = PyPDF2.PdfFileMerger()
        print('Including')
        for file in lst:
            merger.append(file, import_bookmarks=False)
            print(f' {file}{(" as " + key(file)) if key else ""}')
        merger.write(output_file)
    finally:
        merger.close()
        print(f'Output {output_file}')


def main():
    parser = argparse.ArgumentParser(description=mergepdf.__doc__)
    parser.add_argument('-i', '--input-dir', default='.')
    parser.add_argument('-o', '--output-file', default='out.pdf')
    parser.add_argument('-k', '--sorted-key')
    args = parser.parse_args()
    mergepdf(args.input_dir, args.output_file, args.sorted_key)


if __name__ == '__main__':
    main()