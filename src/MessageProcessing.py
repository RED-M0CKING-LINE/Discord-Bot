import json


def read_prefixes():
    with open('config/prefixes.json', 'r') as prefix_list:
        prefix_data = json.load(prefix_list)
        prefix_list.close()

    return prefix_data


def write_prefixes(prefix_data):  # Writes the prefix to prefixes.json
    # Write the new prefix to the file
    with open('config/prefixes.json', 'w') as prefix_list:
        json.dump(prefix_data, prefix_list, indent=4)
        prefix_list.close()


def find_guild(guild, prefix_data):  # Find the index of the guild in prefixes.json
    if guild is None:
        return -1

    for i in range(len(prefix_data)):
        if prefix_data[i]['guildID'] == guild.id:
            return i

    return -1
