# Wheelbot Statistical Analysis

A simple statistical analysis project using the Mini Wheelbot Dataset to investigate the relationship between drive-wheel angular velocity and robot pitch angle.

![Uploading image.png…]()


## Project Overview

This project applies statistical analysis and machine learning techniques to real robotic sensor data collected from a self-balancing Mini Wheelbot.

The main objective is to investigate whether **drive-wheel angular velocity** is statistically associated with **robot pitch angle**.

The project demonstrates a basic workflow for analyzing robotic data using Python.

## Research Question

**Is drive-wheel angular velocity statistically associated with robot pitch angle?**

## Statistical Model

The primary model used in this project is **Simple Linear Regression**.

```text
Pitch = Intercept + Coefficient × Drive-Wheel Angular Velocity
```

### Variables

* **Independent variable (X):** Drive-wheel angular velocity
* **Dependent variable (Y):** Robot pitch angle

## Methodology

The project follows these steps:

1. Load the Wheelbot dataset
2. Select relevant sensor variables
3. Clean and prepare the data
4. Explore the data
5. Visualize the relationship between variables
6. Split the data into training and testing sets
7. Train a Simple Linear Regression model
8. Evaluate the model
9. Interpret the results

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook
* Git
* GitHub

## Repository Structure

```text
wheelbot-statistical-analysis/
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── wheelbot_analysis.ipynb
│
├── src/
│   └── analysis.py
│
├── results/
│   ├── figures/
│   └── model_results.txt
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

## Dataset

This project uses the **Mini Wheelbot Dataset**.

The dataset contains robotic sensor and motion data collected from a self-balancing robot.

The original dataset should be downloaded from its official source rather than stored directly in this repository.

Please refer to the original dataset source for dataset documentation, authorship, and licensing information.

## Results

The project analyzes:

* Relationship between wheel angular velocity and robot pitch
* Data distribution and trends
* Linear regression parameters
* Training and testing performance
* Model predictions
* Statistical interpretation

Results and generated figures are stored in the `results/` directory.

## Learning Objectives

This project is part of my learning journey in **Robotics and Intelligent Systems**.

It helps develop practical skills in:

* Robotic sensor-data analysis
* Statistical modeling
* Linear regression
* Python programming
* Data visualization
* Machine learning fundamentals
* Interpretation of robotic sensor relationships

## License

The source code and original work in this repository are released under the MIT License.

The Wheelbot dataset is subject to its own license and terms. Please refer to the original dataset source before using the dataset.

## Acknowledgment

I acknowledge the original authors and contributors of the Mini Wheelbot Dataset for providing the robotic data used in this project.

This repository contains my own data analysis, implementation, visualizations, and interpretation.
