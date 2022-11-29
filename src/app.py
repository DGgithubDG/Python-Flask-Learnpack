from flask import Flask, request, jsonify 
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
   

    
]
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print(position)
    todos.pop(position-1)
    print("This is the position to delete: ",position)
    return 'something'

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos), 200
    

 
@app.route('/hello', methods=['GET'])
def hello_world():
    return "<h1>Hello World</h1>"

@app.route('/todos', methods=["GET"]) 
def todo():
    json = jsonify(todos)
    return json

 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)