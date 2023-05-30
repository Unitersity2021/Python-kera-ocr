from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/')
def index():
    return 'Server Works!'

# Sample data
graphics = [
    {"id": 1, "title": "Graphic 1", "name": "Star 1"},
    {"id": 2, "title": "Graphic 2", "name": "Star 2"}
]

#GET -Retrieve all
@app.route('/graphics', methods=['GET'])
def get_graphics():
    return jsonify(graphics)

# GET - Retrieve a specific graphic by ID
@app.route('/graphics/<int:graphic_id>', methods=['GET'])
def get_graphic(graphic_id):
    graphic = [graphic for graphic in graphics if graphic['id'] == graphic_id]
    if len(graphic) == 0:
        return jsonify({'error': 'graphic not found'}), 404
    return jsonify(graphic[0])

# POST - Create a new graphic
@app.route('/graphics', methods=['POST'])
def create_graphic():
    if 'title' not in request.json or 'author' not in request.json:
        return jsonify({'error': 'Title and author are required'}), 400
    new_graphic = {
        'id': graphics[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    graphics.append(new_graphic)
    return jsonify(new_graphic), 201

# PUT - Update an existing graphic
@app.route('/graphics/<int:graphic_id>', methods=['PUT'])
def update_graphic(graphic_id):
    graphic = [graphic for graphic in graphics if graphic['id'] == graphic_id]
    if len(graphic) == 0:
        return jsonify({'error': 'graphic not found'}), 404
    graphic[0]['title'] = request.json.get('title', graphic[0]['title'])
    graphic[0]['author'] = request.json.get('author', graphic[0]['author'])
    return jsonify(graphic[0])

# DELETE - Delete an existing graphic
@app.route('/graphics/<int:graphic_id>', methods=['DELETE'])
def delete_graphic(graphic_id):
    graphic = [graphic for graphic in graphics if graphic['id'] == graphic_id]
    if len(graphic) == 0:
        return jsonify({'error': 'graphic not found'}), 404
    graphics.remove(graphic[0])
    return jsonify({'result': 'graphic deleted'})

if __name__ == '__main__':
    app.run(debug=True)