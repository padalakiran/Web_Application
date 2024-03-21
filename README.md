# Web Application
The Repository consist of the Web Application Using Django that can take User inputs And Stores in Database</br>
## Project Setup
Prerequisite for the Project
1. Python:- Python latest Version Can be downloaded using the [Link](https://www.python.org/downloads/)
2. PyCharm:- Pycharm is the platform that Used to run the Python Files That Can Be Downloaded using [Link](https://www.jetbrains.com/pycharm/download/)
3. Django Module:- To work with Django you need to install Django module which is installed by using command $\color{blue}{pip\ install\ django}$ which can be enter in command prompt 
4. Data Base:- Django inbuilt Enabled with Sqllite we can cange the database to MySQL, PostgreSql etc..,
5. HTML,CSS:- You need to Create the form with HTML(Hyper Text Markup Language), CSS(Cascading Style Sheet) that can take the input from the user.
6. Virtual Environment:- You need to create virtual environment that can can setup all the required environment like python etc..,

| Platform    | Download link/command |
| ------------- | ------------- |
| Python  |   [Link](https://www.python.org/downloads/)|
| Pycharm  | [Link](https://www.jetbrains.com/pycharm/download/)  |
|MySQl | [Link](https://www.mysql.com/downloads/)|
|Django     | pip install django |
|MySQL Connector for Python| pip install mysql-connector-python |
## Steps to Run the project
1. After downloading the repository and Extract all Files in the zip folder to your local computer.
2. Open PyCharm: Launch PyCharm from your applications or start menu.
3. Open Existing Project: If you have PyCharm open but no project is currently open, you'll see a welcome screen. Click on "Open" and navigate to the directory where your Django project is located. Select the root directory of your Django project and click "OK". If PyCharm is already open with a project, you can click on "File" -> "Open" and follow the same process.
4. Set Up Interpreter: PyCharm may prompt you to configure a Python interpreter for the project. Ensure that you select the correct Python interpreter that you want to use for your Django project. You can create a new virtual environment or use an existing one.
5. Wait for Indexing: PyCharm will index your project files, which may take some time depending on the size of your project.
6. Open Terminal: Once the project is loaded, you can open the terminal within PyCharm by clicking on **"View" -> "Tool Windows" -> "Terminal"**.
7. Run Server: In the terminal, navigate to the directory where your manage.py file is located and run the Django development server using the command python manage.py runserver.
8. Access Django Admin: Open a web browser and navigate to the address provided by the Django development server (typically http://localhost:8000/). You should see your Django project running. If you have set up Django admin, you can access it at http://localhost:8000/admin/.</br>
9. Here Is the Step by Step Video link to Setup the project-- [Link](https://drive.google.com/file/d/1tI04zOWBlCwA5d3W9hlBRRFfFui7I20O/view?usp=drive_link)

After Running Project you will get the output with the link to access the Project which looks like</br></br>
![image](https://github.com/padalakiran/Web_Application/assets/73814328/6e9a53d6-5282-427c-a36e-e649140fc76d)
</br>
In this page you will get two buttons one for data entry and another for data retrival
</br>
if you press data entry button you will get HTML Form that have the feilds like name,age,email,DOB(Date Of Birth) all are the mandatory feilds.</br></br>
![image](https://github.com/padalakiran/Web_Application/assets/73814328/6e04b597-eb47-49d6-8cf9-f7b489c93dfe)


Output of the data which is data retrival page looks like
![image](https://github.com/padalakiran/Web_Application/assets/73814328/2990bef2-ad18-4e68-bc8d-dd48c5c5fa39)


The Database consist of the Feilds of id which autoincriment with the data and it is a PrimaryKey, Name is a text Feild datatybe will be varchar, Email is a text Feild datatybe will be varchar, Age it is a integer Feild, Date of Birth it is a Date Feild. </br>
Let's Look at the Schema of The Database</br></br>

| Field       | Type         | Null | Key | Default | Extra          |
|:-----------:|:------------:|:-----:|:-----:|:--------:|:---------------:|
| ID          | int          | NO   | PRI | NULL    | auto_increment |
| Name        | varchar(255) | NO   |     | NULL    |                |
| Email       | varchar(255) | NO   |     | NULL    |                |
| Age         | int          | NO   |     | NULL    |                |
| DateOfBirth | date         | NO   |     | NULL    |                |




Here is the demo link of the project ----> [Link](https://drive.google.com/file/d/1-fusr5CzZX4zXuvREAeZ1e-MIxbtxtsf/view?usp=sharing)
