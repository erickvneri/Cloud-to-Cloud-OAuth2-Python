# SmartThings Flask OAuth2 Application

*This sample intends to help developers to follow OAuth2 Authentication process and integrate their devices into SmartThings ecosystem using a AWS Lambda Function or a WebHook Connector.*

---
### **Important**:
1. Create an [SmartThings](https://smartthings.developer.samsung.com) Account. 
1. Install SmartThings App at your phone.
1. This app requires [Python3](https://www.python.org/downloads/) so sake sure to set up proper environment before run this app.

1. Install your virtual environment:

       pip3 install env

1. Open *environment shell* and install dependencies with next commands:

       pipenv shell
       pipenv install
       
---


---
## `About the Database and Session Data`
### This app uses `SQLAlchemy` to save user's credentials and OAuth Tokens. 

1. To create DB, initialize **Python CLI** at your terminal.

       python3

2. Then follow next sequence of commands.

       >>> from db.db import db
       >>> db.create_all()
       >>> exit()

At this point you should be able to see the `db.user` file at db folder.  

This app uses `Redis instance` to save **Session Data**. It is not necessary running `Redis` manually, but you could get values from `Redis CLI` *([Install Redis](https://redis.io/topics/quickstart))*.

---

### To expose this app to the World Wide Web you can use [ngrok](https://ngrok.com/download).

1. Open tunneling:

       ngrok http 3000

2. Paste the `https://` ngrok URI at **BASE_URI** variable in *run.py* file.

3. Run your OAuth app:

       python3 run.py

---
---
## Register your OAuth2 Application at SmartThings.

1. Sign In into the [Developer Workspace](https://smartthings.developer.samsung.com/workspace). 
1. Follow next path: 
    - *New Project / Device Integration / SmartThings Cloud Connector / SmartThings Schema Connector*

1. Select *Register Cloud Connector*.
1. To verify OAuth2 flow, you could register a WebHook Tester. I'd suggest https://webhook.site/
1. Set *Device Cloud Credentials* with values displayed when running app.
1. Name your app.
1. Lastly, Deploy it to Test.

At your **SmartThings App** you should [Enable Developer Mode](https://smartthings.developer.samsung.com/docs/testing/how-to-test.html#Test-your-device) so you can access your Integration. 

Enjoy!