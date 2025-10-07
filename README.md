# Customer Personality Analysis  

### 📊 Big Data Analytics Project (MBA - Business Analytics)  

This project leverages **Big Data tools and frameworks** to analyze the financial and demographic behaviour of **20,000 individuals**. The goal is to uncover trends in income, expenses, and savings, while also building predictive and recommendation models to support **financial planning, advisory, and targeted interventions**.  

---

## 🚀 Project Overview  
- **Objective:** Understand how different population segments earn, spend, and save money.  
- **Dataset:** 20,000 records with demographic, financial, and behavioural attributes.  
- **Tools & Technologies:**  
  - **Hadoop Ecosystem:** HDFS, Hive, Pig, MapReduce, Sqoop  
  - **PySpark & MLlib:** Data preprocessing, Linear Regression, Recommendation system  
  - **SQL & HiveQL:** Querying and aggregation for insights  

---

## 📂 Dataset Features  
- **Demographics:** Age, Occupation, City Tier, Dependents  
- **Financials:** Income, Fixed & Discretionary Expenses, Loan Repayments, Insurance  
- **Savings:** Desired Savings %, Disposable Income, Savings Gap  
- **Derived Metrics:** Expense Ratio, Potential Savings per category  

---

## 🔑 Key Insights  
- **City Tiers:**  
  - Tier 2 has the largest user base.  
  - Tier 3 surprisingly shows the **highest disposable income**.  
  - Tier 1 users spend the **largest share of income (highest expense ratio)**.  
- **Spending Behaviour:**  
  - Tier 1: More on **essential expenses (e.g., education, rent)**.  
  - Tier 3: Higher **discretionary spending flexibility**.  
- **High Spenders:** 18.6% of Tier 1 users spend >90% of income (financially vulnerable).  
- **Savings Gap:** All tiers show **negative savings gap**, worst in Tier 3.  
- **Occupations:** Professionals dominate across tiers, but expense behaviour is similar across jobs.  

---

## 🛠️ Project Components  

1. **Data Preprocessing (PySpark)**  
   - Type casting, feature engineering, handling missing values.  
   - Derived features: Expense Ratio, Savings Gap, Essential vs Discretionary expenses.  

2. **HDFS (Hadoop Distributed File System)**  
   - Storage and distributed file operations for large-scale processing.  

3. **Hive & Pig**  
   - SQL-like queries and aggregation for descriptive analytics.  

4. **MapReduce Programs**  
   - Custom scripts to calculate average expense ratios, occupation mix, and top spending categories.  

5. **Machine Learning (PySpark MLlib)**  
   - Linear Regression to predict **Disposable Income**.  
   - Evaluated using RMSE & R².  

6. **Sqoop**  
   - Exported processed data & predictions to MySQL for integration with BI tools (e.g., Tableau, Power BI).  

7. **Recommendation System (PySpark RDDs)**  
   - Rule-based financial advice:  
     - Cut discretionary expenses if >30% income.  
     - Suggest planning if low disposable income.  

---

## 📌 Key Findings & Impact  
- Tier 3 users, though wealthier on average, struggle with savings discipline.  
- Tier 1 users face **lifestyle-driven overspending** and financial vulnerability.  
- The pipeline demonstrates how **big data analytics + ML** can power **real-world fintech & advisory systems**.  

---
