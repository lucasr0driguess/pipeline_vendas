import pandas as pd
from pathlib import Path


class Extract:

    base_dir = Path(__file__).resolve().parents[2]/ 'data'

    def extraction_df(self) -> list[pd.DataFrame]:
        files = ['clientes.csv','produtos.csv','vendas.csv']
        data_base = {}

        for file in files: 
            path = Extract.base_dir / file
            try:
                df_data = pd.read_csv(path, sep=',', index_col=None)

                table_name=  Path(file).stem
                if not df_data.empty:
                    data_base[table_name] = df_data 
                else:
                    print(f'{file} está vazio')

            except FileNotFoundError as e:
                print('Arquivo não encontrado')
                raise e

        return data_base

    


if __name__ == '__main__':
    e = Extract()
    c,p,v = e.extraction_df()

    print(c.head())
    print(p.head())
    print(v.head())
    