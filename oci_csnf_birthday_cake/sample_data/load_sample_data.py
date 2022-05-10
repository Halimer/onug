import requests
import json
from time import sleep
from random import randint, choice
from datetime import datetime

random_ips = [
    "67.236.8.153",
    "56.96.156.189",
    "140.205.235.34",
    "83.233.62.143",
    "35.160.36.212",
    "77.13.230.37",
    "200.29.146.203",
    "229.18.73.246",
    "93.22.155.126",
    "254.109.120.137",
    "39.167.118.216",
    "198.33.66.73",
    "76.73.194.212",
    "13.89.137.231",
    "202.138.104.247",
    "195.214.192.164",
    "96.148.219.8",
    "126.159.72.60",
    "233.177.130.251",
    "179.197.215.192",
    "199.12.106.87",
    "64.133.235.107",
    "97.49.143.48",
    "229.145.204.138",
    "118.7.192.241",
    "14.173.143.175",
    "129.163.232.200",
    "215.171.5.232",
    "33.245.130.132",
    "95.107.194.25",
    "24.193.160.152"
]

attacker_emails = [
    "alien@mars.planet",
    "martian@mars.planet",
    "phobos@venus.planet",
    "deimos@mars.planet",
    "josh.hammer@oracle.com"
]

now = datetime.utcnow()
now_str = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


def load_sample_request(url, payload): 
    headers = {'Content-Type': 'text/plain'}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def get_suspicious_ip(index):
    return random_ips[index]

url = "https://mva4gj5ehgfbx7afqlwbqt2rnu.apigateway.us-ashburn-1.oci.customer-oci.com/onug/decorate?Auth=karl"




## Loading MSFT Findings
for x in range(0,10):
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    
    msft_sec_file1 = '../sample_data/defender_1.json'
    msft_sec_finding1 = open(msft_sec_file1)
    msft_sec_finding_json1 = json.loads(msft_sec_finding1.read())
    msft_sec_finding1.close()

    msft_sec_finding_json1['id'] = msft_sec_finding_json1['id'].replace("2517538088322968242_7951468c-3909-4b52-a442-c1f4b92d5162", str(random_with_N_digits(56)))
    msft_sec_finding_json1['properties']['reportedSeverity'] = 'Medium'
    msft_sec_finding_json1['properties']['detectedTimeUtc'] = now_str
    msft_sec_finding_json1['properties']['extendedProperties']['client IP address'] = get_suspicious_ip(randint(0, 30))
    msft_sec_finding_json1['properties']['extendedProperties']['client principal name'] = attacker_emails[randint(0, 4)]

    sleep(3)

    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    msft_sec_file2 = '../sample_data/defender_2.json'
    msft_sec_finding2 = open(msft_sec_file2)
    msft_sec_finding_json2 = json.loads(msft_sec_finding2.read())
    msft_sec_finding2.close()

    msft_sec_finding_json2['id'] = msft_sec_finding_json2['id'].replace("2517538088322968242_7951468c-3909-4b52-a442-c1f4b92d5162", str(random_with_N_digits(56)))
    msft_sec_finding_json2['properties']['detectedTimeUtc'] = now_str
    msft_sec_finding_json2['properties']['extendedProperties']['client IP address'] = get_suspicious_ip(randint(0, 30))
    msft_sec_finding_json2['properties']['extendedProperties']['client principal name'] = attacker_emails[randint(0, 4)]

    sleep(random_with_N_digits(1))
    # print(msft_sec_finding_json2)
    # print(msft_sec_finding_json1)
    if choice([True, False]):
        sleep(random_with_N_digits(2))
        load_sample_request(url, json.dumps(msft_sec_finding_json1))
    if choice([True, False]):
        sleep(random_with_N_digits(2))
        load_sample_request(url, json.dumps(msft_sec_finding_json2))

## Loading OCI Data

    oci_file1 = '../sample_data/oci_cg_SUSPICIOUS_IP_ACTIVITY.json'
    oci_cg_finding1 = open(oci_file1)
    oci_cg_finding_json1 = json.loads(oci_cg_finding1.read())
    oci_cg_finding1.close()

    oci_file2 = '../sample_data/oci_cg_public_bucket.json'
    oci_cg_finding2 = open(oci_file2)
    oci_cg_finding_json2 = json.loads(oci_cg_finding2.read())
    oci_cg_finding2.close()

    oci_file3 = '../sample_data/oci_cg_public_bucket.json'
    oci_cg_finding3 = open(oci_file3)
    oci_cg_finding_json3 = json.loads(oci_cg_finding3.read())
    oci_cg_finding3.close()

    oci_file4 = '../sample_data/oci_cg_dhcp_option.json'
    oci_cg_finding4 = open(oci_file4)
    oci_cg_finding_json4 = json.loads(oci_cg_finding4.read())
    oci_cg_finding4.close()

    sleep(random_with_N_digits(1))
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    new_id1 = "ocid1.cloudguardproblem.oc1.iad." + str(random_with_N_digits(60))
    oci_cg_finding_json1['data']['resourceId'] = new_id1
    oci_cg_finding_json1['data']['additionalDetails']['firstDetected'] =  now_str
    oci_cg_finding_json1['data']['additionalDetails']['impactedResourceId'] = get_suspicious_ip(randint(0, 30))
    oci_cg_finding_json1['data']['additionalDetails']['resourceName'] = attacker_emails[randint(0, 4)]

    sleep(random_with_N_digits(1))
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    new_id2 = "ocid1.cloudguardproblem.oc1.iad." + str(random_with_N_digits(60))
    oci_cg_finding_json2['data']['resourceId'] = new_id2
    oci_cg_finding_json2['data']['additionalDetails']['firstDetected'] =  now_str

    sleep(random_with_N_digits(1))
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    new_id3 = "ocid1.cloudguardproblem.oc1.iad." + str(random_with_N_digits(60))
    oci_cg_finding_json3['data']['resourceId'] = new_id3
    oci_cg_finding_json3['data']['additionalDetails']['firstDetected'] =  now_str

    sleep(random_with_N_digits(1))
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    new_id4 = "ocid1.cloudguardproblem.oc1.iad." + str(random_with_N_digits(60))
    oci_cg_finding_json4['data']['resourceId'] = new_id4
    oci_cg_finding_json4['data']['additionalDetails']['firstDetected'] =  now_str
    oci_cg_finding_json4['data']['additionalDetails']['resourceName'] = attacker_emails[randint(0, 4)]


    # print(oci_cg_finding_json1)
    # print("--"* 30)
    # print(oci_cg_finding_json2)
    # print("--"* 30)
    # print(oci_cg_finding_json3) 

    if choice([True, False]):
        sleep(random_with_N_digits(2))
        load_sample_request(url, json.dumps(oci_cg_finding_json1))
    if choice([True, False]):
        sleep(random_with_N_digits(2))        
        load_sample_request(url, json.dumps(oci_cg_finding_json2))
    if choice([True, False]):
        sleep(random_with_N_digits(2))        
        load_sample_request(url, json.dumps(oci_cg_finding_json3))
    if choice([True, False]):
        sleep(random_with_N_digits(2))
        load_sample_request(url, json.dumps(oci_cg_finding_json4))
