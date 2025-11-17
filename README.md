# 🏦 Automated Python Banking System

## 📖 Introduction
Welcome to the **Automated Python Banking System**. This project is a comprehensive simulation of a real-world banking environment. It bridges the gap between Python logic and Database management by automating the entire backend setup.

**What makes this special?**
* **Zero-Config Database:** You don't need to know SQL. The code connects to XAMPP, creates the database, and builds the tables automatically.
* **Real-Time Email Alerts:** Uses SMTP to send actual transaction receipts to your Gmail.
* **Secure:** Credentials are never hardcoded; you input them securely at runtime.



## 🔑 Important: Setting Up Email (Read First!)
To allow the application to send email receipts, you need a **Gmail App Password**. You cannot use your regular login password (Google security blocks that).

**How to get one (It takes 2 minutes):**
1.  Go to your [Google Account Settings](https://myaccount.google.com/).
2.  Click on the **Security** tab on the left.
3.  Under "How you sign in to Google", enable **2-Step Verification** (if not already on).
4.  Once 2-Step is on, go back to the search bar in settings and type **"App Passwords"**.
5.  Create a new App Password:
    * **App name:** Type "Banking Python App".
    * Click **Create**.
6.  Google will give you a **16-character code** (e.g., `abcd efgh ijkl mnop`). **Copy this code.**
    * *You will use this code when the Python app asks for your "App Password".*

---

## 🚀 How to Run the Project

### Step 1: Start the Server
1.  Download and install [XAMPP](https://www.apachefriends.org/download.html).
   
<img width="901" height="439" alt="xampp_download" src="https://github.com/user-attachments/assets/eb7d9a10-35ab-4b70-af1e-13aa6d270353" />

3.  Open **XAMPP Control Panel**.
4.  Click **Start** next to **Apache** and **MySQL**.
    <img width="623" height="455" alt="xampp_control_panel" src="https://github.com/user-attachments/assets/958096da-3970-44ac-806b-93b4071ae3fb" />


### Step 2: Run the Code
Open your terminal or IDE and run the script:
```bash
python banking_app.py
```

### Step 3: The Banking Interface
Once logged in, you are presented with the Main Dashboard.


You can perform the following operations:
1.  **Add Money:** Deposit funds securely.
2.  **Transfer Money:** Simulate sending cash to another user.
3.  **Buy Airtime/Data:** Purchase utilities.
4.  **Check Balance:** Real-time query of your database funds.
5.  **Change Details:** Update your profile.

<img width="645" height="402" alt="app_menu" src="https://github.com/user-attachments/assets/b85c4f11-45e9-4d88-8a9c-e91bbe00f951" />


### Step 4: Instant Feedback (Email Integration)
Every time you perform a critical transaction (like adding money or transferring funds), the system generates a digital receipt and fires it to your registered email via SMTP.

*Here is an example of a transaction receipt:*


![email_receipt1](https://github.com/user-attachments/assets/9e92245f-45b4-4546-807d-4113e6ee241b)



![email_receipt2](https://github.com/user-attachments/assets/effdbdc5-3c11-49b6-83d0-21f5c334b612)


---

## 🛠️ Requirements
* **Python 3.x**
* **XAMPP** (or any local MySQL server)
* **Internet Connection** (Crucial for the email API and initial setup)

## 👤 Author
[Your Name Here]
*Built with Python, MySQL, and Automation in mind.*



