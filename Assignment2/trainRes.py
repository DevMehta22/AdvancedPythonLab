import pandas as pd 

train_details = pd.read_csv("trains.csv")
passenger_details = pd.read_csv("passengers.csv")


def get_train_details(trainid):
    train_detail = train_details[train_details['Train ID'] == trainid]
    return train_detail

def get_passenger_details(passenger_name):
    passenger_detail = passenger_details[passenger_details['Passenger Name'] == passenger_name]
    return passenger_detail

def book_tickets(passenger_name,trainid):
    passenger_detail = get_passenger_details(passenger_name)
    train_detail = get_train_details(trainid)
    if passenger_detail.empty or train_detail.empty:
        return "Invalid passenger or train id"
    else:
        avail_seats  = train_detail['Available Seats'].values[0]
        num_tickets = passenger_detail['Number of Tickets'].values[0]
        if(avail_seats>=num_tickets):
            train_details.loc[train_details['Train ID'] == trainid,'Available Seats'] = avail_seats - num_tickets
            train_details.to_csv("trains.csv",index=False)
            fare = train_detail['Fare'].values[0]
            total_fare = num_tickets*fare
            passenger_details.loc[passenger_details['Passenger Name'] == passenger_name, 'Total Fare'] = total_fare
            passenger_details.to_csv("passengers.csv", index=False)
            return str(passenger_name)+"'s tickets booked successfully . Total fare is: "+str(total_fare)
        else:
            return "Not enough seats available"
        
def generate_report_1():
    report_1 = train_details[['Train ID', 'Train Name', 'Source Station', 'Destination Station', 'Available Seats']]
    report_1.to_csv("report_train_details.csv", index=False)
    print("Report 1 generated: report_train_details.csv")


def generate_report_2():
    revenue_report = train_details.copy()
    revenue_report['Revenue'] = revenue_report['Total Seats'] - revenue_report['Available Seats']
    revenue_report['Revenue'] *= revenue_report['Fare']
    report_2 = revenue_report[['Train ID', 'Train Name', 'Revenue']]
    report_2.to_csv("report_train_revenue.csv", index=False)
    print("Report 2 generated: report_train_revenue.csv")

for index, row in passenger_details.iterrows():
    print(book_tickets(row['Passenger Name'], row['Train ID']))


generate_report_1()
train_report = pd.read_csv("report_train_details.csv")
print(train_report)
generate_report_2()
revenue_report = pd.read_csv("report_train_revenue.csv")
print(revenue_report)            

    
    
    




