from json import dump, load
from dino_runner.utils.constants import DATA_SAVE, DEFAULT_STATS


def save_data(data):
    with open(DATA_SAVE, 'w') as f:
        dump(data, f)


def loading_data():
    try:
        with open(DATA_SAVE) as f:
            data = load(f)
            for stat in DEFAULT_STATS.keys():
                if stat not in data:
                    data[stat] = DEFAULT_STATS[stat]
            return data
    except FileNotFoundError:
        return DEFAULT_STATS
