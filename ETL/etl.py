import csv
import psycopg2 

class luxury_housing_etl:
    def __init__(self,db_config):
        try:
            self.conn = psycopg2.connect(**db_config)
            self.cur = self.conn.cursor()
            print("🔗 Database connected successfully")
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            self.conn = None 
        
    def close_db(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        print("🔒 Database closed successfully")
    def load_data(self):
        with open(r'C:\Users\ASUS\Desktop\Projects\Luxury_house_sale_analysis\data\Cleaned\Luxury_Housing_Bangalore_cleaned_data.csv','r') as f:
            reader=csv.reader(f)
            next(reader)
            self.cur.execute(""" CREATE TABLE IF NOT EXISTS Luxury_housing_sales_data(
                             S_No INT,
                             Property_ID VARCHAR(20) PRIMARY KEY,
                             Micro_Market TEXT,
                             Project_Name TEXT,
                             Developer_Name TEXT,
                             Unit_Size_Sqft FLOAT,
                             Configuration TEXT,
                             Ticket_Price_Cr FLOAT,
                             Transaction_Type TEXT,
                             Buyer_Type TEXT,
                             Purchase_Quarter DATE,
                             Connectivity_Score FLOAT,
                             Amenity_Score FLOAT,
                             Possession_Status TEXT,
                             Sales_Channel TEXT,
                             NRI_Buyer TEXT,
                             Locality_Infra_Score FLOAT,
                             Avg_Traffic_Time_Min INT,
                             Buyer_Comments TEXT,
                             Price_Per_Sqft FLOAT,
                             Year INT,
                             Quarter INT)""")
            insert_query="""INSERT INTO Luxury_housing_sales_data(S_No,
                                 Property_ID,
                                 Micro_Market,
                                 Project_Name,
                                 Developer_Name,
                                 Unit_Size_Sqft,
                                 Configuration,
                                 Ticket_Price_Cr,
                                 Transaction_Type,
                                 Buyer_Type,
                                 Purchase_Quarter,
                                 Connectivity_Score,
                                 Amenity_Score,
                                 Possession_Status,
                                 Sales_Channel,
                                 NRI_Buyer,
                                 Locality_Infra_Score,
                                 Avg_Traffic_Time_Min,
                                 Buyer_Comments,
                                 Price_Per_Sqft,
                                 Year,
                                 Quarter) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            for row in reader:
                self.cur.execute(insert_query,row)
            print("Data loaded successfully")
                
    
if __name__=="__main__":
    db_config={
        "host":"localhost",
        "database":"luxury_housing_sales",
        "user":"postgres",
        "password":"root"

    }

    etl=luxury_housing_etl(db_config)
    etl.load_data()
    etl.close_db()


    
        