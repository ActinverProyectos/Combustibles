#!/usr/bin/env python
# coding: utf-8

# In[20]:


import tabula
import os
import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import pandas as pd


# In[21]:


curren_folder =  os.getcwd()
folder_pdf = 'D:\\ACTINVER\\Proyectos actinver\\Z Info Combustibles\\Archivos_pdf'
save_path = 'D:\\ACTINVER\\Proyectos actinver\\Z Info Combustibles\\CSVs'


# # Descarga del archivo PDF

# In[22]:


def get_date():
    '''
    Return the current day and month
    '''
    return datetime.today().strftime('%d-%b')


# In[23]:


def get_url():
    '''
    Find the most recent pdf uploaded to the page and return its url to download 
    '''
    url = "https://www.gob.mx/cre/documentos/precios-maximos-aplicables-de-gas-lp?idiom=es"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    a =  soup.find_all(attrs={"class" : "btn btn-default"})
    return 'https://www.gob.mx/' + a[0]['href']


# In[24]:


def download_pdf(url: str):
    '''
    Download a pdf fro its url
    '''
    urllib.request.urlretrieve(url,f'{folder_pdf}{get_date()}.pdf')
    print(folder_pdf + f'{folder_pdf}{get_date()}')


# In[44]:


download_pdf(get_url())


# # Conversion de PDF a CSV

# In[25]:


def get_files(path: str):
    '''
    return all the files from a folder
    '''
    contenido = os.listdir(path)
    return contenido


# In[26]:


def get_name_from_data(pdf_name: str):
    name = pdf_name.lower()
    names= name.split('_')
    days = []
    months = []
    year = 0
    try:
        year = int(names[-1][0:4]) 
    except:
        year = 2021

    
    for name in names:
        if len(name) > 0 and len(name) < 3:
            try:
                aux = int(name)
                days.append(aux)
            except:
                pass
        
        if name in ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']:
            months.append(name)
    return f'{days[0]}-{months[0][0:3]}-{year}'


# In[30]:


def pdf_to_csv():
    '''
    Return list of DF of all pdf files
    '''
    for pdf in get_files(folder_pdf):
        df_list = tabula.read_pdf(folder_pdf + '\\' + pdf, pages="all",pandas_options={'header': None})
        df = pd.DataFrame()
        
        for dataFrame in df_list:
            len(dataFrame)
            aux = dataFrame.iloc[1:len(dataFrame), 0:5]
            df = pd.concat([df, aux])
        
        print(pdf)
        
        df.dropna(how='all', axis=1, inplace=True)
        df.columns = ['Región', 'Estado', 'Municipio', 'Precio Litro', 'Precio Kg']
        df = df.assign(Fecha = get_name_from_data(pdf))
        
        df.to_csv(save_path + '\\' + pdf.replace('pdf','csv'), index=False, encoding='latin-1')


# In[31]:


pdf_to_csv()


# In[108]:


#get_name_from_data('PRECIOS_MA_X_VIGENTES_29_DE_AGOSTO_4_DE_SEPTIEMBRE_2021.pdf')


# In[ ]:




