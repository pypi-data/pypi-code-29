import argparse
import collections
import io
import json
import urllib

import boto3
from imd_bands import imd_bands


def get_line(feed):
    return feed.readline()


def line_to_tuple(line):
    if line.index('=') == -1:
        print("Line has no = in it: ", line)
        return
    # split by =
    (name, value) = line.split('=')
    # return tuple of squeezed pieces
    return name.strip(), value.strip()


def process_imd_lines(feed, cur_dictionary):
    # cheat because we know some things about this one weird exceptional tag.
    num_tlc = 0
    while True:
        line = get_line(feed)
        if line is None:
            break
        if not line.strip():
            continue
        if line.strip() == 'END;':
            break
        nvp = line_to_tuple(line)
        tag = nvp[0]
        value = nvp[1]
        if tag == 'BEGIN_GROUP':
            new_dictionary = collections.OrderedDict()
            cur_dictionary[value] = new_dictionary
            process_imd_lines(feed, new_dictionary)
        elif tag == 'END_GROUP':
            break
        elif tag == 'numTLC':
            cur_dictionary[tag] = value
            num_tlc = int(value.replace(';', ''))
            cur_dictionary[tag] = value
        elif tag == 'TLCList':
            caat = value + '\n'
            for i in range(num_tlc):
                caat += get_line(feed)
            # take off the last newline
            caat = caat[:-1]
            cur_dictionary[tag] = caat
        elif tag == 'datumOffset':
            caat = value + '\n'
            while True:
                caat += get_line(feed)
                if ';' in caat:
                    break
            # take off the last newline
            caat = caat[:-1]
            cur_dictionary[tag] = caat
        elif tag == 'mapProjParam':
            caat = value + '\n'
            while True:
                caat += get_line(feed)
                if ';' in caat:
                    break
            # take off the last newline
            caat = caat[:-1]
            cur_dictionary[tag] = caat
        else:
            cur_dictionary[tag] = value
    return cur_dictionary


def read_imd(fileuri):
    url_of_imd = urllib.parse.urlparse(fileuri)
    root_imd_dict = collections.OrderedDict()
    if url_of_imd.scheme == 'file' or url_of_imd.scheme == '':
        print('Processing file: ' + url_of_imd.path)
        feed = open(url_of_imd.path, 'r')
        process_imd_lines(feed, root_imd_dict)
        feed.close()
    elif url_of_imd.scheme == 's3':
        print('Processing S3 Object: ' + url_of_imd.netloc + ' ' + url_of_imd.path)
        bucket = url_of_imd.netloc
        key = url_of_imd.path[1:]
        s3 = boto3.resource('s3')
        obj = s3.Object(bucket, key)
        body = obj.get()['Body'].read().decode('utf-8')
        feed = io.StringIO(body, newline=None)
        process_imd_lines(feed, root_imd_dict)
        feed.close()
    print('Done ingesting IMD')
    return root_imd_dict


def put_imd(fileuri, output_buffer):
    url_of_imd = urllib.parse.urlparse(fileuri)
    if url_of_imd.scheme == 'file' or url_of_imd.scheme == '':
        print('Putting file: ' + url_of_imd.path)
        feed = open(url_of_imd.path, 'w')
        feed.write(output_buffer.getvalue())
        feed.close()
    elif url_of_imd.scheme == 's3':
        print('Putting S3 Object: ' + url_of_imd.netloc + ' ' + url_of_imd.path)
        bucket = url_of_imd.netloc
        key = url_of_imd.path[1:]
        s3 = boto3.resource('s3')
        obj = s3.Object(bucket, key)
        obj.put(Body=output_buffer.getvalue())
    print('Done putting IMD')
    return


def write_imd(output_buffer, ordered_dict, in_group):
    for key, value in ordered_dict.items():
        if isinstance(value, collections.OrderedDict):
            output_buffer.write('BEGIN_GROUP = ' + key + '\n')
            write_imd(output_buffer, value, True)
            output_buffer.write('END_GROUP = ' + key + '\n')
        else:
            if in_group:
                output_buffer.write('\t')
            output_buffer.write(key + ' = ' + value + '\n')
    if not in_group:
        output_buffer.write('END;\n')
    return output_buffer


def edit_imd(input_dict, edit_dict):
    for key, value in edit_dict.items():
        if isinstance(value, dict) or isinstance(value, collections.OrderedDict):
            edit_imd(input_dict[key], value)
        else:
            input_dict[key] = value
    return input_dict


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('edits', nargs=argparse.REMAINDER)
    our_args = parser.parse_args(args)
    print('Reading imd')
    imd_dict = read_imd(our_args.input)
    imd_band_map = imd_bands(imd_dict)
    print("Band map: " + str(imd_band_map))
    imd_edits = our_args.edits
    for cur_edit in imd_edits:
        print('Edit: ' + cur_edit)
        edit_dict = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(cur_edit)
        print('Editing file with:' + str(type(edit_dict)) + " Contents: " + str(edit_dict))
        imd_dict = edit_imd(imd_dict, edit_dict)
    print('IMD after editing: ' + str(imd_dict))
    imd_buffer = io.StringIO()
    write_imd(imd_buffer, imd_dict, False)
    put_imd(our_args.input, imd_buffer)
    return


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
