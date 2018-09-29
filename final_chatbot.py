


import csv
import pandas 
import re
import spacy
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame as df
from scipy.stats import trim_mean, kurtosis
from scipy.stats.mstats import mode, gmean, hmean



data=pandas.read_csv('C:\\Users\\1385\\Desktop\\context_table_aegis (1).csv',sep=",")

#removal of html tags
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

#removal of questions
def stripQuestions(data):
    p = re.compile(r'[^<>,\.?!/d]*(?:Questions)[^<>\.?!]*\?')
    return p.sub(" ",data)


def Questions(data):
    result=re.findall(r'[^<>,\.?!/d]*(?:Questions)[^<>\.?!]*\?',data)
    return (result)



def stripAnswers(data):
    p = re.compile(r'[^<>,\.?!/d]*(?:Answers)[^<>\.?!]*\?')
    return p.sub(data)

#removal of answers
def Answers(data):
    p=re.compile(r'[^<>,!/d]*(Answers)[^<>\?!]*\\Questions')
    return re.sub(p,'',data)

#cleaning the data using this function
def Bapcleaning(data):
    #striphtml(Answers(x))
    y = [value for value in stripQuestions(striphtml(Answers(x))).split('",')]
    j=[]
    for i in range(1,len(y),2):
        cleanstring=re.sub('\Wn',' ',y[i])[1:].strip('"Answer[]:')
        j.append(cleanstring)
    return(j)

#removing punctuations
def removingpunctutions(data):
    s=re.sub(r'[^\w\s?]','',data)
    return(s)

#turning the text into lower cases
def cleaning_text(text):
    text=text.lower()
    text=re.sub(r"faq"," ",text)
    text=re.sub(r"category"," ",text)
    text=re.sub(r"account"," ",text)
    text = re.sub(r"answers","  ",text)
    text = re.sub(r"type","  ",text)
    return(text)

#grammatical cleaning :
def grammer(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    return(text)


#replacing FAQ uptill answer in the response:
def delete(text):
    text = re.sub(r"FAQ" ,"  ",text)
    text = re.sub(r"Category" ,"  ",text)
    text = re.sub(r"Account" ,"  ",text)
    text = re.sub(r"Answers" ,"  ",text)
    text = re.sub(r"   type FAQ", "  ",text)
    text = re.sub(r"answers","  ",text)
    return(text)



data.head()
x=data["response"].count()
y=data["context"]

#plt.plot(x, y, linewidth=2.0)


#getting data1 as the output with FAQ as reponsetype
dataframe=data

data1=dataframe.loc[dataframe["response_type"]=="FAQs"]
account=data1.loc[data1["context"]=="account"]
data3=account

new_index=[range(1,len(data))]
data1=data["response"]
#reindexing the dataframe:
data1 = data1.reset_index(drop=True)


#making accounts as a intent dataframe
accounts=pandas.DataFrame()
myset=set(data["context"])
data["context"]


#making a dataframe as a intent for slow 
slow=data.loc[data["context"]=="slow"]
slow

#making a dataframe as a intent for broadband
broadband=data.loc[data["context"]=="broadband"]
broadband

#making a dataframe as a intent for ping issue
ping_issue=data.loc[data["context"]=="ping issue"]
ping_issue

#making a dataframe as a intent for ping issue
network=data.loc[data["context"]=="network"]
network



account



slow




data1=dataframe.loc[dataframe["response_type"]=="FAQs"]
data1 = data1.reset_index(drop=True)
data2=data1["response"]




#extracting all the questions:
Questions=[]
for i in range(0,len(data2)):
    result=re.findall(r'[^<>,\.?!/d]*(?:Questions)[^<>\.?!]*\?',str(data2[i]))
    result=str(result)
    #t=striphtml(y)
    r=removingpunctutions(result)
    t=r.split("Questions")
    Questions.append(t)



Questions[1][1]



for j in range(0,len(Questions)):
    for i in range(0,len(Questions[j])):
        Quest=print((Questions[j][i]).strip( ))
    


input1=[]

for j in range(0,len(Questions)):
    for i in range(0,len(Questions[j])):
        input1.append(Questions[j][i].strip( ))
        



input1



#all the answers from the reponse cleaning and appending to reesponse list
response=[]
for i in range(0,len(data2)):
    x=data2[i]
    #print(x)
    y=stripQuestions(x)
    #print(y)
    t=striphtml(y)
    r=removingpunctutions((t))
    response.append(r)



final_response=[]
for i in range(0,len(data2)):
    final_response.append(response[i].split("Answers"))




output=[]

for j in range(0,len(final_response)):
    for i in range(0,len(final_response[j])):
        output.append(final_response[j][i].strip( ))
        



dic=[]
for i in range(1,len(input1)):
    dic.append(input1[i])
    dic.append(output[i])
    



import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

supersecretdata = output

for i,e in enumerate(supersecretdata):
    sheet1.write(i,1,e)

name = "Answers.xls"
book.save(name)
book.save(TemporaryFile())



string=dic
string



from chatterbot import ChatBot
chatbot = ChatBot('Norman')
from chatterbot.trainers import ListTrainer
conversation=string[1:1000]
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
        



def conv(data):
    #from chatterbot import ChatBot
    #chatbot = ChatBot('Norman')
    #from chatterbot.trainers import ListTrainer
    #conversation=string[1:100]
    #chatbot.set_trainer(ListTrainer)
    #chatbot.train(conversation)
    response = chatbot.get_response(data)
    return(response)



def anyother(data):
            x=conv(data)
            return(x)
    

mobile_no=["9595","9898"]
while True:
    print("Hi!My name is travis")
    mob=input("what is your mob no.").strip()
    if mob in mobile_no:
        print("Identified {}!".format(mob))
        Q=input("Do u have any questions regarding the ion (y/n)?:").lower().strip()
        if Q=="y":
            Question=input('what the questions').strip()
            print("searching answers....")
            x=conv(Question)
            print(x)
            while True:
                Continue=input("Do you have any other Questions please input yes or no?").strip().lower()
                if Continue=="yes":
                    Quest=input("what is the next Question pls").strip()
                    x=conv(Quest)
                    print(x)
                else:
                    print("it was nice chatting with you")
                    break 
        else:
            print("thank you very much ! I hope i have been of some assistance to you")
    else:
        print("Sorry you need to register")      

print(known_users)
        elif remove=="n":
            print("No problem I didnt want to leave you anyway!")
            print(known_users)
    else:
        print("Hmmm I have not met you yet{}".format(name))
        add_me=input("would you like to be added to the system y/n ").lower().strip()
        if add_me=="y":
            print(known_users)
            known_users.append(name)
            print(known_users)

