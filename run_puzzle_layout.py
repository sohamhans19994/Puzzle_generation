import os
import gym
from PIL import Image
from create.create_game import register_json_folder, register_json_str
import json
repo_dir = os.path.dirname(os.path.abspath(__file__))

starter_json_file = os.path.join(repo_dir, "example_puzzle_layout.json")

visualization_path = os.path.join(repo_dir, "example_puzzle.jpg")
with open(starter_json_file, 'r') as json_file:
            env_json = json.load(json_file)
starter_json_str = json.dumps(env_json)
register_json_str(starter_json_str)

env_name = env_json['name']
env = gym.make(f'CreateLevel{env_name}-v0')
env.reset()
frame = env.render('rgb_array_high_mega_changed_colors')
Image.fromarray(frame).save(visualization_path)
env.close()