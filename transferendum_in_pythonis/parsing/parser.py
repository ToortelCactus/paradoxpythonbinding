import glob
from transferendum_in_pythonis.defines import MOD_PATH


def process_file(filename: str, output, counter, level=1):
    """
    count the brackets so that we know when to process or skip top-level bracketed definitions

    level (1-x), where 1 is top-level, 2. is right above it, etc.
    """
    leftbr = 0
    rightbr = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()

            if not line or line[0] == "#" or "{" not in line or leftbr != rightbr:
                # comment is comment
                if line and line[0] == "#":
                    continue

                leftbr += line.count("{")
                rightbr += line.count("}")
                continue

            counter += 1
            output.write("    " + "".join(filter(valid_chars, line.split(" =")[0])) + " = " + str(counter) + "\n")

            leftbr += line.count("{")
            rightbr += line.count("}")

    return counter


def valid_chars(char: str):
    return char.isalnum() or char == "_"


def parse_files(path: str, output_name: str, recursive=False):
    with open("generated/" + output_name + ".py", "w") as output:
        output.write("from enum import Enum\n\n\n")
        output_name = output_name[0].upper() + output_name[1:]
        output.write("class " + output_name + "(Enum):\n")

        counter = 0

        for filename in glob.glob(path + "*.txt", recursive=recursive):
            if "unwanted" in filename or "unused" in filename:
                continue
            output.write("\n")
            counter = process_file(filename, output, counter)

        output.write("\n")


def parse_mts():
    path = MOD_PATH + "common/modifier_types/"
    parse_files(path, "modifier_type", True)


def parse_modifiers():
    path = MOD_PATH + "common/modifiers/"
    parse_files(path, "modifier", True)


def parse_buildings():
    path = MOD_PATH + "common/buildings/"
    parse_files(path, "building", True)


def parse_countries():
    path = MOD_PATH + "common/country_definitions/"
    parse_files(path, "country", True)


def parse_igs():
    path = MOD_PATH + "common/interest_groups/"
    parse_files(path, "interest_group", True)


def parse_religions():
    path = MOD_PATH + "common/religions/"
    parse_files(path, "religion", True)


def parse_law_groups():
    path = MOD_PATH + "common/law_groups/"
    parse_files(path, "law_group", True)


def parse_cultures():
    path = MOD_PATH + "common/cultures/"
    parse_files(path, "culture", True)


def parse_goods():
    path = MOD_PATH + "common/goods/"
    parse_files(path, "market_goods", True)


def parse_state_regions():
    path = MOD_PATH + "map_data/state_regions/"
    parse_files(path, "state_region", True)


def parse_parties():
    path = MOD_PATH + "common/parties/"
    parse_files(path, "party", True)


def parse_diplo_actions():
    path = MOD_PATH + "common/diplomatic_actions/"
    parse_files(path, "dip_action", True)


def parse_diplo_plays():
    path = MOD_PATH + "common/diplomatic_plays/"
    parse_files(path, "dip_play", True)


def parse_gov_types():
    path = MOD_PATH + "common/government_types/"
    parse_files(path, "gov_type", True)


def parse_laws():
    path = MOD_PATH + "common/laws/"
    parse_files(path, "law", True)


def parse_all():
    parse_mts()
    parse_modifiers()
    parse_buildings()
    parse_countries()
    parse_igs()
    parse_religions()
    parse_law_groups()
    parse_cultures()
    parse_goods()
    parse_state_regions()
    parse_parties()
    parse_diplo_actions()
    parse_diplo_plays()
    parse_gov_types()
    parse_laws()


# for testing
parse_all()