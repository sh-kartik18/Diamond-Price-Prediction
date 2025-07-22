# Diamond Price Prediction

![Python](https://img.shields.io/badge/Python-3.13.5-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Manipulation-purple?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-yellow?logo=matplotlib)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-Regression-orange?logo=scikit-learn)
![Linear Regression](https://img.shields.io/badge/Model-Linear%20Regression-lightgrey)
![Ridge Regression](https://img.shields.io/badge/Model-Ridge%20Regression-lightgrey)
![Lasso Regression](https://img.shields.io/badge/Model-Lasso%20Regression-lightgrey)
![Decision Tree](https://img.shields.io/badge/Model-Decision%20Tree%20Regression-green)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest%20Regression-darkgreen)
![SVR](https://img.shields.io/badge/Model-Support%20Vector%20Regression-blueviolet)
![ANN](https://img.shields.io/badge/Model-Artificial%20Neural%20Network-red)

## Project Overview
This project aims to predict diamond prices using machine learning techniques. By analyzing various factors influencing the price, such as carat, cut, color, and clarity, the project delivers a robust predictive model. The dataset consists of 50,000 diamond records with 10 features. The final models are evaluated using metrics like R², Mean Absolute Error (MAE), and Mean Squared Error (MSE) to ensure accuracy and reliability.

## Problem Statement
Diamond pricing is influenced by multiple attributes such as carat, cut, clarity, and color. Accurately predicting diamond prices is crucial for fair trading, profitability, and transparency. This project employs machine learning models to develop an accurate price prediction system.

## Dataset
- **Source**: Kaggle / Tiffany & Co Diamond Pricelist
- **Size**: 50,000 rows, 10 columns
- **Features**:
  - `Carat`: Weight of the diamond
  - `Cut`: Quality of the cut (e.g., Ideal, Premium, Good, etc.)
  - `Color`: Color grade (D to J, where D is colorless and J is light yellow)
  - `Clarity`: Clarity grade (e.g., IF, VVS1, VS1, etc.)
  - `Depth`: Total depth percentage
  - `Table`: Width of the top of the diamond relative to its widest point
  - `X`, `Y`, `Z`: Dimensions of the diamond (length, width, height)
  - `Price`: Price in USD (Target variable)

## Data Preprocessing
- Checked for missing values and imputed them using different strategies: max, min, mean, standard deviation, and standardization.
- Scaled numerical features using **StandardScaler** to ensure balanced feature contributions.
- Applied **One-Hot Encoding** to categorical features (Cut, Color, Clarity) to convert them into numerical format.

## Exploratory Data Analysis (EDA)
- Visualized the distribution of diamond prices using histograms.
- Generated correlation heatmaps to examine relationships between features.
- Identified carat and price as the most strongly correlated features.

## Machine Learning Models Used
Several regression models were implemented and compared:
- **Linear Regression**
- **Ridge Regression**
- **Lasso Regression**
- **Decision Tree Regression**
- **Random Forest Regression**
- **Support Vector Regression (SVR)**
- **Artificial Neural Network (ANN)**

## Model Evaluation
The models were evaluated using:
- **Mean Absolute Error (MAE)**: Measures average prediction error.
- **Mean Squared Error (MSE)**: Penalizes larger errors.
- **R² Score**: Measures how well features explain price variance.

### Best Performing Models
- **Neural Network Regression**: Achieved the highest accuracy (lowest MAE and MSE, highest R²).
- **Random Forest Regression**: Also performed well, showing robust predictive power.

## Key Insights
- Feature selection and data preprocessing significantly impact model performance.
- Neural Networks effectively capture complex patterns in diamond pricing.
- Random Forest provides a strong alternative for non-linear price trends.
- Standardization improves consistency across regression techniques.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/sh-kartik18/Diamond-Price-Prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the data preprocessing script:
   ```bash
   python preprocess.py
   ```
4. Train and evaluate models:
   ```bash
   python train.py
   ```
5. View results and predictions:
   ```bash
   python evaluate.py
   ```

## Future Enhancements
- Incorporate additional features like fluorescence and certification.
- Optimize hyperparameters for further improvement.
- Deploy the model as a web application for real-time price predictions.


## Contributors
- **Kartik Sharma**

## License
This project is licensed under the MIT License.

