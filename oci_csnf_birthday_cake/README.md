# Oracle Cloud Infrastructure (OCI) CSNF Birthday Cake Sample Code
## Table of Contents
1. [Overview](#overview)
1. [Provider Mapping Spreadsheet](#provider_csv)
    1. [Sample Mapping](#sample_mapping)
    1. [Columns Descriptions](#columns_descriptions)
1. [Provider CSV to JSON Mapping Script](#mapping_script)
    1. [How to Execute](#script_how_to)
    1. [Sample JSON Output](#sample_json)
1. [OCI Birthday Cake Function](#oci_functions)
    1. [Architectures](#func_arch)
    1. [Sample JSON Output](#sample_json)


## <a name="overview"></a>Overview
The ONUG (Open Networking User Group) CSNF (Cloud Security Notification Framework) is a canonical model for mapping cloud security notification from Cloud Service Providers (CSP) and security vendor findings into a standard data model.  In this directory you will find the sample code from OCI that provides a spreadsheet for mapping CSP and security provider alerts to the ONUG CSNF, code to covert that spreadsheet into a JSON for programmatic use, and an OCI function that can convert mapped CSP events to ONUG CSNF then write them to an OCI Log for parsing.


## <a name="provider_csv"></a>Provider Mapping Spreadsheet
A spreadsheet(CSV) is a useful tool for mapping CSP or security provider alerts to the ONUG CSF format.  For ONUG CSNF Birthday Cake demo we created the below mapping of OCI, Azure, Aquasec, and AWS alerts into the ONUG CSNF. The CSV file representing the above mapping can be found here: [provider_input_file_sample.csv](./provider-csv-to-provider-json-script/provider_input_file_sample.csv).

### <a name="sample_mapping"></a> Sample Mapping
| Provider                    | Provider Type | Provider ID | Source      | alertId                 | CSNF Dictionary        | path                                                  | staticValue | entityType     |
| --------------------------- | ------------- | ----------- | ----------- | ----------------------- | ---------------------- | ----------------------------------------------------- | ----------- | -------------- |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | provider.accountId     | data.additionalDetails.tenantId                       |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | event.guid             | data.resourceId                                       |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | event.name             | data.additionalDetails.problemName                    |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | event.shortDescription | data.additionalDetails.problemDescription             |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | event.startTime        | data.additionalDetails.firstDetected                  |             | datetime       |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | event.severity         | data.additionalDetails.riskLevel                      |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | event.status           | data.additionalDetails.status                         |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | resource.identifier    | data.additionalDetails.resourceId                     |             | orclResourceId |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | resource.type          | data.additionalDetails.resourceType                   |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | resource.name          | data.additionalDetails.resourceName                   |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | resource.region        | data.additionalDetails.region                         |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | __default__             | resource.zone          | data.compartmentName                                  |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | BUCKET_IS_PUBLIC        | event.recommendation   | data.additionalDetails.problemRecommendation          |             | string         |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | SUSPICIOUS_IP_ACTIVITY  | event.geolocation.ipv4 | data.additionalDetails.impactedResourceId             |             |                |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | SUSPICIOUS_IP_ACTIVITY  | event.actor            | data.additionalDetails.resourceName                   |             |                |
| Oracle Cloud Infrastructure | CSP           | 1           | Cloud Guard | VCN_DHCP_OPTION_CHANGED | event.actor            | data.additionalDetails.resourceName                   |             |                |
| Azure                       | CSP           | 2           | Defender    | __default__             | provider.accountId     | properties.subscriptionId                             |             | string         |
| Azure                       | CSP           | 2           | Defender    | __default__             | event.guid             | id                                                    |             | string         |
| Azure                       | CSP           | 2           | Defender    | __default__             | event.name             | properties.alertName                                  |             | string         |
| Azure                       | CSP           | 2           | Defender    | __default__             | event.shortDescription | properties.alertDisplayName                           |             | string         |
| Azure                       | CSP           | 2           | Defender    | __default__             | event.longDescription  | properties.description                                |             | string         |
| Azure                       | CSP           | 2           | Defender    | __default__             | event.startTime        | properties.detectedTimeUtc                            |             | string         |
| Azure                       | CSP           | 2           | Defender    | __default__             | event.status           | properties.state                                      |             | string         |
| Azure                       | CSP           | 2           | Defender    | __default__             | resource.identifier    | properties.associatedResource                         |             | string         |
| Azure                       | CSP           | 2           | Defender    | __default__             | resource.type          | properties.extendedProperties.resourceType            |             | string         |
| Azure                       | CSP           | 2           | Defender    | __default__             | event.geolocation.ipv4 | properties.extendedProperties.client IP address       |             |                |
| Azure                       | CSP           | 2           | Defender    | __default__             | event.actor            | properties.extendedProperties.client principal name   |             |                |
| Azure                       | CSP           | 2           | Defender    | __default__             | event.severity         | properties.reportedSeverity                           |             |                |
| Aquasec                     | CSPM          | 3           | Aqua        | __default__             | event.name             | data.control                                          |             | string         |
| Aquasec                     | CSPM          | 3           | Aqua        | __default__             | event.guid             | id                                                    |             | string         |
| Aquasec                     | CSPM          | 3           | Aqua        | __default__             | event.shortDescription | data.reason                                           |             | string         |
| Aquasec                     | CSPM          | 3           | Aqua        | __default__             | event.startTime        | data.time                                             |             | string         |
| Aquasec                     | CSPM          | 3           | Aqua        | __default__             | event.severity         |                                                       | High        | string         |
| Aquasec                     | CSPM          | 3           | Aqua        | __default__             | resource.identifier    | containerid                                           |             | string         |
| Aquasec                     | CSPM          | 3           | Aqua        | __default__             | resource.type          | type                                                  |             | string         |
| Aquasec                     | CSPM          | 3           | Aqua        | __default__             | resource.name          | data.container                                        |             | string         |
| Aquasec                     | CSPM          | 3           | Aqua        | __default__             | resource.region        | data.vm_location                                      |             | string         |
| Amazon Web Services         | CSP           | 4           | GuardDuty   | __default__             | provider.accountId     | accountId                                             |             | string         |
| Amazon Web Services         | CSP           | 4           | GuardDuty   | __default__             | event.guid             | Arn                                                   |             | string         |
| Amazon Web Services         | CSP           | 4           | GuardDuty   | __default__             | provider.accountId     | AccountId                                             |             | string         |
| Amazon Web Services         | CSP           | 4           | GuardDuty   | __default__             | event.actor            | Resource.AccessKeyDetails.GeneratedFindingUserName    |             | string         |
| Amazon Web Services         | CSP           | 4           | GuardDuty   | __default__             | event.startTime        | CreatedAt                                             |             |                |
| Amazon Web Services         | CSP           | 4           | GuardDuty   | __default__             | resource.identifier    | Resource.AccessKeyDetails.GeneratedFindingPrincipalId |             |                |
| Amazon Web Services         | CSP           | 4           | GuardDuty   | __default__             | event.shortDescription | Description                                           |             |                |
| Amazon Web Services         | CSP           | 4           | GuardDuty   | __default__             | event.name             | Title                                                 |             |                |

### <a name="columns_descriptions"></a> Columns Descriptions
- **Provider** - the name of the company providing the record ex. Oracle Cloud Infrastructure, Azure, IBM, Amazon Web Services, etc. 
- **Provider Type** - the type company providing the record ex. CSP, CSPM, etc
- **Source** - the product name providing the record ex. Cloud Guard, Defender
- **Alert Id** - the unique identifier for a field in an alert.  
    - `__default__` is for fields that are same across alerts for a specific source. 
    - For alert specific fields you must use the unique identifier for the alert ex.  BUCKET_IS_PUBLIC 
        - *Demo code only supports OCI Cloud Guard specific alert fields*   
- **CSNF Dictionary** - the CSNF conical mapping in dot notated field ex. event.guid
- **Path** - the source dot notated location of the field in an alert ex:
    - OCI Cloud Guard: `data.resourceId`
    - Azure Defender:  `properties.subscriptionId`
    - AWS GuardDuty: `AccountId`
- **Static Value** - value override for current field. Example "High"
- **Entity Type** - data type of the field being mapped ex. datetime, string, integer 
    - *This feature is currently not used by the demo code*



## <a name="mapping_script"></a> Provider CSV to JSON Mapping Script
For the demo code to use the CSV alert mapping above we converted it to JSON. To make this a more repeatable process we created a Python script [onug_csnf_mapping_load.py](./provider-csv-to-provider-json-script/onug_csnf_mapping_load.py) that takes a CSV in the aforementioned CSV format and converts it into a JSON. Below is the sample mapping in JSON. The JSON file representing the above mapping can be found here: [output_file.json](./provider-csv-to-provider-json-script/output_file.json).
```
{
    "Oracle Cloud Infrastructure": {
        "provider": "Oracle Cloud Infrastructure",
        "providerType": "CSP",
        "providerId": "1",
        "source": {
            "Cloud Guard": {
                "sourceName": "Cloud Guard",
                "sourceId": "None",
                "alerts": {
                    "__default__": {
                        "alertMapping": {
                            "provider.accountId": {
                                "path": "data.additionalDetails.tenantId",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.guid": {
                                "path": "data.resourceId",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.name": {
                                "path": "data.additionalDetails.problemName",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.shortDescription": {
                                "path": "data.additionalDetails.problemDescription",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.startTime": {
                                "path": "data.additionalDetails.firstDetected",
                                "entityType": "datetime",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.severity": {
                                "path": "data.additionalDetails.riskLevel",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.status": {
                                "path": "data.additionalDetails.status",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.identifier": {
                                "path": "data.additionalDetails.resourceId",
                                "entityType": "orclResourceId",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.type": {
                                "path": "data.additionalDetails.resourceType",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.name": {
                                "path": "data.additionalDetails.resourceName",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.region": {
                                "path": "data.additionalDetails.region",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.zone": {
                                "path": "data.compartmentName",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            }
                        }
                    },
                    "BUCKET_IS_PUBLIC": {
                        "alertMapping": {
                            "event.recommendation": {
                                "path": "data.additionalDetails.problemRecommendation",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            }
                        }
                    },
                    "SUSPICIOUS_IP_ACTIVITY": {
                        "alertMapping": {
                            "event.geolocation.ipv4": {
                                "path": "data.additionalDetails.impactedResourceId",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.actor": {
                                "path": "data.additionalDetails.resourceName",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            }
                        }
                    },
                    "VCN_DHCP_OPTION_CHANGED": {
                        "alertMapping": {
                            "event.actor": {
                                "path": "data.additionalDetails.resourceName",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            }
                        }
                    }
                }
            }
        }
    },
    "Azure": {
        "provider": "Azure",
        "providerType": "CSP",
        "providerId": "2",
        "source": {
            "Defender": {
                "sourceName": "Defender",
                "sourceId": "None",
                "alerts": {
                    "__default__": {
                        "alertMapping": {
                            "provider.accountId": {
                                "path": "properties.subscriptionId",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.guid": {
                                "path": "id",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.name": {
                                "path": "properties.alertName",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.shortDescription": {
                                "path": "properties.alertDisplayName",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.longDescription": {
                                "path": "properties.description",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.startTime": {
                                "path": "properties.detectedTimeUtc",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.status": {
                                "path": "properties.state",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.identifier": {
                                "path": "properties.associatedResource",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.type": {
                                "path": "properties.extendedProperties.resourceType",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.geolocation.ipv4": {
                                "path": "properties.extendedProperties.client IP address",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.actor": {
                                "path": "properties.extendedProperties.client principal name",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.severity": {
                                "path": "properties.reportedSeverity",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            }
                        }
                    }
                }
            }
        }
    },
    "Aquasec": {
        "provider": "Aquasec",
        "providerType": "CSPM",
        "providerId": "3",
        "source": {
            "Aqua": {
                "sourceName": "Aqua",
                "sourceId": "None",
                "alerts": {
                    "__default__": {
                        "alertMapping": {
                            "event.name": {
                                "path": "data.control",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.guid": {
                                "path": "id",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.shortDescription": {
                                "path": "data.reason",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.startTime": {
                                "path": "data.time",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.severity": {
                                "path": "",
                                "entityType": "string",
                                "mappedValue": true,
                                "value": "High"
                            },
                            "resource.identifier": {
                                "path": "containerid",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.type": {
                                "path": "type",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.name": {
                                "path": "data.container",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.region": {
                                "path": "data.vm_location",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            }
                        }
                    }
                }
            }
        }
    },
    "Amazon Web Services": {
        "provider": "Amazon Web Services",
        "providerType": "CSP",
        "providerId": "4",
        "source": {
            "GuardDuty": {
                "sourceName": "GuardDuty",
                "sourceId": "None",
                "alerts": {
                    "__default__": {
                        "alertMapping": {
                            "provider.accountId": {
                                "path": "AccountId",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.guid": {
                                "path": "Arn",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.actor": {
                                "path": "Resource.AccessKeyDetails.GeneratedFindingUserName",
                                "entityType": "string",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.startTime": {
                                "path": "CreatedAt",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            },
                            "resource.identifier": {
                                "path": "Resource.AccessKeyDetails.GeneratedFindingPrincipalId",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.shortDescription": {
                                "path": "Description",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            },
                            "event.name": {
                                "path": "Title",
                                "entityType": "",
                                "mappedValue": false,
                                "value": ""
                            }
                        }
                    }
                }
            }
        }
    }
}
```



## <a name="oci_functions"></a>OCI Birthday Cake Demo Functions
In this 

## <a name="func_arch"></a>Architecture
