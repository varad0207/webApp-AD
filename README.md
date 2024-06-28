# Detectify

Detectify is a Flask web application designed for comparative analysis of various anomaly detection algorithms. It empowers users to explore the performance of different algorithms on a variety of datasets.

Key Functionalities:

- Algorithm Selection: Choose one or more of our implemented Machine Learning algorithms for anomaly detection.
- Dataset Exploration: Select a univariate or multivariate dataset from our provided list.
- Model Training & Evaluation: The chosen algorithms are trained on the selected dataset in the backend.
- Performance Visualization: Results are presented through graphs and plots, including AUC curves.
- Evaluation Metrics: Performance is quantified using metrics like precision, recall, F1-score, and AUC score.
- Data Visualization (Univariate): Univariate datasets can be visualized to understand their data distribution.

## Datasets
The anomaly detection algorithms in Detectify are evaluated on various datasets. You can find the datasets used in this project at the following repository:
https://github.com/varad0207/Anomaly-Benchmarking-Datasets.git

## Installation & Usage

Prerequisites: Python Version 3.9 to 3.11 <br/>
Run the following commands in your terminal

1. Clone the repository 
```
git clone https://github.com/varad0207/webApp-AD.git
```

2. Create a virtual environment in the root directory of the project
```
python -m venv venv
```

3. Activate the virtual environment <br/>
Windows: ``` venv/Scripts/activate ```
MacOs/Linux: ``` source venv/bin/activate ```

4. Install dependencies
```
pip install -r requirements.txt
```

5. Run the application
```
python app.py
```

This will start the Detectify web application, typically accessible at ``` http://127.0.0.1:5000/ ``` in your web browser.

## Reference
This project is inspired by research presented in the paper: 
https://arxiv.org/pdf/2402.07281
