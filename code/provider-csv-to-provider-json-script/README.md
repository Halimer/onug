# Provider Mapping 
## Overview
The ONUG (Open Networking User Group) CSNF (Cloud Security Notification Framework) is a canonical model for mapping cloud security notification from Cloud Service Providers (CSP) and security vendor findings into a standard data model.  The CSV [provider_inpuf_file_sample.csv](provider_inpuf_file_sample.csv) representing a mapping of Oracle Cloud Infrastructure [Cloud Guard](https://docs.oracle.com/en-us/iaas/cloud-guard/using/cg-concepts.htm) problems to CSNF canonical model.  The python code [onug_csnf_mapping_load.py](onug_csnf_mapping_load.py) takes a CSV in the aforementioned CSV format and converts into a JSON file to be consumed programmatically.  

### CSV Columns Descriptions
- **Provider** - the name of the company providing the record ex. Oracle Cloud Infrastructure, Azure, IBM, Amazon Web Services, etc. 
- **Provider Type** - the type company providing the record ex. CSP, CSPM, etc
- **Source** - the product name providing the record ex. Cloud Guard, Defender
- **Alert Id** - the unique identifier of the alert.  `__default__` is for 
- CSNF Dictionary - event.guid
- Path - data.resourceId
- Static Value
- Entity type - string, datetime 