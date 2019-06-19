import os
import math
import csv
import argparse

def main():
    parser = argparse.ArgumentParser(
            description='Convert toggl time HH:MM:SS to hour decimal format.')
    parser.add_argument('inputfile', type=str, help='Path to the input file (.csv)')
    parser.add_argument('-o', help='name of the output file')
    args = parser.parse_args()
    if args.inputfile and os.path.exists(args.inputfile):
        infile = args.inputfile
        if args.o:
            out = args.o
            format_time(infile, name=out)
        else:
            format_time(infile)


def format_time(input, name='output.csv'):
    report = []
    output = []

    with open(input, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            report.append(row)

    for rn, row in enumerate(report):
        if rn != 0:
            title = row[2]
            time = row[3]
            t_parts = time.split(':')
            t_sec = int(t_parts[0])*3600 + int(t_parts[1])*60 + int(t_parts[2])
            t_hours = math.ceil((t_sec / 3600)*100)/100

            entry = (title, t_hours)
            output.append(entry)


    with open(name, 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerows(output)


if __name__ == "__main__":
    main()
