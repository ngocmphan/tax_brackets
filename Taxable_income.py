import General_info as gen
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr


taxable_income = pd.read_csv('/Users/ngocphan/Pycharm'
                             'Projects/Personal_tax/taxable_income.csv')
# columns = taxable_income.columns[1:6]
# y_pos_taxable = list(taxable_income.iloc[14, 1:6])


def province_graph(file, x):
    path = '/Users/ngocphan/PycharmProjects/Personal_tax/' + file
    df = pd.read_csv(path)
    columns_function = df.columns[1:6]
    y_pos_name = list(df.iloc[x, 1:6])
    return plt.plot(columns_function, y_pos_name, label=f'{df.iloc[x,0]}')


# Creating plots for each provinces relative to tax brackets
plt.figure(2)
csv = 'taxable_income.csv'
province_graph(csv, 1), province_graph(csv, 2), province_graph(csv, 3)
province_graph(csv, 4), province_graph(csv, 5), province_graph(csv, 6)
province_graph(csv, 7), province_graph(csv, 8), province_graph(csv, 9)
province_graph(csv, 10), province_graph(csv, 11), province_graph(csv, 12)
province_graph(csv, 13)
ax = plt.subplot(111)
ax.get_yaxis().set_major_formatter(tkr.FuncFormatter(lambda x, p:
                                                     format(int(x), ',')))
plt.legend()
plt.show()


# plt.plot(columns, y_pos_taxable, color='red', linestyle='dashed',
#          label='Taxable Income')
# ax = plt.subplot(111)
# ax.get_yaxis().set_major_formatter(tkr.FuncFormatter(lambda x, p:
# format(int(x), ',')))
# plt.legend()
# plt.show()

# Result of comparing the total number of people in brackets
# and actual taxable income:
# Decreasing number of people as heading to the second bracket;
# Increasing taxable income as heading to the second brackets;
# Highest number of people in the first brackets, as heading to second,
# higher taxable income


