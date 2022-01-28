

# Microsoft Movie Analysis


# General Overview
The movie industry is know to many as one of the largest entertainment sectors in the world, projecting a market size measured in revenue as $18.2B in the year of 2022. Whether it's user streaming or general film production, there are a wide array of factors to consider before making a decision as to whether the film industry would be a lucrative entry point for Microsoft Corportation to make. 


# Business Understanding
One of the key deciding factors for Microsoft as a key stakeholder is the potential for long term growth. As a business that made $168B in revenue during the year of 2021, there is no doubt that the main factor for Microsoft's decision to enter the market is whether it can contribute to long term growth in their portfolio. As a team, we decided that these are the key questions to consider. Should Microsoft Movie corporation consider entering the foreign film market or remain within the domestic market before they build a solid portfolio? Which genres and what facet of the genre drives it's profitability? How are ratings related to film profitability? All of these are initial questions associated with revenue growth and profitability. 

# Data Understanding
We utilized two main data sets. The first database we used was The Movie Database API, the second database was from The Numbers: Where Data and the Movie Business Meet. The TMDb API is a large database that contains information ranging from genre and actors writer and director. From this set of data we were able to extract information associated with genre to understand which genres were more lucrative. We created a boolean based on movie title to see whether animated movies compared to regular movies within the same genre performed better. From The Numbers Budget dataset, we were able to web scrape the release date, movie title, production budget, domestic gross earnings, and the worldwide earnings. For the purposes of this project, this dataset was helpful in extracting the financials as a necessary means to filter an analyze foreign and domestic markets. Some important features and limitations that come from this data set come from how we can interpret financial indicators. In the case of the budgets associated with domestic and foreign markets, we found that it was important to strictly analyze within the time frame of 2014 to 2018. Our financial indicators do not account for inflation, however based of of this time frame, there was a 6% price increase. Since all of our values are calculated in USD, we can say 1 USD in 2014 is equivalent to 1.06 in 2018. 

# Methods
We imported data from both of these sources and merged them together, removing unneceesary data and duplicates to make a consistent analysis along all of our probing questions. We were able to use statistics and visualizations to gain keener insights into the trends associated with our pivotal factors. We were able to assess which genre types were the most lucrative along with whether foreign markets or domestic markets provided a larger portfolio.

# Data Analysis

As a means of filtering the data by date, we wanted to look at a time frame that was relevant to a consistent period within the movie and streaming industry. We chose the a range of realease years that fell within the time frame of 2014 to 2018. Our choice to include this time frame came from the prevalence of streaming services as a normal aspect of consumer decision making. Netflix also began their movie industry, creating their own original films and shows in 2014. Within this time frame we found foreign markets to perform 44.5% better in USD than domestic markets of the same film. 









Per our statistical data as shown in the boxplot below, when considering creating a movie in the Action, Comedy and Family genres, it behooves the studio to animate the film one can expect a 120% increase in profit.


![image (2)](https://user-images.githubusercontent.com/97462844/151560058-f94770c8-b1a3-4972-bba5-7d6282ac9392.png)










Written interpretation of statistics which inform business questions
3 visuals that provide value to the stakeholder 

# Conclusion
From our analysis, we can confirm that the three best tactics in terms of moving forward is to incorporate foreign markets into Microsoft's business strategy. Not only do foreign markets in total perform better than singularly domestics markets, but they also increase exposure for the brand. We found that ratings were not as highly associated with profit, but did find that 10% of the films from the sample contributed to 57% of overall profit within the movie industry. From this understanding we can say that film investment is something to consider in order to build a diverse film portfolio. Finally in terms of what genre to focus on, we found that animated genres preform 120% times better than their live action counter part, meaning that a animated comedy can perform much better than that of a live action film. Microsoft is a technology company, so we can hope that their technological expertise can propel them within the animation market. 









