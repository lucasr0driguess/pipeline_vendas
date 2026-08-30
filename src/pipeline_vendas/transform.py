import pandas as pd
import logging


logger = logging.getLogger(__name__)
class Transform():


    def __transform_cliente(self,data: pd.DataFrame) -> pd.DataFrame:
        
        logger.info('Tratando elementos nulos de clientes')
        data = data.dropna()

        logger.info('Conversão de tipagem de clientes')
        data['cliente_id'] = data['cliente_id'].astype(int)

        return data


    def __transform_vendas(self,data: pd.DataFrame) -> pd.DataFrame:
        num_columns = ['venda_id','cliente_id','produto_id','quantidade']

        logger.info('Tratando elementos nulos de vendas')
        data = data.dropna()

        logger.info('Conversão de tipagem de vendas')
        data['data'] = pd.to_datetime(data['data'])
        data[num_columns] = data[num_columns].astype(int)

        return data

    def __transform_produtos(self, data: pd.DataFrame) -> pd.DataFrame:

        logger.info('Tratando elementos nulos de produtos')
        data = data.dropna()

        logger.info('Conversão de tipagem de produtos')
        data['produto_id'] = data['produto_id'].astype(int)
        data['preco'] = data['preco'].astype(float) 

        return data

    def transform_database(self, database: dict[str,pd.DataFrame]) -> dict[str,pd.DataFrame]:
        
        try:

            logger.info('Iniciando transformação de clientes.csv')

            df_clientes = database['clientes']
            clientes_tratados = self.__transform_cliente(df_clientes)
            database['clientes'] = clientes_tratados

            logger.info(f"Clientes: {len(df_clientes)} → {len(clientes_tratados)} registros")

            logger.info('Iniciando transformação de vendas.csv')
            df_vendas = database['vendas']
            vendas_tratadas = self.__transform_vendas(df_vendas)
            database['vendas']= vendas_tratadas

            logger.info(f"Vendas: {len(df_vendas)} → {len(vendas_tratadas)} registros")

            logger.info('Iniciando transformação de produtos.csv')
            df_produtos = database['produtos']
            produtos_tratados =self.__transform_produtos(df_produtos)
            database['produtos'] = produtos_tratados

            logger.info(f"Produtos: {len(df_produtos)} → {len(produtos_tratados)} registros")

            logger.info('Tratamento concluido')

            return database
        
        except Exception as e:
            logger.exception('Erro ao tentar tratar a base de dados')
            raise

            