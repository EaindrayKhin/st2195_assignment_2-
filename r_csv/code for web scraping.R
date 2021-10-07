library('rvest')
wikicsv_url <- 'https://en.wikipedia.org/wiki/Comma-separated_values'
wikitable <- read_html(wikicsv_url) %>%
  html_nodes(xpath = '//*[@id="mw-content-text"]/div[1]/table[2]') %>%
  html_table()  

wikitable

write.csv(wikitable, file = 'r_web_scraping.csv')
readLines('r_web_scraping.csv')
read.csv('r_web_scraping.csv')
