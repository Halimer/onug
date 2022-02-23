import csv
from curses import raw
import json

data = {}


# # Function to convert a CSV to JSON
# # Takes the file paths as arguments
# def make_json(csvFilePath, jsonFilePath):
	
# 	# create a dictionary
# 	data = {}
# 	raw_data = []
# 	# Open a csv reader called DictReader
# 	with open(csvFilePath, encoding='utf-8') as csvf:
# 		csvReader = csv.DictReader(csvf)
		


# 		# Convert each row into a dictionary
# 		# and add it to data
# 		i = 0
# 		for row in csvReader:
# 			raw_data.append(row)
			
# 	# Open a json writer, and use the json.dumps()
# 	# function to dump data
# 	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
# 		jsonf.write(json.dumps(data, indent=4))

# 	print(raw_data)

# 	test = build_tree(raw_data)
# 	print(test)
# 	# current_row = raw_data[0]
# 	# providers = {}
# 	# for row in raw_data:
# 	# 	providers[row["Provider"]] = row["Provider"]
# 	# 	providers["provider"] = row["Provider"]
# 	# 	providers["providerType"] = row['Provider Type']


		

# def build_tree(tree_list):
#     if tree_list:
#         return {tree_list[0]: build_tree(tree_list[1:])}
#     return {}		


# # Driver Code

# # Decide the two file paths according to your
# # computer system
# csvFilePath = r'/Users/hammer/Documents/GitHub/onug/provider/oci1.csv'
# jsonFilePath = r'/Users/hammer/Documents/GitHub/onug/provider/providers.json'

# # Call the make_json function
# make_json(csvFilePath, jsonFilePath)


all_providers = {}
hasHeader = True
with open("/Users/hammer/Documents/GitHub/onug/provider/oci1.csv") as f:
	csvreader = csv.reader(f)
	if hasHeader: next(csvreader) # Consume one line if a header exists
	
	# Iterate over the rows, and unpack each row into three variables
	for provider_name, provider_type, source_name, alert_id_name, csnf_path, provider_path, static_value, entity_type in csvreader:
		# If the provider hasn't been processed yet, create a new dict for it
		if provider_name not in all_providers:
			all_providers[provider_name] = {
				"provider" : provider_name,
				"providerType" : provider_type,
				"providerId" : 1,
				"source" : {}}
		
		# Get the dict object that holds this provider's information
		provider = all_providers[provider_name]
		# If the tournament hasn't been processed already for this team, create a new dict for it in the team's dict
		if source_name not in provider:
			provider["source"][source_name] = { "sourceName" : source_name, "sourceId" : None, "alerts": {}}

		if alert_id_name not in provider["source"][source_name]["alerts"]:
			provider["source"][source_name]["alerts"][alert_id_name] = {"alertMapping" : {}}

		alert_mapping = provider["source"][source_name]["alerts"][alert_id_name]["alertMapping"]
		alert_mapping[csnf_path] = {
			"path" : provider_path,
			"entityType" : entity_type,
			"mappedValue" : True if static_value else False,
			"value" : static_value
		}



with open("/Users/hammer/Documents/GitHub/onug/provider/oci_output.json", "w") as outfile:
    json.dump(all_providers, outfile)
