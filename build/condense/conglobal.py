
global_interactables = [
    {
        "global_interactables": {
            "T29": [
                {
                    "bounding_box": [
                        3,
                        73,
                        200,
                        101
                    ],
                    "eid": "EID213",
                    "associated_tid": "T29",
                    "name": "dashboard"
                },
                {
                    "bounding_box": [
                        4,
                        110,
                        196,
                        135
                    ],
                    "eid": "EID214",
                    "associated_tid": "T30",
                    "name": "calender"
                },
                {
                    "bounding_box": [
                        3,
                        137,
                        196,
                        161
                    ],
                    "eid": "EID217",
                    "associated_tid": "T37",
                    "name": "patients"
                },
                {
                    "bounding_box": [
                        4,
                        174,
                        194,
                        193
                    ],
                    "eid": "EID218",
                    "associated_tid": "T42",
                    "name": "reports"
                },
                {
                    "bounding_box": [
                        2,
                        206,
                        194,
                        228
                    ],
                    "eid": "EID219",
                    "associated_tid": "T43",
                    "name": "profile"
                },
                {
                    "bounding_box": [
                        2,
                        237,
                        196,
                        263
                    ],
                    "eid": "EID220",
                    "associated_tid": "T44",
                    "name": "workspace"
                },
                {
                    "bounding_box": [
                        4,
                        303,
                        196,
                        328
                    ],
                    "eid": "EID221",
                    "associated_tid": "T48",
                    "name": "inventory"
                },
                {
                    "bounding_box": [
                        5,
                        336,
                        198,
                        359
                    ],
                    "eid": "EID222",
                    "associated_tid": "T60",
                    "name": "lab"
                },
                {
                    "bounding_box": [
                        3,
                        370,
                        198,
                        396
                    ],
                    "eid": "EID223",
                    "associated_tid": "T63",
                    "name": "feedbacks"
                },
                {
                    "bounding_box": [
                        3,
                        402,
                        195,
                        425
                    ],
                    "eid": "EID224",
                    "associated_tid": "T64",
                    "name": "diagnostics"
                },
                {
                    "bounding_box": [
                        21,
                        748,
                        66,
                        789
                    ],
                    "eid": "EID225",
                    "associated_tid": "T8",
                    "name": "home"
                },
                {
                    "bounding_box": [
                        109,
                        758,
                        155,
                        793
                    ],
                    "eid": "EID226",
                    "associated_tid": "T13",
                    "name": "files"
                },
                {
                    "bounding_box": [
                        215,
                        757,
                        252,
                        792
                    ],
                    "eid": "EID227",
                    "associated_tid": "T24",
                    "name": "emr"
                },
                {
                    "bounding_box": [
                        293,
                        753,
                        337,
                        789
                    ],
                    "eid": "EID228",
                    "associated_tid": "T16",
                    "name": "messenger"
                },
                {
                    "bounding_box": [
                        388,
                        751,
                        440,
                        791
                    ],
                    "eid": "EID229",
                    "associated_tid": "T22",
                    "name": "gpt"
                }
            ]
        }
    }
]

condensed_global_interactables = {}

for item in global_interactables:
    for key, value in item["global_interactables"].items():
        condensed_global_interactables[key] = [
            {k: tuple(v) if k == 'bounding_box' else v for k, v in subitem.items()}
            for subitem in value
        ]

# Print or use the condensed dictionary as needed
print(condensed_global_interactables)
