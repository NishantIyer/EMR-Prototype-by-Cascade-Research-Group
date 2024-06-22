import os
import json

current_directory = os.path.dirname(os.path.abspath(__file__))

global_interactables_dir = "global_interactables"
local_interactables_dir = "local_interactables"
automated_overlays_dir = "automated_overlays"
interacted_overlays_dir = "interacted_overlays"

def create_directory(dir_name):
    dir_path = os.path.join(current_directory, dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

global_interactables_path = create_directory(global_interactables_dir)
local_interactables_path = create_directory(local_interactables_dir)
automated_overlays_path = create_directory(automated_overlays_dir)
interacted_overlays_path = create_directory(interacted_overlays_dir)

global_interactables_file = os.path.join(global_interactables_path, "global_interactables.json")
with open(global_interactables_file, "w") as file:
    json.dump({}, file, indent=4)

for i in range(1, 65):
    tid = f"T{i}"

    local_interactables_file = os.path.join(local_interactables_path, f"local_interactables_{tid}.json")
    automated_overlays_file = os.path.join(automated_overlays_path, f"automated_overlays_{tid}.json")
    interacted_overlays_file = os.path.join(interacted_overlays_path, f"interacted_overlays_{tid}.json")

    with open(local_interactables_file, "w") as file:
        json.dump([], file, indent=4)

    with open(automated_overlays_file, "w") as file:
        json.dump({}, file, indent=4)

    with open(interacted_overlays_file, "w") as file:
        json.dump([], file, indent=4)

print("Empty JSON files created successfully in their respective directories.")