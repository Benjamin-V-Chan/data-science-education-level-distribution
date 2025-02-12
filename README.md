# data-science-literacy-rate-age-groups

# Project Overview
This project analyzes the distribution of the highest level of education attained across different states, rural and urban areas, and gender groups. It includes data preprocessing, summary statistics, trend analysis, visualizations, and regional disparity analysis.

# Folder Structure
```
project-root/
├── data/                       # Contains the dataset
│   └── REPORT.csv
├── scripts/                    # Python scripts for data processing and analysis
│   ├── 01_preprocess.py
│   ├── 02_summary_statistics.py
│   ├── 03_trends_analysis.py
│   ├── 04_visualization.py
│   ├── 05_regional_disparity.py
├── outputs/                    # Stores cleaned data, results, and visualizations
│   ├── cleaned_data.csv
│   ├── summary_statistics.csv
│   ├── trends_analysis.csv
│   ├── education_distribution.png
│   ├── education_trends.png
│   ├── regional_disparity.csv
├── requirements.txt             # List of required Python dependencies
└── README.md                    # Project documentation
```

# Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 2. Run the Scripts:

#### Preprocess the dataset:
```bash
python scripts/01_preprocess.py
```
This script cleans the dataset and saves it as `outputs/cleaned_data.csv`.

#### Generate summary statistics:
```bash
python scripts/02_summary_statistics.py
```
Computes and saves summary statistics in `outputs/summary_statistics.csv`.

#### Analyze trends in education attainment:
```bash
python scripts/03_trends_analysis.py
```
Identifies trends in educational attainment over time and saves results in `outputs/trends_analysis.csv`.

#### Generate visualizations:
```bash
python scripts/04_visualization.py
```
Creates and saves key visualizations as images in the `outputs/` folder.

#### Analyze rural vs. urban educational disparities:
```bash
python scripts/05_regional_disparity.py
```
Computes disparities between rural and urban education levels and saves the results in `outputs/regional_disparity.csv`.

# Requirements
The required Python packages are listed in `requirements.txt`. Install them using:
```bash
pip install -r requirements.txt
```

# Acknowledgments
**Dataset Name:** Distribution of Highest Level of Education  
**Dataset Author:** EmptyAd  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/avis02/distribution-of-highest-level-of-education)