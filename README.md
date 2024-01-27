# Aircraft Saftey Analysis

**Author**: Noah Meakins

## Overview
This in-depth analysis is intended to guide our company's foray into the commercial and private aviation sectors. By identifying historical safety risks and the most common causes of serious accidents, we aim to implement best practices and safety standards that surpass industry norms. This proactive approach to safety and risk analysis will be foundational in establishing our company as a responsible and trustworthy player in the aviation industry.

***

## Business Problem

My company has decided to expand in to new industries to diversify its portfolio. Specifically, they are interested in purchasing and operating airplanes for commercial and private enterprises. This project uses data cleaning, imputation, analysis, and visualization to generate insights into which models of airplane can be considered the safest for commercial and private flight. The data utilized this project was provided by Kaggle.com. The dataset is from the National Transportation Safety Board and includes aviation accident data from 1962 to 2023 about civil aviation accidents and selected incidents in the United States and international waters.

***

## Data
The data provided for this analysis is from the National Transportation Safety Board that includes aviation accident data from 1962 to 2023 about civil aviation accidents and selected incidents in the United States and international waters. This will provide enough data to determine what models will be the safest for commercial and private enterprises. It's relevant to our analysis as we aim to understand various aircraft models and the levels of saftey associated with them. The dataset consists of individual aircraft accidents, each record detailing the accident. It includes data from incidents in the United States and international waters. Key variables include Country, Location, Make, Model, Number of Engines, Engine Type, Weather Conditions, Injury Severity, and Aircraft Damage. For this analysis, in line with our company's focus on safety and risk assessment, the primary target variable is 'total fatal injuries'. Analyzing this variable will help us assess the severity of accidents and understand the safety challenges inherent in the aviation industry, especially pertinent to commercial and private flight operations.

***

## Methods
Our analysis began with a deep data cleansing process, where we refined our dataset by eliminating irrelevant entries and addressing any data quality issues such as missing or inconsistent values. We then proceeded to construct a series of visualizations and statistical models to explore correlations and patterns within the data, focusing particularly on factors that could influence aircraft safety. By grouping data by specific categories such as aircraft make and model, engine type, and year of incident, we were able to derive meaningful insights into historical safety performance. The outcomes of these analytical procedures were then made to isolate the top aircraft recommendations based on a balance of safety records and operational efficiency. This informed approach ensures that our final recommendations are data-driven, providing a large foundation for making well-considered decisions regarding aircraft selection.

***

## Results
Following a comprehensive process of data preparation, cleaning, and analytical modeling, I have identified three robust aircraft models suitable for recommendation. The analysis has distilled a list of prospective aircraft, each with the potential to serve effectively in commercial and private aviation enterprises. The manufacturers represented in the findings are renowned for their commitment to safety and reliability. The highlighted models are designed to accommodate a range of passenger capacities and are capable of traversing medium to long-haul routes efficiently.

Implementing this model into the business's decision-making process is anticipated to yield positive outcomes. The actionable insights derived from the analysis promise to enhance the strategic selection of aircraft, optimizing the balance between capacity, range, and safety. Nonetheless, it is essential to integrate these findings with a comprehensive risk assessment and to consider them as part of a broader decision framework that includes economic, technical, and regulatory factors.

***


## Conclusions
Through meticulous data preparation, cleansing, and analytical modeling, we have distilled a set of actionable insights and robust aircraft model recommendations tailored to the needs of the business. Our analysis has resulted in several potential models that align with both commercial and private operational requirements, emphasizing safety, reliability, and operational efficiency.

### Recommendations

Based on the findings of our analysis, it is recommended that the business:

Prioritize aircraft models with the lowest historical average of fatal injuries, as these suggest a better safety record.
Consider the operational context of aircraft usage, including the frequency of flights and the environments in which the aircraft operate, to make informed decisions beyond the data presented.
Factor in the technological advancements and safety features of newer models, which may not be fully reflected in historical data.

### Limitations

While the analysis provides a data-driven foundation for decision-making, several limitations must be acknowledged:

Historical data may not account for recent improvements in aircraft design and technology that enhance safety.
The analysis might not fully capture the operational diversity of aircraft usage, which can significantly impact safety outcomes.
External factors such as regulatory changes and maintenance practices, which play a crucial role in aircraft safety, have not been extensively analyzed.

### Future Improvements

To further refine the recommendations for this business problem and create a up-to-date analysis, the following steps could be utilized in the future:

Incorporate real-time data tracking to capture the latest trends and improvements in aircraft safety and performance.
Expand the scope of analysis to include a broader range of safety and performance metrics, offering a more comprehensive view of each aircraft model's operational profile.

In essence, while the analysis conducted provides a solid foundation for informed decision-making, it is crucial to approach the recommendations with an understanding of their inherent constraints and the dynamic nature of aviation safety. Continuous improvement in data collection, analysis techniques, and the incorporation of real-time operational data will significantly enhance the robustness of future recommendations.

It is also to important to consider that due to the state and quantity of the data provided in the original dataset, when choosing Airplane models, the possibility of a new version of the specific model should be conisdered. This can be resolved when communicating with sales representatives of the manufacture you choose for each industry. 
***


## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── README.md                           <- The top-level README for reviewers of this project
├── dsc-phase1-project-template.ipynb   <- Narrative documentation of analysis in Jupyter notebook
├── DS_Project_Presentation.pdf         <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
