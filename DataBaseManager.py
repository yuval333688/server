import os
from supabase import create_client, Client



class DataBaseManager:
    instance: DataBaseManager = None

    def __init__(self):
        if DataBaseManager.instance is None:
            DataBaseManager.instance = self
            self.supabase = self.initialize_supabase()



    def initialize_supabase(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        supabase: Client = create_client(url, key)
        return supabase

    def getCountryBorder(self,countryName:str):
        response = ( self.supabase.table("countryBorder")
                .select("border")
                .eq("name", countryName)
                .execute())
        
        arr  =  response.data[0]['border']
        borderarr = []
        for i in range(len(arr)):
            coords = list(map(int, arr[i].split(',')))
            borderarr.append(coords)
        return borderarr

            
            
        
           
        
        
    



  

        
        
        
        
       
