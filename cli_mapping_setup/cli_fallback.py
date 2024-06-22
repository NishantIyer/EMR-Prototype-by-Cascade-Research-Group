import tkinter as tk
from tkinter import simpledialog, messagebox, PhotoImage
import json
from PIL import Image, ImageTk
import os 

EID_COUNTER_FILE = "eid_counter.json"

def save_eid_counter():
    with open(EID_COUNTER_FILE, "w") as file:
        json.dump(generate_eid.counter, file)

def load_eid_counter():
    if os.path.exists(EID_COUNTER_FILE):
        try:
            with open(EID_COUNTER_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return 1
    return 1

global_interactables = {f"T{i}": [] for i in range(1, 65)}
local_interactables = {f"T{i}": [] for i in range(1, 65)}
automated_overlays = {f"T{i}": {} for i in range(1, 65)}
interacted_overlays = {f"T{i}": [] for i in range(1, 65)}

def generate_eid():
    generate_eid.counter += 1
    save_eid_counter()
    return f"EID{generate_eid.counter}"

generate_eid.counter = load_eid_counter()

def capture_clicks(canvas):
    clicks = []
    def on_click(event):
        clicks.append((event.x, event.y))
        if len(clicks) == 2:
            canvas.unbind("<Button-1>")
            canvas.event_generate('<<ClicksCaptured>>')
    canvas.bind("<Button-1>", on_click)
    canvas.bind('<<ClicksCaptured>>', lambda e: canvas.quit())
    canvas.mainloop()
    return clicks[0] + clicks[1]

def ask_interaction_type(root):
    return simpledialog.askinteger("Input", "Interaction Type (1 for Interactable, 2 for Automated Overlay, 3 for Interacted Overlay):", parent=root)

def process_interaction(root, bbox, tid, interaction_type):
    name = simpledialog.askstring("Input", "Enter a name for the element/overlay:", parent=root)
    if not name:
        messagebox.showwarning("Warning", "No name provided. Interaction skipped.")
        return

    if interaction_type == 1:
        element_type = simpledialog.askinteger("Input", "Element Type (1 for Global, 2 for Local):", parent=root)
        associated_tid = simpledialog.askstring("Input", "Enter Associated TID:", parent=root)
        eid = generate_eid()
        entry = {"bounding_box": bbox, "eid": eid, "associated_tid": associated_tid, "name": name}
        if element_type == 1:
            global_interactables[tid].append(entry)
        elif element_type == 2:
            local_interactables[tid].append(entry)

    elif interaction_type == 2:
        overlay_tid = simpledialog.askstring("Input", "Enter Overlay TID:", parent=root)
        eid = generate_eid()
        entry = {"bounding_box": bbox, "eid": eid, "name": name}
        if overlay_tid not in automated_overlays:
            automated_overlays[overlay_tid] = {f"A1": entry}
        else:
            count = len(automated_overlays[overlay_tid]) + 1
            automated_overlays[overlay_tid][f"A{count}"] = entry

    elif interaction_type == 3:
        overlay_tid = simpledialog.askstring("Input", "Enter Overlay TID:", parent=root)
        eid = generate_eid()
        entry = {"bounding_box": bbox, "eid": eid, "name": name}
        interacted_overlays[tid].append(entry)

def display_template(root, tid, template_files):
    if tid in template_files:
        img = Image.open(template_files[tid])
        img_tk = ImageTk.PhotoImage(img)
        canvas = tk.Canvas(root, width=img.width(), height=img.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor="nw", image=img_tk)
        bbox = capture_clicks(canvas)
        interaction_type = ask_interaction_type(root)
        process_interaction(root, bbox, tid, interaction_type)
        canvas.destroy()

def main_cli(template_files):
    root = tk.Tk()
    root.withdraw()
    while True:
        tid = simpledialog.askstring("Input", "Open Template (q to quit):", parent=root)
        if tid in ['q', None]:
            break
        display_template(root, tid, template_files)
    root.mainloop()

if __name__ == "__main__":
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
    main_cli(template_files)