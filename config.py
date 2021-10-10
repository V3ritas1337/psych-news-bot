import yaml

def config(yml_file: str, info: str):
   with open(yml_file, 'r') as f:
      data = yaml.load(f, Loader=yaml.FullLoader)
      return(data[f'{info}'])
