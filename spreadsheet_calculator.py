import pandas as pd

data = pd.read_csv(r'LIBERTY NOV 2020 - Test Worksheet.csv')

df = pd.DataFrame(data)
print(df.head())

df[' NEW PRICE '] = df[' NEW PRICE '].str.replace('$', '').str.replace(',', '')


print(df[' NEW PRICE '])

df['30 Percent Profit Margin'] = (df[' NEW PRICE '].astype(float)/(1 - 0.30))



df['30 Percent Profit Margin'] = df['30 Percent Profit Margin'].round(2)

print(df['30 Percent Profit Margin'])

df.to_csv(r'C:\Users\Kim\PycharmProjects\liberty_glove_profit_margin_spreadsheet\liberty_nov_2020_equip_direct_retail_pricing.csv')
