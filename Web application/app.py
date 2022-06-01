from Website import app
import os
#the main file to run on the server
#configured to run both locally and on Heroku (with proc file)
#if you need to reuse the code make sure you change variables such as database URL on the __init__.py file
if __name__ == '__main__':


    app.run(debug=True, use_reloader=True, host="0.0.0.0", threaded=True)