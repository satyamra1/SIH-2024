from flask import render_template,request,Flask
from flask import current_app as app
from application.models import *
from application.predict import *



@app.route("/")
def f1():
    #var11=Cources.query.filter_by(c_name="btech cse").all()
    if request.method=="GET":
        return render_template("index.html")
    
    
@app.route("/table.html",methods=["GET","POST"])
def f3():
    
    if request.method=="GET":
        var11=Basics.query.all()
        return render_template("table.html",var111=var11)
    
    
@app.route("/form.html",methods=['GET','POST'])
def f2():
    if request.method=="GET":
        return render_template("form.html",a="get")
    elif request.method=="POST":
        #return render_template("form.html",result="Message",a="post")
        try:
            a=Basics()
            a.Index,a.State,a.District,a.Variety,a.Arrival_Date,a.Min_x0020_Price,a.Max_x0020_Price,a.Modal_x0020_Price=request.form["index"],request.form["state"],request.form["district"],request.form["variety"],str(request.form["arrival-date"]),request.form["min_x0020_price"],request.form["max_x0020_price"],request.form["modal_x0020_price"]
            db.session.add(a)
            db.session.commit()
            return render_template("form.html",result="Succesfully Added",a="post")

        except:
            return render_template("form.html",result="Some Error Occure",a="post")

@app.route("/models.html",methods=["GET",'POST'])  
def f4():
    if request.method=="GET":
        return render_template("models.html")
    else:
        new_data = pd.DataFrame({
            'State': [request.form["state"]],
            'District': ['request.form["district"]'],
            'Variety': ['request.form["variety"]'],
            'Min_x0020_Price': [request.form["min_value"]],
            'Max_x0020_Price': [request.form["max_value"]]
        })
        predicted_modal_price = pipeline.predict(new_data)
        return render_template('models.html',result=predicted_modal_price,a="post")
