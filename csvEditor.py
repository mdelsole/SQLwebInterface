import csv, os


def deleteCSV(theIndex):
    with open('flowersImages.csv', 'r') as inp, open('new.csv', 'w') as out:
        writer = csv.writer(out)
        for num, row in enumerate(csv.reader(inp)):
            if num != theIndex:
                writer.writerow(row)
    os.remove('flowersImages.csv')
    os.rename('new.csv', 'flowersImages.csv')


def updateCSV(theIndex, value):
    with open('flowersImages.csv', 'r') as inp, open('new.csv', 'w') as out:
        writer = csv.writer(out)
        for num, row in enumerate(csv.reader(inp)):
            if num != theIndex:
                writer.writerow(row)
            else:
                writer.writerow([value])
    os.remove('flowersImages.csv')
    os.rename('new.csv', 'flowersImages.csv')


def insertCSV(value):
    with open('flowersImages.csv', 'r') as inp, open('new.csv', 'w') as out:
        writer = csv.writer(out)
        for num, row in enumerate(csv.reader(inp)):
            writer.writerow(row)
        writer.writerow([value])
    os.remove('flowersImages.csv')
    os.rename('new.csv', 'flowersImages.csv')

