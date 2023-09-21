from flask import Flask

app = Flask(__name__)

@app.route("/index")
@app.route("/") # decorator
def index(): #handalar
    return """
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Моя Сучасна Сторінка</title>
    <style>
        /* Стилі для всієї сторінки */
        body {
            background-color: #FFFF00; /* Жовтий фон */
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        /* Стилі для заголовка */
        header {
            background-color: #007BFF; /* Блакитний фон */
            color: #fff;
            padding: 20px 0;
            text-align: center;
        }

        h1 {
            color: #333;
        }

        /* Стилі для навігаційного меню */
        nav ul {
            list-style: none;
            padding: 0;
        }

        nav li {
            display: inline;
            margin-right: 20px;
        }

        nav a {
            text-decoration: none;
            color: #007BFF;
            font-weight: bold;
        }

        /* Стилі для розділів */
        main {
            padding: 20px;
        }

        section {
            margin: 20px 0;
        }

        h2 {
            font-size: 24px;
            color: #007BFF;
        }

        p {
            font-size: 16px;
            line-height: 1.5;
        }

        ul {
            list-style: disc;
            margin-left: 20px;
        }

        /* Стилі для підвалу */
        footer {
            background-color: #007BFF; /* Блакитний фон */
            color: #fff;
            padding: 10px 0;
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <h1>Ласкаво просимо на мою сторінку</h1>
        <nav>
            <ul>
                <li><a href="#">Головна</a></li>
                <li><a href="#">Про нас</a></li>
                <li><a href="#">Послуги</a></li>
                <li><a href="#">Контакти</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h2>Про нас</h2>
            <p>Ми - команда професіоналів, яка надає найкращі послуги у сфері веб-розробки.</p>
        </section>

        <section>
            <h2>Наші послуги</h2>
            <ul>
                <li>Веб-дизайн</li>
                <li>Розробка веб-сайтів</li>
                <li>Оптимізація для пошукових систем (SEO)</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Моя Сучасна Сторінка</p>
    </footer>
</body>"""
@app.route("/about")
def about():
    return "<h1> about site </h1>"

if __name__ == '__main__':
    app.run(debug=True)

