import logger

from extract import Extract
from transform import Transform
from load import Load

if __name__ == "__main__":
    extractor = Extract()
    transform = Transform()
    load = Load()
    
    df_dict = extractor.extraction_df()
    df_database_tratada = transform.transform_database(df_dict)
    load.load_database(df_database_tratada)