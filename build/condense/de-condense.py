interacted_overlays = {'T17': [{'bounding_box': (428, 637, 1000, 708), 'eid': 'EID1400', 'name': 'input'}], 'T19': [{'bounding_box': (445, 641, 1004, 711), 'eid': 'EID1800', 'name': 'input'}], 'interacted_overlays_T26': [{'bounding_box': (653, 449, 997, 494), 'eid': 'EID206', 'name': 'number'}], 'T22': [{'bounding_box': (33, 628, 981, 701), 'eid': 'EID189', 'name': 'input'}], 'T25': [{'bounding_box': (649, 352, 1015, 402), 'eid': 'EID202', 'name': 'user'}, {'bounding_box': (651, 421, 1014, 477), 'eid': 'EID203', 'name': 'pass'}]}

def expand_dict(variable_name, d):
    print(f"{variable_name} = {{")
    for key, value in d.items():
        print(f"    '{key}': [")
        for item in value:
            print("        {")
            for k, v in item.items():
                print(f"            '{k}': {v},")
            print("        },")
        print("    ],")
    print("}")

expand_dict("interacted_overlays", interacted_overlays)
