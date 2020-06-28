import pandas as pd

cities_df = pd.read_csv("../cities.csv")

to_html = cities_df.to_html()


print(to_html)
