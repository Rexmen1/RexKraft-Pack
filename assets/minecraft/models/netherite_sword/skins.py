import json

# Define the model IDs and their corresponding names
model_ids = {
    15: "vibranium_edge",
    16: "widows_sting",
    17: "withers_bane",
    18: "zombie_saber",
    19: "blossom_blade",
    20: "absolute_zero",
    21: "ark_of_the_cosmos",
    22: "bloodsucker",
    23: "calamity",
    24: "cobra",
    25: "daedalus_replica",
    26: "death_embrace",
    27: "deathbringer",
    28: "duskshadow",
    29: "earthbound",
    30: "executioner_blade",
    31: "fearmonger",
    32: "flesh_flayer",
    33: "fury_katana",
    34: "guillotine",
    35: "harbinger_of_death",
    36: "hemophobia",
    37: "immolus",
    38: "justice",
    39: "last_breath",
    40: "mythril_greatsword",
    41: "orichalcum_sword",
    42: "protego",
    43: "rememberence",
    44: "securus",
    45: "shadow",
    46: "silverlight",
    47: "sub_zero",
    48: "the_trickster",
    49: "titanium_blade",
    50: "withered"
}

# Define the JSON template
json_template = {
    "parent": "item/handheld",
    "textures": {
        "layer0": "netherite_sword/{}"
    }
}

# Generate the JSON files
for model_id, model_name in model_ids.items():
    json_data = json_template.copy()
    json_data["textures"]["layer0"] = json_data["textures"]["layer0"].format(model_name)
    with open("{}.json".format(model_name), "w") as f:
        json.dump(json_data, f, indent=4)