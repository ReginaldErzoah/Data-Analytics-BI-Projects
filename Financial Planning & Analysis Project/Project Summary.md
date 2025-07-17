# Financial Planning & Analysis Project Summary

## Project Objective:
To support strategic financial planning by comparing departmental budgets vs actuals, identifying cost variances, and enabling scenario-based forecasting for forward-looking insights and budget optimization.
This helps stakeholders understand how financial performance aligns with operational goals and plan for future resource allocation.

## Data Source:
Financial Dataset [expenses]: Budget VS Actual dataset from Kaggle.
https://www.kaggle.com/datasets/saharsyed/financial-dataset-expenses-budget-vs-actual?select=Financial+analysis_Data+Set.xlsx


## Analytics Procedure:
Data preparation was done in Power Query with additional transformations using DAX.
The BI report interface and structure were built in Power BI, with custom background visuals designed in Figma.

Key DAX measures were created for: Budget Utilization %, Forecasted Spend, Adjusted Budget (with What-If).
A What-If Budget Adjustment Slicer was included to simulate ±10% budget changes and visualize impact.

## Key Insights:
1. Departmental overspending was observed in Marketing, IT, HR, Finance and Operations in descending order.
2. Overall Budget Utilization stood at 99.82%, indicating tight budget control.
3. Scenario simulation suggests a 2% increase in budget would result in GHS 614,479 underspend, indicating potential for reallocation rather than expansion.

## Next Steps:
1. Automate monthly refreshes using Google Sheets → Power BI pipeline.
2. Incorporate performance-based scoring for departments based on budget discipline.

Explore the report and files in the project folder to see the full BI solution.
