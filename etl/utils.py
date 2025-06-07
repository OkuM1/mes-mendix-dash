import json
import logging
import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List
import os

def setup_logging(name: str, level: str = "INFO") -> logging.Logger:
    """
    Set up logging configuration
    
    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR)
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Create console handler if no handlers exist
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

def ensure_directory(path: str) -> None:
    """
    Ensure directory exists, create if it doesn't
    
    Args:
        path: Directory path to create
    """
    Path(path).mkdir(parents=True, exist_ok=True)

def save_to_json(data: Any, filepath: str) -> None:
    """
    Save data to JSON file
    
    Args:
        data: Data to save (dict, list, etc.)
        filepath: Output file path
    """
    ensure_directory(os.path.dirname(filepath))
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, default=str, ensure_ascii=False)
    
    logging.getLogger(__name__).info(f"Saved JSON data to {filepath}")

def save_to_csv(df: pd.DataFrame, filepath: str) -> None:
    """
    Save DataFrame to CSV file
    
    Args:
        df: Pandas DataFrame to save
        filepath: Output file path
    """
    ensure_directory(os.path.dirname(filepath))
    
    df.to_csv(filepath, index=False, encoding='utf-8')
    
    logging.getLogger(__name__).info(f"Saved CSV data to {filepath} ({len(df)} rows)")

def load_json(filepath: str) -> Any:
    """
    Load data from JSON file
    
    Args:
        filepath: Input file path
    
    Returns:
        Loaded data
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        logging.getLogger(__name__).info(f"Loaded JSON data from {filepath}")
        return data
        
    except FileNotFoundError:
        logging.getLogger(__name__).error(f"File not found: {filepath}")
        return None
    except json.JSONDecodeError as e:
        logging.getLogger(__name__).error(f"Error parsing JSON from {filepath}: {e}")
        return None

def load_csv(filepath: str) -> pd.DataFrame:
    """
    Load DataFrame from CSV file
    
    Args:
        filepath: Input file path
    
    Returns:
        Loaded DataFrame
    """
    try:
        df = pd.read_csv(filepath, encoding='utf-8')
        logging.getLogger(__name__).info(f"Loaded CSV data from {filepath} ({len(df)} rows)")
        return df
        
    except FileNotFoundError:
        logging.getLogger(__name__).error(f"File not found: {filepath}")
        return pd.DataFrame()
    except Exception as e:
        logging.getLogger(__name__).error(f"Error loading CSV from {filepath}: {e}")
        return pd.DataFrame()

def calculate_kpis(orders_df: pd.DataFrame, quality_df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate key performance indicators from production data
    
    Args:
        orders_df: Orders DataFrame
        quality_df: Quality metrics DataFrame
    
    Returns:
        Dictionary of calculated KPIs
    """
    kpis = {}
    
    if not orders_df.empty:
        # Production KPIs
        kpis['total_orders'] = len(orders_df)
        kpis['completed_orders'] = len(orders_df[orders_df['status'] == 'completed'])
        kpis['completion_rate'] = (kpis['completed_orders'] / kpis['total_orders'] * 100) if kpis['total_orders'] > 0 else 0
        
        # Efficiency KPIs
        kpis['avg_completion_percentage'] = orders_df['completion_percentage'].mean() if 'completion_percentage' in orders_df.columns else 0
        
        # Production volume
        kpis['total_planned_quantity'] = orders_df['quantity_planned'].sum()
        kpis['total_produced_quantity'] = orders_df['quantity_produced'].sum()
        kpis['production_efficiency'] = (kpis['total_produced_quantity'] / kpis['total_planned_quantity'] * 100) if kpis['total_planned_quantity'] > 0 else 0
    
    if not quality_df.empty:
        # Quality KPIs
        kpis['total_quality_tests'] = len(quality_df)
        kpis['passed_tests'] = len(quality_df[quality_df['result'] == 'pass'])
        kpis['quality_pass_rate'] = (kpis['passed_tests'] / kpis['total_quality_tests'] * 100) if kpis['total_quality_tests'] > 0 else 0
        kpis['defect_rate'] = 100 - kpis['quality_pass_rate']
    
    # Round all values to 2 decimal places
    kpis = {k: round(v, 2) if isinstance(v, float) else v for k, v in kpis.items()}
    
    logging.getLogger(__name__).info(f"Calculated {len(kpis)} KPIs")
    return kpis

def generate_summary_report(output_dir: str = "../data") -> Dict[str, Any]:
    """
    Generate a summary report from the latest processed data
    
    Args:
        output_dir: Directory containing processed data files
    
    Returns:
        Summary report dictionary
    """
    logger = logging.getLogger(__name__)
    
    # Find latest files
    data_path = Path(output_dir)
    
    latest_orders_csv = None
    latest_quality_csv = None
    latest_stats_json = None
    
    if data_path.exists():
        # Find most recent files
        orders_files = list(data_path.glob("orders_*.csv"))
        quality_files = list(data_path.glob("quality_*.csv"))
        stats_files = list(data_path.glob("production_stats_*.json"))
        
        if orders_files:
            latest_orders_csv = max(orders_files, key=lambda x: x.stat().st_mtime)
        if quality_files:
            latest_quality_csv = max(quality_files, key=lambda x: x.stat().st_mtime)
        if stats_files:
            latest_stats_json = max(stats_files, key=lambda x: x.stat().st_mtime)
    
    # Load latest data
    orders_df = load_csv(str(latest_orders_csv)) if latest_orders_csv else pd.DataFrame()
    quality_df = load_csv(str(latest_quality_csv)) if latest_quality_csv else pd.DataFrame()
    production_stats = load_json(str(latest_stats_json)) if latest_stats_json else {}
    
    # Calculate KPIs
    kpis = calculate_kpis(orders_df, quality_df)
    
    # Generate summary
    summary = {
        "report_timestamp": datetime.now().isoformat(),
        "data_sources": {
            "orders_file": str(latest_orders_csv) if latest_orders_csv else None,
            "quality_file": str(latest_quality_csv) if latest_quality_csv else None,
            "stats_file": str(latest_stats_json) if latest_stats_json else None
        },
        "kpis": kpis,
        "api_stats": production_stats,
        "data_freshness": {
            "orders_count": len(orders_df),
            "quality_tests_count": len(quality_df),
            "last_updated": datetime.now().isoformat()
        }
    }
    
    # Save summary report
    summary_file = data_path / f"summary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    save_to_json(summary, str(summary_file))
    
    logger.info("Generated summary report")
    return summary

def validate_data_quality(df: pd.DataFrame, required_columns: List[str]) -> Dict[str, Any]:
    """
    Validate data quality of a DataFrame
    
    Args:
        df: DataFrame to validate
        required_columns: List of required column names
    
    Returns:
        Validation report
    """
    report = {
        "is_valid": True,
        "row_count": len(df),
        "column_count": len(df.columns),
        "missing_columns": [],
        "null_counts": {},
        "duplicate_count": 0,
        "issues": []
    }
    
    if df.empty:
        report["is_valid"] = False
        report["issues"].append("DataFrame is empty")
        return report
    
    # Check required columns
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        report["is_valid"] = False
        report["missing_columns"] = missing_cols
        report["issues"].append(f"Missing required columns: {missing_cols}")
    
    # Check for null values
    null_counts = df.isnull().sum()
    report["null_counts"] = null_counts.to_dict()
    
    # Check for duplicates
    duplicate_count = df.duplicated().sum()
    report["duplicate_count"] = duplicate_count
    
    if duplicate_count > 0:
        report["issues"].append(f"Found {duplicate_count} duplicate rows")
    
    logging.getLogger(__name__).info(f"Data validation completed: {'PASSED' if report['is_valid'] else 'FAILED'}")
    return report
