from ntscraper import Nitter
import pickle
import json
import csv
import pandas as pd

scraper = Nitter(log_level=1)
username = "Microsoft"

sinceDate='2021-01-01'
untilDate='2023-11-06'

exportData = scraper.get_tweets(username, mode='user', since=sinceDate, until=untilDate)
nomeFile=username+"_"+sinceDate+"_"+untilDate+".json"
with open(nomeFile, "w") as file:
    json.dump(exportData, file)

#df = pd.read_json('Tesla_2021-01-01_2023-11-06.json', lines=True)
#df.to_csv('Tesla_2021-01-01_2023-11-06.csv', index=False)


