#Scraping using BeautifulSoup
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

season = 01
while page != 06:
      url = f"https://gameofthronesscripts.wordpress.com/2016/03/13/s01e01{page}"
      print(url)
      page = page + 1