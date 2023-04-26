from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '1195a65a13dd49e37cd35374bcca0911'



posts = [
    {
    'author': 'Trevor Strobel',
    'title': 'Blog post 1',
    'content': 'First blog post',
    'date_posted': 'April 25th, 2023'
    },
    {
    'author': 'Elton John',
    'title': 'Blog post 2',
    'content': 'Second blog post',
    'date_posted': 'April 26th, 2023'
    }
]

#Home Page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)



# About Page
@app.route("/about")
def about():
    return render_template('about.html', title='About')


#Registration Route
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


#LoginRoute
@app.route("/login", methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)