from flask import Flask,request,jsonify
import json
import base64
import wikipedia
import webbrowser

app = Flask(__name__)
@app.route('/api',methods=['GET'])
def take_command():
    d = {}
    d['Query']= str(request.args['Query'])
    
    #WIKIPEDIA
    if 'wikipedia' in d['Query']:
        d['Query'] = d['Query'].replace("wikipedia", "")
        results = wikipedia.summary(d['Query'], sentences=2)
        return jsonify(results)
    
    #YOUTUBE
    elif 'open youtube' in d['Query']:
        url = f"https://www.youtube.com"
        webbrowser.open(url)
    elif 'youtube' in d['Query']:
        d['Query'] = d['Query'].replace("youtube", "")
        url = f"https://www.youtube.com/results?search_query={d['Query']}"
        webbrowser.get().open(url)
    
    #GOOGLE
    elif 'open google' in d['Query']:
        url = f"https://google.com/search?q="
        webbrowser.open(url)
    elif 'google' in d['Query']:
        d['Query'] = d['Query'].replace("google", "")
        url = f"https://google.com/search?q={d['Query']}"
        webbrowser.get().open(url)
    
    #TIME-TABLE
    elif 'time table' in d['Query']:
        data = {}
        with open(r'C:\Users\divya\OneDrive\Desktop\CLG\191270\Project\ZEUS\pictures\timetable_sem_3.jpg', mode='rb') as file:
            img = file.read()
        data['img'] = base64.encodebytes(img).decode("utf-8")
        return(json.dumps(data))
    return jsonify (d)


if __name__ == "__main__":
    app.run(host='0.0.0.0') 


