# -*- coding: utf-8 -*-
from apps import hackernews


if __name__ == "__main__":
    new = hackernews.HackerNewsNew()
    print(new)
    new.print_top_ten()
