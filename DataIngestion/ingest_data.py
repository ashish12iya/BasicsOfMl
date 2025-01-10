import numpy as np
import pandas as pd 
from abc import ABC, abstractmethod
from pprint import pprint

import loggin


class DataIngestionStratergy(ABC):
    """
    this is the blue print for the DataIngestion
    """

    @abstractmethod
    def load_data()->pd.DataFrame:
        pass 



class IngestDataFromPath(DataIngestionStratergy): 
    """
    this will ingestion data from path
    """

    def load_data(data_path: str)-> pd.DataFrame: 
        try:

            df = pd.read_csv(data_path)
            loggin.info(f"Your data is sucessfully loaded from path : {path}")
            return df 
        
        expect Exception as e: 
            logging.erro(f"error during data ingestion : {e}")
            raise e 

