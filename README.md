# AgroDigitalBank

Setup:
1. Install all the requirements
2. Go to BankSite folder
3. Open the settings.py file
4. Change the user, name, password, host and port according to your PostGreSQL instance
5. Run the python manage.py migrate command
    ```console
        python manage.py migrate
    ```
6. Generate fake data using a custom command
    ```console
        python manage.py seed
    ```
7. Run the server using the runserver command
    ```console
        python manage.py runserver
    ```
