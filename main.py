# -*- coding: utf-8 -*-
from apps import hackernews


if __name__ == "__main__":
    top = hackernews.HackerNewsTop()
    print(top)
    print(len(top))
    new = hackernews.HackerNewsNew()
    print(new)
    print(len(new))
    best = hackernews.HackerNewsBest()
    print(best)
    print(len(best))
