import pyrebase



 config={"apiKey": "AIzaSyCR-nv7ecsj5gJcEOGU2SlAvTbcXjAqmYs",
    "authDomain": "atm-database-3e193.firebaseapp.com",
    "databaseURL": "https://atm-database-3e193-default-rtdb.firebaseio.com",
    "projectId": "atm-database-3e193",
    "storageBucket": "atm-database-3e193.appspot.com",
    "messagingSenderId": "347257870204"",
    "appId": "1:347257870204:web:359fd053f91cb52bef36f9",
    "measurementId": "G-HR44HZS668"
  }
  firebase=pyrebase.initialize_app(config)

  db=firebase.database()

 
  data={"name":"hrishi", "password":"abc"}
  db.push(data)