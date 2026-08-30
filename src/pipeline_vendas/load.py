import logging
import pandas as pd 
from sqlalchemy import create_engine 
from config import Settings

logger = logging.getLogger(__name__)
class Load:

    def __init__(self):
        self.engine = create_engine(Settings.DB_URL)

    def __load_clientes(self,data: pd.DataFrame) -> None:
        logger.info(f'Carregando {len(data)} clientes para o banco de dados')
        data.to_sql(
            name='clientes',
            con=self.engine,
            if_exists='append',
            index=False
        )


    def __load_produtos(self,data: pd.DataFrame) -> None:
        logger.info(f'Carregando {len(data)} produtos para o banco de dados')

        data.to_sql(
            name='produtos',
            con=self.engine,
            if_exists='append',
            index=False
        )

    def __load_vendas(self, data: pd.DataFrame) -> None:
        logger.info(f'Carregando {len(data)} vendas para o banco de dados')

        data.to_sql(
                name='vendas',
                con=self.engine,
                if_exists='append',
                index=False
            )

    def load_database(self,data_base: dict[str,pd.DataFrame]):


        try:
            self.__load_clientes(data_base.get('clientes'))
            self.__load_produtos(data_base.get('produtos'))
            self.__load_vendas(data_base.get('vendas'))

            logger.info('A base de dados foi carregada com sucesso')
        except:
            logger.exception('Erro ao carregar a base de dados')
            raise
        
        


if __name__ == '__main__':
    pass
