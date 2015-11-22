A restructuring of the MathSoc website (mathsoc.uwaterloo.ca)

##Setup##
1. Setup a mathsoc postgresql database, with username mathsoc and password whatever you want. Place this password in the keys_and_pws folder under the name database_pw. 
2. Set up virtual environment and pip. Source in to the virtual environment you've made, and run pip install -r requirements.txt
3. As long as DEBUG=True in mathsocwebsite/settings.py, then you can run the standard manage.py runserver command. If you want to run the dev server closer to how it runs on our server, you will have to set up Apache (with ssl support turned on). This is going to be different based on personal preference, so I'll leave that process to you.