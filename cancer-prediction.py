{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b4851363",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dataset Loaded Successfully\n",
      "   mean radius  mean texture  mean perimeter  mean area  mean smoothness  \\\n",
      "0        17.99         10.38          122.80     1001.0          0.11840   \n",
      "1        20.57         17.77          132.90     1326.0          0.08474   \n",
      "2        19.69         21.25          130.00     1203.0          0.10960   \n",
      "3        11.42         20.38           77.58      386.1          0.14250   \n",
      "4        20.29         14.34          135.10     1297.0          0.10030   \n",
      "\n",
      "   mean compactness  mean concavity  mean concave points  mean symmetry  \\\n",
      "0           0.27760          0.3001              0.14710         0.2419   \n",
      "1           0.07864          0.0869              0.07017         0.1812   \n",
      "2           0.15990          0.1974              0.12790         0.2069   \n",
      "3           0.28390          0.2414              0.10520         0.2597   \n",
      "4           0.13280          0.1980              0.10430         0.1809   \n",
      "\n",
      "   mean fractal dimension  ...  worst texture  worst perimeter  worst area  \\\n",
      "0                 0.07871  ...          17.33           184.60      2019.0   \n",
      "1                 0.05667  ...          23.41           158.80      1956.0   \n",
      "2                 0.05999  ...          25.53           152.50      1709.0   \n",
      "3                 0.09744  ...          26.50            98.87       567.7   \n",
      "4                 0.05883  ...          16.67           152.20      1575.0   \n",
      "\n",
      "   worst smoothness  worst compactness  worst concavity  worst concave points  \\\n",
      "0            0.1622             0.6656           0.7119                0.2654   \n",
      "1            0.1238             0.1866           0.2416                0.1860   \n",
      "2            0.1444             0.4245           0.4504                0.2430   \n",
      "3            0.2098             0.8663           0.6869                0.2575   \n",
      "4            0.1374             0.2050           0.4000                0.1625   \n",
      "\n",
      "   worst symmetry  worst fractal dimension  target  \n",
      "0          0.4601                  0.11890       0  \n",
      "1          0.2750                  0.08902       0  \n",
      "2          0.3613                  0.08758       0  \n",
      "3          0.6638                  0.17300       0  \n",
      "4          0.2364                  0.07678       0  \n",
      "\n",
      "[5 rows x 31 columns]\n",
      "Dataset Split into Training and Testing Sets\n",
      "Feature Scaling Completed\n",
      "Model Training Completed\n",
      "\n",
      "Accuracy Score: 0.9532163742690059\n",
      "\n",
      "Confusion Matrix:\n",
      " [[ 57   6]\n",
      " [  2 106]]\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0       0.97      0.90      0.93        63\n",
      "           1       0.95      0.98      0.96       108\n",
      "\n",
      "    accuracy                           0.95       171\n",
      "   macro avg       0.96      0.94      0.95       171\n",
      "weighted avg       0.95      0.95      0.95       171\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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48yZMwgICICZmRn8/Py0ev2KThAdN24coqOjUaNGDQwbNgzR0dGws7NTMiQiIqIKYdmyZQCATp06abSvXbsWAQEBAIDp06cjKysL48aNw/379+Hl5YXdu3fD0tJSq7Eoep8NAwMD1KhRA56enq+cjLJp06ZiHZf32SAqGO+zQZRfWdxn40LqI60cp66jmVaOU9YUrWy8++67Wp/xSkREpGv0/S+d4jf1IiIiqvD0PNtQfIIoERERVWw68Yh5IiKiiqy4K0kqGiYbREREMtP36YkcRiEiIiJZsbJBREQkMz0vbDDZICIikp2eZxscRiEiIiJZsbJBREQkM65GISIiIllxNQoRERGRjFjZICIikpmeFzaYbBAREclOz7MNJhtEREQy0/cJopyzQURERLJiZYOIiEhm+r4ahckGERGRzPQ81+AwChEREcmLlQ0iIiKZcRiFiIiIZKbf2QaHUYiIiEhWrGwQERHJjMMoREREJCs9zzU4jEJERETyYmWDiIhIZhxGISIiIlnp+7NRmGwQERHJTb9zDc7ZICIiInmxskFERCQzPS9sMNkgIiKSm75PEOUwChEREcmKlQ0iIiKZcTUKERERyUu/cw0OoxAREZG8WNkgIiKSmZ4XNphsEBERyY2rUYiIiIhkxMoGERGRzLgahYiIiGTFYRQiIiIiGTHZICIiIllxGIWIiEhm+j6MwmSDiIhIZvo+QZTDKERERCQrVjaIiIhkxmEUIiIikpWe5xocRiEiIiJ5sbJBREQkNz0vbTDZICIikhlXoxARERHJiJUNIiIimXE1ChEREclKz3MNJhtERESy0/Nsg3M2iIiISFasbBAREclM31ejMNkgIiKSmb5PEOUwChEREclKEkIIpYOgiik7OxshISEIDAyESqVSOhwincHfDdI3TDZINg8ePIC1tTXS09NhZWWldDhEOoO/G6RvOIxCREREsmKyQURERLJiskFERESyYrJBslGpVAgKCuIEOKKX8HeD9A0niBIREZGsWNkgIiIiWTHZICIiIlkx2SAiIiJZMdmgMuXm5oawsDClwyDSmqtXr0KSJCQkJAAA9u/fD0mS8PfffysaF5EuYbJBAICAgABIkqTe7Ozs0L17d5w6dUqr54mLi8OoUaO0ekyi4nr+8z5mzJh8+8aNGwdJkhAQEFCiY7dt2xYpKSmwtrYuZZTaFxkZ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ubnqNgcHB1SrVg1XrlzBkCFDCjxugwYNsG7dOmRlZakTmlfFQUT6g8MoRDqsa9euaNOmDfr27YtffvkFV69exeHDh/Hxxx8jPj4eADBp0iSsWbMGa9aswcWLFxEUFISzZ88WekwTExPMmDED06dPxzfffIPExEQcPXoUq1evBgBUrVoVpqam2LVrF27fvo309HQAz24UFhISgq+++goXL17E6dOnsXbtWixcuBAA4OfnBwMDA4wYMQLnzp3Djh078MUXX8j8CRFRecBkg0iHSZKEHTt2oGPHjhg+fDjq1KmDQYMG4erVq3BwcAAADBw4ELNnz8aMGTPQokULJCcnY+zYsa887qxZszB16lTMnj0b9evXx8CBA5GWlgYAqFSpEhYvXowVK1bA2dkZffr0AQCMHDkSq1atQmRkJBo3bgxvb29ERkaql8paWFhg27ZtOHfuHDw9PTFz5kwsWLBAxk+HiMoLSXCglYiIiGTEygYRERHJiskGERERyYrJBhEREcmKyQYRERHJiskGERERyYrJBhEREcmKyQYRERHJiskGERERyYrJBhEREcmKyQYRERHJiskGERERyYrJBhEREcnq/wDiMmKr6gXTyQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Program Execution Completed Successfully\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report\n",
    "from sklearn import datasets\n",
    "\n",
    "cancer = datasets.load_breast_cancer()\n",
    "df = pd.DataFrame(cancer.data, columns=cancer.feature_names)\n",
    "df['target'] = cancer.target\n",
    "print(\"Dataset Loaded Successfully\")\n",
    "print(df.head())\n",
    "\n",
    "X = df.drop('target', axis=1)\n",
    "y = df['target']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
    "print(\"Dataset Split into Training and Testing Sets\")\n",
    "\n",
    "scaler = StandardScaler()\n",
    "X_train = scaler.fit_transform(X_train)\n",
    "X_test = scaler.transform(X_test)\n",
    "print(\"Feature Scaling Completed\")\n",
    "\n",
    "model = LinearRegression()\n",
    "model.fit(X_train, y_train)\n",
    "print(\"Model Training Completed\")\n",
    "\n",
    "y_pred = model.predict(X_test)\n",
    "y_pred_binary = [1 if i > 0.5 else 0 for i in y_pred]\n",
    "\n",
    "print(\"\\nAccuracy Score:\", accuracy_score(y_test, y_pred_binary))\n",
    "\n",
    "conf_matrix = confusion_matrix(y_test, y_pred_binary)\n",
    "print(\"\\nConfusion Matrix:\\n\", conf_matrix)\n",
    "\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_test, y_pred_binary))\n",
    "\n",
    "sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Benign', 'Malignant'], yticklabels=['Benign', 'Malignant'])\n",
    "plt.title('Confusion Matrix Heatmap')\n",
    "plt.xlabel('Predicted')\n",
    "plt.ylabel('Actual')\n",
    "plt.show()\n",
    "\n",
    "print(\"Program Execution Completed Successfully\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1598d7ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\Sridharkannan\\\\cancer-prediction.py'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "os.path.abspath(\"cancer-prediction.py\")  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e94428cf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
