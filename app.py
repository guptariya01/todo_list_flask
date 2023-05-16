from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shabd@2003..",
    database="todolist"
)

@app.route('/')
def index():
    cursor = conn.cursor()
    query = "SELECT * FROM todo"
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('todo.html', data=data)

@app.route('/return', methods=['POST'])
def ret():
    cursor = conn.cursor()
    query = "SELECT * FROM todo"
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('todo.html', data=data)

@app.route('/adding', methods=['POST'])
def adding():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    description = request.form['description']

    # Insert new todo item into the database
    cursor = conn.cursor()
    query = "INSERT INTO todo (title, description) VALUES (%s, %s)"
    cursor.execute(query, (title, description))
    conn.commit()
    #########################################
    query = "SELECT * FROM todo"
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('todo.html', data=data)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    # Delete todo item from the database
    cursor = conn.cursor()
    query = "DELETE FROM todo WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    query = "SELECT * FROM todo"
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('todo.html', data=data)

@app.route('/todo')
def todo():
    # Fetch all todo items from the database
    cursor = conn.cursor()
    query = "SELECT * FROM todo"
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('todo.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
