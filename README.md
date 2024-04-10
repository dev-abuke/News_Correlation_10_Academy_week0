# Welcome to Week-0 Task-1 of 10 Academy's intensive training program!

## Overview

This project focuses on leveraging Git and GitHub for version control, setting up a Python environment, implementing continuous integration and continuous deployment (CI/CD), and employing key performance indicators (KPIs) related to development environment setup and relevant skills. The project also involves utilizing the CRISP-DM framework for project planning and conducting exploratory data analysis (EDA) and statistical thinking.

## Table of Contents

- [Project Title](#Welcome-to-Week-0-Task-1-of-10-Academy's-intensive-training-program!)
  - [Overview](#overview)
  - [Goals to Achieve](#goals-to-achieve)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Branches](#branches)
    - [Commits](#commits)
    - [Code Organization](#code-organization)
    - [Notebooks](#notebooks)
        - [Day 1 Analysis](#day-1-analysis)
    - [Analysis Results](#analysis-results)
        - [Top and Bottom 10 Users](#top-and-bottom-users)
            - [By Reply Count](#Reply-Count)
            - [By Mention Count](#Mention-Count)
            - [By Message Count](#Message-Count)
        - [Top 10 Messages](#top-messages)
            - [By Reply Count](#Replies)
            - [By Mention Count](#Reactions)
            - [By Message Count](#Mentions)
        - [Channel Analysis](#channel-analysis)
        - [Time Analysis](#time-analysis)
  - [Contributing](#contributing)
  - [License](#license)

## Goals to Achieve

- **Dev Environment Setup:** Successfully set up the Python environment, Git version control, and CI/CD.
- **Relevant Skills Demonstration:** Showcase proficiency in the CRISP-DM framework, data understanding, EDA techniques, and statistical thinking.
- **Project Planning - EDA & Stats:** Effectively plan and execute the project using the CRISP-DM framework, perform EDA, and derive actionable insights from statistical analyses.

## Installation

To get started with the project, follow these installation steps:

1. **Python Environment:**
    ```bash
    python -m venv your_env_name
    ```

    Replace `your_env_name` with the desired name for your environment.
    
    **Activate the environment:**

    - On Windows:

    ```bash
    .\your_env_name\scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source your_env_name/bin/activate
    ```

2. **Clone this package**
    To install the `network_analysis` package, follow these steps:

    1. Clone the repository:
        ```bash
        git clone https://github.com/dev-abuke/News_Correlation_10_Academy_week0.git
        ```
    2. Navigate to the project directory:
        ```bash
        cd News_Correlation_10_Academy_week0
        ```
    
    3. Install the required dependencies:
        ```bash
        pip install -r requirements.txt
        ```


3. **Continuous Integration:**
    - CI/CD configurations are already set up. Refer to the CI/CD documentation for additional details.

## Usage

### Branches

In this repository, the branches are organized as follows:

- **main:** The main branch, initially forked from [https://github.com/10xac/week0_starter_network_analysis](https://github.com/10xac/week0_starter_network_analysis).

- **task-1:** The current branch for Day 1 analysis. 

  ```bash
  git checkout -b task-1
    ```


### Code Organization

Restructured the code by moving functions into `/src/loader.py` and `/src/utils.py`. In the analysis notebooks, used the `loader` from `/src/loader.py` and functions from `/src/utils.py` for data loading needs and helper functions.

## Notebooks
### Day 1 Analysis
`/notebooks/NewsEDA.ipynb`

## Analysis Results

### Top and Bottom Users

#### Reply Count
- Websites that have the largest count of news articles.
  - ***Top and Bottom 10 Websites - Article Count***
   ![Alt text](screenshots/top10newsarticles.png)
#### Mention Count
- Websites with the highest numbers of visitors traffic.
  - ***Top and Bottom 10 Websites - Global Rank***
    ![Alt text](screenshots/globalrank_bysource.png)
#### Message Count
- Countries with the highest number of news media organisations.
  - ***Top and Bottom 10 Websites - Media Count By Country***
    ![Alt text](screenshots/highestnumberofmediabycountry.png)
#### Message Count
- Countries that have many articles written about them.
  - ***Top and Bottom 10 Websites - Article By Country***
    ![Alt text](screenshots/top10botom10countrymentions.png)
#### Message Count
- Websites that reported (the news content) about Africa, US, China, EU, Russia, Ukraine, Middle East.
  - ***Top and Bottom 10 Websites - Africa***
    ![Alt text](screenshots/africa.png)
  - ***Top and Bottom 10 Websites - Europe***
    ![Alt text](screenshots/europe.png)
  - ***Top and Bottom 10 Websites - China***
    ![Alt text](screenshots/china.png)
  - ***Top and Bottom 10 Websites - Asia***
    ![Alt text](screenshots/asia.png)
  - ***Top and Bottom 10 Websites - USA***
    ![Alt text](screenshots/USA.png)
#### Reaction Count
- Websites with the highest count of positive, neutral, and negative sentiment.
  - ***Top and Bottom 10 Websites - Positive***
    ![Alt text](screenshots/positive_sentiment.png)
  - ***Top and Bottom 10 Websites - Negative***
    ![Alt text](screenshots/negative_sentiment.png)
  - ***Top and Bottom 10 Websites - Neutral***
    ![Alt text](screenshots/neutral_sentiment.png)

### Top 

- How similar are the number of words in the title  across sites
  - ***Top 10 Websites (Source) - Title Length***
  *Title Length Distribution*
  ![Alt text](screenshots/title_length_distribution.png)

- The impact of frequent news reporting and sentiment to the website’s global ranking.
  - ***Top 10 Messages - Reactions***
    - *Scatter plot*
    ![Alt text](screenshots/2dscatterplot.png)

## Contributing
Contributions are welcome! Before contributing, please review our contribution guidelines.

##  License
This project is licensed under the MIT License.
