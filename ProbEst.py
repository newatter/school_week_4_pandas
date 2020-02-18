import pandas as pd

print("Data 51100- Spring 2020")
print("Neil Watters")
print("2/16/2020")
print("Programming Assignment #4")
print('\n')

#create dataframe from data in file cars.csv
def get_data():
    #store csv data in dataframe data
    data = pd.read_csv('cars.csv')

    #df is a filter of data
    df = data[['make','aspiration']]

    return df

def print_make_prob(df):
    total = df['make'].count()

    #N is unique only to N not aspiration
    N = df['make'].value_counts().sort_index()

    #calculate probability
    prob = ((N/total)*100).round(decimals=2)

    #create dataframe for make name and probability
    prob_df = pd.DataFrame({'make_name' : df['make'].unique(),
                            'make_prob' : prob})

    #create lamda function to print out a line for each make and make probability
    print_prob_df = lambda x: print('Prob(make=' + x['make_name'] + ') = ', x['make_prob'], '%')

    #print lines
    prob_df.apply(print_prob_df, axis=1)

def print_make_asp_prob(df):
    #ceate 1D dataframe
    asp = df['aspiration'].unique()
    
    #for first instance, create make count filtered by aspiration index 0
    make_asp0 = df[df['aspiration']==asp[0]]['make'].value_counts().sort_index()
    
    #calculate totals for make, used in probability total
    total = df['make'].value_counts().sort_index()
    
    #probablity of make_aspiration value 0 
    prob0 = ((make_asp0/total)*100).round(decimals=2)
    
    #new dataframe created for make_aspiration 0
    prob_df0 = pd.DataFrame({'asp' : asp[0], 
                             'prob' : prob0}).fillna(0)
    
    #for second instance, create make count filtered by aspiration index 1
    make_asp1 = df[df['aspiration']==asp[1]]['make'].value_counts().sort_index()
    
    #probablity of make_aspiration value 1
    prob1 = ((make_asp1/total)*100).round(decimals=2)
    
    #new dataframe created for make_aspiration 1
    prob_df1 = pd.DataFrame({'asp' : asp[1], 
                             'prob' : prob1}).fillna(0)
    
    #concatenate prob_df0 and prob_df1 to ceate 1 sorted dataframe
    prob_df = pd.concat([prob_df0,prob_df1]).sort_index().reset_index()
    
    #print final dataframe
    print_prob_df = lambda x: print('Prob(aspiration=' + x['asp'] + '|make='+ x['index'] + ') = ', x['prob'], '%')
    prob_df.apply(print_prob_df, axis=1)

#run script
data = get_data()
print_make_asp_prob(data)
print('\n')
print_make_prob(data)