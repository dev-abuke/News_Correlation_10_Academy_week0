import json
import argparse
import os
import io
import shutil
import copy
import csv
from datetime import datetime
from pick import pick
from time import sleep



# Create wrapper classes for using slack_sdk in place of slacker
class NewsDataLoader:
    '''
    Slack exported data IO class.

    When you open slack exported ZIP file, each channel or direct message 
    will have its own folder. Each folder will contain messages from the 
    conversation, organised by date in separate JSON files.

    You'll see reference files for different kinds of conversations: 
    users.json files for all types of users that exist in the slack workspace
    channels.json files for public channels, 
    
    These files contain metadata about the conversations, including their names and IDs.

    For secruity reason, we have annonymized names - the names you will see are generated using faker library.
    
    '''
    def __init__(self, path):
        '''
        path: path to the slack exported data folder
        '''
        self.path = path
        self.news = self.get_news()
        self.traffic = self.get_traffic()
        self.domain_location = self.get_domain_location()
    

    def get_news(self):
        '''
        write a function to get all the news from the csv file
        '''
        news = os.path.join(self.path, 'rating.csv')
        
        return news
    
    def get_traffic(self):
        '''
        write a function to get all the traffic from the csv file
        '''
        traffic = os.path.join(self.path, 'traffic.csv')

        return traffic  
      
    def get_domain_location(self):
        '''
        write a function to get all the domain_location from the csv file
        '''
        domain_location = os.path.join(self.path, 'domains_location.csv')

        return domain_location



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export News history')

    
    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()
