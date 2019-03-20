from flask import Flask
app = Flask(__name__)
from flask import render_template
from flask import request
import mbta_helper
Accessible=0

@app.route('/')
def hello():
    return render_template('WebPageHello.html')

@app.route('/nearest/', methods =['POST', 'GET'])
def nearest():
    if request.method == 'POST':
        Address = request.form['Address']
        Address=Address.strip()
        Address = Address.replace(" ", "+")
        Address=Address.replace(".", "")
        print(Address)
        City=request.form['City']
        State=request.form['State']
        ZIP=request.form['zip']
        Location=Address+","+City+","+ State +","+ ZIP
        print(Location)
        outputs= mbta_helper.main(Location)
        print(outputs)
        if outputs==():
            return render_template('Errors.html')
        Stop_name=(outputs[0])
        Accessible= outputs[1]
        if Accessible==1:
            Accessible="This Stop Is Wheelchair Accessible!"
        else:
            Accessible="Sorry, This Stop Is Not Wheelchair Accessible."
        return render_template('Loading.html', Accessible=Accessible, Stop_name=Stop_name )
    else:
        return render_template('WebPageHello.html')
if __name__ == '__main__':
    app.run()
