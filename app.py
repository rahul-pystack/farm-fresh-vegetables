from flask import Flask,render_template,redirect,url_for,request
from flask_mysqldb import MySQL
import MySQLdb
import os




UPLOAD_FOLDER = 'static/uploads'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)

# DATABASE CONNECTION SECTION
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'vegecommerce'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


 
mysql = MySQL(app)


@app.route('/')
def indexpage():
    return render_template('home.html')

# HOME PAGE
@app.route('/main')
def Homepage():
    return render_template('index.html')



# INDEX PAGE REDIRECTION
@app.route('/indexpage',methods=['GET','POST'])
def homepageredirect():
    if request.method == 'POST':
        btn = request.form['submit']
        if btn == 'Administrator Login':
            return render_template('adminlogin.html')
        elif btn == 'Seller Login':
            return render_template('sellerlogin.html')
        elif btn == 'Buyer Login':
            return render_template('buyerlogin.html')
    return "invalid"


#----------- ADMIN CONTROL --------------#

# ADMINISTRATOR LOGIN PAGE
@app.route('/adminlogin',methods=['GET','POST'])
def Administratorlogin():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        if  name == 'admin' and pwd == 'admin':
            return render_template('adminmainpage.html')
    return 'wrong information'


# ADMIN PAGE REDIRECTIONS
@app.route('/adminmain',methods=['GET','POST'])
def adminmainpageredirection():
    if request.method == 'POST':
        btn = request.form['submit']
        if btn == 'Seller Register':
            return render_template('SellerRegister.html')
        elif btn == 'Buyer Register':
            return render_template('BuyerRegister.html')
        elif btn == 'View Seller Details':
            return redirect(url_for('viewseller'))
        elif btn == 'View Buyer Details':
            return redirect(url_for('viewbuyer'))
        elif btn == 'View Product Details':
            return redirect(url_for('viewproduct'))
    return "something wrong"


# NEW SELLER INFORMATION REGISTER
@app.route('/register_seller',methods = ['GET','POST'])
def newseller():
    try:
        name = request.form['name']
        gender = request.form['gender']
        area = request.form['area']
        district = request.form['district']
        contact = request.form['contact']
        address = request.form['address']
        shop_name = request.form['shop_name']
        # Image Handling
        image = request.files['image']
        image_path = f"static/uploads/{image.filename}"
        image.save(image_path)
        pwd = request.form['password']
        cursor = mysql.connection.cursor()
        # Insert into Database
        query = "INSERT INTO sellerregister (name,gender,area,district,contact_number,address,shop_name,image_path,password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, gender, area, district, contact, address, shop_name, image_path,pwd)
        print(values)
        cursor.execute(query,values)
        mysql.connection.commit()
        cursor.close()
        return render_template ('tick.html')
    except Exception as e:
        print(e)
    return "404 error...!!!"

# BUYER REGISTER
@app.route('/register_buyer',methods=['GET','POST'])
def buyerregister():
    try:
        name = request.form['name']
        gender = request.form['gender']
        area = request.form['area']
        district = request.form['district']
        contact = request.form['contact']
        address = request.form['address']
        # Image Handling
        image = request.files['image']
        image_path = f"static/uploads/{image.filename}"
        image.save(image_path)
        pwd = request.form['password']
        cursor = mysql.connection.cursor()
        # Insert into Database
        query = "INSERT INTO buyerregister (name,gender,area,district,contact_number,address,image_path,password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, gender, area, district, contact, address, image_path,pwd)
        print(values)
        cursor.execute(query,values)
        mysql.connection.commit()
        cursor.close()
        return render_template ('tick.html')
    except Exception as e:
        print(e)
    return "404 error...!!!"

# VIEW SELLER DETAILS
@app.route('/showseller',methods=['GET','POST'])
def viewseller():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sqlstr = "select * from sellerregister"
    cursor.execute(sqlstr)
    mysql.connection.commit()
    users = cursor.fetchall()
    drow = cursor.rowcount
    cursor.close
    print(users)
    return render_template("viewseller.html",sellers=users)

# VIEW BUYER DETAILS
@app.route('/viewbuyer',methods=['GET','POST'])
def viewbuyer():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sqlstr = "select * from buyerregister"
    cursor.execute(sqlstr)
    mysql.connection.commit()
    users = cursor.fetchall()
    drow = cursor.rowcount
    cursor.close
    print(users)
    return render_template("viewbuyer.html",buyers=users)
    

# VIEW PRODUCT DETAILS
@app.route('/viewproducts',methods=['GET','POST'])
def viewproduct():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sqlstr = "select * from products"
    cursor.execute(sqlstr)
    mysql.connection.commit()
    users = cursor.fetchall()
    drow = cursor.rowcount
    cursor.close
    print(users)
    return render_template("viewproducts.html",products=users)


# ------------ SELLER CONTROLS --------------#

# SELLER LOGIN
@app.route('/sellerlogin',methods=['GET','POST'])
def sellerlogin():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        cursor = mysql.connection.cursor()
        sqlstr = "select * from sellerregister where name=%s and password=%s"
        data = (name,pwd)
        msg = cursor.execute(sqlstr,data)
        mysql.connection.commit()
        cursor.close()
        if msg == 0:
            return "User name and password is invalid"
        else:
            return render_template('sellermain.html')
    return "something wrong"



# SELLER MAIN PAGE REDIRECTION
@app.route('/sellermain',methods=['GET','POST'])
def sellerredirect():
    if request.method == 'POST':
        btn = request.form['submit']
        if btn == 'Upload Product':
            return render_template('uploadproduct.html')
        elif btn ==  'View Product Details':
            return redirect(url_for('viewproduct'))
        elif btn == 'View Buyer Details':
            return redirect(url_for('viewbuyer'))

# UPLOAD NEW PRODUCTS
@app.route('/upload_product',methods=['GET','POST'])
def newproduct():
    if request.method == 'POST':
        pname = request.form['product_name']
        sname = request.form['seller_name']
        shopname = request.form['shop_name']
        price = request.form['price']
        image = request.files['product_image']
        image_path = f"static/uploads/{image.filename}"
        image.save(image_path)
        cursor = mysql.connection.cursor()
        sql = 'insert into products(product_name,seller_name,shop_name,price,image_path)values(%s,%s,%s,%s,%s)'
        data = (pname,sname,shopname,price,image_path)
        cursor.execute(sql,data)
        mysql.connection.commit()
        cursor.close()
        print(data)
        return render_template ('tick.html')
    return "something wrong"

#----------------- BUYER CONTROLS ------------#
# BUYER LOGIN
@app.route('/buyerlogin',methods=['GET','POST'])
def buyerlogin():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        cursor = mysql.connection.cursor()
        sqlstr = "select * from buyerregister where name=%s and password=%s"
        data = (name,pwd)
        msg = cursor.execute(sqlstr,data)
        mysql.connection.commit()
        cursor.close()
        if msg == 0:
            return "User name and password is invalid"
        else:
            return render_template('buyermainpage.html')
    return "something wrong"


# BUYER MAIN PAGE REDIRECTIONS
@app.route('/buermainpage',methods=['GET','POST'])
def buyermain():
    if request.method == 'POST':
        btn = request.form['submit']
        if btn == 'View Seller Details':
            return redirect(url_for('viewseller'))
        elif btn == 'View Product Details':
            return redirect(url_for('viewproduct'))
        elif btn == 'Buy Product':
            return redirect(url_for('showallproducts'))
    return "something wrong"


# SHOW ALL PRODUCTS
@app.route('/add_to_cart')
def showallproducts():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sqlstr = "select * from products"
    cursor.execute(sqlstr)
    mysql.connection.commit()
    users = cursor.fetchall()
    drow = cursor.rowcount
    cursor.close
    print(users)
    return render_template('allproducts.html',products=users)


# ADD TO CART
@app.route('/add_to_cart',methods=['GET','POST'])
def addtocart():
    if request.method == 'POST':
        try:
            pname = request.form.get('product_name')
            price = request.form.get('product_price')
            image = request.form.get('product_image')
            cursor = mysql.connection.cursor()
            sql = 'insert into cart(product_name,price,image_path)values(%s,%s,%s)'
            data = (pname,price,image)
            print(data)
            cursor.execute(sql,data)
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('view_cart'))
        except Exception as e:
            print(e)
    return "something wrong"


# VIEW CART
@app.route('/view_cart',methods=['GET','POST'])
def view_cart():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sqlstr = "select * from cart"
    cursor.execute(sqlstr)
    mysql.connection.commit()
    users = cursor.fetchall()
    drow = cursor.rowcount
    cursor.close
    print(users)
    return render_template('viewcart.html', cart_items=users)


@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    product_id = request.form['product_id']
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM cart WHERE id = %s", (product_id,))
    mysql.connection.commit()
    cursor.close()
    return redirect('/view_cart')  # Redirect back to the cart page after removing

@app.route('/tick')
def tick():
    return render_template('/tick.html')


if __name__ == "__main__":
    app.run(debug=True)





