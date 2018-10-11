from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678fghj129876efghzd'
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Joe Black',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 29, 2018'
    }
]   

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='about' )

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Loging unsuccessful!', 'danger')
            
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)