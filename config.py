import yaml

with open('dev-config.yaml', 'r') as f:
   data = yaml.load(f, Loader=yaml.FullLoader)

PA = data['feeds'][0]['psilocybinalpha']
TR = data['feeds'][1]['trufflereport']
CS = data['feeds'][2]['cannabisstock']
PSW = data['feeds'][3]['psychedelicstockwatch']
