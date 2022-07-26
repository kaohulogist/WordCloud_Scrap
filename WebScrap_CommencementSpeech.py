import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

page_url = 'https://www.rev.com/blog/transcript-tag/commencement-speech-transcripts'
driver.get(page_url)



