# Importing all necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

tax_filers = pd.read_csv('/Users/ngocphan/Pycharm'
                         'Projects/Personal_tax/number_of_filers.csv')

# Numbers of tax payers by brackets within the provinces
columns = tax_filers.columns[1:6]
y_pos = list(tax_filers.iloc[14, 1:6])
y_pos_NFL = list(tax_filers.iloc[0, 1:6])
y_pos_Edward = list(tax_filers.iloc[1, 1:6])
y_pos_Nova = list(tax_filers.iloc[2, 1:6])
y_pos_NB = list(tax_filers.iloc[3, 1:6])
y_pos_QB = list(tax_filers.iloc[4, 1:6])
y_pos_ON = list(tax_filers.iloc[5, 1:6])
y_pos_MB = list(tax_filers.iloc[6, 1:6])
y_pos_Saska = list(tax_filers.iloc[7, 1:6])
y_pos_AB = list(tax_filers.iloc[8, 1:6])
y_pos_BC = list(tax_filers.iloc[9, 1:6])
y_pos_NT = list(tax_filers.iloc[10, 1:6])
y_pos_YK = list(tax_filers.iloc[11, 1:6])
y_pos_NN = list(tax_filers.iloc[12, 1:6])
y_pos_non_res = list(tax_filers.iloc[13, 1:6])

# Graph the tax payers number per provinces and total number by tax brackets
plt.plot(columns, y_pos, color='yellow', linewidth=2, label='All Brackets')
plt.title('General personal tax population by tax brackets')
plt.plot(columns, y_pos_NFL, markerfacecolor='blue', markersize=12,
         color='skyblue', linewidth=4)
plt.plot(columns, y_pos_Edward, marker='', color='olive', linewidth=2,
         label ="Prince Edward")
plt.plot(columns, y_pos_Nova, marker='', color='fuchsia',
         linewidth=2, linestyle='dashed', label="Nova Scotia")
plt.plot(columns, y_pos_NB, color='green', label='New Brunswik')
plt.plot(columns, y_pos_QB, color='aqua', linestyle='dashed', label='Quebec')
plt.plot(columns, y_pos_ON, marker='', color='red',
         linewidth=2, linestyle='dashed', label="ON")
plt.plot(columns, y_pos_MB, linestyle='dashed', color='indigo', label='Manitoba')
plt.plot(columns, y_pos_Saska, color='cyan', label='Saskatchewan')
plt.plot(columns, y_pos_AB, color='orange', label='Alberta', linestyle='dashed')
plt.plot(columns, y_pos_BC, color='Purple', label='British Columbia')
plt.plot(columns, y_pos_NT, color='Grey', label='Northwest Territories')
plt.plot(columns, y_pos_YK, color='turquoise', linestyle='dashed', label='Yukon')
plt.plot(columns,y_pos_NN, color='brown', label='Nunavut')
plt.plot(columns, y_pos_non_res, color='lavender', linestyle='dashed',
         label='non_resident')

# Customizing the graphs with numerical y_axis and legends
plt.legend()
ax = plt.subplot(111)
plt.ticklabel_format(style='plain', axis='y')
ax.get_yaxis().set_major_formatter(tkr.FuncFormatter(lambda x, p: format(int(x),
                                                                         ',')))
plt.show()


# From the graph, the four provinces with the difference in taxable income,
# mostly range in the lower $45,000 and less than $91,000: Ontario, Quebec,
# British Columbia, and Alberta
# => Choose these 4 provinces to continue further due to diversity and range

