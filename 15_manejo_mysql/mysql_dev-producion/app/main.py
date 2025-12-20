# app/main.py
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
from decouple import config

app = Flask(__name__)

# Configuración de la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=config('MYSQL_HOST', default='mysql_db'),
            port=config('MYSQL_PORT', default=3306, cast=int),
            database=config('MYSQL_DATABASE', default='mydb'),
            user='root',
            password=config('MYSQL_ROOT_PASSWORD', default='password123')
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Crear tabla si no existe
def create_table():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            connection.commit()
            print("Table 'users' created or already exists")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# CREATE - Crear usuario
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400
    
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s)",
                (name, email)
            )
            connection.commit()
            user_id = cursor.lastrowid
            return jsonify({
                'id': user_id,
                'name': name,
                'email': email,
                'message': 'User created successfully'
            }), 201
        except Error as e:
            return jsonify({'error': str(e)}), 400
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return jsonify({'error': 'Database connection failed'}), 500

# READ - Obtener todos los usuarios
@app.route('/users', methods=['GET'])
def get_users():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT id, name, email, created_at FROM users")
            users = cursor.fetchall()
            return jsonify(users)
        except Error as e:
            return jsonify({'error': str(e)}), 400
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return jsonify({'error': 'Database connection failed'}), 500

# READ - Obtener usuario por ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT id, name, email, created_at FROM users WHERE id = %s",
                (user_id,)
            )
            user = cursor.fetchone()
            if user:
                return jsonify(user)
            return jsonify({'error': 'User not found'}), 404
        except Error as e:
            return jsonify({'error': str(e)}), 400
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return jsonify({'error': 'Database connection failed'}), 500

# UPDATE - Actualizar usuario
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400
    
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE users SET name = %s, email = %s WHERE id = %s",
                (name, email, user_id)
            )
            connection.commit()
            if cursor.rowcount == 0:
                return jsonify({'error': 'User not found'}), 404
            return jsonify({
                'id': user_id,
                'name': name,
                'email': email,
                'message': 'User updated successfully'
            })
        except Error as e:
            return jsonify({'error': str(e)}), 400
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return jsonify({'error': 'Database connection failed'}), 500

# DELETE - Eliminar usuario
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            connection.commit()
            if cursor.rowcount == 0:
                return jsonify({'error': 'User not found'}), 404
            return jsonify({'message': 'User deleted successfully'})
        except Error as e:
            return jsonify({'error': str(e)}), 400
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return jsonify({'error': 'Database connection failed'}), 500

if __name__ == '__main__':
    # Crear tabla al iniciar
    create_table()
    
    port = int(config('APP_PORT', default=8000))
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
