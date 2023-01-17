This repo is for the Sayari Data Assignment
<!-- Explain each file in the repo-->
## Files
1. `README.md` - This file
2. `data` - This folder contains the data files
3. `src` - This folder contains the source code
4. `output` - This folder contains the output files

## File Descriptions

`src/spider_x_business.py` scrapes data on active businesses starting with X and saves them to `data/x_business.json`

`src/plot_graph.py` reads `data/x_business.json` and draws a graph of the relationships between entities in it and saves it to `output/plot.png`

## How to run   
1. Clone the repo
2. Run `python3 src/spider_x_business.py` to scrape data on active businesses starting with X
3. Run `python3 src/plot_graph.py` to draw a graph of the relationships between entities in the scraped data




