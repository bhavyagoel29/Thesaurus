from flask import Flask, render_template,request
import synonyms
import antonyms
import definition 
app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def thesaurus():
    syn=['type something']
    ant=['typee something']
    defi=['typeee something']
    if request.method=='POST':
        word=request.form['username']
        syn=synonyms.synonyms(word)
        ant=antonyms.antonyms(word)
        defi=[str(definition.definition(word))]
    return render_template('home.html',syn=syn,ant=ant,defi=defi)
app.run(debug=True)
