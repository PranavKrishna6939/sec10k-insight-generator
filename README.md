# SEC 10-K Filing Insight Generator

This repository contains a Streamlit web application that generates insights from SEC 10-K filings for **any** public companies. 
The application allows users to input a stock ticker and select a word limit for the generated insights.

## To access the deployed application [click here](http://13.234.213.129:8501/)
![](InsightGenerator.gif)

## Features

- Fetches the latest SEC 10-K filings for the specified stock ticker.
- Cleans the data (removing html tags and other unwanted information) and extracts sections of the filing.
- Analyzes the text of the filings to generate insights for different sections: Business Overview, Risk Factors, and Financial Highlights.
- Displays the generated insights using Streamlit's user interface.

## Tech Stack
- **Python:** Chosen for its versatility and extensive libraries for text processing.
- **Streamlit:** Selected for its simplicity in building interactive web applications with Python.
- **AWS EC2:** Program hosted on a EC2 instance for its ability to quickly setup python scripts.

## Prompt used for Insight Generation
```bash
Generate insights for the following SEC 10K Filing Part for {ticker} in about {word_count} words. ENSURE THAT YOU FOLLOW THE BELOW 4 GUIDELINES\n 1) Use multiple neccessary sub-heading with bullet points, discussing Fiscal Year Highlights, Products and Services Performance, Segment wise Performance, Operating Expenses and Gross margin, Liquidity and Capital Resources and Conclusion.\n 2) USE :orange[<insert sub-heading>] for sub-headings.\n 3) Present the answer in a markdown format.\n 4) DO NOT USE \' or \" characters in the answer.\n An example of a suitable format is given as:\n # :orange[Fiscal Year Highlights]\n {ticker}'s fiscal year 2024 witnessed: -\n **Rise in Product & Services Performance:**\n - Successful launch of Products.\n - Growth in Business. \n- Sustained leadership in Technology.\n Format your answer in such a way. The data to be summarised starts below this line \n {Part2_text}
```
