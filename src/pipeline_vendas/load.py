import pandas as pd # pyright: ignore[reportMissingModuleSource]
from sqlalchemy import create_engine # pyright: ignore[reportMissingImports]
from pipeline_vendas.config import Settings


class Load:

    def __init__(self):
        self.engine = create_engine(Settings.DB_URL)

    def load_clientes(self,data: pd.DataFrame) -> None:

        data.to_sql(
            name='clientes',
            con=self.engine,
            if_exists='append',
            index=False
        )


    def load_produtos(self,data: pd.DataFrame) -> None:

        data.to_sql(
            name='produtos',
            con=Load.engine,
            if_exists='append',
            index=False
        )

    def load_vendas(self, data: pd.DataFrame) -> None:

        data.to_sql(
                name='vendas',
                con=Load.engine,
                if_exists='append',
                index=False
            )

    def load_data_base(self,data_base: dict[str,pd.DataFrame]):

        self.load_clientes(data_base.get('clientes'))
        self.load_produtos(data_base.get('produtos'))
        self.load_vendas(data_base.get('vendas'))

        print('A base de dados foi carregada com sucesso')
        
        
        


if __name__ == '__main__':
    teste = Load()
    
    dados = {
        'cliente_id': [4],
        'nome': ['Julia'],
        'cidade': ['Goiania'],
        'estado': ['GO'],
    }

    df = pd.DataFrame(dados)
    
    teste.load_clientes(df)