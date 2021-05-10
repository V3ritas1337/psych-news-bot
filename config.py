import yaml

with open('dev-config.yaml', 'r') as f:
  print(yaml.load(f))