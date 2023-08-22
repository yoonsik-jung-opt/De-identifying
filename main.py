import pandas as pd
import argparse
from tqdm import tqdm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('-p','--path', required=True, help='path of target data')
    parser.add_argument('-c', '--cols', required=True, help='de-identifying columns', nargs='*')
    parser.add_argument('--prefix', required=False, default='MASK', help='prefix of masked data')
    parser.add_argument('--save', required=True, help='masked dataset path & file name to save')
    parser.add_argument('--mapping', required=True, help='mapping table path & file name to save')

    args = parser.parse_args()
    # Read CSV File
    print('='*50, 'READ DATASET','='*50)
    df = pd.read_csv(args.path)
    deident_cols = args.cols
    unq_cols = [d for c in deident_cols for d in df[c].unique().tolist()]

    prefix = args.prefix
    print('='*50, 'CREATE MAPPING TABLE','='*50)
    mapping_dict = {}
    for i, col in enumerate(unq_cols):
        if col not in mapping_dict.keys():
            mapping_dict[col] = f'{prefix}_{i}'

    convert_mappting_dict = {}
    keys = [k for k in mapping_dict.keys()]
    values = [mapping_dict[k] for k in keys]
    convert_mappting_dict['key'] = keys
    convert_mappting_dict['value'] = values
    mapping_table = pd.DataFrame.from_dict(convert_mappting_dict)

    print('='*50, 'MASKING','='*50)
    for c in tqdm(deident_cols):
        for i in range(df.shape[0]):
            df[c].iloc[i] = mapping_dict[df[c].iloc[i]]
    

    # Save de-identified dataset
    print('='*50, 'SAVE DATA','='*50)
    df.to_csv(args.save, index=False)
    mapping_table.to_csv(args.mapping, index=False)

    