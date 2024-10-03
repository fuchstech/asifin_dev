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

# Backtest sayfası ve sonuç gösterimi
@app.route('/backtest', methods=['GET', 'POST'])
def backtest():
    if request.method == 'POST':
        max_transactions = request.form['max_transactions']
        stable_coin = request.form['stable_coin']
        budget = request.form['budget']
        trade_pair = request.form['trade_pair']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        strategy = request.form['strategy']
        time_frame = request.form['time_frame']

        # Varsayılan bir result_message tanımlıyoruz
        result_message = "İşlem yapıldı."

        # Backtest başlat butonuna mı basıldı yoksa parametre optimizasyonu mu?
        if 'backtest' in request.form:
            result_message = "Backtest başarıyla başlatıldı!"
        elif 'optimize' in request.form:
            result_message = "Parametre optimizasyonu başlatıldı!"

        # İşlenmiş veriyi bir sözlükte tutalım
        result = {
            'max_transactions': max_transactions,
            'stable_coin': stable_coin,
            'budget': budget,
            'trade_pair': trade_pair,
            'start_date': start_date,
            'end_date': end_date,
            'strategy': strategy,
            'time_frame': time_frame,
            'message': result_message
        }

        # Formdan gelen verileri txt dosyasına yazalım
        with open('backtest_results.txt', 'w') as file:
            file.write(f"En Fazla Açılacak İşlem: {max_transactions}\n")
            file.write(f"Stabil Para: {stable_coin}\n")
            file.write(f"Bütçe: {budget}\n")
            file.write(f"İşlem Çifti: {trade_pair}\n")
            file.write(f"Başlangıç Tarihi: {start_date}\n")
            file.write(f"Bitiş Tarihi: {end_date}\n")
            file.write(f"Strateji: {strategy}\n")
            file.write(f"Zaman Biçimi: {time_frame}\n")

        # İşlenen veriyi aynı sayfada göstermek için geri gönderiyoruz
        return render_template('backtest.html', result=result)
    return render_template('backtest.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
