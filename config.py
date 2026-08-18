import json
import os

def load_config(defaults, config_file='config.json'):
    if not os.path.isfile(config_file):
        return defaults
    with open(config_file, 'r') as file:
        config = json.load(file)
    return {**defaults, **config}

defaults = {
    'click_interval': 0.1,
    'clicks_count': 100,
    'mouse_button': 'left',
    'run_in_background': False
}

if __name__ == '__main__':
    config = load_config(defaults)
    print(config)