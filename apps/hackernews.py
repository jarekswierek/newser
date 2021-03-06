# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from datetime import date, datetime

import requests


API_URL = "https://hacker-news.firebaseio.com/v0/"


def get_date(timestamp):
    """Get date from timestamp.
    """
    return date.fromtimestamp(timestamp)


class Item:
    """Hacker News Item.
    """
    def __init__(self, id, title, type, time, *args, **kwargs):
        self.id = id
        self.title = title
        self.url = kwargs.get('url', '')
        self.type = type
        self.time = get_date(time)

    def __repr__(self):
        return repr(self.title)

class HackerNews(ABC):
    """Abstract Hacker News base class.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items = requests.get(self.url).json()
        self.items.reverse()

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return "{} from {!r}".format(self.name, self.timestamp)

    def __getitem__(self, position):
        return self.get_item(self.items[position])

    def __reversed__(self):
        return self[::-1]

    def pop(self):
        item_id = self.items.pop()
        return self.get_item(item_id)

    def get_item(self, item_id):
        """Method return Item object with given item id.
        """
        item_url = "item/{item_id}.json".format(item_id=item_id)
        url = API_URL + item_url
        r = requests.get(url)
        return Item(**r.json())

    @property
    def top_ten(self):
        """Top ten items.
        """
        return [self.get_item(self.items[i]) for i in range(10)]

    def print_top_ten(self):
        """Print top ten items in console.
        """
        for i, item in enumerate(self.top_ten, 1):
            print("\n{} [{}]".format(i, item.time))
            print(item)
            if item.url:
                print(item.url)

    @property
    @abstractmethod
    def url(self):
        pass


class HackerNewsTop(HackerNews):
    """Top Hacker News stories.
    """
    name = "Top stories"

    @property
    def url(self):
        return API_URL + "topstories.json"


class HackerNewsNew(HackerNews):
    """New Hacker News stories.
    """
    name = "New stories"

    @property
    def url(self):
        return API_URL + "newstories.json"


class HackerNewsBest(HackerNews):
    """Best Hacker News stories.
    """
    name = "Best stories"

    @property
    def url(self):
        return API_URL + "beststories.json"
