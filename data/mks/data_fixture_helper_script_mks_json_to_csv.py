__author__ = 'yotam'

import json
import csv
from pprint import pprint

json_file = open('data_fixture_mks.json', mode='r')
json_data = json.load(json_file, encoding='utf-8')  # insert name of json
knesset_dict = [x for x in json_data if x['model'] == 'mks.knesset']
party_dict = [x for x in json_data if x['model'] == 'mks.party']
partyaltname_dict = [x for x in json_data if x['model'] == 'mks.partyaltname']
member_dict = [x for x in json_data if x['model'] == 'mks.member']
coalitionmembership_dict = [x for x in json_data if x['model'] == 'mks.coalitionmembership']
membership_dict = [x for x in json_data if x['model'] == 'mks.membership']
weeklypresence_dict = [x for x in json_data if x['model'] == 'mks.weeklypresence']
memberaltname_dict = [x for x in json_data if x['model'] == 'mks.memberaltname']

all_dicts = [knesset_dict,
             party_dict,
             member_dict,
             coalitionmembership_dict,
             membership_dict,
             weeklypresence_dict,
             partyaltname_dict,
             memberaltname_dict,
]


def insert_to_csv(chosen_dict):
    field_names = chosen_dict[0].keys()[:-1]
    for field in chosen_dict[0]['fields'].keys():
        field_names.append(field)
    print field_names
    flat_dict_list = []
    for dict_object in chosen_dict:
        flat_dict = {}
        for key in dict_object.keys()[:-1]:
            if type(dict_object[key]) == str:
                flat_dict[key] = dict_object[key]
            elif type(dict_object[key]) == list:
                flat_dict[key] = str(dict_object[key])
            else:
                flat_dict[key] = dict_object[key]
        for key in dict_object['fields'].keys():
            if type(dict_object['fields'][key]) == str:
                flat_dict[key] = dict_object['fields'][key]
            else:
                flat_dict[key] = dict_object['fields'][key]
        flat_dict_list.append(flat_dict)
    pprint(flat_dict_list)

    file_name = 'data_from_json_%s.csv' % chosen_dict[0]['model']
    output_file = open(file_name, mode='wb')
    csv_data = csv.DictWriter(output_file, field_names)
    headers = {field_name: field_name for field_name in field_names}
    csv_data.writerow(headers)
    for flat_dict in flat_dict_list:
        print flat_dict
        csv_data.writerow({k: unicode(v).encode('utf-8') for k, v in flat_dict.items()})
    output_file.close()


for i, json_dict in enumerate(all_dicts):
    print 'dict num', i + 1
    insert_to_csv(json_dict)

len_of_dics = [
    len(knesset_dict),
    len(party_dict),
    len(partyaltname_dict),
    len(member_dict),
    len(membership_dict),
    len(coalitionmembership_dict),
    len(weeklypresence_dict),
    len(memberaltname_dict),
]

print len_of_dics

