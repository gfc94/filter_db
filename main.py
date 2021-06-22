# This is a sample Python script.

# Press F6 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import config as cfg

def filter_files():

    normal_tissue = pd.read_csv(cfg.data['data'] + 'normal_tissue.tsv', sep='\t')
    pathology = pd.read_csv(cfg.data['data'] + 'pathology.tsv', sep='\t')
    vhldb = pd.read_csv(cfg.data['data'] + 'vhldb.csv', sep=';')
    vhldb = vhldb.loc[(vhldb.source == 'manual')]['hgnc_symbol']
    df_vhldb = pd.DataFrame()
    df_vhldb['Gene name'] = vhldb

    normal_tissue_merged = df_vhldb.merge(normal_tissue, on='Gene name')
    pathology_merged = df_vhldb.merge(pathology, on='Gene name')
    normal_tissue_merged.to_csv(cfg.data['data'] + 'normal_tissue_filtered.tsv', sep='\t')
    pathology_merged.to_csv(cfg.data['data'] + 'pathology_filtered.tsv', sep='\t')
    print(vhldb)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filter_files()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
