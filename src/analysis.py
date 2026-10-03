# ============================================================
# MINI WHEELBOT STATISTICAL ANALYSIS
# Drive-Wheel Angular Velocity vs Robot Pitch
# ============================================================

import os
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import ( r2_score , mean_absolute_error , mean_squared_error )


# 1. PROJECT PATHS

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FILE = os.path.join( PROJECT_ROOT , "data" , "velocity_pitch" , "0.csv" )

RESULTS_DIR = os.path.join( PROJECT_ROOT , "results" )

os.makedirs(RESULTS_DIR, exist_ok=True)


# 2. VARIABLES

velocity_column = "/dq_DR/drive_wheel"
pitch_column = "/q_yrp/pitch"

# 3. LOAD DATA

print("=" * 60)
print("MINI WHEELBOT STATISTICAL ANALYSIS")
print("=" * 60)

print("\n[1] Loading dataset...")

df = pd.read_csv(DATA_FILE)

print("Dataset loaded successfully.")


# 4. DATASET INFORMATION


print("\n" + "=" * 60)
print("[2] DATASET INFORMATION")
print("=" * 60)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)


# 5. DATASET SUMMARY


print("\n" + "=" * 60)
print("[3] STATISTICAL SUMMARY")
print("=" * 60)

print(df.describe())


# ============================================================
# 6. MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("[4] DATA QUALITY CHECK")
print("=" * 60)

missing_values = df.isnull().sum()

print("\nMissing values by column:")
print(missing_values)

print(
    "\nTotal missing values:",
    missing_values.sum()
)


# ============================================================
# 7. DUPLICATES
# ============================================================

duplicate_count = df.duplicated().sum()

print("\nDuplicate rows:", duplicate_count)


# ============================================================
# 8. SELECT PROJECT VARIABLES
# ============================================================

print("\n" + "=" * 60)
print("[5] SELECT PROJECT VARIABLES")
print("=" * 60)

print("X:", velocity_column)
print("Y:", pitch_column)

analysis_df = df[[velocity_column, pitch_column]].copy()


# ============================================================
# 9. DATA CLEANING
# ============================================================

rows_before = len(analysis_df)

analysis_df = analysis_df.dropna()

rows_after = len(analysis_df)

print("\nRows before cleaning:", rows_before)
print("Rows after cleaning :", rows_after)
print("Rows removed        :", rows_before - rows_after)


# ============================================================
# 10. CREATE X AND Y
# ============================================================

X = analysis_df[[velocity_column]]

y = analysis_df[pitch_column]


# ============================================================
# 11. DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("[6] PROJECT VARIABLE STATISTICS")
print("=" * 60)

print("\nDrive-wheel angular velocity:")
print(X.describe())

print("\nRobot pitch:")
print(y.describe())


# ============================================================
# 12. CORRELATION
# ============================================================

correlation = X[velocity_column].corr(y)

print("\n" + "=" * 60)
print("[7] CORRELATION")
print("=" * 60)

print(f"Correlation coefficient: {correlation:.6f}")


# ============================================================
# 13. TRAIN / TEST SPLIT
# ============================================================

print("\n" + "=" * 60)
print("[8] TRAIN / TEST SPLIT")
print("=" * 60)

split_index = int(len(analysis_df) * 0.80)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))


# ============================================================
# 14. CREATE AND TRAIN MODEL
# ============================================================

print("\n" + "=" * 60)
print("[9] SIMPLE LINEAR REGRESSION")
print("=" * 60)

model = LinearRegression()

model.fit(X_train,y_train)

intercept = model.intercept_
coefficient = model.coef_[0]

print("\nIntercept:")
print(intercept)

print("\nCoefficient:")
print(coefficient)

print("\nRegression Equation:")

print(f"Pitch = {intercept:.6f} + "f"({coefficient:.6f} × Drive-Wheel Angular Velocity)")


# ============================================================
# 15. PREDICTIONS
# ============================================================

print("\n" + "=" * 60)
print("[10] PREDICTIONS")
print("=" * 60)

y_pred = model.predict(X_test)

prediction_results = pd.DataFrame({
    "Actual_Pitch": y_test.values,
    "Predicted_Pitch": y_pred,
    "Residual": y_test.values - y_pred
})

print(
    prediction_results.head(10)
)


# ============================================================
# 16. MODEL EVALUATION
# ============================================================

print("\n" + "=" * 60)
print("[11] MODEL EVALUATION")
print("=" * 60)

r2 = r2_score(
    y_test,
    y_pred
)

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

print(f"R²   : {r2:.6f}")
print(f"MAE  : {mae:.6f}")
print(f"RMSE : {rmse:.6f}")


# ============================================================
# 17. SAVE MODEL RESULTS
# ============================================================

results = pd.DataFrame({
    "Metric": [
        "Correlation",
        "Coefficient",
        "Intercept",
        "R2",
        "MAE",
        "RMSE"
    ],

    "Value": [
        correlation,
        coefficient,
        intercept,
        r2,
        mae,
        rmse
    ]
})

results_file = os.path.join(
    RESULTS_DIR,
    "model_results.csv"
)

results.to_csv(
    results_file,
    index=False
)


# ============================================================
# 18. SAVE PREDICTIONS
# ============================================================

prediction_file = os.path.join(
    RESULTS_DIR,
    "predictions.csv"
)

prediction_results.to_csv(
    prediction_file,
    index=False
)


# ============================================================
# 19. SAVE METRICS REPORT
# ============================================================

metrics_file = os.path.join(
    RESULTS_DIR,
    "metrics.txt"
)

with open(
    metrics_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "MINI WHEELBOT STATISTICAL ANALYSIS\n"
    )

    file.write(
        "Drive-Wheel Angular Velocity vs Robot Pitch\n\n"
    )

    file.write(
        f"Dataset rows: {len(df)}\n"
    )

    file.write(
        f"Clean rows: {len(analysis_df)}\n"
    )

    file.write(
        f"Training samples: {len(X_train)}\n"
    )

    file.write(
        f"Testing samples: {len(X_test)}\n\n"
    )

    file.write(
        f"Correlation: {correlation:.6f}\n"
    )

    file.write(
        f"Coefficient: {coefficient:.6f}\n"
    )

    file.write(
        f"Intercept: {intercept:.6f}\n"
    )

    file.write(
        f"R2: {r2:.6f}\n"
    )

    file.write(
        f"MAE: {mae:.6f}\n"
    )

    file.write(
        f"RMSE: {rmse:.6f}\n"
    )


# ============================================================
# 20. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)

print("\nGenerated files:")

print("- results/model_results.csv")
print("- results/predictions.csv")
print("- results/metrics.txt")

print("\nUse wheelbot.ipynb for visualization and graphs.")