import facebook
from dotenv import load_dotenv
import os

load_dotenv()

def get_lastday_impressions(page_id):
    graph = facebook.GraphAPI(access_token=os.getenv("ACCESS_TOKEN"))
    page_impressions = graph.get_connections(id=page_id, connection_name='insights',metric='page_impressions')
    return page_impressions['data'][0]['values'][1]['value']

def get_lastday_engagement(page_id):
    graph = facebook.GraphAPI(access_token=os.getenv("ACCESS_TOKEN"))
    page_impressions = graph.get_connections(id=page_id, connection_name='insights',metric='page_impressions_viral',period='week')
    return page_impressions
    
val = get_lastday_engagement(os.getenv("PAGE_ID"))
print(val)