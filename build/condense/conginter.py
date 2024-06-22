def condense_interacted_overlays(original_list):
    condensed_dict = {}

    for item in original_list:
        for overlay_key, overlay_list in item.items():
            if overlay_list:  # Check if the list is not empty
                condensed_dict.setdefault(overlay_key, [])

                for overlay_item in overlay_list:
                    # Convert 'bounding_box' list to tuple
                    if 'bounding_box' in overlay_item:
                        overlay_item['bounding_box'] = tuple(overlay_item['bounding_box'])

                    condensed_dict[overlay_key].append(overlay_item)

    return condensed_dict

# Your original list of dictionaries
original_interacted_overlays = [
    {
        "interacted_overlays_T4": []
    },
    {
        "interacted_overlays_T61": []
    },
    {
        "interacted_overlays_T8": []
    },
    {
        "interacted_overlays_T17": [
            {
                "bounding_box": [
                    428,
                    637,
                    1000,
                    708
                ],
                "eid": "EID1400",
                "name": "input"
            }
        ]
    },
    {
        "interacted_overlays_T33": []
    },
    {
        "interacted_overlays_T35": []
    },
    {
        "interacted_overlays_T42": []
    },
    {
        "interacted_overlays_T43": []
    },
    {
        "interacted_overlays_T2": []
    },
    {
        "interacted_overlays_T56": []
    },
    {
        "interacted_overlays_T16": []
    },
    {
        "interacted_overlays_T10": []
    },
    {
        "interacted_overlays_T51": []
    },
    {
        "interacted_overlays_T38": []
    },
    {
        "interacted_overlays_T15": []
    },
    {
        "interacted_overlays_T12": []
    },
    {
        "interacted_overlays_T30": []
    },
    {
        "interacted_overlays_T47": []
    },
    {
        "interacted_overlays_T5": []
    },
    {
        "interacted_overlays_T1": []
    },
    {
        "interacted_overlays_T14": []
    },
    {
        "interacted_overlays_T49": []
    },
    {
        "interacted_overlays_T32": []
    },
    {
        "interacted_overlays_T57": []
    },
    {
        "interacted_overlays_T64": []
    },
    {
        "interacted_overlays_T13": []
    },
    {
        "interacted_overlays_T29": []
    },
    {
        "interacted_overlays_T28": [
            {
                "bounding_box": [
                    574,
                    353,
                    718,
                    376
                ],
                "eid": "EID210",
                "name": "ver"
            }
        ]
    },
    {
        "interacted_overlays_T40": []
    },
    {
        "interacted_overlays_T27": [
            {
                "bounding_box": [
                    802,
                    385,
                    1120,
                    422
                ],
                "eid": "EID208",
                "name": "docname"
            }
        ]
    },
    {
        "interacted_overlays_T48": []
    },
    {
        "interacted_overlays_T21": []
    },
    {
        "interacted_overlays_T55": []
    },
    {
        "interacted_overlays_T20": [
            {
                "bounding_box": [
                    445,
                    641,
                    1004,
                    711
                ],
                "eid": "EID2000",
                "name": "input"
            }
        ]
    },
    {
        "interacted_overlays_T54": []
    },
    {
        "interacted_overlays_T6": []
    },
    {
        "interacted_overlays_T7": []
    },
    {
        "interacted_overlays_T52": []
    },
    {
        "interacted_overlays_T19": [
            {
                "bounding_box": [
                    445,
                    641,
                    1004,
                    711
                ],
                "eid": "EID1800",
                "name": "input"
            }
        ]
    },
    {
        "interacted_overlays_T39": []
    },
    {
        "interacted_overlays_T45": []
    },
    {
        "interacted_overlays_T58": []
    },
    {
        "interacted_overlays_T53": []
    },
    {
        "interacted_overlays_T9": []
    },
    {
        "interacted_overlays_T23": []
    },
    {
        "interacted_overlays_T18": []
    },
    {
        "interacted_overlays_T50": []
    },
    {
        "interacted_overlays_T34": []
    },
    {
        "interacted_overlays_T36": []
    },
    {
        "interacted_overlays_T62": []
    },
    {
        "interacted_overlays_T60": []
    },
    {
        "interacted_overlays_T26": [
            {
                "bounding_box": [
                    653,
                    449,
                    997,
                    494
                ],
                "eid": "EID206",
                "name": "number"
            }
        ]
    },
    {
        "interacted_overlays_T22": [
            {
                "bounding_box": [
                    33,
                    628,
                    981,
                    701
                ],
                "eid": "EID189",
                "name": "input"
            }
        ]
    },
    {
        "interacted_overlays_T31": []
    },
    {
        "interacted_overlays_T41": []
    },
    {
        "interacted_overlays_T59": []
    },
    {
        "interacted_overlays_T37": []
    },
    {
        "interacted_overlays_T46": []
    },
    {
        "interacted_overlays_T44": []
    },
    {
        "interacted_overlays_T3": []
    },
    {
        "interacted_overlays_T63": []
    },
    {
        "interacted_overlays_T25": [
            {
                "bounding_box": [
                    649,
                    352,
                    1015,
                    402
                ],
                "eid": "EID202",
                "name": "user"
            },
            {
                "bounding_box": [
                    651,
                    421,
                    1014,
                    477
                ],
                "eid": "EID203",
                "name": "pass"
            }
        ]
    },
    {
        "interacted_overlays_T11": []
    },
    {
        "interacted_overlays_T24": []
    }
]

# Perform the conversion
condensed_interacted_overlays = condense_interacted_overlays(original_interacted_overlays)

# Print or use the condensed dictionary as needed
print(condensed_interacted_overlays)
