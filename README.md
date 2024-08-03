# Django CSV Analyzer

This is a Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Features

- **File Upload:** Users can upload CSV files for analysis.
- **Data Processing:**
  - Displays the first few rows of the data.
  - Calculates summary statistics (mean, median, standard deviation) for numerical columns.
  - Identifies and handles missing values.
- **Data Visualization:** 
  - Generates and displays basic plots such as histograms for numerical columns.
- **User Interface:** 
  - Simple and user-friendly interface to interact with the application and view analysis results.

## Requirements

- Python 3.6 or higher
- Django 5.0.7 or higher
- pandas
- numpy
- matplotlib
- seaborn

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/csv_analyzer.git
cd csv_analyzer
