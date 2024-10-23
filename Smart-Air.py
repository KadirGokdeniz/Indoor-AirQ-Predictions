import streamlit as st
import pandas as pd
import datetime
import altair as alt

st.title("Air-Smart Controller")
st.subheader("Air Quality")

rooms = ["Cloakroom", "Home Office", "Kitchen", "Living Room", "Secondary Bedroom",None]

rooms_dict ={"Cloakroom":"predictions0.csv",
             "Home Office":"predictions1.csv",
             "Kitchen":"predictions2.csv",
             "Living Room":"predictions3.csv",
             "Secondary Bedroom":"predictions4.csv"}

selected_room = st.selectbox(
    "Rooms:",
    rooms,
    index=5
)

def get_data(data_name):
    timestamp = pd.date_range(start ='2022-04-17 00:40:00',
                          end= "2022-06-01 00:00:00",
                          freq='10T')

    data = pd.read_csv(data_name)
    data = pd.DataFrame({'Timestamp': timestamp,
                        'Temperature (°C)': data.iloc[:, 0][144:],
                        'Realitive Humidity (%)':data.iloc[:, 1][144:],
                        "Air Pressure (Pa)":data.iloc[:, 2][144:]})

    data.set_index('Timestamp', inplace=True)
    data["AC Condition"] =["Stable" for i in range(len(data))]
    data["Humidifier Condition"] = ["Stable" for i in range(len(data))]
    data["Pressure Contoller Condition"] = ["Stable" for i in range(len(data))]

    for row in range(len(data)):
        if data['Temperature (°C)'][row] <=20:
            data["AC Condition"] [row]= "AC mode in <20°C"
        elif data['Temperature (°C)'][row] >= 26:
            data["AC Condition"][row] = "AC mode in >26°C"
        elif data['Realitive Humidity (%)'][row] <= 25:
            data["Humidifier Condition"][row] = "Humidifier mode in 25 %"
        elif data['Realitive Humidity (%)'][row] >= 45:
            data["Humidifier Condition"][row] = "Humidifier mode in 45 %"
        elif data["Air Pressure (Pa)"][row] <= 99000:
            data["Pressure Contoller Condition"][row] = "Pressure Contr. mode in < 99k"
        elif data["Air Pressure (Pa)"][row] >= 101000:
            data["Pressure Contoller Condition"][row] = "Pressure Contr. mode in > 101k"
    return data

def button_function():
    button_clicked = st.button("Save Data")

    if button_clicked:
        data.to_csv('data.csv', index=False)
        st.success("Data was saved!")

selected_item=None

if selected_room!=None:
    for key,value in rooms_dict.items():
        if selected_room == key:
            data = get_data(value)
    options = ["Temperature (°C)", "Realitive Humidity (%)", "Air Pressure (Pa)",None]

    selected_item = st.selectbox(
        "Type of data:",
        options,
        index=3
    )

if selected_item!= None:

    chart = alt.Chart(data.reset_index()).mark_line().encode(
            x='Timestamp:T',
            y=alt.Y(f'{selected_item}:Q', scale=alt.Scale(domain=[data[f'{selected_item}'].min(), data[f'{selected_item}'].max()]))
        ).properties(
            width=800,
            height=400
        )
    st.altair_chart(chart, use_container_width=True)

    selected_day = st.date_input("Select a date:", value=datetime.date(2022, 4, 17), min_value=datetime.date(2022, 4, 17), max_value=datetime.date(2022, 5, 29))

    selected_datetime = datetime.datetime.combine(selected_day, datetime.datetime.min.time())

    days_passed = (selected_datetime.date() - pd.to_datetime('2022-04-17').date()).days
    index_start = days_passed * (len(data)+3) // 45
    index_end = (days_passed + 1) * (len(data)+3) // 45 

    cases=[False,False,False]

    if selected_item == 'Temperature (°C)':
        st.write(data[['Temperature (°C)',"AC Condition"]][index_start:index_end])
        cases= [True,False,False]
    if selected_item == 'Realitive Humidity (%)':
        st.write(data[['Realitive Humidity (%)',"Humidifier Condition"]][index_start:index_end])
        cases= [False, True, False]
    if selected_item == "Air Pressure (Pa)":
        st.write(data[["Air Pressure (Pa)","Pressure Contoller Condition"]][index_start:index_end])
        cases= [False, False, True]

    choice = st.selectbox(
        "Select your choice:",
        ["Get Stable", "Shedule", None],
        index=2)

    interval_size = st.selectbox(
        "Select the interval size for manipulation:",
        ["Daily", "Hourly", "30 Minutes", "10 Minutes",None],
        index=4)
    start_time = index_start
    end_time = index_end

    from datetime import datetime, timedelta
    selected_datetime = datetime.combine(selected_datetime, datetime.min.time())
    selected_datetime = selected_datetime + timedelta(minutes=40)

    if interval_size =="Hourly":
        time_range = [(selected_datetime + timedelta(hours=hour)).time() for hour in range(24)]
        selected_hour = st.selectbox("Select starting hour:", options=time_range)
        start_time = index_start + selected_hour.hour*6
        end_time = start_time + 6

    if interval_size == "30 Minutes":

        time_range = [(selected_datetime + timedelta(minutes=30*minutes)).time() for minutes in range(48)]
        selected_30_minutes = st.selectbox("Select starting time:", options=time_range)

        if selected_30_minutes.minute ==40:
            start_time = index_start + selected_30_minutes.hour*6
        if selected_30_minutes.minute == 10:
            start_time = index_start + selected_30_minutes.hour*6 -3
        end_time = start_time + 3

    if interval_size == "10 Minutes":

        time_range = [(selected_datetime + timedelta(minutes=10*minutes)).time() for minutes in range(144)]
        selected_10_minutes = st.selectbox("Select starting time:", options=time_range)

        if selected_10_minutes.minute ==40:
            start_time = index_start + selected_10_minutes.hour*6        
        if selected_10_minutes.minute == 10:
            start_time = index_start + selected_10_minutes.hour*6 -3
        if selected_10_minutes.minute == 20:
            start_time = index_start + selected_10_minutes.hour*6 -2
        if selected_10_minutes.minute == 30:
            start_time = index_start + selected_10_minutes.hour*6 -1
        if selected_10_minutes.minute == 50:
            start_time = index_start + selected_10_minutes.hour*6 +1
        end_time = start_time + 1

    if cases[0] and choice=="Get Stable" and interval_size!=None:
        data["AC Condition"][start_time:end_time] = 'Stabled'
        st.write("Manipulated Data:",data[['Temperature (°C)',"AC Condition"]][index_start:index_end])
        button_function()
    if cases[1] and choice=="Get Stable" and interval_size!=None:
        data["Humidifier Condition"][start_time:end_time]= 'Stabled'
        st.write("Manipulated Data:",data[['Realitive Humidity (%)',"Humidifier Condition"]][index_start:index_end])
        button_function()
    if cases[2] and choice=="Get Stable" and interval_size!=None:
        data["Pressure Contoller Condition"][start_time:end_time]= 'Stabled'
        st.write("Manipulated Data:",data[["Air Pressure (Pa)","Pressure Contoller Condition"]][index_start:index_end])
        button_function()
    if cases[0] and choice=="Shedule" and interval_size!=None:
        data["AC Condition"][start_time:end_time] = 'Scheduled'
        st.write("Manipulated Data:",data[['Temperature (°C)',"AC Condition"]][index_start:index_end])
        button_function()
    if cases[1] and choice=="Shedule" and interval_size!=None:
        data["Humidifier Condition"][start_time:end_time]= 'Scheduled'
        st.write("Manipulated Data:",data[['Realitive Humidity (%)',"Humidifier Condition"]][index_start:index_end])
        button_function()
    if cases[2] and choice=="Shedule" and interval_size!=None:
        data["Pressure Contoller Condition"][start_time:end_time]= 'Scheduled'
        st.write("Manipulated Data:",data[["Air Pressure (Pa)","Pressure Contoller Condition"]][index_start:index_end])
        button_function()