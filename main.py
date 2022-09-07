"""
Earthquake and Popular news Monitoring
"""
from bmkg_earthquake_info import data_extraction, data_show

if __name__ == '__main__':
    print('Main Application')
    result = data_extraction()
    data_show(result)
