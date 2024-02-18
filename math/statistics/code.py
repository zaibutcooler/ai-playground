import os
import json

# Define the list of topics and corresponding descriptions
topics = [
    ("Probability Basics", "Introduction to basic probability concepts, including sample spaces, events, and probability rules."),
    ("Descriptive Statistics", "Exploration of data using measures such as mean, median, mode, variance, and standard deviation. Introduction to graphical representations like histograms and box plots."),
    ("Statistical Distributions", "Understanding common probability distributions such as the normal, binomial, and Poisson distributions."),
    ("Statistical Inference", "Fundamental concepts of statistical inference, including estimation, hypothesis testing, and confidence intervals."),
    ("Linear Regression", "Introduction to simple and multiple linear regression, including model fitting, interpretation, and diagnostics."),
    ("Data Visualization", "Techniques for visualizing data effectively, including scatter plots, bar charts, and heatmaps."),
    ("Hypothesis Testing", "Understanding hypothesis testing procedures, including types of errors, significance levels, and p-values."),
    ("Exploratory Data Analysis", "Exploration of data patterns, outliers, and relationships using statistical and visualization techniques."),
    ("Machine Learning Fundamentals", "Overview of basic machine learning concepts, including supervised and unsupervised learning, model evaluation, and cross-validation."),
    ("Multivariate Analysis", "Advanced analysis of data involving multiple variables, including principal component analysis and factor analysis."),
    ("Time Series Analysis", "Analysis of time-dependent data, including time series decomposition, forecasting, and trend analysis."),
    ("Experimental Design", "Principles of experimental design, including randomization, blocking, and factorial experiments."),
    ("Bayesian Statistics", "Introduction to Bayesian inference, including Bayesian estimation, hypothesis testing, and hierarchical modeling."),
    ("Statistical Computing with Python", "Introduction to statistical computing using Python, including data manipulation, visualization, and basic statistical analysis with libraries like NumPy, pandas, and Matplotlib."),
    ("Statistical Computing with R", "Introduction to statistical computing using R, including data manipulation, visualization, and basic statistical analysis with libraries like tidyverse and ggplot2."),
    ("Causal Inference", "Understanding causal relationships in observational and experimental data, including methods for causal inference."),
    ("Survival Analysis", "Analysis of time-to-event data, including survival curves, Kaplan-Meier estimation, and Cox proportional hazards models."),
    ("Text Mining and Natural Language Processing", "Introduction to text mining and NLP techniques for analyzing and extracting insights from text data."),
    ("Network Analysis", "Analysis of complex networks, including social networks, biological networks, and network visualization."),
    ("Deep Learning for Data Analysis", "Application of deep learning techniques for data analysis tasks, including image recognition, natural language processing, and time series forecasting.")
]


# Loop through the list of topics and create notebooks
for index, (topic, description) in enumerate(topics, start=1):
    # Construct the notebook filename
    notebook_filename = f"./{index:02d}_{topic.replace(' ', '_')}.ipynb"
    
    # Write description to the top cell of the notebook
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {topic}",
                    "",
                    description
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.11"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    # Write notebook content to file
    with open(notebook_filename, "w") as file:
        json.dump(notebook_content, file)

print("Notebooks created successfully!")
