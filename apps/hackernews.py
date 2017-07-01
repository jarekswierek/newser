# -*- coding: utf-8 -*-
import requests
from datetime import date, datetime


API_URL = "https://hacker-news.firebaseio.com/v0/"


def get_date(timestamp):
    """Get date from timestamp.
    """
    return date.fromtimestamp(timestamp)


class Item():
    """Hacker News Item.
    """
    def __init__(self, id, title, url, type, time, *args, **kwargs):
        self.id = id
        self.title = title
        self.url = url
        self.type = type
        self.time = get_date(time)

    def __repr__(self):
        return repr(self.title)

class HackerNews():
    """Hacker News class with top, new and best stories.
    """
    def __init__(self, *args, **kwargs):
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.top = requests.get(API_URL + "topstories.json").json()
        self.new = requests.get(API_URL + "newstories.json").json()
        self.best = requests.get(API_URL + "beststories.json").json()

    def __repr__(self):
        return "Top, new and best stories from {}".format(self.timestamp)

    def get_item(self, item_id):
        """Method return Item object with given item id.
        """
        item_url = "item/{item_id}.json".format(item_id=item_id)
        url = API_URL + item_url
        r = requests.get(url)
        return Item(**r.json())
