import urlextract
from urlextract import URLExtract

import pandas as pd
import urllib.request as url
import re

# use urllib.request to retrieve txt file from url
data = url.urlopen("https://raw.githubusercontent.com/justindlc/randomdata/main/databases.txt")

extractor = URLExtract()

links = []
names = []

# data is HTTPResponse object, so it must be decoded
for line in data:
  decoded_line = line.decode("utf-8")
  urls = extractor.find_urls(decoded_line)
  links.append(urls) # adds urls as items to links list
  try: # adds link names as items to names list
    substring = re.search('target="_blank">(.*)</a>', decoded_line).group(1)
    names.append(substring)
  except AttributeError: # necessary to avoid errors
    substring = ''

# convert url list to strings
urls_cleaned = [str(s) for s in list]

# clean url list by removing [, ], and ' from items
urls_cleaned2 = [s.replace('[','') for s in list_cleaned]
urls_cleaned3 = [s.replace(']','') for s in list_cleaned2]
urls_cleaned4 = [s.replace("'","") for s in list_cleaned3]

# remove empty list items
urls_cleaned5 = [i for i in list_cleaned4 if i]

# create dataframe, populate with both lists as columns
df = pd.DataFrame()
df['URLS'] = urls_cleaned5
df['NAMES'] = names

# save dataframe as csv without the numbering column (index)
df.to_csv("databases.csv", index=False)


"""

References:

*   https://www.kite.com/python/answers/how-to-read-a-text-file-from-a-url-in-python
*   https://www.pythontutorial.net/python-basics/python-write-text-file/
*   https://www.kite.com/python/answers/how-to-get-the-substring-between-two-markers-in-python
*   https://www.kite.com/python/answers/how-to-remove-a-character-from-a-list-of-strings-in-python
*   https://stackoverflow.com/a/30964049
*   https://stackoverflow.com/a/3369000

"""