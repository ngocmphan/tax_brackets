import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr


# tbl03 - Net Federal Tax
def visualize(csv):
    path = '/Users/ngocphan/PycharmProjects/Personal_tax/' + csv
    df = pd.read_csv(path)
    columns = df.columns[1:6]
    y_pos = df.iloc[14, 1:6]
    return plt.plot(columns, y_pos, label=f'{csv[:-4]}')

plt.figure(1)
tbl03 = 'federal_tax.csv'
tbl02 = 'taxable_income.csv'

taxable_income = visualize(tbl02)
federal_tax = visualize(tbl03)
ax = plt.subplot(111)
ax.get_yaxis().set_major_formatter(tkr.FuncFormatter(lambda x,
                                                    p: format(int(x), ',')))
plt.legend()


plt.figure(2)
tbl01 = 'number_of_filers.csv'
people = visualize(tbl01)
plt.ticklabel_format(style='plain', axis='y')
ax.get_yaxis().set_major_formatter(tkr.FuncFormatter(lambda x, p: format(int(x),
                                                                         ',')))
plt.legend()
plt.show()


