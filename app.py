from flask import Flask, render_template

app = Flask(__name__)

# Ana sayfa için rota
@app.route('/')
def index():
    return render_template('index.html')

# Hakkımızda sayfası için rota
@app.route('/hakkimizda')
def hakkimizda():
    return render_template('hakkimizda.html')

# Hizmetler sayfası için rota
@app.route('/hizmetler')
def hizmetler():
    return render_template('hizmetler.html')

@app.route('/run_backtest')
def run_backtest():
    print("Backtest başlatıldı!")
    return "Backtest başlatıldı, konsolu kontrol edin."

if __name__ == '__main__':
    app.run(debug=True)
