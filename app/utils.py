def get_population(country_dict):
  population_dict = {
  '2022': int(country_dict['2022 Population']),
  '2020': int(country_dict['2020 Population']),
  '2015': int(country_dict['2015 Population']),
  '2010': int(country_dict['2010 Population']),
  '2000': int(country_dict['2000 Population']),
  '1990': int(country_dict['1990 Population']),
  '1980': int(country_dict['1980 Population']),
  '1970': int(country_dict['1970 Population'])
  }
  labels = sorted(population_dict.keys())
  values = [population_dict[label] for label in labels]
  return labels, values

def population_by_country(data, country):
  result = list(filter(lambda i: i['Country/Territory'] == country, data))
  return result

def get_world_percentages(data):
    percentages_dict = {}
    for fila in data:
      percentage = float(fila['World Population Percentage'])
      country = fila['Country/Territory']
      percentages_dict[country] = percentage

    names = list(percentages_dict.keys())
    per = list(percentages_dict.values())
    return names, per
