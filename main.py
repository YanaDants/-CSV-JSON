import csv
import json


def make_json(csvFilePath, jsonFilePath):
    new_spisk = {}

    update = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06",
              "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12",
              "1": "01", "2": "02", "3": "03", "4": "04", "5": "04", "6": "06", "7": "07", "8": "08", "9": "09"}

    upAPI = {"1.0 and up": "API 1", "1.5 and up": "API 3", "1.6 and up": "API 4", "2.0 and up": "API 5",
             "2.0.1 and up": "API 6", "2.1 and up": "API 7", "2.2 - 7.1.1": "API 8", "2.2 and up": "API 8",
             "2.3 and up": "API 9", "2.3.3 and up": "API 10", "3.0 and up": "API 11", "3.1 and up": "API 12",
             "3.2 and up": "API 13", "4.0 and up": "API 14", "4.0.3 - 7.1.1": "API 15", "4.0.3 and up": "API 15",
             "4.1 - 7.1.1": "API 16", "4.1 and up": "API 16", "4.2 and up": "API 17", "4.3 and up": "API 18",
             "4.4 and up": "API 19", "4.4W and up": "API 19", "5.0 - 6.0": "API 21", "5.0 - 7.1.1": "API 21",
             "5.0 - 8.0": "API 21", "5.0 and up": "API 21", "5.1 and up": "API 22", "6.0 and up": "API 23",
             "7.0 - 7.1.1": "API 24", "7.0 and up": "API 24", "7.1 and up": "API 25", "8.0 and up": "API 26",
             "NaN": "NaN", "Varies with device": "Varies with device"}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
#Android Ver
            if rows['Android Ver'] in upAPI:
                rows['Android Ver'] = upAPI[rows['Android Ver']]
#Last Updated
            stroke = rows['Last Updated'].split()
            i = 0

            for data in stroke:
                if data in update:
                    data = update[data]
                    if i == 1:
                        stroke[i] = data
                        i += 1
                    else:
                        stroke[i] = data
                        i +=1
                else:
                    stroke[i] = data
                    i += 1

            if (stroke[0] != "1.0.19"):
                stroke = stroke[2] + "-" + stroke[0] + "-" + stroke[1][:-1]
                rows['Last Updated'] = stroke
#Installs
            count = rows['Installs']
            rows['Installs'] = count[:-1]
#Price
            if rows['Price'] == "1":
                rows['Price'] = "true"
            else:
                rows['Price'] = "false"


            new_spisk.setdefault(rows['App'], rows)
            #new_spisk = { rows['App']: rows }


    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(new_spisk, indent=4))

csvFilePath = r'googleplaystore.csv'
jsonFilePath = r'google.json'

make_json(csvFilePath, jsonFilePath)
