# code-crew-django-app
This repository contains Django Application Example for Code Crew PH-IDEAS Students.
It is to serve as a proof of concept of the following:

1. Fetching Data from an external API
2. Performing Analysis in Python
3. Rendering a Plotly figure in html


To run the app:
1. Be sure to have python3, virtualenv, and pip installed on your machine.
2. Clone this repo into a directory on your local machine.
3. In the terminal navigate into the code-crew-django-app directory:
    ```
   cd code-crew-django-app
    ```
4. Create a Python virtual environment
   ```
   python3 -m venv env
   ```
5. Install the application dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```
6. Start the Django Dev Server using the manage.py file.
   ```
    python3 providers/providers/manage.py runserver 
   ```
7. Open a web browser, and navigate to the following url (local host port 8000):
   ```
     http://127.0.0.1:8000/plot/
   ```


