import os, json
from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/search', methods=['GET'])
def search():
  key = request.args.get("key")
  domain = request.args.get("domain")
  search = request.args.get("search")
  
  print("key is",key,"domain is",domain,"search type is",search)

  dict_domain = {"Animals":["tiger","cat","goat","cheetah"],"Birds":["parrot","pigeon","owl","sparrow"],"Flowers":["lily","lotus","jasmine"]}

  filtered_dict=[]

  if search =="contains":
  	for word in dict_domain[domain]:
  		if key in word:
  			filtered_dict.append(word)
  			#print(filtered_dict)
  else:
  	for word in dict_domain[domain]:
  		if word.startswith(key) :
  			filtered_dict.append(word)
  			#print(filtered_dict)

  print("filtered dict",filtered_dict)		
  resp = json.dumps(filtered_dict)

  return resp

if __name__ == '__main__':
    app.run(debug=True)