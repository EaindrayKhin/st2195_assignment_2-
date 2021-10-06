#install.packages("rvest")
#install.packages("dplyr")

library(rvest)
library(dplyr)

link = "https://en.wikipedia.org/wiki/Comma-separated_values"
table = read_html(link)

wiki_table <- html_nodes(table,xpath='//*[@id="mw-content-text"]/div[1]/table[2]') %>% html_table()
my_df <- as.data.frame(wiki_table)
View(my_df)
write.csv(my_df, "cars.csv", row.names = FALSE)

