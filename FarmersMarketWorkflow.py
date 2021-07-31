# @begin farmers_market_cleaning
# @in farmers_markets.csv
# @out farmers_market_all_cols.csv
# @out farmers_market_final.csv

# @begin csv_to_dataframe
# @in farmers_markets.csv
# @out fm_data
# @end csv_to_dataframe

# @begin drop_duplicates
# @in fm_data
# @out fm_data_no_duplicates
# @end drop_duplicates

# @begin columns
# @in fm_data_no_duplicates
# @out FMID
# @out MarketName
# @out SocialMediaColumns
# @out updateTime
# @out street
# @out city
# @out State
# @out zip
# @out x
# @out y
# @out Season1..4Date
# @out Season1..4Time
# @out PaymentColumns
# @out ProductColumns
# @end columns

# @begin to_datetime
# @in updateTime
# @in datetime
# @out updateTimeStamp
# @end to_datetime

# @begin get_year
# @in updateTimeStamp
# @out updateYear
# @end get_year

# @begin make_address
# @in street
# @in city
# @in State
# @in zip
# @out address
# @end make_address

# @begin address_to_coords
# @in geocoder
# @in address
# @out geolatitude
# @out geolongitude
# @end address_to_coords

# @begin final_coordinates
# @in x
# @in y
# @in geolatitude
# @in geolongitude
# @out latitude
# @out longitude
# @end final_coordinates

# @begin split_dates
# @in Season1..4Date
# @out Season1..4StartDateRough
# @out Season1..4EndDateRough
# @end split_dates

# @begin append_year
# @in Season1..4StartDateRough
# @out Season1..4StartDateRoughYear
# @end append_year

# @begin append_year
# @in Season1..4EndDateRough
# @in updateYear
# @out Season1..4EndDateRoughYear
# @end append_year

# @begin fix_start_date
# @in Season1..4StartDateRoughYear
# @in datetime.date
# @out Season1..4StartDate'
# @end fix_start_date

# @begin fix_end_date
# @in Season1..4EndDateRoughYear
# @in datetime.date
# @out Season1..4EndDate'
# @end fix_start_date

# @begin add_date_unknown
# @in Season1..4StartDate'
# @in Season1..4EndDate'
# @out Season1..4StartDate
# @out Season1..4EndDate
# @end add_unknown

# @begin split_days
# @in Season1..4Time
# @out Season1..4Sun..SatTime
# @end split_days

# @begin split_times
# @in Season1..4Sun..SatTime
# @out Season1..4Sun..SatStartTimeRough
# @out Season1..4Sun..SatEndTimeRough
# @end split_times

# @begin standardize_time
# @in Season1..4Sun..SatStartTimeRough
# @out Season1..4Sun..SatStartTime'
# @end standardize_time

# @begin standardize_time
# @in Season1..4Sun..SatEndTimeRough
# @out Season1..4Sun..SatEndTime'
# @end standardize_time

# @begin add_time_unknown
# @in Season1..4Sun..SatStartTime'
# @in Season1..4Sun..SatEndTime'
# @out Season1..4Sun..SatStartTime
# @out Season1..4Sun..SatEndTime
# @end add_unknown

# @begin make_payment_list
# @in PaymentColumns
# @out PaymentList
# @end make_payment_list

# @begin make_product_list
# @in ProductColumns
# @out ProductList
# @end make_product_list

# @begin dataframe
# @in FMID
# @in MarketName
# @in SocialMediaColumns
# @in updateTimeStamp
# @in address
# @in latitude
# @in longitude
# @in Season1..4StartDate
# @in Season1..4EndDate
# @in Season1..4Sun..SatStartTime
# @in Season1..4Sun..SatEndTime
# @in PaymentList
# @in ProductList
# @out fm_data_final
# @end dataframe

# @begin dataframe_to_csv
# @in fm_data_final
# @out farmers_market_final.csv
# @end dataframe_to_csv

# @end farmers_marketcleaning
