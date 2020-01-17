import sys
import csv
import datetime


def csvReader(argv):
    """Reads a csv file and returns all rows that contain the label that is passed to it.
    """
    labels = list(sys.argv)
    today = datetime.datetime.strftime(datetime.datetime.now(), format="%m_%d_%Y")
    outpath = f'data/results/{today}.csv'
    with open(outpath, 'w', newline='') as outfile:
        csvWriter = csv.writer(outfile, delimiter=' ')
        with open('data/tmp/data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                if any(l in row for l in labels):
                    csvWriter.writerow(row)


if __name__ == '__main__':
    csvReader(sys.argv)
