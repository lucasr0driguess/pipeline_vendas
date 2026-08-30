import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__) 

class Extract:

    def __init__(self):
        self._base_dir = Path(__file__).resolve().parents[2]/'data'

    def extraction_df(self) -> dict[str,pd.DataFrame]:
        logger.info('Iniciando extração do arquivo csv')
        
        files = ['clientes.csv','produtos.csv','vendas.csv']
        database_csv = {}

        for file in files: 
            path = f'{self._base_dir}\\{file}'
     
            try:
                df_data = pd.read_csv(path, sep=',', index_col=None)


                table_name= Path(file).stem

                if df_data.empty:
                    logger.warning(f'{file} está vazio') 
                    continue

                database_csv[table_name] = df_data
                logger.info(f'{file} carregado com {len(df_data)} registros')
                
            except FileNotFoundError as e:
                logger.exception(f'Arquivo {file} não encontrado')

        logger.info('Extração concluida')
        return database_csv    
    

    


if __name__ == '__main__':
    teste = Extract()
    df = teste.extraction_df()
    print(len(df))
    