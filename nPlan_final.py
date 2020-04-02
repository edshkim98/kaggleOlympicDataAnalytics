import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def men(a):
    male = a['Sex'] == 'M'
    return a[male]

def women(a):
    female = a['Sex'] == 'F'
    return a[female]

def winter(a):
    winter = a['Season'] == 'Winter'
    return a[winter]

def summer(a):
    summer = a['Season'] == 'Summer'
    return a[summer]

def medal_only(a):
    return pd.notnull(a["Medal"])

def grp_yr_cnt(a):
    return a.groupby("Year").count()

def no_of_sport(a):
    a = a[["Year","Sport"]]
    x = a.drop_duplicates(["Year","Sport"])
    x1 = x.groupby("Year").size()
    return x1

def graph_plot1(x):
    for i in range(0,len(x)):
        plt.subplot(2,2,i+1)
        
        if (i+1) == 1:
            plt.title('Figure 1(a). Number of medalists in Summer')
            plt.ylabel('No. of medals')
        elif (i+1) == 2:
            plt.title('Figure 1(b). Number of medals in Winter')
        elif (i+1) == 3:
            plt.ylabel('No. of olympian')
            plt.xlabel('Year')
            plt.title('Figure 2(a). Number of olympian in Summer')
        elif (i+1) == 4:
            plt.xlabel('Year')
            plt.title('Figure 2(b). Number of olympian in Winter')
        for j in range(0,len(x[0])):
            plt.plot(x[i][j])
        plt.legend(['Male','Female'],loc="upper right")
    plt.savefig('graph1')

def graph_plot2(x):
    for i in range(0,len(x)):
        plt.subplot(2,1,i+1)
        if (i+1) == 1:
            plt.title('Figure 3. Number of different type of sports played in Winter Olympic')
        else:
            plt.title('Figure 3. Number of different type of sports played in Summer Olympic')
            plt.xlabel('Year')
        plt.ylabel('No. of sports')
        for j in range(0,len(x[0])):
            plt.plot(x[i][j])
        plt.legend(['Male','Female'],loc="upper left")
    plt.savefig('graph2')

def cnt_no_olympian(x):
    x = x.drop_duplicates(subset=['ID','Year'])
    x = grp_yr_cnt(x)
    return x['ID']

def cnt_no_medal(x):
    x = x.drop_duplicates(subset=["Year","Medal","Event"]) #remove duplicates
    return x[medal_only(x)]

if __name__ == '__main__':
    
    #read excel file
    data = pd.read_csv("C:\\shkim\\Internship\\nPlan\\data\\athlete_events.csv")

    #Data extraction and simplification
    
    #Display coloumns that are only necessary 
    gb = data["NOC"]=="GBR" #Extract players who are assigned to GBR only
    data_gb = data[gb]
    
    #remove players playing more than once in same olympic
    data_gb_wt = winter(data_gb) #Seperate it by Season
    data_gb_sm = summer(data_gb)
    
    data_gb_wt_m = men(data_gb_wt) #Seperate it by Gender
    data_gb_wt_f = women(data_gb_wt)
    data_gb_sm_m = men(data_gb_sm)
    data_gb_sm_f = women(data_gb_sm)

    #Calculate a number of different type of sports played and assign a variable
    data_gb_wt_m_sport = no_of_sport(data_gb_wt_m) 
    data_gb_wt_f_sport = no_of_sport(data_gb_wt_f)
    data_gb_sm_m_sport = no_of_sport(data_gb_sm_m)
    data_gb_sm_f_sport = no_of_sport(data_gb_sm_f)

    #Narrow the data to medalists only
    data_gb_wt_m_medal = cnt_no_medal(data_gb_wt_m)
    data_gb_wt_f_medal = cnt_no_medal(data_gb_wt_f)
    data_gb_sm_m_medal = cnt_no_medal(data_gb_sm_m)
    data_gb_sm_f_medal = cnt_no_medal(data_gb_sm_f)

    m_medal_summer = grp_yr_cnt(data_gb_sm_m_medal) #Group the data by Year
    m_medal_winter = grp_yr_cnt(data_gb_wt_m_medal)
    f_medal_summer = grp_yr_cnt(data_gb_sm_f_medal)
    f_medal_winter = grp_yr_cnt(data_gb_wt_f_medal)

    m_summer = cnt_no_olympian(data_gb_sm_m)#Count the number of olympian
    m_winter = cnt_no_olympian(data_gb_wt_m)
    f_summer = cnt_no_olympian(data_gb_sm_f)
    f_winter = cnt_no_olympian(data_gb_wt_f)

    #graph plotting
    #Take out only necessary column for the calculation
    a1 = m_medal_summer['Medal']
    a2 = m_medal_winter['Medal']
    b1 = f_medal_summer["Medal"]
    b2 = f_medal_winter["Medal"]

    z1 = data_gb_wt_m_sport
    z2 = data_gb_wt_f_sport 
    z3 = data_gb_sm_m_sport
    z4 = data_gb_sm_f_sport

    x = [[a1,b1],[a2,b2],[m_summer,f_summer],[m_winter,f_winter]]
    y = [[z1,z2],[z3,z4]]
    plt.figure(figsize = (12,16))
    plt.figure(1)
    graph_plot1(x)
    plt.figure(figsize = (12,16))
    plt.figure(2)
    graph_plot2(y)
    
    plt.show()



    
