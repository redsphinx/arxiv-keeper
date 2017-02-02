import subprocess

from flask import Flask, request, session

from mendeley import Mendeley

app = Flask(__name__)
app.debug = False
app.secret_key = "asehaiosehao"

secret = "VdwFxQAb3B0QZMiq"
redirect_uri = "http://localhost:5000/oauth"

@app.route('/oauth')
def auth_return():
    code = request.args.get("code")
    state = request.args.get("state")
    auth = mendeley.start_authorization_code_flow(state=state)
    mendeley_session = auth.authenticate(request.url)

    return str(mendeley_session.token)


if __name__ == '__main__':
    mendeley = Mendeley(3950, secret, redirect_uri)

    auth = mendeley.start_authorization_code_flow()

    login_url = auth.get_login_url()
    subprocess.call(['open', login_url])

    app.run(host='localhost', port=5000, debug=False)

