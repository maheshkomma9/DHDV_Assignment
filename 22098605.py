#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:37:27 2024

@author: maheshroyal
"""
#import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#declaring global variable countries to use in both bar graphs
countries=['India','China','United States','United Kingdom','France','Italy','Germany']

#function to read the file
def read_file(file_name):
    my_data_frame = pd.read_excel(file_name, skiprows=3)
    
    #retreving requied data from overall data set
    my_req_data_frame = my_data_frame[my_data_frame['Country Name'].isin(countries)]
    [['Country Name', '2021']]
    plt.figure(figsize=(15,6.5))
    sns.set_style('darkgrid')
    
    #plot the figure
    g = sns.barplot(data=my_req_data_frame, x='2021', y='Country Name',ci=False, 
                    palette='YlGnBu', orient='h')
    g.set_yticklabels(my_req_data_frame['Country Name'], fontdict={'fontsize':20})
    
    #labelling the plot
    plt.xticks(fontsize=20)
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Food Production Index 2022',fontsize=30, color='mediumblue')
    plt.savefig('22098605.png',dpi=300)
    
    
    
#declaring the file   
read_file('food production index.xls')


#function to read the file
def read_file(file_name):
    my_data_frame = pd.read_excel(file_name, skiprows=3)
        
    #retreving requied data from overall data set
    my_req_data_frame = my_data_frame[my_data_frame['Country Name'].isin(countries)]
    [['Country Name', '2022']]

    plt.figure(figsize=(15,6.5))
    sns.set_style('darkgrid')
    
    #plot the figure
    g = sns.barplot(data=my_req_data_frame, x='2022', y='Country Name',ci=False, 
                    palette='PuBuGn', orient='h')
    g.set_yticklabels(my_req_data_frame['Country Name'], fontdict={'fontsize':20})
    
    #labelling the plot
    plt.xticks(fontsize=20)
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Fertilizer consumption in Kilograms per one hectare of ariable land 2022' ,fontsize=30, color='mediumblue')
    plt.savefig('22098605.png',dpi=300)
    
#declaring the file   
read_file('fertilizer.xls')

#function to read the file
def read_file(file_name):
    my_data_set = pd.read_excel(file_name,skiprows=3)
    countries=['China', 'Japan','India','Brazil', 'Canada','Australia']
    
    #retreving required data
    req_set_of_years=[str(year) for year in range(2000, 2022)]
    my_req_set_countries=my_data_set[my_data_set['Country Name'].isin(countries)]
    [['Country Name'] + req_set_of_years]
    
    #plot the figure
    plt.figure(figsize=(12, 6))
    for index, row in my_req_set_countries.iterrows():
        plt.plot(req_set_of_years, row[req_set_of_years], label=row['Country Name'])
    plt.grid(linestyle='--',linewidth=0.5,color='black')


    # Adding labels and title
    plt.xlabel('')
    plt.ylabel('GDP (%)',fontsize=15,color='deepskyblue')
    plt.title('Total Agriculture contribution in country\'s GDP',fontsize=17, color='mediumblue')
    plt.legend()
    plt.xticks(req_set_of_years[::3], fontsize='15')
    plt.savefig('22098605.png',dpi=300)
    
file_name='Agriculture_value_added(%gdp).xls'
read_file(file_name)

#define the function to read dataset
def read_file(file_name):
    my_data_frame=pd.read_excel(file_name,skiprows=3)
    
    #declaring the country
    my_req_country='United Kingdom'
    
    #declaring the indicators to show in pie chart
    indicators=['Forest area (% of land area)','Arable land (% of land area)',
                'Agricultural land (% of land area)']
    
    #retriving required data
    my_sorted_df = my_data_frame[(my_data_frame['Country Name'] == my_req_country) & 
                          (my_data_frame['Indicator Name'].isin(indicators))]

    colors = ['green','gold','yellowgreen']
    explode = (0.1,0,0.1)


    # Plotting a pie chart
    plt.figure(figsize=(10, 10))
    plt.pie(my_sorted_df['2021'], labels = my_sorted_df['Indicator Name'],
            colors = colors, autopct='%1.1f%%', explode = explode, shadow = True, startangle = 140,
            textprops ={'fontsize':20})

    # Adding title
    plt.title('Land Distribution of United Kingdom 2021',fontsize=30, color='mediumblue')
    plt.savefig('22098605.png',dpi=300)
    
file_name='Land_Distrubment.xls'
read_file(file_name)