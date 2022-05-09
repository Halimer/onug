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
LOGGER.setLevel(level=logging.ERROR)
LOGGER.info("Inside Event Logging Function")

# while open
# oci_provider_file = open('../provider/oci.json')
# oci_provider_mapping = json.loads(oci_provider_file.read())

# oci_provider_file.close()

# while open
#file = '../../sample_data/oci_cg_public_bucket.json'
file = '../../sample_data/oci_cg_SUSPICIOUS_IP_ACTIVITY.json'
oci_cg_finding = open(file)


oci_cg_finding_json = json.loads(oci_cg_finding.read())
oci_cg_finding.close()


aqua_sec_file = '../../sample_data/aquasec_new.json'
aqua_sec_finding = open(aqua_sec_file)

aqua_sec_finding_json = json.loads(aqua_sec_finding.read())
aqua_sec_finding.close()

# print(aqua_sec_finding)

# msft_sec_file = '../../sample_data/defender_2.json'
# msft_sec_finding = open(msft_sec_file)

# msft_sec_finding_json = json.loads(msft_sec_finding.read())
# msft_sec_finding.close()

aws_gd_file = '../../sample_data/aws_gd_test.json'
aws_gd_finding = open(aws_gd_file)
aws_gd_finding_json = json.loads(aws_gd_finding.read())
aws_gd_finding.close()
print("#" * 30)
print(aws_gd_finding_json)
print("#" * 30)

# config = oci.config.from_file("~/.oci/config","CGDemo")
config = oci.config.from_file("~/.oci/config","Oracle")

print(config)
auth = Signer(
    tenancy=config['tenancy'],
    user=config['user'],
    fingerprint=config['fingerprint'],
    private_key_file_location=config['key_file'],
    pass_phrase=config['pass_phrase']
    )

url = 'https://objectstorage.us-ashburn-1.oraclecloud.com/n/orasenatdpltsecitom01/b/HammerPublic/o/output_file.json'
#url = 'https://objectstorage.us-ashburn-1.oraclecloud.com/n/orasenatdpltsecitom01/b/HammerPublic/o/aqua.json'
my_onug = onug(url,aws_gd_finding_json)
# my_onug = onug(url,oci_cg_finding_json)

print(my_onug.get_finding())
# log_ocid = 'ocid1.log.oc1.iad.amaaaaaatr7ig7aaox3ie3bz2vcbbuboayl544wkcvuxdz32mzpqi5qbrduq' # CGDemo
log_ocid = 'ocid1.log.oc1.iad.amaaaaaa24o7ldyaetp2uvhrraubii3vsoxg7obopzs5bph2jokouof34vta' # Security


# my_msft = onug(url, msft_sec_finding_json)
# print(my_msft.get_finding())


# payload = my_msft.get_finding()
# payload = my_aqua_sec.get_finding()
payload = my_onug.get_finding()
write_onug_to_log(auth,config,payload,log_ocid)
#write_event_to_log(auth,config, oci_cg_finding_json,log_ocid)
