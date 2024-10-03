from flask import Flask, render_template, request

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Hakkımızda sayfası
@app.route('/hakkimizda')
def hakkimizda():
    return render_template('hakkimizda.html')

# Hizmetler sayfası
@app.route('/hizmetler')
def hizmetler():
    return render_template('hizmetler.html')

# Backtest sayfası
@app.route('/backtest')
def backtest():
    return render_template('backtest.html')

# Backtest sonucu (POST işlemi)
@app.route('/backtest_result', methods=['POST'])
def backtest_result():
    max_transactions = request.form['max_transactions']
    stable_coin = request.form['stable_coin']
    budget = request.form['budget']
    trade_pair = request.form['trade_pair']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    strategy = request.form['strategy']
    time_frame = request.form['time_frame']

    # Verileri bir txt dosyasına yazma
    with open('backtest_results.txt', 'w') as file:
        file.write(f"En Fazla Açılacak İşlem: {max_transactions}\n")
        file.write(f"Stabil Para: {stable_coin}\n")
        file.write(f"Bütçe: {budget}\n")
        file.write(f"İşlem Çifti: {trade_pair}\n")
        file.write(f"Başlangıç Tarihi: {start_date}\n")
        file.write(f"Bitiş Tarihi: {end_date}\n")
        file.write(f"Strateji: {strategy}\n")
        file.write(f"Zaman Biçimi: {time_frame}\n")

    return "Backtest verileri başarıyla kaydedildi!"

if __name__ == '__main__':
    app.run(debug=True)
