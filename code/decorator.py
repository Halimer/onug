import logging
import json
from webbrowser import get


## to be moved 
LOGGER = logging.getLogger()
LOGGER.setLevel(level=logging.DEBUG)
LOGGER.info("Inside Event Logging Function")

# while open
oci_provider_file = open('../provider/oci.json')
oci_provider_mapping = json.loads(oci_provider_file.read())

oci_provider_file.close()

# while open
oci_cg_finding = open('../sample_data/oci_cg_public_bucket.json')
oci_cg_finding_json = json.loads(oci_cg_finding.read())
oci_cg_finding.close()

class onug: 
    
    __finding = {}
    __finding["provider"] = {}
    __finding["source"] = {}
    __finding["event"] = {}
    __finding["resource"] = {}

    def __init__(self,raw_finding):
        self.__raw_finding = raw_finding
        self.__set_provider_from_raw_finding()
        self.__set_provider_mapping_from_provider()
        self.__set_finding_provider_data()
        self.__set_data_source_mapping_from_provider()
        self.__set_data_mapping_from_raw_finding()
        self.__map_raw_finding_to_onug()
        return

    def __set_provider_from_raw_finding(self):
        # function needs support for multiple providers
        self.__provider = "Oracle CLoud Infrastructure"

    def __set_finding_provider_data(self):
        # function needs support for multiple providers
        oci_provider_file = open('../provider/oci.json')
        self.__provider_mapping = json.loads(oci_provider_file.read())
        self.__finding["provider"]["providerId"] = self.__oci_provider_mapping["providerId"]
        logging.debug("__set_provider_from_finding: ProviderId is set to: " + self.__finding["provider"]["providerId"]) 
        self.__finding["provider"]["providerType"] = self.__oci_provider_mapping["providerType"]
        logging.debug("__set_provider_from_finding: ProviderId is set to: " + self.__finding["provider"]["providerType"])
        self.__finding["provider"]["name"] = "Oracle CLoud Infrastructure"
        logging.debug("__set_provider_from_finding: Provider is set to: " + self.__finding["provider"]["name"])
        return

    def __set_provider_mapping_from_provider(self):
        if self.__provider == "Oracle CLoud Infrastructure":
            oci_provider_file = open('../provider/oci.json')
            logging.debug("__set_provider_mapping_from_provider")
            #print(json.loads(oci_provider_file.read()))
            self.__oci_provider_mapping = json.loads(oci_provider_file.read())
            oci_cg_finding.close()
        return

    def __set_data_source_mapping_from_provider(self):
        # function needs support of multiple providers    
        if self.__provider == "Oracle CLoud Infrastructure":
            try:
                if "cloudguard" in self.__raw_finding["data"]["resourceId"]:
                    self.__source = "OCI Cloud Guard"
                    logging.debug("__set_data_source_mapping_from_provider: Source Name is: " + self.__oci_provider_mapping["source"][self.__source]["sourceName"])
                    self.__finding["source"]["sourceName"] = self.__oci_provider_mapping["source"][self.__source]["sourceName"]
                    logging.debug("__set_data_source_mapping_from_provider: Source id is: " + self.__oci_provider_mapping["source"][self.__source]["sourceId"])
                    self.__finding["source"]["sourceId"] = self.__oci_provider_mapping["source"][self.__source]["sourceId"]

                    self.__source_mapping = self.__oci_provider_mapping["source"][self.__source]["alerts"]["__default__"]["alertMapping"]
                    logging.debug("__set_data_source_mapping_from_provider: Default Alerting Set ")


                    for alert_name in self.__oci_provider_mapping["source"][self.__source]["alerts"]:
                        if alert_name ==  self.__raw_finding["data"]["additionalDetails"]["problemName"]:
                            logging.debug("__set_data_source_mapping_from_provider: Found problem: " + alert_name)
                            for mapping in self.__oci_provider_mapping["source"][self.__source]["alerts"][alert_name]["alertMapping"]:
                                logging.debug("__set_data_source_mapping_from_provider: Adding alert mapping: " + mapping)
                                self.__source_mapping[mapping] = self.__oci_provider_mapping["source"][self.__source]["alerts"][alert_name]["alertMapping"][mapping]

            except:
                self.__source = "OCI Default"
                self.__source_mapping = "Default"


    def __set_data_mapping_from_raw_finding(self):
        # function needs support of multiple providers    
        if self.__provider == "Oracle CLoud Infrastructure":
            return

    def __mapped_item_from_path(self, path, finding):
        logging.debug("get_mapped_item_from_path: path is: " + str(path))
        tuple_path = tuple(path.split("."))
        for key in tuple_path:
            finding = finding[key]
        logging.debug("get_mapped_item_from_path: mapped_item is: " + str(finding))
        return finding

    def __set_item_from_path(self, path, item):
        # Cheating
        logging.debug("__set_item_from_path: path is: " + str(item))
        keys = path.split(".")
        self.__finding[keys[0]][keys[1]] = item

        

    def __map_raw_finding_to_onug(self):
        for element in self.__source_mapping:
            print(self.__source_mapping[element]["MappedValue"])
            if self.__source_mapping[element]["MappedValue"]:
                path = self.__source_mapping[element]["path"]
                logging.debug("map_to_onug: path is: " + str(path))
                #logging.debug("map_to_onug: finding is: " + str(finding))
                mapped_item = self.__mapped_item_from_path(path, self.__raw_finding)

                logging.debug(f'map_to_onug: {element} is mapped to {mapped_item} via path: {self.__source_mapping[element]["path"]}')
                self.__set_item_from_path(element, mapped_item)
            elif not(self.__source_mapping[element]["MappedValue"]):
                mapped_item = self.__source_mapping[element]["value"]
                logging.debug(f'Static map_to_onug: {element} is mapped to {mapped_item} via path: {self.__source_mapping[element]["path"]}')
                self.__set_item_from_path(element, mapped_item)



    def get_provider_data(self):
        return self.__finding["provider"]
    
    def get_finding(self):
        return self.__finding

my_onug = onug(oci_cg_finding_json)
print(my_onug.get_finding())



# def get_alert_provider(alert):
#     return "Oracle CLoud Infrastructure"

# def get_alert_source(alert_source):
#     if alert_source == "CloudGuardResponderEngine":
#         return "OCI Cloud Guard"
#     else:
#         return "Source not found"
 

# print(oci_cg_finding_json)

# def get_alert_mapping(source, alert_id):
#     try:
#         logging.debug("get_alert_mapping: OCI Provider type is: " + str(oci_provider_mapping["source"][source]["alerts"][alert_id]["alertMapping"]))
#         return oci_provider_mapping["source"][source]["alerts"][alert_id]["alertMapping"]
#     except:
#         logging.debug("get_alert_mapping: OCI Provider is the default: " + str(oci_provider_mapping["source"][source]["alerts"]["__default__"]["alertMapping"]))
#         return oci_provider_mapping["source"][source]["alerts"]["__default__"]["alertMapping"]
    

# def get_alert_id_from_finding(alert):
#     logging.debug("get_alert_id_from_finding: Alert ID is: " + str(alert["data"]["additionalDetails"]["problemName"]))
#     return alert["data"]["additionalDetails"]["problemName"]

# def get_mapped_item_from_path(path, finding):
#     logging.debug("get_mapped_item_from_path: path is: " + str(path))
#     tuple_path = tuple(path.split("."))
#     for key in tuple_path:
#         finding = finding[key]
#     logging.debug("get_mapped_item_from_path: mapped_item is: " + str(finding))
#     return finding

# def map_to_onug(alert_mapping, finding):
#     onug = {}
#     for element in alert_mapping:
#         # print(alert_mapping[element]["MappedValue"])
#         if alert_mapping[element]["MappedValue"]:
#             path = alert_mapping[element]["path"]
#             logging.debug("map_to_onug: path is: " + str(path))
#             #logging.debug("map_to_onug: finding is: " + str(finding))
#             mapped_item = get_mapped_item_from_path(path, finding)
#             logging.debug(f"map_to_onug: {element} is mapped to {mapped_item} via path: {alert_mapping[element]["path"]}")
#         elif not(alert_mapping[element]["MappedValue"]):

#     return onug

# provider = get_alert_provider(oci_cg_finding_json)
# source = get_alert_source(oci_cg_finding_json["source"])
# alert_id = get_alert_id_from_finding(oci_cg_finding_json)
# alert_mapping = get_alert_mapping(source, alert_id)


# # oci_cg_finding_json

# print(map_to_onug(alert_mapping, oci_cg_finding_json))


#     # json_map["path"]
#     # mapped_item = get_mapped_item_from_path(path, oci_cg_finding_json)
#     # print(f"{element} is mapped to {mapped_item} via path: {path}")


# def get_function_config(ctx):
#     config = dict(ctx.Config())
#     # Getting LOG_LEVEL from function config
#     try:
#         log_level = getattr(logging,config["LOG_LEVEL"].upper(),None)
#         if isinstance(log_level, int):
#             LOGGER.setLevel(level=log_level)
#         else:
#             LOGGER.warning("Invalid LOG_LEVEL in function configuration.")    
#     except KeyError:
#         LOGGER.warning("LOG_LEVEL not defined in function configuration.")
    
#     # Getting LOGGING_OCID from function config
#     global LOGGING_OCID
#     try:
#         LOGGER.info(config["LOGGING_OCID"])
#         LOGGING_OCID = config["LOGGING_OCID"]
#     except (Exception) as ex:
#         raise Exception("Event type LOGGING_OCID Required." + str(ex))

# def handler(ctx, data: io.BytesIO = None):

#     global LOGGER
#     LOGGER = logging.getLogger()
#     LOGGER.setLevel(level=logging.DEBUG)
#     LOGGER.info("Inside Event Logging Function")

#     # Getting function configuration
#     get_function_config(ctx)
    
#     # Getting Event Message
#     try:
#         body = json.loads(data.getvalue())
#     except (Exception) as ex:
#         raise Exception("Event type not properly formatted." + str(ex))

#     # Getting Resource principal 
#     signer = get_signer()
    
#     write_event_to_log(signer, body, LOGGING_OCID)
    
#     return response.Response(
#         ctx, response_data=json.dumps( {"message": "Wrote Event to Log" }), 
#         headers={"Content-Type": "application/json"})