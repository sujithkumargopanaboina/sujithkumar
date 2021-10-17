

import pandas as pd
import numpy as np



def creat_data():

    r = int(input("number of Rows:"))
    c = int(input("Number of Columns:"))
    hall = []
    for i in range(0, r):
        s = []
        for j in range(0, c):
            s.append('S')
        hall.append(s)
    df = pd.DataFrame(hall)
    df.index = np.arange(1, len(df) + 1)
    df.columns = np.arange(1, len(df.columns) + 1)
    return df

class b_ticket:

    def __init__(self,df,user_info):
        self.df=df
        self.user_info=user_info

        print("<------enter the details of the reservation------>")
        x=int(input("enetr the row:"))
        y=int(input("enetr the col:"))
        if df[x][y] == 'B':
            print("The seat is already reserved")
        else:
            k={}
            df[x][y]='B'
            name=input("please enetr your name:")
            age=int(input("Age:"))
            gender=input('Gender (M/F):')
            phone=int(input("Contact No:"))
            k['name']=name
            k['gender']=gender
            k['age']=age
            k['phone']=phone
            seat=x*10+y
            if ((len(df.columns) * len(df)) <= 60):
                cost= 10
            else:
                s = int((len(df)) / 2)
                la=int(seat/10)
                if s >= la:
                    cost =10
                else:
                    cost= 8
            k['cost']=cost
            user_info[seat]=k



class show_data:
    def __init__(self,user_info):
        self.user_info=user_info
        a=int(input("please enter the Row:"))
        b=int(input("please enter the Row:"))
        seat = a * 10 + b
        detail=user_info[seat]
        print("Name:",detail['name'])
        print("Gender:",detail['gender'])
        print('Age:',detail['age'])
        print('Phone No:',detail['phone'])
        print('Ticket Price:$', detail['cost'])


class sta:
    def __init__(self,df,user_info):
        self.df=df
        self.user_info=user_info
        sum = 0
        for k in user_info:
            a = user_info[k]
            s = a['cost']
            sum = sum + s

        print("Number of Purchased :")
        print("tickets",len(user_info.keys()))
        print("Percentage:",(len(user_info.keys())/(len(df)*len(df.columns))*100),'%')
        print("Current income:$",sum)


def total_income(df):
    if ((len(df.columns) * len(df)) <= 60):
        print('Total income:',((len(df.columns) * len(df))))
    else:
        s = int((len(df)) / 2)
        fir=(s*(len(df.columns)))*10
        sec=((len(df)-s)*(len(df.columns))*8)
        t=int(fir)+int(sec)
        print('Total income:$', t)



if __name__ == '__main__':
    user_info = {}
    df = creat_data()

    while True:
        print("\n\n<------------MENU------------>\n\n")
        print("1.Show the seats\n2.Buy a ticket\n3.Statistics\n4.Show booked Tickets User Info\n5.Exit\n")
        op = int(input("Please select:"))

        if 1 > op or op > 5:
            print("Please select proper option")
        elif op == 1:
            print(df)
        elif op == 2:
            b_ticket(df,user_info)
        elif op == 3:
            sta(df,user_info)
            total_income(df)
        elif op == 4:
            show_data(user_info)
        elif op == 5:
            exit()
    



