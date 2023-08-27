inventory.rename(columns = {'departure_station_code':'origin_station_code', 'arrival_station_code':'destination_station_code', 'scheduled_departure_dtl':'scheduled_departure_date'}, inplace = True)
preOrder.rename(columns = {'departure_station_code':'origin_station_code', 'arrival_station_code':'destination_station_code', 'scheduled_departure_dtl':'scheduled_departure_date'}, inplace = True)

df = pd.merge(satisfactionScore, inventory, on = ['flight_number', 'origin_station_code', 'destination_station_code', 'scheduled_departure_date'], how = 'left')
df = pd.merge(df, preOrder, on = ['flight_number', 'origin_station_code', 'destination_station_code', 'scheduled_departure_date', 'record_locator'], how = 'left')
# df = pd.merge(df, customerComments[['flight_number', 'origin_station_code', 'destination_station_code', 'scheduled_departure_date','verbatim_text']], on = ['flight_number', 'origin_station_code', 'destination_station_code', 'scheduled_departure_date'], how = 'left')

df.head()

# df.to_csv('final_merge.csv')