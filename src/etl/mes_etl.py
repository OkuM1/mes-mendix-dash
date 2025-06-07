"""
MES ETL Pipeline
Siemens Mobility Demo Project

Clean, professional ETL script that:
1. Fetches data from MES API
2. Processes and validates it with Pandas
3. Calculates KPIs
4. Exports results for Mendix dashboard
"""

import requests
import pandas as pd
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MESProcessor:
    """Handles ETL processing for manufacturing data"""
    
    def __init__(self, api_url: str = "http://localhost:8000"):
        self.api_url = api_url
        
    def fetch_work_orders(self) -> pd.DataFrame:
        """Get work order data from the API and convert to DataFrame"""
        try:
            response = requests.get(f"{self.api_url}/api/v1/workorders")
            response.raise_for_status()
            
            data = response.json()
            df = pd.DataFrame(data)
            
            logger.info(f"Fetched {len(df)} work orders from API")
            return df
            
        except requests.RequestException as e:
            logger.error(f"Failed to fetch data: {e}")
            return pd.DataFrame()
    
    def fetch_kpis(self) -> dict:
        """Fetch calculated KPIs from API"""
        try:
            response = requests.get(f"{self.api_url}/api/v1/kpis")
            response.raise_for_status()
            return response.json()
            
        except requests.RequestException as e:
            logger.error(f"Failed to fetch KPIs: {e}")
            return {}
    
    def process_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean up the data and add some useful calculated fields"""
        if df.empty:
            return df
        
        # Clean up data types
        df['order_id'] = df['order_id'].astype(str)
        df['quantity_planned'] = pd.to_numeric(df['quantity_planned'], errors='coerce')
        df['quantity_produced'] = pd.to_numeric(df['quantity_produced'], errors='coerce')
        
        # Calculate some useful metrics
        df['completion_percentage'] = (df['quantity_produced'] / df['quantity_planned'] * 100).round(2)
        df['status_priority'] = df['status'].map({
            'completed': 4,
            'in_progress': 3,
            'pending': 2,
            'on_hold': 1
        })
        
        logger.info("Data processing completed")
        return df
    
    def export_results(self, df: pd.DataFrame, kpis: dict):
        """Export processed data for Mendix consumption"""
        import os
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        data_dir = os.path.join(os.path.dirname(__file__), "../data")
        
        # Export work orders as CSV for Mendix import
        csv_file = os.path.join(data_dir, f"processed_orders_{timestamp}.csv")
        df.to_csv(csv_file, index=False)
        logger.info(f"Exported work orders to {csv_file}")
        
        # Export KPIs as JSON
        kpi_file = os.path.join(data_dir, f"kpis_{timestamp}.json")
        with open(kpi_file, 'w') as f:
            json.dump(kpis, f, indent=2)
        logger.info(f"Exported KPIs to {kpi_file}")
        
        return csv_file, kpi_file
    
    def print_summary(self, df: pd.DataFrame, kpis: dict):
        """Print professional summary for demo purposes"""
        print("\n" + "="*60)
        print("MES DATA PROCESSING SUMMARY")
        print("="*60)
        
        if not df.empty:
            print(f"📊 Total Work Orders: {len(df)}")
            print(f"✅ Completed: {kpis.get('completed_orders', 0)}")
            print(f"🔄 In Progress: {kpis.get('in_progress_orders', 0)}")
            print(f"⏳ Pending: {kpis.get('pending_orders', 0)}")
            print(f"📈 Completion Rate: {kpis.get('completion_rate', 0)}%")
            print(f"⚡ Production Efficiency: {kpis.get('efficiency', 0)}%")
            
            print("\n📋 Order Status Breakdown:")
            status_counts = df['status'].value_counts()
            for status, count in status_counts.items():
                print(f"   {status.title()}: {count}")
                
        print("="*60)
    
    def run_pipeline(self):
        """Execute the complete ETL pipeline"""
        logger.info("Starting MES ETL Pipeline")
        
        # Step 1: Extract
        df = self.fetch_work_orders()
        kpis = self.fetch_kpis()
        
        if df.empty:
            logger.error("No data retrieved. Check API connection.")
            return
        
        # Step 2: Transform
        df = self.process_data(df)
        
        # Step 3: Load (Export)
        csv_file, kpi_file = self.export_results(df, kpis)
        
        # Step 4: Summary
        self.print_summary(df, kpis)
        
        logger.info("ETL Pipeline completed successfully")
        return df, kpis

if __name__ == "__main__":
    processor = MESProcessor()
    processor.run_pipeline()
