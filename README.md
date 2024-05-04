# SEC 10-K Filing Insight Generator

This repository contains a Streamlit web application that generates insights from SEC 10-K filings for **any** public companies. 
The application allows users to input a stock ticker and select a word limit for the generated insights.

### To access the deployed application [click here](http://13.234.213.129:8501/)
![](InsightGenerator.gif)

## Features

- Fetches the latest SEC 10-K filings for the specified stock ticker.
- Cleans the data (removing html tags and other unwanted information) and extracts sections of the filing.
- Analyzes the text of the filings to generate insights for different sections: `Business Overview`, `Risk Factors`, and `Financial Highlights`.
- Displays the generated insights using Streamlit's user interface.

## Tech Stack
- `Python:` Chosen for its versatility and extensive libraries for text processing.
- `Streamlit:` Selected for its simplicity in building interactive web applications with Python.
- `AWS EC2:` Program hosted on a EC2 instance for its ability to quickly setup python scripts.

## Prompt used for insight generation
```
Generate insights for the following SEC 10K Filing Part for {ticker} in about {word_count} words. ENSURE THAT YOU FOLLOW THE BELOW 4 GUIDELINES
1) Use clear sub-headings with bullet points to discuss key aspects such as Fiscal Year Highlights, Products and Services Performance, Segment wise Performance, Operating Expenses and Gross margin, Liquidity and Capital Resources and Conclusion.
2) USE :orange[<insert sub-heading>] for sub-headings.
3) Present the answer in a markdown format.
4) Avoid using single or double quotation marks in the response.
An example of a suitable format is given as:
:orange[Fiscal Year Highlights]
{ticker}'s fiscal year 2024 witnessed:
- Rise in Product & Services Performance:
- Successful launch of Products.
- Growth in Business.
- Sustained leadership in Technology.
Format your answer in such a way. The data to be summarised starts below this line
{Part3_text}
```
One of the three similar prompts used for insight generation. Prompts designed such as to provide a rough overview of the inner workings of the company.

## Insight Categories

### 1. `Business Overview`
Generates insights for the text extracted from `Item 1.` of the 10K filing. Explore the heart of the company's operations. Discover its products, services, and market position, along with insights into industry competition.
### 2. `Risk Factors`
Generates insights for the text extracted from `Item 1A.` of the 10K filing. Understand the risks that could impact the company's performance and explore strategies for risk mitigation.
### 3. `Financial Highlights`
Generates insights for the text extracted from `Item 7.` of the 10K filing. Gain insights into the company's financial performance, including revenue trends, operating expenses, and gross margins.

## Scope of improvement over current version
Only the latest SEC 10K filing used for insight generation. Use of previous available reports to generate insights will allow to:
- Draw comparision to determine the shift in goals and priorities of a company, by tracking the frequency of usage of a particular word (such as Artificial Intelligence) over the years.
- Analyse the growth in financial performance of a company, compare the split of revenue between different products and services offered.
- Determine the sentiment of board members surrounding the company.

## Acknowledgments
- `Financial Services Innovation Lab, Georgia Tech`, for providing the programming task.
- Google for developing the `Gemini Pro` model used for generating insights.

