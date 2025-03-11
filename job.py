import json

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config
  
if __name__ == "__main__":
    config_file_path = 'config.json'  # Adjust the path if necessary
    config = load_config(config_file_path)
    print(json.dumps(config, indent=4))  # Pretty print the JSON content
    print("hello")

