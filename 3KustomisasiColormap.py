import pandas as pd 
import datetime
import matplotlib.pyplot as plt 

#membaca file data.csv
dataset = pd.read_csv('data.csv')

#Buat kolom baru yg bertipe datetime dalam format '%Y-%m'
dataset['order_month'] = dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
#Buat kolom GMV
dataset['gmv'] = dataset['item_price']*dataset['quantity']
# plt.clf()
dataset.groupby(['order_month','province'])['gmv'].sum().unstack().plot(cmap='Set1')
plt.title('GMV Bulanan Tahun 2019 - Perincian menurut provinsi', loc='center',pad=30, fontsize=10, color='blue')
plt.xlabel('Bulan Pemesanan', fontsize=15)
plt.ylabel('Jumlah Total (dalam Miliaran)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.5), shadow=True, ncol=2, title='Provinsi', fontsize=9, title_fontsize=11)
plt.gcf().set_size_inches(10, 8)
plt.tight_layout()
plt.savefig('monthly_gmv.png', quality=95)
plt.show()