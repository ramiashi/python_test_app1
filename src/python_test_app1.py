from flask import Flask
app = Flask(__name__)

def factors(num):
  return [x for x in range(1, num+1) ]

@app.route('/')
def home():
  return '<h1><a href="/AUTO_BUILD_Orange_Jordan/10"> An Automated build test Page</a></h1>'

@app.route('/AUTO_BUILD_Orange_Jordan/<int:n>')
def factors_display_raw_html(n):
	factors_list = factors(int(n))
	# First we put the stuff at the top, adding "n" in there
	html = "<h1> This build has  "+str(n)+" numbers</h1>"+"\n"+"<ul>"

	# for each factor, we make a <li> item for it
	for f in factors_list:
		html += "<li>"+str(f)+"</li>"+"\n"
	html += "</ul> </body>" # the close tags at the bottom
	return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')

