# Description
<p> A Flask server that takes information from Iot devices in the form of integers and strings via webhook. Offers a fully featured login and sign up systems with hashed password database. a dedicated account section.</p>

<img src="https://media.giphy.com/media/5dzCJe9ePHRHvRECoX/giphy.gif" alt="Web app" width="100%">


# Instructions
<li> Download Repository, unzip it</li><br>
<li>install requirements</li> <br>
<code> <i> python -m pip install -r requierments.txt </code></li><br>
<li>run app.py.</li><br>
<code> <i> python app.py </code></li><br>

<p>The certfication folder holds the clinet and server certificates.



# Login and Sign up
<img src="https://i.ibb.co/1T3ZGZ4/Microsoft-Teams-image-4.png" alt="Microsoft-Teams-image-4" width="100%">
<img src="https://i.ibb.co/SmVNVdt/Microsoft-Teams-image-9.png" alt="Microsoft-Teams-image-9" width="100%">

# Analytics Dashboard
<p>This dashboard made using google data studio connected to the database.</p><img src="https://i.ibb.co/4gx8H0M/Microsoft-Teams-image-2.png" alt="Microsoft-Teams-image-2" width="100%">

# Find available room
<P> This page show available room and it properties.</p><img src="https://i.ibb.co/PFxH9s6/Microsoft-Teams-image-1.png" alt="Microsoft-Teams-image-1" width="100%">

# Admin dasboard
<p> Admin will be able to add users, rooms and show data in the database records.</p>
<img src="https://i.ibb.co/30sTdVD/Microsoft-Teams-image-7.png" alt="Microsoft-Teams-image-7" width="100%">

# Deployement
<p> Simply change the variables in <code>__ini__.py</code> to suit your needs, check the PROCFILE for any needed upgrades and run the following commands in heroku CLI:
<code> <i> heroku login </code>
<code> <i> heroku git:clone -a YOURAPPNAME </code>
<code> <i> cd YOURAPPNAME</code>
<code> <i> git add . </code>
<code> <i> git commit -am 'val' </code>
<code> <i> git push heroku master </code>
</p>




