from rdkit import Chem
from rdkit.Chem.ChemUtils import SDFToCSV

def sdf2csv(csv_name, sdf_name):
    '''
    Convert sdf to csv
    '''
    f = open(csv_name, 'w')
    suppl = Chem.SDMolSupplier(sdf_name)
    SDFToCSV.Convert(suppl, f)
    f.close()
    print('Done.')
    
