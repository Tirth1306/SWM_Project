# G12 - P1 - Survey: Web Data Scrapers
Aaryan Gupta

Krisha Vijay Gala

Pranav Kishor Katariya

Radhika Ganapathy

Tirth Patel

# Problem Statement

- Compare multiple data scraping techniques by automating the extraction of data from social media websites.
- Different types of scrapers are available such that some can be directly used without the need to know any programming language while some need extensive programming knowledge.
- A survey of these tools and frameworks will enable us to understand the advantages and disadvantages of using each technique on a particular website.
- In sum - Which scraper is good for what use-cases? Why? How?
- We finally compare 3 scrapers - Selenium, Scrapy and Reaper.social

# Datasets

In this project, we aim to scrape data from the following social media websites:
- Reddit: Titles, Timestamps, comments, number of upvotes, etc.
- Twitter: User Id, comments, likes count, retweet count, hashtags, tweet content, etc.
- Youtube: Channel Name, subscriber, hashtags, trending, likes, dislikes, publish date, etc.

How does Scraper collects this data? - Prepare for the execution of the agent -> Start the process of data extraction -> Gather raw data until the extraction process is completed -> Data is eventually structured in required format

Size of the datasets? User can define whatever size dataset they want when starting the scraper. We have considered low volume data as ~10 items and high volume data as ~1000 items for evaluations.

Data Processing? No data pre-processing needed before scraping. After data is scraper, we need to do data post-processing to parse the HTML responses into structured formats such as json or csv.

# Evaluations

<img width="430" alt="Evaluation table" src="https://user-images.githubusercontent.com/61615185/203661083-c864428a-1544-43e1-9e55-73ee5eee4c8c.png">

# Data Viz

