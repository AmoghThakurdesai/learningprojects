#! python3
# remove csv header - removes headers from csv files in current working directory

import csv,os
os.makedirs('headerRemoved',exist_ok=True)

#loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from'+ csvFilename +'...')

    #Read the CSV file in (skipping first row)
    csvRows=[]
    csvFileObj=open(csvFilename)
    readerObj=csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num==1:
            continue    #skip first row
        csvRows.append(row)
    csvFileObj.close()

    #Write out the CSV file.
    csvFileObj=open(os.path.join('headerRemoved',csvFilename),'w',newline='')
    csvWriter=csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()


