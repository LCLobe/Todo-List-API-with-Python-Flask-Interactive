from flask import Flask, jsonify, request

app = Flask(__name__)


todos = [
  {"id":147,  "label": "My first task", "done": False },
  {"id":628, "label": "My second task", "done": False }
  ]

@app.route('/todos', methods=['GET'])
def get_todos():
  global todos
  response = jsonify(todos)
  return response


@app.route('/todos', methods=['POST'])
def add_new_todo():
  body = request.json
  todos.append(body)
  response = jsonify(todos)
  return response
  
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
  global todos
 
  remaining_todos = [todo for todo in todos if todo["id"] != id]
  todos = remaining_todos
  
  response = jsonify(remaining_todos)
  return response

#DO NOT WRITE BELOW THIS
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)