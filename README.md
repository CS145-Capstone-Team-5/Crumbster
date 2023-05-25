# Crumbster
Crumbster is a household food waste tracking system that aims to let families better plan the food that will buy. <br/>

<!--This is an IOT-based project that will serve as the Capstone Project for CS 145 -->
# Dependencies
Note: *To be updated.*
<ul>
  <li>Mobile App</li>
  <ul>
  <li>Node.js</li>
  <li>NPM</li>
  </ul>

  <li>Server</li>
  <ul>
  <li>Python3</li>
  <li>Flask</li>
  <li>Flask_RESTful</li>
  <li>firebase_admin</li>
  </ul>
</ul>

# Setting up the notifications (FCM)
<ol>
  <li>Obtaining the Service Account Key</li>
  <ol>
    <li>In the Firebase Project's console, open Settings > Service Accounts</li>
    <li>Click Generate New Private Key, and Generate Key</li>
  </ol>
  <li>Store the obtained key, copy the path to it and replace PATH-TO-SERVICE-ACCOUNT-KEY in notifs.py</li>
  <li>Copy one's token (obtained from running the app) and replace REGISTRATION-TOKEN in notifs.py</li>
</ol>

# Running the server (Windows)
<ol>
<li>Check the IP address of the device (i.e. the one that will host the server)</li>
<li>In the root directory, enter the following on the terminal:</li>

```
set FLASK_APP=CrumbsterAPI 

flask --app CrumbsterAPI run --host=[IP_ADDRESS]
```
</ol>

# Running the mobile app
Note: *To be updated.*
