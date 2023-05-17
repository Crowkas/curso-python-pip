import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = list(filter(lambda i: i['Continent'] == 'South America', data))
  print("Registros filtrados para Sudamérica:", len(data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent']== 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  country = input('Ingrese el país -> ').capitalize()
  print("País ingresado:", country)
  
  charts.generate_pie_chart(country, countries, percentages)
  print("Gráfico de pie generado exitosamente.")

  data = read_csv.read_csv('data.csv')
  print("Total de registros en el archivo CSV:", len(data))

  result = utils.population_by_country(data, country)

  if result:
    print("País encontrado en los datos.")
    country_dict = result[0]
    labels, values = utils.get_population(country_dict)
    charts.generate_bar_chart(country, labels, values)
    print("Gráfico de barras generado exitosamente.")
  else:
    print("País no encontrado en los datos.")

  world_percentages = utils.get_world_percentages(data)
  if country in world_percentages[0]:
    index = world_percentages[0].index(country)
    percentage = world_percentages[1][index]
    print(f'Porcentaje de población mundial para {country}: {percentage}%')
  else:
    print(f'No se encontró información de porcentaje de población mundial para {country}')

if __name__ == '__main__':
    run()