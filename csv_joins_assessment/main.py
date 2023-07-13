import pandas


#reading csv files
customer_data = pandas.read_csv("order.csv")
order_data = pandas.read_csv("customer.csv")

# combined = combined.merge()

#mergind two files
combined = customer_data.merge(order_data, how='outer')

#creating a csv file
combined.to_csv("combined_data.csv", index= False)

#Merging the maching records on two files
combined = customer_data.merge(order_data, how="inner")

#creating a csv file
combined.to_csv("combined_matching_data.csv", index= False)










































# combined.to_csv("combined_files.csv")
# print(glob.glob("Z:\My_python\csv_joins_assessment\f*.csv"))


#
# combined = combined._append(pandas.read_csv("order.csv"))

# files = os.listdir(
# for file in files:
#     if file.endswith(".csv"):
#         combined._append(customer_data)
