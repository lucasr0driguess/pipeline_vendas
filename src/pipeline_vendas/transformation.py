import pandas as pd
import datetime

class Transformation():


    def transform_cliente(self,data: pd.DataFrame) -> pd.DataFrame:
        data = data.dropna()
        data['cliente_id'] = data['cliente_id'].astype(int)
        return data


    def transform_vendas(self,data: pd.DataFrame) -> pd.DataFrame:
        num_columns = ['venda_id','cliente_id','produto_id','quantidade']
        data = data.dropna()
        data['data'] = pd.to_datetime(data['data'])
        data[num_columns] = data[num_columns].astype(int)

        return data

    def transform_produtos(self, data: pd.DataFrame) -> pd.DataFrame:
        data = data.dropna()
        data['produto_id'] = data['produto_id'].astype(int)
        data['preco'] = data['preco'].astype(float) 

        return data

    def transform_database(self, data_base: dict[str,pd.DataFrame]) -> dict[str,pd.DataFrame]:
        
        try:

            cliente = self.transform_cliente(data_base.get('clientes'))
            data_base['cliente'] = cliente
            vendas = self.transform_vendas(data_base.get('vendas'))
            data_base['vendas']= vendas
            produtos =self.transform_produtos(data_base.get('produtos'))
            data_base['produtos'] = produtos

            print('Tratamento concluido...')

            return data_base
        except Exception as e:
            print('Erro ao tentar tratar a base de dados')
            
            