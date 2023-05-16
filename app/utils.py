def get_population(country_dict):
  population_dict = {
  '2022': str(country_dict['2022 Population']),
  '2020': str(country_dict['2020 Population']),
  '2015': str(country_dict['2015 Population']),
  '2010': str(country_dict['2010 Population']),
  '2000': str(country_dict['2000 Population']),
  '1990': str(country_dict['1990 Population']),
  '1980': str(country_dict['1980 Population']),
  '1970': str(country_dict['1970 Population'])
  }
  labels = list(population_dict.keys())
  values = list(population_dict.values())
  return labels, values

def population_by_country(data, country):
  result = list(filter(lambda i: i['Country/Territory'] == country, data))
  print(result)
  return result

'''def get_world_percentages(data):
  percentages_dict = {int(fila[10]) for fila in data}
  names = percentages_dict.keys()
  per = percentages_dict.values()
  return names, per'''
  

