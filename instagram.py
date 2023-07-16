from flask import render_template,request,redirect,make_response,flash
from database import db
from database import app
from database import post,Users,likes,id,Follow
import datetime
import jdatetime
import os
app.app_context().push()
db.create_all()

id.query.all()[0].id_pic=str(0)


path='./static/uploads/'
@app.errorhandler(404)
def showerror(error):
    return render_template("error.html"), 404

@app.route("/",methods=['POST','GET'])
def home():
    return render_template('index.html',user=request.cookies.get("user"),item=post.query.all(), path=path)

@app.route("/profile2/<int:id>",methods=['POST','GET'])
def profile2(id):
    
    profile=post.query.get(id)
    print(profile.poster)
    sub=Follow.query.all()
    if sub.follower==request.cookies.get("user") & sub.following==profile.poster:
        is_follow=True
    else:
        is_follow=False



    return render_template('profile2.html',Profile=profile,coocki=request.cookies.get("user"),path="/static/uploads/",is_follow=is_follow)


@app.route("/follow/<int:id>",methods=['POST','GET'])
def follow(id):
    
    profile=post.query.get(id)
    print(profile.poster)
    admin = Follow(following=profile.poster,follower=request.cookies.get("user"))
    db.session.add(admin)
    db.session.commit()

    return render_template('/')



@app.route("/delete/<int:id>",methods=['POST','GET'])
def delete(id):
    if request.cookies.get("user"):
         admin=post.query.get(id)
         db.session.delete(admin)
         db.session.commit()
         return redirect("/")
    else:
        return redirect('/login')

@app.route("/logout")
def logout():
    flash("کاربر خارج شد", "danger")
    response = make_response(redirect('/login'))
    response.delete_cookie("user")
    return response

@app.route("/profile",methods=['POST','GET'])
def profile():
    if request.cookies.get("user"):
        if request.method=='POST':

            flash("ذخیره شد", "primary")
            file1 = request.files.get('file1')


            if file1:
                file1.save(os.path.join(path, request.cookies.get("user") + ".jpg"))
                user= Users.query.filter_by(username=request.cookies.get("user")).first()

                db.session.commit()

            return render_template('profile.html', user=request.cookies.get("user"), path=path)
        else:
            return render_template('profile.html')
    else:
        return redirect('/login')




@app.route("/add",methods=['POST','GET'])
def add():

    if request.cookies.get("user"):
        if request.method=='POST':
            flash("پست شما ارسال شد.", "primary")

            text = request.form.get('textarea')
            file1 = request.files.get('file1')


            num=id.query.all()[0].id_pic
            num=int(num)+1
            id.query.all()[0].id_pic=str(num)
            print(path+request.cookies.get("user")+str(num)+".jpg")
            if file1 :
                file1.save(os.path.join("./static/uploads/"+request.cookies.get("user")+str(num) + ".jpg"))
            poster=request.cookies.get("user")

            admin = post(poster=poster,text=text,Picture="./static/uploads/"+request.cookies.get("user")+str(num) + ".jpg")


            db.session.add(admin)
            db.session.commit()
            return redirect('/')
        else:
            return render_template('add.html')
    else:
        return redirect('/login')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_name = request.form.get('user_name_login')
        password = request.form.get('password_login')
        found=False
        for u in range(len(Users.query.all())):
            if user_name==Users.query.all()[u].username and password==Users.query.all()[u].password:
                flash("خوش آمدید","success")
                response=make_response(redirect('/'))
                response.set_cookie("user",user_name)
                found = True
                return response
        if found==False:
                flash("نام یا رمز اشتباه است", "danger")
                return render_template('login.html')
    return render_template('login.html')
@app.route('/register',methods=['POST','GET'])
def Register():
    if request.method=='POST':
        user_name1 = request.form.get('user_name_register')
        password1 = request.form.get('password_register')
        password2 = request.form.get('password_register2')


        if password1==password2:

            admin1 = Users(username=user_name1, password=password1)
            db.session.add(admin1)
            db.session.commit()
            flash("عضو شدید","success")
            return redirect('/login')
        else:
            flash("رمز و تکرار رمز هم خوانی ندارد","danger")
            return render_template('Register.html')
    else:
        return render_template('Register.html')













if __name__=='__main__':
    app.run(host='0.0.0.0',port=2158)
