from flask import Flask, jsonify, request
import mysql.connector

# Create Flask app instance
app = Flask(__name__)

# Connect to MySQL database
conn = mysql.connector.connect(
    host='your_mysql_host',
    user='your_mysql_user',
    password='your_mysql_password',
    database='your_database'
)

cursor = conn.cursor(dictionary=True)

# CRUD operations go here

# Create
@app.route('/records', methods=['POST'])
def create_record():
    new_record = request.get_json()
    insert_query = "INSERT INTO records (name, value) VALUES (%s, %s)"
    cursor.execute(insert_query, (new_record['name'], new_record['value']))
    conn.commit()
    return jsonify({'message': 'Record created successfully'}), 201

# Read (all records)
@app.route('/records', methods=['GET'])
def get_all_records():
    select_query = "SELECT * FROM records"
    cursor.execute(select_query)
    records = cursor.fetchall()
    return jsonify(records), 200

# Read (single record by ID)
@app.route('/records/<int:record_id>', methods=['GET'])
def get_record(record_id):
    select_query = "SELECT * FROM records WHERE id = %s"
    cursor.execute(select_query, (record_id,))
    record = cursor.fetchone()
    if record is None:
        return jsonify({'message': 'Record not found'}), 404
    return jsonify(record), 200

# Update
@app.route('/records/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    updated_data = request.get_json()
    update_query = "UPDATE records SET name = %s, value = %s WHERE id = %s"
    cursor.execute(update_query, (updated_data['name'], updated_data['value'], record_id))
    conn.commit()
    return jsonify({'message': 'Record updated successfully'}), 200

# Delete
@app.route('/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    delete_query = "DELETE FROM records WHERE id = %s"
    cursor.execute(delete_query, (record_id,))
    conn.commit()
    return jsonify({'message': 'Record deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
