# Welcome 
# Task 1 of Week 0 | 10 Academy's intensive training program!

## Overview

This project is centered around harnessing the power of Git and GitHub for effective version control, establishing a Python-based environment, and integrating continuous integration and deployment (CI/CD) practices. It emphasizes the use of key performance indicators (KPIs) to monitor the setup of the development environment and the enhancement of pertinent skills. Additionally, the project incorporates the CRISP-DM framework for strategic project planning, and promotes the application of exploratory data analysis (EDA) and statistical reasoning.

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
  - [Contributing](#contributing)
  - [License](#license)

## Goals to Achieve
<!--todo add here a check box -->

- **Dev Environment Setup:**
- **Relevant Skills Demonstration:** 
- **Project Planning - EDA & Stats:** 

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
        git clone https://github.com/dev-abuke/News_Correlation_10_Academy_week0
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

Restructured the code by moving functions into `/src/loader.py` and `/src/utils.py`. In the analysis notebooks, used the `NewsDataLoader` from `/src/loader.py` and functions from `/src/utils.py` for data loading needs.

## Notebooks
### Day 1 Analysis
`/notebooks/NewsEDA.ipynb`

## Contributing
Contributions are welcome! Before contributing, please review our contribution guidelines.

##  License
This project is licensed under the MIT License.