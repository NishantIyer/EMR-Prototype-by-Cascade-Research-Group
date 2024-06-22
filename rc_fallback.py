import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from PIL import Image  
import requests
import json
import tkinter.font as tkFont


scaling_factor = 0.9
template_files = {
    "T1": "T1-land.png",
    "T2": "T2-user.png",
    "T3": "T3-userlogin.png",
    "T4": "T4-auth.png",
    "T5": "T5-sec.png",
    "T6": "T6-boot.png",
    "T7": "T7-root.png",
    "T8": "T8-desktop.png",
    "T9": "T9-notif.png",
    "T10": "T10-deepnotif.png",
    "T11": "T11-menu.png",
    "T12": "T12-others.png",
    "T13": "T13-files.png",
    "T14": "T14-specific.png",
    "T15": "T15-speclink.png",
    "T16": "T16-messenger.png",  
    "T17": "T17-specific.png",
    "T18": "T18-contacts.png",
    "T19": "T19-groups.png",
    "T20": "T20-ops.png",  
    "T21": "T21-rss.png",
    "T22": "T22-gpt.png",
    "T23": "T23-history.png",
    "T24": "T24-home.png",
    "T25": "T25-login.png",
    "T26": "T26-login.png",
    "T27": "T27-create.png",
    "T28": "T28-verif.png",
    "T29": "T29-emrhome.png",
    "T30": "T30-alarm.png",
    "T31": "T31-menu.png",
    "T32": "T32-calender.png",
    "T33": "T33-createappointments.png",
    "T34": "T34-invitedpatients.png",
    "T35": "T35-invitepatient.png",
    "T36": "T36-editappointment.png",
    "T37": "T37-patients.png",
    "T38": "T38-addpatient.png",
    "T39": "T39-specific.png",
    "T40": "T40-expandedspecific.png",
    "T41": "T41-visitcard.png",
    "T42": "T42-financereport.png",
    "T43": "T43-profile.png",
    "T44": "T44-cc.png",
    "T45": "T45wkspace.png",
    "T46": "T46-digitalhpi.png",
    "T47": "T47-createtemplate.png",
    "T48": "T48-inventory.png",
    "T49": "T49-masters.png",
    "T50": "T50-company.png",
    "T51": "T51-producttype.png",
    "T52": "T52-unitmaster.png",
    "T53": "T53-productmasters.png",
    "T54": "T54-billing.png",
    "T55": "T55-inward.png",
    "T56": "T56-purchaseorder.png",
    "T57": "T57-salesrequest.png",
    "T58": "T58-roi.png",
    "T59": "T59-requests.png",
    "T60": "T60-labs.png",
    "T61": "T61-labspecific.png",
    "T62": "T62-test.png",
    "T63": "T63-feedback.png",
    "T64": "T64-diagnostics.png",
}
# this is extremely
global_interactables = {
    'T8': [
        {
            'bounding_box': (58, 535, 176, 654),
            'eid': EID44,
            'associated_tid': T24,
            'name': emr,
        },
        {
            'bounding_box': (5, 737, 85, 796),
            'eid': EID45,
            'associated_tid': T11,
            'name': lubera,
        },
        {
            'bounding_box': (121, 762, 162, 798),
            'eid': EID46,
            'associated_tid': T13,
            'name': files,
        },
        {
            'bounding_box': (225, 763, 266, 800),
            'eid': EID47,
            'associated_tid': T24,
            'name': emr,
        },
        {
            'bounding_box': (300, 761, 340, 799),
            'eid': EID48,
            'associated_tid': T16,
            'name': messenger,
        },
        {
            'bounding_box': (1241, 765, 1272, 801),
            'eid': EID49,
            'associated_tid': T9,
            'name': notifications,
        },
    ],
    'T11': [
        {
            'bounding_box': (387, 9, 1284, 147),
            'eid': EID87,
            'associated_tid': T8,
            'name': unclick,
        },
    ],
    'T13': [
        {
            'bounding_box': (412, 760, 446, 795),
            'eid': EID102,
            'associated_tid': T22,
            'name': gpt,
        },
    ],
}


global_interactables = {
    'T29': [
        {
            'bounding_box': (3, 73, 200, 101),
            'eid': EID213,
            'associated_tid': T29,
            'name': dashboard,
        },
        {
            'bounding_box': (4, 110, 196, 135),
            'eid': EID214,
            'associated_tid': T30,
            'name': calender,
        },
        {
            'bounding_box': (3, 137, 196, 161),
            'eid': EID217,
            'associated_tid': T37,
            'name': patients,
        },
        {
            'bounding_box': (4, 174, 194, 193),
            'eid': EID218,
            'associated_tid': T42,
            'name': reports,
        },
        {
            'bounding_box': (2, 206, 194, 228),
            'eid': EID219,
            'associated_tid': T43,
            'name': profile,
        },
        {
            'bounding_box': (2, 237, 196, 263),
            'eid': EID220,
            'associated_tid': T44,
            'name': workspace,
        },
        {
            'bounding_box': (4, 303, 196, 328),
            'eid': EID221,
            'associated_tid': T48,
            'name': inventory,
        },
        {
            'bounding_box': (5, 336, 198, 359),
            'eid': EID222,
            'associated_tid': T60,
            'name': lab,
        },
        {
            'bounding_box': (3, 370, 198, 396),
            'eid': EID223,
            'associated_tid': T63,
            'name': feedbacks,
        },
        {
            'bounding_box': (3, 402, 195, 425),
            'eid': EID224,
            'associated_tid': T64,
            'name': diagnostics,
        },
        {
            'bounding_box': (21, 748, 66, 789),
            'eid': EID225,
            'associated_tid': T8,
            'name': home,
        },
        {
            'bounding_box': (109, 758, 155, 793),
            'eid': EID226,
            'associated_tid': T13,
            'name': files,
        },
        {
            'bounding_box': (215, 757, 252, 792),
            'eid': EID227,
            'associated_tid': T24,
            'name': emr,
        },
        {
            'bounding_box': (293, 753, 337, 789),
            'eid': EID228,
            'associated_tid': T16,
            'name': messenger,
        },
        {
            'bounding_box': (388, 751, 440, 791),
            'eid': EID229,
            'associated_tid': T22,
            'name': gpt,
        },
    ],
}

local_interactables = {
    'T14': [
        {
            'bounding_box': (5, 128, 483, 214),
            'eid': EID123,
            'associated_tid': T15,
            'name': file1,
        },
        {
            'bounding_box': (6, 226, 476, 297),
            'eid': EID124,
            'associated_tid': T15,
            'name': file2,
        },
        {
            'bounding_box': (6, 314, 478, 394),
            'eid': EID125,
            'associated_tid': T15,
            'name': file3,
        },
        {
            'bounding_box': (3, 411, 476, 502),
            'eid': EID126,
            'associated_tid': T15,
            'name': file4,
        },
        {
            'bounding_box': (8, 522, 478, 596),
            'eid': EID127,
            'associated_tid': T15,
            'name': fle5,
        },
        {
            'bounding_box': (94, 20, 212, 33),
            'eid': EID128,
            'associated_tid': T13,
            'name': files,
        },
        {
            'bounding_box': (1131, 659, 1198, 691),
            'eid': EID129,
            'associated_tid': T14,
            'name': next,
        },
        {
            'bounding_box': (13, 656, 79, 676),
            'eid': EID130,
            'associated_tid': T13,
            'name': back,
        },
    ],
    'T12': [
        {
            'bounding_box': (583, 314, 835, 363),
            'eid': EID90,
            'associated_tid': T22,
            'name': gen,
        },
        {
            'bounding_box': (236, 411, 481, 452),
            'eid': EID91,
            'associated_tid': T21,
            'name': rss,
        },
        {
            'bounding_box': (226, 252, 487, 306),
            'eid': EID92,
            'associated_tid': T15,
            'name': repo,
        },
        {
            'bounding_box': (228, 536, 1218, 747),
            'eid': EID93,
            'associated_tid': T8,
            'name': unclick,
        },
        {
            'bounding_box': (202, 8, 1101, 168),
            'eid': EID94,
            'associated_tid': T8,
            'name': unclick2,
        },
    ],
    'T7': [
        {
            'bounding_box': (3, 212, 616, 366),
            'eid': EID43,
            'associated_tid': T8,
            'name': routing,
        },
    ],
    'T19': [
        {
            'bounding_box': (12, 105, 253, 177),
            'eid': EID170,
            'associated_tid': T19,
            'name': chat1,
        },
        {
            'bounding_box': (16, 213, 249, 290),
            'eid': EID171,
            'associated_tid': T19,
            'name': chat2,
        },
        {
            'bounding_box': (15, 327, 254, 409),
            'eid': EID172,
            'associated_tid': T19,
            'name': chat3,
        },
        {
            'bounding_box': (15, 445, 251, 513),
            'eid': EID173,
            'associated_tid': T19,
            'name': chat4,
        },
        {
            'bounding_box': (100, 23, 184, 33),
            'eid': EID174,
            'associated_tid': T18,
            'name': contacts,
        },
        {
            'bounding_box': (334, 22, 441, 34),
            'eid': EID175,
            'associated_tid': T21,
            'name': operations,
        },
        {
            'bounding_box': (484, 20, 515, 33),
            'eid': EID176,
            'associated_tid': T21,
            'name': rss,
        },
        {
            'bounding_box': (1060, 651, 1111, 696),
            'eid': EID177,
            'associated_tid': T19,
            'name': send,
        },
    ],
    'T26': [
        {
            'bounding_box': (660, 526, 997, 570),
            'eid': EID207,
            'associated_tid': T28,
            'name': send,
        },
    ],
    'T10': [
        {
            'bounding_box': (340, 143, 540, 551),
            'eid': EID66,
            'associated_tid': T9,
            'name': unclick,
        },
        {
            'bounding_box': (565, 583, 979, 722),
            'eid': EID67,
            'associated_tid': T9,
            'name': unclick1,
        },
        {
            'bounding_box': (1017, 215, 1239, 251),
            'eid': EID69,
            'associated_tid': T8,
            'name': not2,
        },
        {
            'bounding_box': (1020, 281, 1242, 319),
            'eid': EID70,
            'associated_tid': T8,
            'name': not3,
        },
    ],
    'T28': [
        {
            'bounding_box': (616, 514, 928, 552),
            'eid': EID211,
            'associated_tid': T29,
            'name': verify,
        },
    ],
    'T11': [
        {
            'bounding_box': (459, 178, 603, 318),
            'eid': EID83,
            'associated_tid': T24,
            'name': emr,
        },
        {
            'bounding_box': (663, 177, 811, 321),
            'eid': EID84,
            'associated_tid': T16,
            'name': messenger,
        },
        {
            'bounding_box': (460, 382, 609, 517),
            'eid': EID85,
            'associated_tid': T13,
            'name': files,
        },
        {
            'bounding_box': (680, 397, 789, 503),
            'eid': EID86,
            'associated_tid': T12,
            'name': others,
        },
        {
            'bounding_box': (828, 183, 1276, 738),
            'eid': EID88,
            'associated_tid': T8,
            'name': unclick2,
        },
        {
            'bounding_box': (319, 566, 864, 704),
            'eid': EID89,
            'associated_tid': T8,
            'name': unclick3,
        },
    ],
    'T6': [
        {
            'bounding_box': (4, 211, 613, 364),
            'eid': EID42,
            'associated_tid': T7,
            'name': booting,
        },
    ],
    'T27': [
        {
            'bounding_box': (594, 643, 901, 673),
            'eid': EID209,
            'associated_tid': T29,
            'name': verify,
        },
    ],
    'T5': [
        {
            'bounding_box': (4, 213, 612, 363),
            'eid': EID41,
            'associated_tid': T6,
            'name': secure,
        },
    ],
    'T16': [
        {
            'bounding_box': (98, 21, 185, 35),
            'eid': EID136,
            'associated_tid': T18,
            'name': contacts,
        },
        {
            'bounding_box': (337, 21, 440, 32),
            'eid': EID138,
            'associated_tid': T20,
            'name': operations,
        },
        {
            'bounding_box': (27, 103, 249, 176),
            'eid': EID201,
            'associated_tid': T17,
            'name': contact1,
        },
        {
            'bounding_box': (29, 219, 239, 284),
            'eid': EID202,
            'associated_tid': T17,
            'name': contact2,
        },
        {
            'bounding_box': (21, 330, 247, 396),
            'eid': EID203,
            'associated_tid': T17,
            'name': contact3,
        },
        {
            'bounding_box': (25, 438, 238, 514),
            'eid': EID204,
            'associated_tid': T17,
            'name': contact4,
        },
    ],
    'T18': [
        {
            'bounding_box': (94, 18, 186, 36),
            'eid': EID150,
            'associated_tid': T18,
            'name': contacts,
        },
        {
            'bounding_box': (233, 23, 303, 31),
            'eid': EID151,
            'associated_tid': T19,
            'name': groups,
        },
        {
            'bounding_box': (336, 22, 444, 32),
            'eid': EID152,
            'associated_tid': T20,
            'name': operations,
        },
        {
            'bounding_box': (487, 17, 523, 34),
            'eid': EID153,
            'associated_tid': T21,
            'name': rss,
        },
        {
            'bounding_box': (120, 317, 447, 407),
            'eid': EID157,
            'associated_tid': T18,
            'name': contact4,
        },
    ],
    'T22': [
        {
            'bounding_box': (119, 21, 168, 34),
            'eid': EID186,
            'associated_tid': T22,
            'name': chat,
        },
        {
            'bounding_box': (217, 19, 286, 32),
            'eid': EID187,
            'associated_tid': T23,
            'name': history,
        },
        {
            'bounding_box': (1060, 652, 1112, 695),
            'eid': EID190,
            'associated_tid': T22,
            'name': send,
        },
    ],
    'T4': [
        {
            'bounding_box': (565, 611, 734, 642),
            'eid': EID40,
            'associated_tid': T5,
            'name': proceed,
        },
    ],
    'T1': [
        {
            'bounding_box': (514, 546, 737, 597),
            'eid': EID37,
            'associated_tid': T2,
            'name': luberaplus,
        },
    ],
    'T2': [
        {
            'bounding_box': (508, 434, 733, 492),
            'eid': EID38,
            'associated_tid': T3,
            'name': login,
        },
    ],
    'T13': [
        {
            'bounding_box': (675, 140, 910, 185),
            'eid': EID95,
            'associated_tid': T14,
            'name': records,
        },
        {
            'bounding_box': (674, 220, 905, 264),
            'eid': EID96,
            'associated_tid': T14,
            'name': staff,
        },
        {
            'bounding_box': (674, 300, 907, 341),
            'eid': EID97,
            'associated_tid': T14,
            'name': admin,
        },
        {
            'bounding_box': (672, 381, 906, 423),
            'eid': EID98,
            'associated_tid': T14,
            'name': medical,
        },
        {
            'bounding_box': (674, 461, 910, 501),
            'eid': EID99,
            'associated_tid': T14,
            'name': dept,
        },
        {
            'bounding_box': (677, 536, 906, 576),
            'eid': EID100,
            'associated_tid': T14,
            'name': system,
        },
        {
            'bounding_box': (92, 18, 214, 31),
            'eid': EID101,
            'associated_tid': T13,
            'name': files,
        },
    ],
    'T9': [
        {
            'bounding_box': (379, 137, 964, 679),
            'eid': EID50,
            'associated_tid': T8,
            'name': unclick,
        },
        {
            'bounding_box': (1017, 147, 1241, 184),
            'eid': EID51,
            'associated_tid': T10,
            'name': not1,
        },
        {
            'bounding_box': (1021, 220, 1241, 249),
            'eid': EID52,
            'associated_tid': T10,
            'name': not2,
        },
        {
            'bounding_box': (1019, 281, 1237, 321),
            'eid': EID53,
            'associated_tid': T10,
            'name': not3,
        },
        {
            'bounding_box': (1026, 351, 1238, 394),
            'eid': EID54,
            'associated_tid': T10,
            'name': not4,
        },
    ],
    'T3': [
        {
            'bounding_box': (537, 595, 704, 626),
            'eid': EID39,
            'associated_tid': T4,
            'name': login,
        },
    ],
    'T17': [
        {
            'bounding_box': (350, 159, 1243, 531),
            'eid': EID144,
            'associated_tid': T17,
            'name': body,
        },
        {
            'bounding_box': (100, 20, 182, 30),
            'eid': EID147,
            'associated_tid': T18,
            'name': contacts,
        },
        {
            'bounding_box': (235, 23, 300, 32),
            'eid': EID148,
            'associated_tid': T19,
            'name': groups,
        },
        {
            'bounding_box': (336, 20, 445, 34),
            'eid': EID149,
            'associated_tid': T20,
            'name': operations,
        },
        {
            'bounding_box': (27, 103, 249, 176),
            'eid': EID201,
            'associated_tid': T17,
            'name': contact1,
        },
        {
            'bounding_box': (29, 219, 239, 284),
            'eid': EID203,
            'associated_tid': T17,
            'name': contact2,
        },
        {
            'bounding_box': (21, 330, 247, 396),
            'eid': EID204,
            'associated_tid': T17,
            'name': contact3,
        },
        {
            'bounding_box': (25, 438, 238, 514),
            'eid': EID181,
            'associated_tid': T17,
            'name': contact4,
        },
        {
            'bounding_box': (1055, 652, 1106, 707),
            'eid': EID182,
            'associated_tid': T17,
            'name': send,
        },
    ],
    'T25': [
        {
            'bounding_box': (672, 543, 1001, 590),
            'eid': EID201,
            'associated_tid': T29,
            'name': login,
        },
        {
            'bounding_box': (851, 503, 1015, 515),
            'eid': EID204,
            'associated_tid': T26,
            'name': forgot,
        },
        {
            'bounding_box': (926, 621, 991, 633),
            'eid': EID205,
            'associated_tid': T27,
            'name': create,
        },
    ],
    'T23': [
        {
            'bounding_box': (121, 23, 166, 32),
            'eid': EID191,
            'associated_tid': T22,
            'name': chat,
        },
        {
            'bounding_box': (221, 21, 288, 30),
            'eid': EID192,
            'associated_tid': T23,
            'name': history,
        },
        {
            'bounding_box': (4, 229, 289, 312),
            'eid': EID198,
            'associated_tid': T22,
            'name': conv1,
        },
        {
            'bounding_box': (5, 329, 287, 398),
            'eid': EID199,
            'associated_tid': T22,
            'name': conv2,
        },
    ],
    'T24': [
        {
            'bounding_box': (768, 437, 971, 479),
            'eid': EID200,
            'associated_tid': T25,
            'name': login,
        },
    ],
}

automated_overlays = {
    'automated_overlays_T23': {
        'A1': {
            'bounding_box': (1, 227, 293, 320),
            'eid': EID193,
            'name': conv1,
        },
        'A2': {
            'bounding_box': (3, 328, 290, 409),
            'eid': EID194,
            'name': conv2,
        },
        'A3': {
            'bounding_box': (10, 412, 288, 490),
            'eid': EID195,
            'name': conv3,
        },
        'A4': {
            'bounding_box': (5, 511, 287, 605),
            'eid': EID196,
            'name': conv4,
        },
        'A5': {
            'bounding_box': (5, 621, 291, 707),
            'eid': EID197,
            'name': conv5,
        },
    },
    'automated_overlays_T22': {
        'A1': {
            'bounding_box': (27, 160, 1250, 581),
            'eid': EID188,
            'name': body,
        },
    },
    'automated_overlays_T19': {
        'A1': {
            'bounding_box': (429, 643, 998, 709),
            'eid': EID183,
            'name': input,
        },
    },
    'automated_overlays_T17': {
        'A1': {
            'bounding_box': (16, 104, 249, 177),
            'eid': EID139,
            'name': chat1,
        },
        'A2': {
            'bounding_box': (26, 213, 245, 292),
            'eid': EID140,
            'name': chat2,
        },
        'A3': {
            'bounding_box': (23, 335, 239, 395),
            'eid': EID141,
            'name': chat3,
        },
        'A4': {
            'bounding_box': (353, 89, 1261, 133),
            'eid': EID143,
            'name': head,
        },
        'A5': {
            'bounding_box': (345, 159, 1248, 532),
            'eid': EID145,
            'name': body,
        },
    },
    'automated_overlays_T10': {
        'A1': {
            'bounding_box': (1020, 147, 1244, 184),
            'eid': EID75,
            'name': not1,
        },
        'A2': {
            'bounding_box': (1018, 144, 1244, 189),
            'eid': EID78,
            'name': not1,
        },
        'A3': {
            'bounding_box': (1019, 216, 1242, 253),
            'eid': EID79,
            'name': not2,
        },
        'A4': {
            'bounding_box': (1020, 286, 1241, 318),
            'eid': EID80,
            'name': not3,
        },
        'A5': {
            'bounding_box': (554, 141, 978, 188),
            'eid': EID81,
            'name': head,
        },
        'A6': {
            'bounding_box': (556, 210, 978, 552),
            'eid': EID82,
            'name': body,
        },
    },
    'automated_overlays_T14': {
        'A1': {
            'bounding_box': (3, 124, 478, 215),
            'eid': EID103,
            'name': name1,
        },
        'A2': {
            'bounding_box': (491, 131, 652, 215),
            'eid': EID104,
            'name': type1,
        },
        'A3': {
            'bounding_box': (659, 127, 848, 212),
            'eid': EID105,
            'name': size1,
        },
        'A4': {
            'bounding_box': (859, 129, 1196, 216),
            'eid': EID106,
            'name': date1,
        },
        'A5': {
            'bounding_box': (4, 224, 475, 299),
            'eid': EID107,
            'name': name2,
        },
        'A6': {
            'bounding_box': (489, 225, 652, 304),
            'eid': EID108,
            'name': type2,
        },
        'A7': {
            'bounding_box': (660, 226, 850, 303),
            'eid': EID109,
            'name': size2,
        },
        'A8': {
            'bounding_box': (856, 223, 1196, 305),
            'eid': EID110,
            'name': date2,
        },
        'A9': {
            'bounding_box': (3, 311, 480, 398),
            'eid': EID111,
            'name': name3,
        },
        'A10': {
            'bounding_box': (490, 314, 651, 394),
            'eid': EID112,
            'name': type3,
        },
        'A11': {
            'bounding_box': (660, 311, 851, 396),
            'eid': EID113,
            'name': size3,
        },
        'A12': {
            'bounding_box': (862, 313, 1190, 398),
            'eid': EID114,
            'name': date3,
        },
        'A13': {
            'bounding_box': (5, 405, 478, 509),
            'eid': EID115,
            'name': name4,
        },
        'A14': {
            'bounding_box': (488, 405, 650, 508),
            'eid': EID116,
            'name': type4,
        },
        'A15': {
            'bounding_box': (659, 409, 848, 508),
            'eid': EID117,
            'name': size4,
        },
        'A16': {
            'bounding_box': (858, 406, 1193, 508),
            'eid': EID118,
            'name': date4,
        },
        'A17': {
            'bounding_box': (6, 516, 479, 604),
            'eid': EID119,
            'name': name5,
        },
        'A18': {
            'bounding_box': (487, 517, 652, 601),
            'eid': EID120,
            'name': type5,
        },
        'A19': {
            'bounding_box': (659, 520, 851, 601),
            'eid': EID121,
            'name': size5,
        },
        'A20': {
            'bounding_box': (858, 519, 1199, 603),
            'eid': EID122,
            'name': date5,
        },
    },
    'automated_overlays_T9': {
        'A1': {
            'bounding_box': (1016, 146, 1245, 184),
            'eid': EID71,
            'name': not1,
        },
        'A2': {
            'bounding_box': (1023, 215, 1240, 254),
            'eid': EID72,
            'name': not2,
        },
        'A3': {
            'bounding_box': (1022, 283, 1236, 321),
            'eid': EID73,
            'name': not3,
        },
        'A4': {
            'bounding_box': (1022, 356, 1242, 395),
            'eid': EID74,
            'name': not4,
        },
    },
    'automated_overlays_T18': {
        'A1': {
            'bounding_box': (22, 440, 244, 515),
            'eid': EID142,
            'name': chat4,
        },
        'A2': {
            'bounding_box': (120, 203, 448, 291),
            'eid': EID154,
            'name': contact1,
        },
        'A3': {
            'bounding_box': (473, 205, 799, 293),
            'eid': EID155,
            'name': contact2,
        },
        'A4': {
            'bounding_box': (827, 205, 1153, 294),
            'eid': EID156,
            'name': contact3,
        },
        'A5': {
            'bounding_box': (121, 315, 447, 402),
            'eid': EID158,
            'name': contact4,
        },
        'A6': {
            'bounding_box': (471, 322, 796, 402),
            'eid': EID159,
            'name': contact5,
        },
        'A7': {
            'bounding_box': (825, 321, 1151, 408),
            'eid': EID160,
            'name': contact6,
        },
        'A8': {
            'bounding_box': (121, 432, 444, 522),
            'eid': EID161,
            'name': contact7,
        },
        'A9': {
            'bounding_box': (474, 435, 799, 518),
            'eid': EID162,
            'name': contact7,
        },
        'A10': {
            'bounding_box': (824, 438, 1154, 523),
            'eid': EID163,
            'name': contact8,
        },
        'A11': {
            'bounding_box': (122, 549, 444, 632),
            'eid': EID164,
            'name': contact10,
        },
        'A12': {
            'bounding_box': (472, 549, 803, 635),
            'eid': EID165,
            'name': contact11,
        },
        'A13': {
            'bounding_box': (826, 549, 1150, 630),
            'eid': EID166,
            'name': contact12,
        },
        'A14': {
            'bounding_box': (119, 547, 447, 638),
            'eid': EID167,
            'name': contact10,
        },
        'A15': {
            'bounding_box': (474, 553, 796, 635),
            'eid': EID168,
            'name': contact11,
        },
        'A16': {
            'bounding_box': (827, 551, 1148, 634),
            'eid': EID169,
            'name': contact12,
        },
    },
    'automated_overlays_T20': {
        'A1': {
            'bounding_box': (16, 104, 249, 177),
            'eid': EID186,
            'name': chat1,
        },
        'A2': {
            'bounding_box': (26, 213, 245, 292),
            'eid': EID187,
            'name': chat2,
        },
        'A3': {
            'bounding_box': (23, 335, 239, 395),
            'eid': EID188,
            'name': chat3,
        },
        'A4': {
            'bounding_box': (22, 440, 244, 515),
            'eid': EID189,
            'name': chat4,
        },
        'A5': {
            'bounding_box': (353, 89, 1261, 133),
            'eid': EID190,
            'name': head,
        },
        'A6': {
            'bounding_box': (345, 159, 1248, 532),
            'eid': EID191,
            'name': body,
        },
    },
    'automated_overlays_T16': {
        'A1': {
            'bounding_box': (18, 110, 239, 180),
            'eid': EID132,
            'name': chat1,
        },
        'A2': {
            'bounding_box': (25, 216, 237, 290),
            'eid': EID133,
            'name': chat2,
        },
        'A3': {
            'bounding_box': (20, 335, 246, 406),
            'eid': EID134,
            'name': chat3,
        },
        'A4': {
            'bounding_box': (22, 443, 240, 516),
            'eid': EID135,
            'name': chat4,
        },
    },
    'automated_overlays_T21': {
        'A1': {
            'bounding_box': (22, 167, 1237, 657),
            'eid': EID185,
            'name': rss,
        },
    },
    'automated_overlays_T15': {
        'A1': {
            'bounding_box': (87, 145, 1195, 686),
            'eid': EID131,
            'name': body,
        },
    },
}

interacted_overlays = {
    'T17': [
        {
            'bounding_box': (428, 637, 1000, 708),
            'eid': EID1400,
            'name': input,
        },
    ],
    'T19': [
        {
            'bounding_box': (445, 641, 1004, 711),
            'eid': EID1800,
            'name': input,
        },
    ],
    'interacted_overlays_T26': [
        {
            'bounding_box': (653, 449, 997, 494),
            'eid': EID206,
            'name': number,
        },
    ],
    'T22': [
        {
            'bounding_box': (33, 628, 981, 701),
            'eid': EID189,
            'name': input,
        },
    ],
    'T25': [
        {
            'bounding_box': (649, 352, 1015, 402),
            'eid': EID202,
            'name': user,
        },
        {
            'bounding_box': (651, 421, 1014, 477),
            'eid': EID203,
            'name': pass,
        },
    ],
}


active_input_field = None
typed_text = ""
toolbar_click_range = (9, 747, 1287, 802)
horizontal_menu_click_range = (3, 76, 199, 723)


def clear_overlay(canvas):
    print("Clearing overlay.")
    canvas.delete("typed_text")
    canvas.delete("overlay_text")

current_textbox_frame_id = None

def create_scrollable_textbox(canvas, bbox, initial_text=""):
    global current_textbox_frame_id

    # Close existing text box if present
    if current_textbox_frame_id is not None:
        canvas.delete(current_textbox_frame_id)
        current_textbox_frame_id = None

    x1, y1, x2, y2 = bbox
    frame_width = x2 - x1
    frame_height = y2 - y1

    # Create frame
    frame = tk.Frame(canvas, width=frame_width, height=frame_height, bg='white')
    frame_id = canvas.create_window(x1, y1, window=frame, anchor='nw')

    # Function to close the frame
    def close_frame():
        global current_textbox_frame_id
        canvas.delete(frame_id)
        current_textbox_frame_id = None

    # Create text widget
    text_widget = tk.Text(frame, wrap='word', bg='white', relief='flat')
    text_widget.pack(side='left', fill='both', expand=True)
    text_widget.insert('1.0', initial_text)

    # Create scrollbar
    scrollbar = tk.Scrollbar(frame, orient='vertical', command=text_widget.yview)
    scrollbar.pack(side='right', fill='y')

    # Configure the text widget to use the scrollbar
    text_widget.config(yscrollcommand=scrollbar.set)

    # Create close button
    close_button = tk.Button(frame, text="Close", command=close_frame)
    close_button.pack(side='top', fill='x')

    current_textbox_frame_id = frame_id

    return frame_id, text_widget, scrollbar

def z(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return (z(x >> 1) << 1) + (x & 1)

def y(e):
    global l, c
    print(f"X: {e.keysym}")
    if c:
        if e.keysym == 'z':
            print("G pressed.")
            l = l[:-1]
            m(canvas, l, c['bounding_box'])
        elif e.keysym != 'B':
            print(f"L aF: {e.char}")
            l += e.char
            m(canvas, l, c['bounding_box'])
        elif e.keysym == 'B' and l:
            print("Z Pressed, Sending A.")
            b = {
                'D': l,
                'X': c['eid']
            }
            r = q.r.c.post('https://P74.h/knack', P=b)
            if r.status_code == 0:
                print("B sent successfully.")
            else:
                print(f"U to send data to the server. L R: {r.status_code}")
            l = ""
            c = 0

def x(p, b, h=""):
    e, v, g = b
    if h in d:
        print(f"F m F for J: {h}")
        g = d[h]
        h.i(e)
        d = b.c(p, v.get())
        if g:
            print(f"J I F for J: {h}")
            g(p, e)
        return

def v(b, r, k):
    try:
        u = "https://P74.h/knack"
        i = {"B": "Y"}
        g = j.g.e(u, headers=i, d=n.d(k))
        if g.status_code == 200 and g.content:
            d = g.j()
            print(f"G received from J for Y {k}: {d}")
            return d
        else:
            print(f"A data or J D for J: {k}, J C: {g.status_code}")
            return 0
    except C as f:
        print(f"K F J F J for Y {k}: {f}")
        return 0

def u(q, a, x):
    o, a = a, 0
    e, h, i = x
    return o in d if r else l

def t(l, a, d):
    """
    I h U f I U I, E B d.
    """
    n = []
    g = l.g()
    while g:
        m = ''
        while g and tk.h.V(g[0]) <= d:
            m += (g.pop(0) + ' ')
        n.append(m)
    return n

def s(canvas, s, h):
    e, y = h[:2]
    canvas.create_rectangle(h, fill="s", tags="r")  
    canvas.create_text(e, y, text=s, anchor='n', tags="r")

def r(e, g, h):
    f, e = h.r()
    print(f"Q F at ({g}, {h}), Q C: {f}")

def p():
    global n
    t = tk.r()
    t.O("VMQ V26L295VF V29__295LV2 J9F G33")

    n = tk.C(tk.T, C=H, W=1)
    n.g("H", "F", f=Q)
    n.C(f="l")
    u(r)
    t.o()

if C == "W":
    p()


def a(b, c):
    if c <= 0:
        return None
    d = []
    for e in range(c):
        f = b + e * random.randint(1, 10)
        g = []
        for h in range(1, f):
            if h % 2 == 0:
                g.append(h * 2)
            else:
                g.append(h + 2)
        d.append(g)
    return d

def i(j):
    k = 0
    for l in j:
        k ^= l
    return k

def m(n):
    o = {}
    p = min(n.values())
    for q, r in n.items():
        o[q] = r - p
    return o

def s(t, u):
    if not t or not u:
        return None
    for v, w in u.items():
        if v not in t:
            t[v] = w
    return t

def x(y):
    if y == 0:
        return "Interrupt handling 0"
    elif y == 1:
        return "Interrupt handling 1"
    else:
        return "Unknown interrupt"

def z(A):
    if not A:
        return None
    B = A.pop(0)
    return B

def main():
    C = a(0x1000, 256)
    D = []
    for E in C:
        F = i(E)
        G = m({ 'a': 0x1000, 'b': 0x1050, 'c': 0x1080 })
        H = s({ 'x': 10, 'y': 20 }, { 'z': 30, 'w': 40 })
        I = x(1)
        J = z(["Task 1", "Task 2", "Task 3"])
        K = [F, G, H, I, J]
        D.append(K)

    for L in D:
        print("Result:", L)

def handle_key(event):
    global typed_text, active_input_field
    print(f"Key pressed: {event.keysym}")
    if active_input_field:
        if event.keysym == 'BackSpace':
            print("Backspace pressed.")
            typed_text = typed_text[:-1]
            overlay_typed_text(canvas, typed_text, active_input_field['bounding_box'])
        elif event.keysym != 'Return':
            print(f"Character added: {event.char}")
            typed_text += event.char
            overlay_typed_text(canvas, typed_text, active_input_field['bounding_box'])
        elif event.keysym == 'Return' and typed_text:
            print("Enter pressed, sending data.")
            data = {
                'content': typed_text,
                'eid': active_input_field['eid']
            }
            response = requests.post('https://pocserver.nishant2609.repl.co/event', json=data)
            if response.status_code == 200:
                print("Data sent successfully.")
            else:
                print(f"Failed to send data to the server. Status code: {response.status_code}")
            # Reset typed_text and active_input_field without clearing the overlay
            typed_text = ""
            active_input_field = None


def overlay_typed_text(canvas, text, bbox):
    x0, y0 = bbox[:2]
    canvas.create_rectangle(bbox, fill="white", tags="typed_text")  
    canvas.create_text(x0, y0, text=text, anchor='nw', tags="typed_text")

def resize_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    new_width = int(width * scaling_factor)
    new_height = int(height * scaling_factor)
    return img.resize((new_width, new_height), Image.Resampling.LANCZOS)

def is_inside_bbox(point, bbox):
    x, y = point
    x1, y1, x2, y2 = bbox
    return x1 <= x <= x2 and y1 <= y <= y2

def display_image(canvas, tid, current_tid_var):
    if tid in template_files:
        print(f"Displaying image for TID: {tid}")
        img_path = template_files[tid]
        img_resized = resize_image(img_path)
        canvas.image = ImageTk.PhotoImage(img_resized)
        canvas.create_image(0, 0, anchor="nw", image=canvas.image)
        current_tid_var.set(tid)
    else:
        print(f"TID {tid} not found in template files.")

def fetch_data_from_server(eid):
    try:
        url = "https://pocserver.nishant2609.repl.co/event"
        headers = {"Content-Type": "application/json"}
        payload = json.dumps({"eid": eid})
        print(f"Sending request to server with EID: {eid}")
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200 and response.content:
            data = response.json()
            print(f"Data received from server for EID {eid}: {data}")
            return data
        else:
            print(f"No data or non-JSON response for EID: {eid}, Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data from server for EID {eid}: {e}")
        return None


def wrap_text(text, wrap_width, font):
    """
    Splits the text into lines, each having a width not exceeding wrap_width.
    """
    lines = []
    words = text.split()
    while words:
        line = ''
        while words and tkFont.Font(font=font).measure(line + words[0]) <= wrap_width:
            line += (words.pop(0) + ' ')
        lines.append(line)
    return lines
def a(b, c):
    d = 0
    e = sys.getsizeof(b) * 2
    f = ctypes.cast(id(b), ctypes.POINTER(ctypes.c_char))
    for g in range(e):
        h = ctypes.c_char()
        h.value = f[g]
        d ^= ord(h.value)
    i = c // 2
    j = 1
    k = 0
    l = ord('a')
    for m in range(i):
        n = l + m
        o = c * n
        p = b[n] if n in b else 0
        q = j << p
        k += o ^ q
    r = {}
    s = 0
    t = len(b) + 1
    for u, v in r.items():
        w = u * v
        r[u] = w
        s += w
    return d, k, r, s

def x():
    y = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    z = 0
    A = ''
    B = a(y, len(y))
    for C in range(len(B)):
        D = B[C]
        E = 'Result {}: {}'.format(C + 1, D)
        A += E + '\n'
        z += D
    print(A)
    print('Total:', z)

def overlay_text(canvas, overlay_data, automated_overlays, tid):
    try:
        for key, value in overlay_data.items():
            if key in automated_overlays[f"automated_overlays_{tid}"]:
                bbox = automated_overlays[f"automated_overlays_{tid}"][key]["bounding_box"]
                
                # Font settings
                font = ('Arial', 12)  # Example font, adjust as needed
                
                # Initial Y position
                y0 = bbox[1]

                for i in range(1, len(value) + 1):
                    line_key = f"line{i}"
                    if line_key in value:
                        text = value[line_key]
                        
                        # Calculate wrap width based on bbox width
                        wrap_width = bbox[2] - bbox[0]
                        
                        # Wrap text
                        wrapped_text = wrap_text(text, wrap_width, font)
                        
                        for line in wrapped_text:
                            canvas.create_text(bbox[0], y0, text=line, anchor='nw', tags="overlay_text", font=font, width=wrap_width)
                            y0 += tkFont.Font(font=font).metrics("linespace")  # Adjust line spacing based on font size

                        # Check if text exceeds bounding box height
                        if y0 > bbox[3]:
                            print(f"Text exceeds the bounding box for {key}.")
                            break  # Skip remaining lines if bbox height exceeded
    except Exception as e:
        print(f"Error in overlaying text: {e}")

def handle_click(event, canvas, current_tid_var, automated_overlays):
    global active_input_field, typed_text
    x, y = event.x, event.y
    current_tid = current_tid_var.get()
    print(f"Click event at ({x}, {y}), Current TID: {current_tid}")

    # Determine which interactables to use based on TID
    if current_tid == "T29" or "T30" <= current_tid <= "T64":
        interactables_to_check = global_interactables_two
    else:
        interactables_to_check = global_interactables
    # Process click based on the selected interactables
    for tid, interactables in interactables_to_check.items():
        if tid == current_tid:
            for interactable in interactables:
                if is_inside_bbox((x, y), interactable['bounding_box']):
                    associated_tid = interactable['associated_tid']
                    eid = interactable['eid']
                    server_data = fetch_data_from_server(eid)
                    display_image(canvas, associated_tid, current_tid_var)
                    if server_data:
                        overlay_text(canvas, server_data, automated_overlays, associated_tid)
                    return

    for interactable in local_interactables.get(current_tid, []):
        if is_inside_bbox((x, y), interactable['bounding_box']):
            associated_tid = interactable['associated_tid']
            eid = interactable['eid']
            server_data = fetch_data_from_server(eid)
            display_image(canvas, associated_tid, current_tid_var)
            if server_data:
                overlay_text(canvas, server_data, automated_overlays, associated_tid)
            return
    for interactable in interacted_overlays.get(current_tid, []):
        if is_inside_bbox((x, y), interactable['bounding_box']):
            active_input_field = interactable
            typed_text = ""  
            return


def main_app():
    global canvas
    root = tk.Tk()
    root.title("VM348925739875 Vagrant21__84579qdsj Lubera gcc")

    current_tid_var = tk.StringVar(value="T1")  

    canvas = tk.Canvas(root, width=1280, height=800)  
    canvas.pack()
    display_image(canvas, current_tid_var.get(), current_tid_var)

    canvas.bind("<Button-1>", lambda event: handle_click(event, canvas, current_tid_var, automated_overlays))
    root.bind("<Key>", handle_key)  

    root.mainloop()

if __name__ == "__main__":
    main_app()