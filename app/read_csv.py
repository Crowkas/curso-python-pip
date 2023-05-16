import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader: 
      iterable = zip(header, row)
      country_dict = {Key : value for (Key, value) in iterable}
      #population_dict = {Key : value for (Key, value) in country_dict if 'Population' in Key} 
      data.append(country_dict)
    return data 

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(type(data[0]))
  
  