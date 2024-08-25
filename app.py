from flask import Flask,jsonify,request,redirect,render_template,url_for
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import llamaConn as conn
import os

load_dotenv()

app= Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


key= os.getenv('AWS_ACCESS_KEY')
access_key= os.getenv('AWS_SECRET_KEY')

# user_messages=[]

@app.before_request
def before_request():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = app.make_default_options_response()
    
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,access-control-allow-origin')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response




# @app.route('/',methods=['GET'])
# def welcome():
#      return render_template('home.html')

@app.route('/',methods=['GET'])
def welcome():
     return "working"




# @app.route('/getResponse', methods=['POST'])
# def get_response():
#     data = request.json
#     user_message = data.get('message', '')
#     if not user_messages:
#         response= conn.stream_chat(user_message)
#     else:
#         print('here')
#         response= conn.stream_chat(user_message,history=user_messages)

#     context= f"User Message: {user_message}\n\nAI Message: {response}"
#     user_messages.append(context)
    
   
    
#     return jsonify({"response": str(response)})


@app.route('/chatLlama',methods=['POST'])
def chat_llama():
    data= request.get_json()
    query= data['query']
    history= data['history']
    if not history:
        response= conn.stream_chat(query)
    else:
        print('here')
        response= conn.stream_chat(query,history=history)
    
    return response



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)