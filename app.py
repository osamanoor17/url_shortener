from flask import Flask, render_template, request, jsonify
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    url = data.get('url', '')
    service = data.get('service', '')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        s = get_shortener_instance(service)
        short_url = s.short(url)
        return jsonify({'short_url': short_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def get_shortener_instance(service):
    if service == 'TinyURL.com':
        return pyshorteners.Shortener().tinyurl
    elif service == 'Is.gd':
        return pyshorteners.Shortener().isgd
    elif service == 'Da.gd':
        return pyshorteners.Shortener().dagd
    elif service == 'Clck.ru':
        return pyshorteners.Shortener().clckru
    else:
        raise ValueError("Unsupported shortening service.")

if __name__ == '__main__':
    app.run(debug=True)
