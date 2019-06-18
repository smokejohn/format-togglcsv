import math
import csv
import argparse

parser = argparse.ArgumentParser(description='Convert toggl time HH:MM:SS to hour format.')
parser.add_argument('path', metavar='P', type=str, help='Path to the input file')
parser.add_argument('-o', help='name of the output file')
args = parser.parse_args()

input = None

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

