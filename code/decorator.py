import json

# while open
oci_provider_file = open('../provider/oci.json')

oci_provider_mapping = json.load(oci_provider_file)

oci_provider_file.close()

# while open
oci_cg_finding = open('../sample_data/oci_cg_public_bucket.json')

oci_cg_finding_json = json.load(oci_cg_finding)
oci_cg_finding.close()

alert_mapping =  oci_provider_mapping["source"]["alerts"]["alertMapping"]


def get_mapped_item_from_path(path, finding):
    tuple_path = tuple(path.split("."))
    mapped_item = finding
    for key in tuple_path:
        mapped_item = mapped_item[key]

    return mapped_item


for element in alert_mapping:
    path = alert_mapping[element]["path"]
    mapped_item = get_mapped_item_from_path(path, oci_cg_finding_json)
    print(f"{element} is mapped to {mapped_item} via path: {path}")
