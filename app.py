import os
from flask import Flask, request

app = Flask(__name__)

# --- واجهة Geno-X Pro الاحترافية ---
HTML_CODE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GENO-X PRO | الإمبراطورية الرقمية</title>
    <style>
        :root { --blue: #00aaff; --bg: #05080a; --card: rgba(13, 17, 23, 0.9); }
        body { 
            background: var(--bg) url('https://w0.peakpx.com/wallpaper/429/904/壓路機-wallpaper-abstract-digital-art-space-stars-nebula.jpg') no-repeat center center fixed;
            background-size: cover; color: white; font-family: 'Segoe UI', Tahoma, sans-serif; margin: 0;
        }
        .overlay { background: rgba(0, 0, 0, 0.75); min-height: 100vh; width: 100%; }
        .promo-bar { background: linear-gradient(90deg, #ff0000, #b30000); color: white; padding: 10px; text-align: center; font-weight: bold; font-size: 14px; box-shadow: 0 0 15px rgba(255,0,0,0.5); }
        .navbar { padding: 20px 60px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(0, 170, 255, 0.3); background: rgba(13, 17, 23, 0.9); }
        .logo { font-size: 28px; font-weight: bold; color: var(--blue); text-shadow: 0 0 15px var(--blue); letter-spacing: 2px; }
        .hero { text-align: center; padding: 60px 20px; }
        .hero h1 { font-size: clamp(30px, 5vw, 55px); margin: 0; text-shadow: 0 0 20px var(--blue); }
        .stats-bar { display: flex; justify-content: space-around; background: rgba(0, 170, 255, 0.15); padding: 20px; border-top: 1px solid var(--blue); border-bottom: 1px solid var(--blue); margin: 30px 0; backdrop-filter: blur(10px); }
        .main-content { display: flex; gap: 30px; padding: 20px 60px; flex-wrap: wrap; justify-content: center; }
        .services-grid { flex: 2; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; min-width: 300px; }
        .service-card { background: var(--card); border: 1px solid #1e2631; padding: 30px; border-radius: 15px; text-align: center; transition: 0.4s; backdrop-filter: blur(10px); }
        .service-card:hover { border-color: var(--blue); transform: translateY(-10px); box-shadow: 0 0 25px rgba(0, 170, 255, 0.4); }
        .order-panel { flex: 1; min-width: 320px; background: var(--card); padding: 35px; border-radius: 20px; border: 2px solid var(--blue); box-shadow: 0 0 30px rgba(0, 170, 255, 0.2); }
        input, select { width: 100%; padding: 15px; margin: 12px 0; background: #0a0e14; border: 1px solid #1e2631; color: white; border-radius: 8px; box-sizing: border-box; }
        .btn-confirm { width: 100%; padding: 18px; background: var(--blue); border: none; color: black; font-weight: bold; cursor: pointer; border-radius: 8px; font-size: 18px; transition: 0.3s; }
        .btn-confirm:hover { background: white; transform: scale(1.02); }
        .wa-btn { display: block; text-align: center; margin-top: 20px; color: #25d366; text-decoration: none; font-weight: bold; border: 1px solid #25d366; padding: 15px; border-radius: 8px; transition: 0.3s; }
        .wa-btn:hover { background: #25d366; color: white; }
        footer { text-align: center; padding: 50px; color: #555; font-size: 13px; }
    </style>
</head>
<body>
    <div class="overlay">
        <div class="promo-bar">🔥 عرض محدود: خصم 70% ينتهي خلال: <span id="timer">01:59:59</span></div>
        <div class="navbar"><div class="logo">GENO-X PRO</div></div>
        <div class="hero">
            <h1>إمبراطورية الخدمات الرقمية</h1>
            <p>سرعة البرق | أمان تام | دعم يمني مباشر</p>
        </div>
        <div class="stats-bar">
            <div>الطلبات<span>+2.5M</span></div>
            <div>السرعة<span>0.5s</span></div>
            <div>المستخدمين<span>+5K</span></div>
        </div>
        <div class="main-content">
            <div class="services-grid">
                <div class="service-card"><h3>INSTAGRAM</h3><p>متابعين ولايكات حقيقية</p></div>
                <div class="service-card"><h3>TIKTOK</h3><p>دعم بث وإكسبلور</p></div>
                <div class="service-card"><h3>YOUTUBE</h3><p>مشتركين وساعات</p></div>
                <div class="service-card"><h3>FACEBOOK</h3><p>تفاعل ومتابعين بيج</p></div>
            </div>
            <div class="sidebar">
                <div class="order-panel">
                    <h2 style="text-align:center; color:var(--blue); margin:0 0 20px 0;">إنشاء طلب جديد</h2>
                    <form action="/order" method="post">
                        <select name="p"><option>INSTAGRAM</option><option>TIKTOK</option><option>YOUTUBE</option></select>
                        <input type="text" name="l" placeholder="رابط الحساب / الفيديو" required>
                        <input type="number" name="q" placeholder="الكمية المطلوبة" required>
                        <button type="submit" class="btn-confirm">تأكيد وانطلاق 🚀</button>
                    </form>
                    <a href="https://wa.me/967771424137?text=أريد تفعيل طلبي في جينو إكس" class="wa-btn">💬 تواصل مع الإدارة (واتساب)</a>
                </div>
            </div>
        </div>
        <footer>GENO-X PRO SYSTEMS - 2026 | COPYRIGHT</footer>
    </div>
    <script>
        let time = 7200;
        setInterval(() => {
            let h = Math.floor(time/3600); let m = Math.floor((time%3600)/60); let s = time%60;
            document.getElementById('timer').innerHTML = `${h}:${m}:${s}`;
            if(time > 0) time--;
        }, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return HTML_CODE

@app.route('/order', methods=['POST'])
def order():
    # هنا يتم حفظ الطلب (في السيرفر الحقيقي سنستخدم Database)
    return "<body style='background:#05080a; color:#00aaff; text-align:center; padding-top:100px;'><h1>✅ تم استلام طلبك!</h1><p>تواصل مع الإدارة لتأكيد الدفع والبدء.</p><a href='/' style='color:white;'>عودة</a></body>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))