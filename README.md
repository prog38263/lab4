# Lab 4 - Hello World in Docker, Python, Flask and Redis

## Setup

1. Clone this repository and cd into the folder.
2. Run <code>docker-compose up</code> to start the application.
3. Browse to the app on port 80 in a web browser (your VM's IP if browsing from the VM's host)
4. Once you've confirmed that the base page is working, try loading the simple form by navigating to /simpleform in your browser.
5. If you can see a counter incrementing each time you load the page with data in the textbox, everything is working.
6. Explore the code (mostly the contents of the web/app/ directory) and try to get an understanding of how it works.
7. Modify the code to change the position of the messages from the form. You'll want to change one of the files in the web/app/templates directory.
8. Modify the code to add a PasswordField to the simple form. See web/app/forms.py. Pay close attention to the imports.
9. Add validation to the username and password in the form. You can use a hardcoded username and password for now. See this article for help <https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/>
10. Using the notes from class regarding password storage, see if you can hash the incoming password according to good password storage practices.

