import logging
import pandas as pd 
from sqlalchemy import create_engine, text 
from config import Settings

logger = logging.getLogger(__name__)
class Load:

    def __init__(self):
        self.engine = create_engine(Settings.DB_URL)

    def __load_clientes(self,data: pd.DataFrame) -> None:
        logger.info(f'Carregando {len(data)} clientes para o banco de dados')

        query = text("""
            INSERT INTO clientes (
                cliente_id,
                nome,
                cidade,
                estado
            ) VALUES (
                :cliente_id,
                :nome,
                :cidade,
                :estado
            ) 
            ON CONFLICT (cliente_id)
                DO UPDATE SET
                nome = EXCLUDED.nome,
                cidade = EXCLUDED.cidade,
                estado = EXCLUDED.estado
        """)

        data = data.to_dict(orient='records')


        with self.engine.begin() as conn:
            conn.execute(query,data)


    def __load_produtos(self,data: pd.DataFrame) -> None:
        logger.info(f'Carregando {len(data)} produtos para o banco de dados')

        query = text("""
            INSERT INTO produtos (
                produto_id,
                nome,
                categoria,
                preco
            ) VALUES (
                :produto_id,
                :nome,
                :categoria,
                :preco
            ) 
            ON CONFLICT (produto_id)
                DO UPDATE SET
                nome = EXCLUDED.nome,
                categoria = EXCLUDED.categoria,
                preco = EXCLUDED.preco
        """)
        
        data = data.to_dict(orient='records')
        
        
        with self.engine.begin() as conn:
                    conn.execute(query,data)

    def __load_vendas(self, data: pd.DataFrame) -> None:
        logger.info(f'Carregando {len(data)} vendas para o banco de dados')

        query = text("""
                    INSERT INTO vendas (
                        venda_id,
                        data,
                        cliente_id,
                        produto_id,
                        quantidade
                    ) VALUES (
                        :venda_id,
                        :data,
                        :cliente_id,
                        :produto_id,
                        :quantidade
                    ) 
                    ON CONFLICT (venda_id)
                        DO UPDATE SET
                        data = EXCLUDED.data,
                        cliente_id = EXCLUDED.cliente_id,
                        produto_id = EXCLUDED.produto_id,
                        quantidade = EXCLUDED.quantidade
                """)

        data = data.to_dict(orient='records')
                
                
        with self.engine.begin() as conn:
            conn.execute(query,data)

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
