def condense_automated_overlays(original_data):
    condensed_dict = {}

    for item in original_data:
        for overlay_key, inner_dict in item.items():
            # Check if the inner dictionary is not empty
            if inner_dict:
                condensed_dict[overlay_key] = {}
                for key, value in inner_dict.items():
                    # Convert 'bounding_box' list to tuple
                    if 'bounding_box' in value:
                        value['bounding_box'] = tuple(value['bounding_box'])
                    condensed_dict[overlay_key][key] = value

    return condensed_dict

# Provided original list of dictionaries
original_data = [
    {
        "automated_overlays_T28": {}
    },
    {
        "automated_overlays_T24": {}
    },
    {
        "automated_overlays_T64": {}
    },
    {
        "automated_overlays_T44": {}
    },
    {
        "automated_overlays_T23": {
            "A1": {
                "bounding_box": [
                    1,
                    227,
                    293,
                    320
                ],
                "eid": "EID193",
                "name": "conv1"
            },
            "A2": {
                "bounding_box": [
                    3,
                    328,
                    290,
                    409
                ],
                "eid": "EID194",
                "name": "conv2"
            },
            "A3": {
                "bounding_box": [
                    10,
                    412,
                    288,
                    490
                ],
                "eid": "EID195",
                "name": "conv3"
            },
            "A4": {
                "bounding_box": [
                    5,
                    511,
                    287,
                    605
                ],
                "eid": "EID196",
                "name": "conv4"
            },
            "A5": {
                "bounding_box": [
                    5,
                    621,
                    291,
                    707
                ],
                "eid": "EID197",
                "name": "conv5"
            }
        }
    },
    {
        "automated_overlays_T63": {}
    },
    {
        "automated_overlays_T5": {}
    },
    {
        "automated_overlays_T8": {}
    },
    {
        "automated_overlays_T2": {}
    },
    {
        "automated_overlays_T22": {
            "A1": {
                "bounding_box": [
                    27,
                    160,
                    1250,
                    581
                ],
                "eid": "EID188",
                "name": "body"
            }
        }
    },
    {
        "automated_overlays_T4": {}
    },
    {
        "automated_overlays_T58": {}
    },
    {
        "automated_overlays_T47": {}
    },
    {
        "automated_overlays_T42": {}
    },
    {
        "automated_overlays_T27": {}
    },
    {
        "automated_overlays_T53": {}
    },
    {
        "automated_overlays_T36": {}
    },
    {
        "automated_overlays_T19": {
            "A1": {
                "bounding_box": [
                    429,
                    643,
                    998,
                    709
                ],
                "eid": "EID183",
                "name": "input"
            }
        }
    },
    {
        "automated_overlays_T30": {}
    },
    {
        "automated_overlays_T46": {}
    },
    {
        "automated_overlays_T17": {
            "A1": {
                "bounding_box": [
                    16,
                    104,
                    249,
                    177
                ],
                "eid": "EID139",
                "name": "chat1"
            },
            "A2": {
                "bounding_box": [
                    26,
                    213,
                    245,
                    292
                ],
                "eid": "EID140",
                "name": "chat2"
            },
            "A3": {
                "bounding_box": [
                    23,
                    335,
                    239,
                    395
                ],
                "eid": "EID141",
                "name": "chat3"
            },
            "A4": {
                "bounding_box": [
                    353,
                    89,
                    1261,
                    133
                ],
                "eid": "EID143",
                "name": "head"
            },
            "A5": {
                "bounding_box": [
                    345,
                    159,
                    1248,
                    532
                ],
                "eid": "EID145",
                "name": "body"
            }
        }
    },
    {
        "automated_overlays_T10": {
            "A1": {
                "bounding_box": [
                    1020,
                    147,
                    1244,
                    184
                ],
                "eid": "EID75",
                "name": "not1"
            },
            "A2": {
                "bounding_box": [
                    1018,
                    144,
                    1244,
                    189
                ],
                "eid": "EID78",
                "name": "not1"
            },
            "A3": {
                "bounding_box": [
                    1019,
                    216,
                    1242,
                    253
                ],
                "eid": "EID79",
                "name": "not2"
            },
            "A4": {
                "bounding_box": [
                    1020,
                    286,
                    1241,
                    318
                ],
                "eid": "EID80",
                "name": "not3"
            },
            "A5": {
                "bounding_box": [
                    554,
                    141,
                    978,
                    188
                ],
                "eid": "EID81",
                "name": "head"
            },
            "A6": {
                "bounding_box": [
                    556,
                    210,
                    978,
                    552
                ],
                "eid": "EID82",
                "name": "body"
            }
        }
    },
    {
        "automated_overlays_T14": {
            "A1": {
                "bounding_box": [
                    3,
                    124,
                    478,
                    215
                ],
                "eid": "EID103",
                "name": "name1"
            },
            "A2": {
                "bounding_box": [
                    491,
                    131,
                    652,
                    215
                ],
                "eid": "EID104",
                "name": "type1"
            },
            "A3": {
                "bounding_box": [
                    659,
                    127,
                    848,
                    212
                ],
                "eid": "EID105",
                "name": "size1"
            },
            "A4": {
                "bounding_box": [
                    859,
                    129,
                    1196,
                    216
                ],
                "eid": "EID106",
                "name": "date1"
            },
            "A5": {
                "bounding_box": [
                    4,
                    224,
                    475,
                    299
                ],
                "eid": "EID107",
                "name": "name2"
            },
            "A6": {
                "bounding_box": [
                    489,
                    225,
                    652,
                    304
                ],
                "eid": "EID108",
                "name": "type2"
            },
            "A7": {
                "bounding_box": [
                    660,
                    226,
                    850,
                    303
                ],
                "eid": "EID109",
                "name": "size2"
            },
            "A8": {
                "bounding_box": [
                    856,
                    223,
                    1196,
                    305
                ],
                "eid": "EID110",
                "name": "date2"
            },
            "A9": {
                "bounding_box": [
                    3,
                    311,
                    480,
                    398
                ],
                "eid": "EID111",
                "name": "name3"
            },
            "A10": {
                "bounding_box": [
                    490,
                    314,
                    651,
                    394
                ],
                "eid": "EID112",
                "name": "type3"
            },
            "A11": {
                "bounding_box": [
                    660,
                    311,
                    851,
                    396
                ],
                "eid": "EID113",
                "name": "size3"
            },
            "A12": {
                "bounding_box": [
                    862,
                    313,
                    1190,
                    398
                ],
                "eid": "EID114",
                "name": "date3"
            },
            "A13": {
                "bounding_box": [
                    5,
                    405,
                    478,
                    509
                ],
                "eid": "EID115",
                "name": "name4"
            },
            "A14": {
                "bounding_box": [
                    488,
                    405,
                    650,
                    508
                ],
                "eid": "EID116",
                "name": "type4"
            },
            "A15": {
                "bounding_box": [
                    659,
                    409,
                    848,
                    508
                ],
                "eid": "EID117",
                "name": "size4"
            },
            "A16": {
                "bounding_box": [
                    858,
                    406,
                    1193,
                    508
                ],
                "eid": "EID118",
                "name": "date4"
            },
            "A17": {
                "bounding_box": [
                    6,
                    516,
                    479,
                    604
                ],
                "eid": "EID119",
                "name": "name5"
            },
            "A18": {
                "bounding_box": [
                    487,
                    517,
                    652,
                    601
                ],
                "eid": "EID120",
                "name": "type5"
            },
            "A19": {
                "bounding_box": [
                    659,
                    520,
                    851,
                    601
                ],
                "eid": "EID121",
                "name": "size5"
            },
            "A20": {
                "bounding_box": [
                    858,
                    519,
                    1199,
                    603
                ],
                "eid": "EID122",
                "name": "date5"
            }
        }
    },
    {
        "automated_overlays_T49": {}
    },
    {
        "automated_overlays_T41": {}
    },
    {
        "automated_overlays_T34": {}
    },
    {
        "automated_overlays_T32": {}
    },
    {
        "automated_overlays_T48": {}
    },
    {
        "automated_overlays_T40": {}
    },
    {
        "automated_overlays_T11": {}
    },
    {
        "automated_overlays_T50": {}
    },
    {
        "automated_overlays_T3": {}
    },
    {
        "automated_overlays_T57": {}
    },
    {
        "automated_overlays_T9": {
            "A1": {
                "bounding_box": [
                    1016,
                    146,
                    1245,
                    184
                ],
                "eid": "EID71",
                "name": "not1"
            },
            "A2": {
                "bounding_box": [
                    1023,
                    215,
                    1240,
                    254
                ],
                "eid": "EID72",
                "name": "not2"
            },
            "A3": {
                "bounding_box": [
                    1022,
                    283,
                    1236,
                    321
                ],
                "eid": "EID73",
                "name": "not3"
            },
            "A4": {
                "bounding_box": [
                    1022,
                    356,
                    1242,
                    395
                ],
                "eid": "EID74",
                "name": "not4"
            }
        }
    },
    {
        "automated_overlays_T54": {}
    },
    {
        "automated_overlays_T37": {}
    },
    {
        "automated_overlays_T60": {}
    },
    {
        "automated_overlays_T18": {
            "A1": {
                "bounding_box": [
                    22,
                    440,
                    244,
                    515
                ],
                "eid": "EID142",
                "name": "chat4"
            },
            "A2": {
                "bounding_box": [
                    120,
                    203,
                    448,
                    291
                ],
                "eid": "EID154",
                "name": "contact1"
            },
            "A3": {
                "bounding_box": [
                    473,
                    205,
                    799,
                    293
                ],
                "eid": "EID155",
                "name": "contact2"
            },
            "A4": {
                "bounding_box": [
                    827,
                    205,
                    1153,
                    294
                ],
                "eid": "EID156",
                "name": "contact3"
            },
            "A5": {
                "bounding_box": [
                    121,
                    315,
                    447,
                    402
                ],
                "eid": "EID158",
                "name": "contact4"
            },
            "A6": {
                "bounding_box": [
                    471,
                    322,
                    796,
                    402
                ],
                "eid": "EID159",
                "name": "contact5"
            },
            "A7": {
                "bounding_box": [
                    825,
                    321,
                    1151,
                    408
                ],
                "eid": "EID160",
                "name": "contact6"
            },
            "A8": {
                "bounding_box": [
                    121,
                    432,
                    444,
                    522
                ],
                "eid": "EID161",
                "name": "contact7"
            },
            "A9": {
                "bounding_box": [
                    474,
                    435,
                    799,
                    518
                ],
                "eid": "EID162",
                "name": "contact7"
            },
            "A10": {
                "bounding_box": [
                    824,
                    438,
                    1154,
                    523
                ],
                "eid": "EID163",
                "name": "contact8"
            },
            "A11": {
                "bounding_box": [
                    122,
                    549,
                    444,
                    632
                ],
                "eid": "EID164",
                "name": "contact10"
            },
            "A12": {
                "bounding_box": [
                    472,
                    549,
                    803,
                    635
                ],
                "eid": "EID165",
                "name": "contact11"
            },
            "A13": {
                "bounding_box": [
                    826,
                    549,
                    1150,
                    630
                ],
                "eid": "EID166",
                "name": "contact12"
            },
            "A14": {
                "bounding_box": [
                    119,
                    547,
                    447,
                    638
                ],
                "eid": "EID167",
                "name": "contact10"
            },
            "A15": {
                "bounding_box": [
                    474,
                    553,
                    796,
                    635
                ],
                "eid": "EID168",
                "name": "contact11"
            },
            "A16": {
                "bounding_box": [
                    827,
                    551,
                    1148,
                    634
                ],
                "eid": "EID169",
                "name": "contact12"
            }
        }
    },
    {
        "automated_overlays_T43": {}
    },
    {
        "automated_overlays_T52": {}
    },
    {
        "automated_overlays_T29": {}
    },
    {
        "automated_overlays_T7": {}
    },
    {
        "automated_overlays_T6": {}
    },
    {
        "automated_overlays_T51": {}
    },
    {
        "automated_overlays_T20": {
            "A1": {
                "bounding_box": [
                    16,
                    104,
                    249,
                    177
                ],
                "eid": "EID186",
                "name": "chat1"
            },
            "A2": {
                "bounding_box": [
                    26,
                    213,
                    245,
                    292
                ],
                "eid": "EID187",
                "name": "chat2"
            },
            "A3": {
                "bounding_box": [
                    23,
                    335,
                    239,
                    395
                ],
                "eid": "EID188",
                "name": "chat3"
            },
            "A4": {
                "bounding_box": [
                    22,
                    440,
                    244,
                    515
                ],
                "eid": "EID189",
                "name": "chat4"
            },
            "A5": {
                "bounding_box": [
                    353,
                    89,
                    1261,
                    133
                ],
                "eid": "EID190",
                "name": "head"
            },
            "A6": {
                "bounding_box": [
                    345,
                    159,
                    1248,
                    532
                ],
                "eid": "EID191",
                "name": "body"
            }
        }
    },
    {
        "automated_overlays_T38": {}
    },
    {
        "automated_overlays_T35": {}
    },
    {
        "automated_overlays_T59": {}
    },
    {
        "automated_overlays_T33": {}
    },
    {
        "automated_overlays_T25": {}
    },
    {
        "automated_overlays_T45": {}
    },
    {
        "automated_overlays_T16": {
            "A1": {
                "bounding_box": [
                    18,
                    110,
                    239,
                    180
                ],
                "eid": "EID132",
                "name": "chat1"
            },
            "A2": {
                "bounding_box": [
                    25,
                    216,
                    237,
                    290
                ],
                "eid": "EID133",
                "name": "chat2"
            },
            "A3": {
                "bounding_box": [
                    20,
                    335,
                    246,
                    406
                ],
                "eid": "EID134",
                "name": "chat3"
            },
            "A4": {
                "bounding_box": [
                    22,
                    443,
                    240,
                    516
                ],
                "eid": "EID135",
                "name": "chat4"
            }
        }
    },
    {
        "automated_overlays_T13": {}
    },
    {
        "automated_overlays_T21": {
            "A1": {
                "bounding_box": [
                    22,
                    167,
                    1237,
                    657
                ],
                "eid": "EID185",
                "name": "rss"
            }
        }
    },
    {
        "automated_overlays_T26": {}
    },
    {
        "automated_overlays_T62": {}
    },
    {
        "automated_overlays_T12": {}
    },
    {
        "automated_overlays_T61": {}
    },
    {
        "automated_overlays_T15": {
            "A1": {
                "bounding_box": [
                    87,
                    145,
                    1195,
                    686
                ],
                "eid": "EID131",
                "name": "body"
            }
        }
    },
    {
        "automated_overlays_T39": {}
    },
    {
        "automated_overlays_T1": {}
    },
    {
        "automated_overlays_T56": {}
    },
    {
        "automated_overlays_T55": {}
    },
    {
        "automated_overlays_T31": {}
    }
]

# Perform the conversion
condensed_data = condense_automated_overlays(original_data)

# Print or use the condensed dictionary as needed
print(condensed_data)
