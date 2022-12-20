import pandas as pd

class HM():
    """
    Класс для получения основных файлов датасета
    """
    path_not_prepar = './data'
    path_prepar = './data_prepared'
    
    def __init__(self):
        pass
    
    def get_articles(self, is_prepared: bool = False): 
        path = self.path_not_prepar

        if is_prepared:
            path = self.path_prepar
            
        return pd.read_csv(f'{path}/articles.csv')
    
    def get_customers(self, is_prepared: bool = False):
        path = self.path_not_prepar

        if is_prepared:
            path = self.path_prepar
        
        return pd.read_csv(f'{path}/customers.csv')
    
    def get_transactions_train(self, is_prepared: bool = False):
        path = self.path_not_prepar

        if is_prepared:
            path = self.path_prepar

        return pd.read_csv(f'{path}/transactions_train.csv')

    def get_sample_submission(self):
        return pd.read_csv('./data/sample_submission.csv')