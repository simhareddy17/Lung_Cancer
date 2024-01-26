from django.contrib import messages

from .models import copd
from django.views.generic.detail import DetailView
from patient.models import PatientReg
from django.contrib.auth.models import User, auth
from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Image,Spacer
#creating the reportlab pdf library here.
import time
from reportlab.lib.enums import TA_JUSTIFY

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
#creating the CNN library from here
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.layers import GRU, Input, Dense, TimeDistributed, Activation, RepeatVector, Bidirectional
#from keras.layers.embeddings import Embedding
#from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy
import datetime
#new tensorflow


from keras import layers
import tensorflow
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from sklearn import preprocessing
from keras.models import Sequential

#random forest importing for the heart
from sklearn.ensemble import RandomForestClassifier
#importing the smtp
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
#creating the reportlab pdf library here.
import time
from reportlab.lib.enums import TA_JUSTIFY

from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Create your views here.

def index(request):
    return render(request,"doctor/index.html")
def home(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"doctor/option.html")
        else :
            messages.info(request,'invalid crenditials')
            return render(request,"doctor/home.html")
    
    else :        

        return render(request,"doctor/home.html")    
    return render(request,'doctor/home.html')

def login(request):
    
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"doctor/option.html")
        else :
            messages.info(request,'invalid crenditials')
            return render(request,"doctor/home.html")
    
    else :        

        return render(request,"doctor/home.html")    
    #return render(request,'doctor/home.html')
#def register(request):
#    return render(request,'doctor/register.html')

def login2(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"doctor/option.html")
        else :
            messages.info(request,'invalid crenditials')
            return render(request,"doctor/home.html")
    
    else :        

        return render(request,"doctor/home.html")    
    return render(request,'doctor/home.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email1=request.POST['email']
        email2=request.POST['email2']
        password1=request.POST['password']
        password2=request.POST['password2']
        if password1 == password2 and email1 == email2:
            if User.objects.filter(username=email1):
                #print("Username is taken")
                messages.info(request,'Username is taken')
                return redirect('register')
            else:
                
                user = User.objects.create_user(username=email1, password = password1, email = email1, first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
        else:
            #print("Password not matching or email is not matching")
            messages.info(request,'Password not matching or email is not matching')
            return redirect('register')
        #return HttpResponse("<script>alert('User created')</script>")
        return render(request,'doctor/registerComplet.html')
    
    else :
        
        return render(request,'doctor/register.html')

def rcomplete(request):
    return render(request,'doctor/registerComplet.html')


def lungcancer(request):
    return render(request, 'doctor/patientReport.html')


def predict(request):
    a = request.POST['Genetic_Risk']
    b = request.POST['Occupational_hazard']
    c = request.POST['chest_pain']
    d = request.POST['chronic_lung_cancer']
    e = request.POST['clubbing_of_finger_nail']
    f = request.POST['coughing_of_blood']
    g = request.POST['dry_cough']
    h = request.POST['fatigue']
    i = request.POST['passive_smoker']
    j = request.POST['smocking']
    k = request.POST['weight_loss']
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof = request.POST['reportof']
    
    lists =[a,b,c,d,e,f,g,h,i,j,k]
    df = pd.read_csv(r"static/database/lungcancer.csv")
    X_train = df[['Genetic Risk','OccuPational Hazards','Chest Pain','chronic Lung Disease','Clubbing of Finger Nails','Coughing of Blood','Dry Cough','Fatigue','Passive Smoker','Smoking','Weight Loss']]
    
    Y_train = df[['Level']]
    tree = DecisionTreeClassifier(max_leaf_nodes=6, random_state=0)

    tree.fit(X_train, Y_train)
    prediction = tree.predict([[a,b,c,d,e,f,g,h,i,j,k]])
    
    return render(request,'doctor/predict.html',{"data":prediction,"lists":lists,"a1":a,"b1":b,"c1":c,"d1":d,"e1":e,"f1":f,"g1":g,"h1":h,"i1":i,"j1":j,"k1":k,"pemail1":pemail1,"docname1":docname1,"reportof":reportof})

def datafetch(request):
    d = PatientReg.objects.all()
    return render(request,'doctor/datafetch.html',{"data6":d})

    
    
def lungesv(request):
	
   
    a1 = request.POST['Genetic_Risk']
    b = request.POST['Occupational_hazard']
    c = request.POST['chest_pain']
    d1 = request.POST['chronic_lung_cancer']
    e = request.POST['clubbing_of_finger_nail']
    f = request.POST['coughing_of_blood']
    g = request.POST['dry_cough']
    h = request.POST['fatigue']
    i = request.POST['passive_smoker']
    j = request.POST['smocking']
    k = request.POST['weight_loss']
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof1 = request.POST['reportof']
    detail = request.POST['data']
     #importing the package in realtime.
    from .models import lungreport
    from patient.models import PatientReg
    #importing reportlab
    
    #Genrating the report here
    basename = "lungReport"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename2 = "_".join([basename, suffix])
    loc="static/report/"+filename2+".pdf"

    b3 = PatientReg.objects.get(pemail=pemail1)
   
    fname = b3.pname

    #file naming is in above
    doc = SimpleDocTemplate(loc,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
    Story=[]
    logo = "static/images/seal.png"

    #giving all body of report
    formatted_time = time.ctime()
    full_name = fname
    address_parts = [pemail1]

    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size="12">%s</font>' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '<font size="12"></font>' 
    Story.append(Paragraph(ptext, styles["Normal"]))       
    for part in address_parts:
        
        ptext = '<font size="12">%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   

    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Dear %s:</font>' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">We have generated the report of <b> %s</b>, we found the your risk of %s is \
        =<b>%s</b>, we recommend you to care for your health, because your this health will\
        help you to live the happy life. We are attaching the report here</font>' % (reportof1,reportof1,detail)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Patient email = %s    || Doctor name=%s                    \
    </font>' % (pemail1,docname1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Report of = <b>%s  </b>                 \
    </font>' % (reportof1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    <b>Genetic_Risk</b>= %s     || <b>Occupational_hazard</b>= %s   ||    <b>chest_pain</b>=%s             \
    </font>' % (a1,b,c)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>chronic_lung_cancer</b>= %s     || <b>clubbing_of_finger_nail</b>= %s   ||    <b>coughing_of_blood</b>=%s             \
    </font>' % (d1,e,f)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))



    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>dry_cough</b>= %s     || <b>fatigue</b>= %s   ||   <b> passive_smoker</b>=%s             \
    </font>' % (g,h,i)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>smocking</b>= %s     || <b>weight_loss</b>= %s                \
    </font>' % (j,k)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))




    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Your rishk about the<b> %s</b>=<b> %s</b>                 \
    </font>' % (reportof1,detail)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
                \
    </font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Thank you very much and we look forward to serving you.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = '<font size="12">%s</font>' % (docname1)
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))





    doc.build(Story)
    #applying the smtp server here
    """from redmail import outlook

    outlook.user_name = "kasthurikrish@outlook.com"
    outlook.password = "Kasthu@07"

    outlook.send(
            receivers=pemail1,
            subject="Lung Cancer Report",
            msg=MIMEMultipart()
            msg.attach(MIMEText(body,'plain'))
            filename = filename2+".pdf"
            attachment = open(loc, "rb")
            p = MIMEBase('application', 'octet-stream') 


            p.set_payload((attachment).read()) 

 
            encoders.encode_base64(p) 

            p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 


            msg.attach(p) """

            
            
    fromaddr = "techcitiforyou@outlook.com"
    toaddr = pemail1
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 


    msg['To'] = toaddr 
    msg['Subject'] = "This is your report"
    body = "Kindly check the attachment"
    msg.attach(MIMEText(body, 'plain')) 


    filename = filename2+".pdf"
    attachment = open(loc, "rb")
    p = MIMEBase('application', 'octet-stream') 


    p.set_payload((attachment).read()) 

 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 


    msg.attach(p) 

 
    s = smtplib.SMTP('smtp-mail.outlook.com', 587) 


    s.starttls() 

 
    s.login(fromaddr, "techcititech@1234") 


    text = msg.as_string() 

 
    s.sendmail(fromaddr, toaddr, text) 

    print("Msg sent successful")
    s.quit()
    #saving the data

    if len(lungreport.objects.filter(patientemail=pemail1)) == 1:
        a = lungreport.objects.get(patientemail = pemail1)
        a.docname = docname1
        a.reportof = reportof1
        a.reportnm = filename
        a.Genetic_Risk = a1
        a.Occupational_hazard = b
        a.chest_pain = c
        a.chronic_lung_cancer = d1
        a.clubbing_of_finger_nail = e
        a.coughing_of_blood = f
        a.dry_cough = g
        a.fatigue = h
        a.passive_smoker = i
        a.smocking = j 
        a.weight_loss = k
        a.riskvalue = detail
        a.save()
    else:
        

        d = lungreport(patientemail=pemail1,docname=docname1,reportof=reportof1,reportnm=filename,Genetic_Risk=a1,Occupational_hazard=b,chest_pain=c,chronic_lung_cancer=d1,clubbing_of_finger_nail=e,coughing_of_blood=f,dry_cough=g,fatigue=h,passive_smoker=i,smocking=j,weight_loss=k,riskvalue=detail)
        d.save()
    return render(request,'doctor/sendSuccess.html')


