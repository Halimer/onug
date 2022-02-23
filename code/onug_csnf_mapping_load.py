import csv
import json


all_providers = {}
hasHeader = True
with open("/Users/hammer/Documents/GitHub/onug/provider/oci1.csv") as f:
	csvreader = csv.reader(f)
	if hasHeader: next(csvreader) # Consume one line if a header exists
	
	# Iterate over the rows, and unpack each row into the variables
	for provider_name, provider_type, provider_id, source_name, alert_id_name, csnf_path, provider_path, static_value, entity_type in csvreader:
		# If the provider hasn't been processed yet, create a new dict for it
		if provider_name not in all_providers:
			all_providers[provider_name] = {
				"provider" : provider_name,
				"providerType" : provider_type,
				"providerId" : provider_id,
				"source" : {}}
		
		# Get the dict object that holds this provider's information
		provider = all_providers[provider_name]
		# If the tournament hasn't been processed already for this team, create a new dict for it in the team's dict
		if source_name not in provider["source"]:
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

#print(all_providers)
# Write to JSON File 
with open("/Users/hammer/Documents/GitHub/onug/provider/oci_output.json", "w") as outfile:
    json.dump(all_providers, outfile)
