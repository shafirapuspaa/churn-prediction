# churn-prediction
### **Dataset churn**

**machine learning model yang dapat memprediksi siapa saja customers yang akan meninggalkan bank!**

- Tujuannya adalah menentukan apakah seorang customer akan melakukan churn (tidak menggunakan jasa lagi) dari bank ini.

**Features:**
- Surname: Surname
- CreditScore: Credit score
- Geography: Country (Germany/ France/ Spain)
- Gender: Gender (Female/ Male)
- Age: Age
- Tenure: How many years of customer
- Balance: Balance
- NumOfProducts: The number of bank product used
- HasCrCard: Credit card status (0 = No, 1 = Yes)
- IsActiveMember: Active membership status (0 = No, 1 = Yes)
- EstimatedSalary: Estimated salary
- Exited: Churn or not? (0 = No, 1 = Yes)

## **Business Problem**

Tujuan dari project ini adalah menentukan apakah seorang customer akan melakukan churn (tidak menggunakan jasa lagi) dari bank ini.

- FP: kita prediksi si customer akan churn (action --> kita beri promosi dengan cost $100), padahal aktualnya tidak churn
- FN: kita prediksi si customer tidak akan churn (action --> kita tidak memberi perhatian pada customer ini), padahal aktualnya churn (kehilangan customer dengan cost $500)
<br>
<br>
- Cost FP: $100
- Cost FN: $500

Karena cost FN lebih tinggi, maka metric yg digunakan adalah f2 score

