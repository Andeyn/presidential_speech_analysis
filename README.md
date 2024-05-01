# Presidential Speech Analysis
### Overview ###
The purpose of this repository is to scrape the [UCSB's Database of Presidential Speeches](https://www.presidency.ucsb.edu/documents) to explore how geopolitical topics such as communism has changed over the years throughout diffferent wars and political shifts in accordance to the changes between Republican and Democratic presidents. 

This code aggregates all presidential speeches, perform sentiment analysis, and analyze the speeches by number of mentions of each country per speech and total mentions of each country.

### Things to Note ###
The code has been written Python in a Jupyter Notebook. 
To install Jupyter Notebook, follow the [link](https://jupyter.org/install).

### Table of Contents ### 
- scraping_data/scraping_all_speeches.ipynb scrapes [UCSB's Database of Presidential Speeches](https://www.presidency.ucsb.edu/documents).

- scraping_data/all_presidential_speeches.csv is all the compiled speeches from each category (i.e. oral speech, farewell addresses, weekly addresses, etc.)

- counting_speeches.ipynb aggregates the data.

- country_count_by_speech.csv is a matrix of the country count mentions by speech where (columns=country_codes, rows=speech_id) matched to all_presidential_speeches.csv for speech_id.


