# SEC 10-K Filing Insight Generator

This repository contains a Streamlit web application that generates insights from SEC 10-K filings for **any** public companies. 
The application allows users to input a stock ticker and select the word limit for the generated insights.

## To access the deployed application [click here](http://13.234.213.129:8501/)
![](InsightGenerator.gif)

## Features

- Fetches the latest SEC 10-K filings for the specified stock ticker.
- Cleans the data (removing html tags and other unwanted information) and extracts sections of the filing.
- Analyzes the text of the filings to generate insights for different sections: Business Overview, Risk Factors, and Financial Highlights.
- Displays the generated insights using Streamlit's user interface.
