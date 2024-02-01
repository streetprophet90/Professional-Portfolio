from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()