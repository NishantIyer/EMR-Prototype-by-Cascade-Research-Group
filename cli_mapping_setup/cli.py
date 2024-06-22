import tkinter as tk
from tkinter import simpledialog
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

scaling_factor = 0.9  

# these are based on my local paths, if you cloned this repo, please change the path of the templates to the appropriate location.
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

global_interactables, local_interactables = {}, {}
automated_overlays, interacted_overlays = {}, {}

for i in range(1, 65):
    tid = f"T{i}"
    global_interactables[tid] = []
    local_interactables[tid] = []
    automated_overlays[tid] = {}
    interacted_overlays[tid] = []

def generate_eid():
    eid_counter = generate_eid.counter
    generate_eid.counter += 1
    save_eid_counter()  
    return f"EID{eid_counter}"

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
    return simpledialog.askinteger("Input", "Interaction Type (1 for Interactable Element, 2 for Automated Overlays, 3 for Interacted Overlays):", parent=root)

def ask_tid(root, prompt):
    return simpledialog.askstring("Input", prompt, parent=root)

def process_interaction(root, bbox, current_tid, interaction_type):

    name = simpledialog.askstring("Input", "Enter name for the element/overlay:", parent=root)
    if not name:
        return  

    if interaction_type == 1:
        element_type = simpledialog.askinteger("Input", "Type (1 for global, 2 for local):", parent=root)
        associated_tid = ask_tid(root, "Enter Associated TID:")
        eid = generate_eid()
        entry = {"bounding_box": bbox, "eid": eid, "associated_tid": associated_tid, "name": name}

        if element_type == 1:
            if current_tid not in global_interactables:
                global_interactables[current_tid] = []  
            global_interactables[current_tid].append(entry)
        elif element_type == 2:
            if current_tid not in local_interactables:
                local_interactables[current_tid] = []  
            local_interactables[current_tid].append(entry)

    elif interaction_type == 2:  
        overlay_tid = ask_tid(root, "Enter local overlay table TID:")
        eid = generate_eid()
        entry = {"bounding_box": bbox, "eid": eid, "name": name}
        if overlay_tid not in automated_overlays:
            automated_overlays[overlay_tid] = {f"A1": entry}
        else:
            count = len(automated_overlays[overlay_tid]) + 1
            automated_overlays[overlay_tid][f"A{count}"] = entry

    elif interaction_type == 3:  
        overlay_tid = ask_tid(root, "Enter local overlay table TID:")
        eid = generate_eid()
        entry = {"bounding_box": bbox, "eid": eid, "name": name}
        interacted_overlays[overlay_tid].append(entry)

def resize_image(image):

    width, height = image.size
    new_width = int(width * scaling_factor)
    new_height = int(height * scaling_factor)
    return image.resize((new_width, new_height), Image.ANTIALIAS)

def reopen_template_selection(root):
    while True:
        tid = ask_tid(root, "Open Template (q to quit):")
        if tid in ['q', None]:
            break
        display_template(root, tid)

def display_template(root, tid):
    if tid in template_files:
        top = tk.Toplevel(root)
        top.title(f"Template: {tid}")  
        img = Image.open(template_files[tid])
        img_resized = resize_image(img)
        img_tk = ImageTk.PhotoImage(img_resized)
        canvas = tk.Canvas(top, width=img_resized.width, height=img_resized.height)
        canvas.pack()
        canvas.create_image(0, 0, anchor="nw", image=img_tk)
        canvas.image = img_tk

        top.bind("<Control-s>", lambda event: save_data())

        top.bind("<Control-q>", lambda event: reopen_template_selection(root))

        while True:
            bbox = capture_clicks(canvas)
            interaction_type = ask_interaction_type(top)
            if interaction_type in [None, "q"]:
                break
            process_interaction(top, bbox, tid, interaction_type)

        top.destroy()

global_interactables_dir = "global_interactables"
local_interactables_dir = "local_interactables"
automated_overlays_dir = "automated_overlays"
interacted_overlays_dir = "interacted_overlays"

current_directory = os.path.dirname(os.path.abspath(__file__))

global_interactables_path = os.path.join(current_directory, global_interactables_dir)
local_interactables_path = os.path.join(current_directory, local_interactables_dir)
automated_overlays_path = os.path.join(current_directory, automated_overlays_dir)
interacted_overlays_path = os.path.join(current_directory, interacted_overlays_dir)

def read_data_from_file(filename, directory):
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} if 'overlays' in filename else []

global_interactables = read_data_from_file("global_interactables.json", global_interactables_path)
local_interactables = {f"T{i}": read_data_from_file(f"local_interactables_T{i}.json", local_interactables_path) for i in range(1, 65)}
automated_overlays = {f"T{i}": read_data_from_file(f"automated_overlays_T{i}.json", automated_overlays_path) for i in range(1, 65)}
interacted_overlays = {f"T{i}": read_data_from_file(f"interacted_overlays_T{i}.json", interacted_overlays_path) for i in range(1, 65)}

def save_data():

    global_file = os.path.join(global_interactables_path, "global_interactables.json")
    with open(global_file, "w") as file:
        json.dump(global_interactables, file, indent=4)

    for tid in range(1, 65):
        local_file = os.path.join(local_interactables_path, f"local_interactables_T{tid}.json")
        automated_file = os.path.join(automated_overlays_path, f"automated_overlays_T{tid}.json")
        interacted_file = os.path.join(interacted_overlays_path, f"interacted_overlays_T{tid}.json")

        with open(local_file, "w") as file:
            json.dump(local_interactables[f"T{tid}"], file, indent=4)
        with open(automated_file, "w") as file:
            json.dump(automated_overlays[f"T{tid}"], file, indent=4)
        with open(interacted_file, "w") as file:
            json.dump(interacted_overlays[f"T{tid}"], file, indent=4)

def main_cli():
    root = tk.Tk()
    root.withdraw()

    while True:
        tid = ask_tid(root, "Open Template (q to quit):")
        if tid in ['q', None]:
            break
        display_template(root, tid)

    save_data()

if __name__ == "__main__":
    main_cli()