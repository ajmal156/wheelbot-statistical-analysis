## Dataset Analysis

This project uses the **Mini Wheelbot Dataset** from the official Wheelbot repository.

The analysis focuses on two variables from the original dataset:

| Variable             | Dataset Field        | Role                     |
| -------------------- | -------------------- | ------------------------ |
| Drive-wheel velocity | `/dq_DR/drive_wheel` | Independent variable (X) |
| Robot pitch angle    | `/q_yrp/pitch`       | Dependent variable (Y)   |

The analysis investigates the statistical relationship between drive-wheel velocity and robot pitch angle using **Simple Linear Regression**.

### Research Question

> Is drive-wheel velocity statistically associated with robot pitch angle?

### Analysis Workflow

```text
Mini Wheelbot Dataset
        ↓
Select relevant dataset fields
        ↓
/dq_DR/drive_wheel
        +
/q_yrp/pitch
        ↓
Data preprocessing
        ↓
Exploratory visualization
        ↓
Train / Test Split
        ↓
Simple Linear Regression
        ↓
Model Evaluation
        ↓
Interpretation
```

### Regression Model

The model estimates robot pitch angle from drive-wheel velocity:

```text
Pitch = Intercept + Coefficient × Drive-Wheel Velocity
```

Where:

* **X = `/dq_DR/drive_wheel`**
* **Y = `/q_yrp/pitch`**

The regression model is used as an introductory statistical model to examine the association between these two robotic variables. It should not be interpreted as establishing a causal relationship.

## Original Dataset

**Mini Wheelbot Dataset — Official Repository**

https://github.com/wheelbot/dataset

The original dataset repository contains the dataset documentation, variable descriptions, examples, and information about obtaining the data.

The dataset itself is not redistributed in this repository.

## My Contribution

My contribution to this project consists of:

* Selecting relevant Wheelbot variables
* Preparing the data for analysis
* Performing exploratory data analysis
* Implementing Simple Linear Regression
* Evaluating model performance
* Creating visualizations
* Interpreting the statistical results
* Organizing the analysis into a reproducible project structure

The underlying dataset belongs to the original Wheelbot dataset authors and contributors.

## Attribution

I acknowledge the original authors and contributors of the **Mini Wheelbot Dataset**.

This repository contains an independent analysis using the publicly available dataset and does not claim ownership of the original data.

Please refer to the original Wheelbot repository for the dataset's official documentation, citation requirements, and license.
