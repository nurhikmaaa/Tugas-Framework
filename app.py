from flask import flask

app = Flask (__name__)

@app.route('/nama/<string:nama>')
def getnama(Hikma):
    return "nama anda adalah {Hikma}".format(nama)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')  # Variabel name diambil dari URL
def user(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', username=name)

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Profile</title>
</head>
<body>
    <h1>Selamat datang, {{ username }}!</h1>
</body>
</html>

app_name = "My Flask App"  # Variabel global

@app.route('/')
def home():
    return f"Welcome to {app_name}!"


@app.route('/data')
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('data.html', user=user)

<h1>Nama: {{ user.name }}</h1>
<p>Umur: {{ user.age }}</p>
<p>Kota: {{ user.city }}</p>

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users')
def users():
    user_list = ["Ali", "Budi", "Citra", "Dewi"]
    return render_template('users.html', users=user_list)

if __name__ == '__main__':
    app.run(debug=True)

<ul>
    {% if users %}
        {% for user in users %}
            <li>{{ user }}</li>
        {% endfor %}
    {% else %}
        <p>Tidak ada pengguna.</p>
    {% endif %}
</ul>

@app.route('/users')
def users():
    user_list = [
        {"name": "Ali", "role": "admin"},
        {"name": "Budi", "role": "user"},
        {"name": "Citra", "role": "admin"},
        {"name": "Dewi", "role": "user"},
    ]
    return render_template('users.html', users=user_list)

<ul>
    {% for user in users %}
        <li>{{ loop.index }}. {{ user }}</li>
    {% endfor %}
</ul>



    