import sys
import os
from datetime import datetime
from tropycal import realtime
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_dir):
    """Setup logging configuration"""
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, 'storm_monitor.log')
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            RotatingFileHandler(log_file, maxBytes=1000000, backupCount=5),
            logging.StreamHandler(sys.stdout)
        ],
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def get_storm_data():
    """Fetch and format storm data"""
    output = []
    try:
        realtime_obj = realtime.Realtime(jtwc=True)
        active_storms = realtime_obj.list_active_storms()
        output.append(f"Number of active storms: {len(active_storms)}")
        
        if active_storms:
            output.append("\nActive storms details:")
            for storm_id in active_storms:
                try:
                    storm = realtime_obj.get_storm(storm_id)
                    output.append("=" * 40)
                    output.append(f"Storm ID: {storm_id}")
                    output.append(f"Name: {storm.name}")
                    output.append(f"Status: {getattr(storm, 'status', 'Unknown')}")
                    output.append(f"Category: {getattr(storm, 'category', 'Unknown')}")
                    output.append(f"Maximum Sustained Winds (knots): {getattr(storm, 'wspd', 'Unknown')}")
                    output.append(f"Minimum Pressure (hPa): {getattr(storm, 'mslp', 'Unknown')}")
                    output.append(f"Location: Lat {getattr(storm, 'lat', 'Unknown')}°N, Lon {getattr(storm, 'lon', 'Unknown')}°E")
                except Exception as e:
                    output.append(f"Error fetching details for Storm ID {storm_id}: {str(e)}")
        else:
            output.append("No active storms found.")
            
        return "\n".join(output)
    except Exception as e:
        return f"Error running storm monitor: {str(e)}"

def main():
    base_dir = "/Users/evangelos/Documents/tropycal_daily_tc_monitoring"
    data_dir = os.path.join(base_dir, "data")
    log_dir = os.path.join(base_dir, "logs")
    
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)
    
    setup_logging(log_dir)
    logging.info("Starting storm monitor script")
    
    try:
        current_date = datetime.now().strftime("%Y-%m-%d")
        output_file = os.path.join(data_dir, f"storm_data_{current_date}.txt")
        
        storm_data = get_storm_data()
        
        with open(output_file, "w") as f:
            f.write(f"Tropical Storm Report - {current_date}\n")
            f.write("=" * 50 + "\n\n")
            f.write(storm_data)
        
        logging.info(f"Successfully saved storm data to {output_file}")
        
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()
