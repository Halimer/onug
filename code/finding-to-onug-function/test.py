import io
import oci
import json
import logging
from datetime import datetime
from onug_decorator import onug
from write_to_oci_log import write_onug_to_log
from write_to_oci_log import write_event_to_log
from oci.signer import Signer

## to be moved 
LOGGER = logging.getLogger()
LOGGER.setLevel(level=logging.DEBUG)
LOGGER.info("Inside Event Logging Function")

# while open
# oci_provider_file = open('../provider/oci.json')
# oci_provider_mapping = json.loads(oci_provider_file.read())

# oci_provider_file.close()

# while open
#file = '../../sample_data/oci_cg_public_bucket.json'
file = '../../sample_data/oci_cg_vss.json'
oci_cg_finding = open(file)


oci_cg_finding_json = json.loads(oci_cg_finding.read())
oci_cg_finding.close()


aqua_sec_file = '../../sample_data/aquasec_new.json'
aqua_sec_finding = open(aqua_sec_file)

aqua_sec_finding_json = json.loads(aqua_sec_finding.read())
aqua_sec_finding.close()

# print(aqua_sec_finding)

msft_sec_file = '../../sample_data/defender_2.json'
msft_sec_finding = open(msft_sec_file)

msft_sec_finding_json = json.loads(msft_sec_finding.read())
msft_sec_finding.close()

config = oci.config.from_file("~/.oci/config","CGDemo")
print(config)
auth = Signer(
    tenancy=config['tenancy'],
    user=config['user'],
    fingerprint=config['fingerprint'],
    private_key_file_location=config['key_file'],
    pass_phrase=config['pass_phrase']
    )

url = 'https://objectstorage.us-ashburn-1.oraclecloud.com/n/orasenatdpltsecitom01/b/HammerPublic/o/file.json'
#url = 'https://objectstorage.us-ashburn-1.oraclecloud.com/n/orasenatdpltsecitom01/b/HammerPublic/o/aqua.json'
# my_onug = onug(url,oci_cg_finding_json)
# print(my_onug.get_finding())
log_ocid = 'ocid1.log.oc1.iad.amaaaaaatr7ig7aaox3ie3bz2vcbbuboayl544wkcvuxdz32mzpqi5qbrduq'
# print(type(oci_cg_finding_json))
# print(type(my_onug.get_finding()))
my_aqua_sec = onug(url, aqua_sec_finding_json,"Aquasec")
print(my_aqua_sec.get_finding())

# my_msft = onug(url, msft_sec_finding_json)
# print(my_msft.get_finding())


# payload = my_msft.get_finding()
#write_onug_to_log(auth,config, payload,log_ocid)
#write_event_to_log(auth,config, oci_cg_finding_json,log_ocid)
