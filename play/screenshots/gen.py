import sys
from playwright.sync_api import sync_playwright
L=sys.argv[1]
nb=L=="nb"
t=lambda a,b:a if nb else b
msg=t("Du trenger ikke fikse alt i dag. Én ting er nok.","You don't have to fix everything today. One thing is enough.")
msg2=t("Drikk et glass vann. Det tar 20 sekunder og hjelper mer enn du tror.","Drink a glass of water. It takes 20 seconds and helps more than you think.")
msg3=t("Dette er også en dag som går over.","This too is a day that passes.")
css="""
*{box-sizing:border-box;margin:0;font-family:Roboto,'Noto Sans',Arial,sans-serif}
body{width:360px;height:640px;background:#FFF8EE;color:#2B2116;position:relative;overflow:hidden}
.sb{height:24px;display:flex;justify-content:space-between;padding:4px 14px;font-size:12px;font-weight:500}
.nav{position:absolute;bottom:0;left:0;right:0;height:80px;background:#F7EBD8;display:flex;justify-content:space-around;padding-top:12px}
.ni{display:flex;flex-direction:column;align-items:center;font-size:12px;gap:4px;width:80px}
.ni .pill{width:64px;height:32px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:16px}
.ni.sel .pill{background:#FFE2B0}.ni.sel{font-weight:600}
.c{padding:16px;display:flex;flex-direction:column;gap:14px}
h1{font-size:22px;font-weight:700}
.card{border-radius:28px;padding:24px;min-height:250px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.card .e{font-size:48px;margin-bottom:14px}.card .m{font-size:26px;line-height:34px;font-weight:700;color:#3A2A1A}
.card .k{margin-top:14px;font-size:12px;letter-spacing:1.4px;color:#5A4630}
.btn{background:#8A5A00;color:#fff;border-radius:20px;height:40px;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:500}
.row{display:flex;gap:10px}.ob{flex:1;border:1px solid #8A7A66;border-radius:20px;height:40px;display:flex;align-items:center;justify-content:center;font-size:14px;color:#8A5A00;font-weight:500}
.sm{font-size:12px}
.sw{display:flex;align-items:center;justify-content:space-between;font-size:16px}
.tg{width:52px;height:32px;border-radius:16px;background:#8A5A00;position:relative}.tg:after{content:'';position:absolute;right:4px;top:4px;width:24px;height:24px;border-radius:12px;background:#fff}
.tg.off{background:#E6D8C2;border:2px solid #8A7A66}.tg.off:after{left:4px;right:auto;background:#8A7A66;width:16px;height:16px;top:6px}
hr{border:0;border-top:1px solid #D9C9B0}
.sl{height:4px;background:#E6D8C2;border-radius:2px;position:relative;margin:10px 0}.sl i{position:absolute;left:0;width:50%;height:4px;background:#8A5A00;border-radius:2px}.sl b{position:absolute;left:50%;top:-8px;width:20px;height:20px;border-radius:10px;background:#8A5A00;margin-left:-10px}
.st{display:flex;align-items:center;gap:8px;font-size:16px}.st span{flex:1}.st .n{border:1px solid #8A7A66;border-radius:20px;padding:6px 16px;color:#8A5A00;font-size:16px}
.chip{border:1px solid #8A7A66;border-radius:8px;padding:6px 12px;font-size:14px}.chip.on{background:#FFE2B0;border-color:#FFE2B0;font-weight:500}
"""
def nav(i):
    labs=[t("Hjem","Home"),t("Mine","Mine"),t("Innstillinger","Settings")];ic=["☀️","★","⚙️"]
    return '<div class="nav">'+''.join(f'<div class="ni {"sel" if k==i else ""}"><div class="pill">{ic[k]}</div>{labs[k]}</div>' for k in range(3))+'</div>'
sb='<div class="sb"><span>9:41</span><span>▲ ▮ 100%</span></div>'
def home(grad,emo,m,cat,fav=False):
    return f'''{sb}<div class="c"><h1>Pocketsun</h1>
<div class="card" style="background:linear-gradient(135deg,{grad[0]},{grad[1]})"><div class="e">{emo}</div><div class="m">{m}</div><div class="k">{cat.upper()}</div></div>
<div class="btn">{t("Ny melding","New message")}</div>
<div class="row"><div class="ob">{"♥" if fav else "♡"} {t("Favoritt","Favorite")}</div><div class="ob">{t("Skjul","Hide")}</div></div>
<div class="row"><div class="ob">{t("Liker","Like")}</div><div class="ob">{t("Liker ikke","Dislike")}</div></div>
<div style="font-size:14px">{t("Neste melding: tor. 26. nov. 13:30","Next message: Thu 26 Nov 1:30 PM")}</div>
<div class="row"><div class="ob sm">{t("Pause 1 time","Pause 1 hour")}</div><div class="ob sm">{t("Pause i dag","Pause today")}</div><div class="ob sm">{t("Pause 1 uke","Pause 1 week")}</div></div></div>{nav(0)}'''
def settings():
    cats=[(t("Varm","Warm"),1),(t("Humor","Humor"),1),(t("Liten handling","Small action"),1),(t("Perspektiv","Perspective"),1)]
    return f'''{sb}<div class="c" style="gap:12px"><h1>{t("Innstillinger","Settings")}</h1>
<div class="sw"><span>{t("Varsler","Notifications")}</span><div class="tg"></div></div>
<div style="font-weight:600;font-size:16px">{t("Meldinger per dag","Messages per day")}: 3</div><div class="sl"><i></i><b></b></div>
<div style="font-weight:600;font-size:16px">{t("Tidsvindu","Time window")}</div>
<div class="st"><span>{t("Fra kl.","From")}</span><div class="n">−</div><b>09:00</b><div class="n">+</div></div>
<div class="st"><span>{t("Til kl.","To")}</span><div class="n">−</div><b>20:00</b><div class="n">+</div></div>
<div class="sw"><span>{t("Myk vibrasjon","Soft vibration")}</span><div class="tg"></div></div><hr>
<div style="font-weight:600;font-size:16px">{t("Meldingstyper","Message types")}</div>
{''.join(f'<div class="sw"><span>{c}</span><div class="tg"></div></div>' for c,_ in cats)}
</div>{nav(2)}'''
def mine():
    return f'''{sb}<div class="c"><h1>{t("Mine meldinger","My messages")}</h1>
<div style="font-size:16px">{t("Skriv noe fint til deg selv, eller noe en venn pleier å si til deg.","Write something kind to yourself, or something a friend often says to you.")}</div>
<div style="border:1px solid #8A7A66;border-radius:4px;height:72px;padding:12px;font-size:16px">{t("Du klarer dette.","You've got this.")}</div>
<div class="btn" style="width:110px">{t("Legg til","Add")}</div>
<div class="sw"><span style="flex:1">{t("Du klarer dette.","You've got this.")}</span><span style="color:#8A5A00;font-size:14px;font-weight:500">{t("Slett","Delete")}</span></div><hr>
<div style="font-size:20px;font-weight:700">{t("Favoritter","Favorites")}</div>
<div class="sw"><span style="flex:1;font-size:16px">{msg3}</span><span style="color:#8A5A00;font-size:14px;font-weight:500">{t("Fjern","Remove")}</span></div>
<div class="sw"><span style="flex:1;font-size:16px">{msg}</span><span style="color:#8A5A00;font-size:14px;font-weight:500">{t("Fjern","Remove")}</span></div></div>{nav(1)}'''
def notif():
    return f'''<body style="background:linear-gradient(#5b6f8f,#2d3a52)"><div class="sb" style="color:#fff"><span>9:41</span><span>▲ ▮ 100%</span></div>
<div style="color:#fff;padding:30px 24px 0"><div style="font-size:64px;font-weight:300">9:41</div><div style="font-size:14px;opacity:.85">{t("torsdag 26. november","Thursday, November 26")}</div></div>
<div style="margin:40px 12px 0;background:#FFF8EE;border-radius:24px;padding:14px 16px;color:#2B2116">
<div style="display:flex;align-items:center;gap:8px;font-size:12px;color:#5a4a36"><span style="color:#FFB703;font-size:16px">☀</span> Pocketsun · {t("nå","now")}</div>
<div style="font-size:16px;font-weight:600;margin-top:6px">💛 Pocketsun</div>
<div style="font-size:14px;margin-top:2px;line-height:20px">{msg}</div></div>
<div style="margin:10px 12px 0;background:#FFF8EE;border-radius:24px;padding:14px 16px;color:#2B2116;opacity:.92">
<div style="display:flex;align-items:center;gap:8px;font-size:12px;color:#5a4a36"><span style="color:#FFB703;font-size:16px">☀</span> Pocketsun · 13:30</div>
<div style="font-size:16px;font-weight:600;margin-top:6px">🌿 Pocketsun</div>
<div style="font-size:14px;margin-top:2px;line-height:20px">{msg2}</div></div></body>'''
def widget():
    return f'''<body style="background:linear-gradient(160deg,#f6c28b,#e98f9d 45%,#6d6fb8)"><div class="sb" style="color:#fff"><span>9:41</span><span>▲ ▮ 100%</span></div>
<div style="padding:60px 16px 0"><div style="border-radius:22px;background:linear-gradient(135deg,#FFE8B3,#FFC999);padding:14px;width:328px;height:150px;display:flex;flex-direction:column;justify-content:center">
<div style="font-size:22px">💛</div><div style="font-size:15px;font-weight:700;color:#3A2A1A;margin-top:4px">{msg}</div></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:22px 10px;margin-top:40px;color:#fff;font-size:11px;text-align:center">
{''.join('<div><div style="width:56px;height:56px;border-radius:16px;background:rgba(255,255,255,.28);margin:0 auto 6px"></div>'+n+'</div>' for n in [t("Kamera","Camera"),t("Kart","Maps"),t("Klokke","Clock"),t("Notater","Notes"),t("Kalender","Calendar"),t("Bilder","Photos"),t("Nettleser","Browser"),t("Meldinger","Messages")])}
<div><div style="width:56px;height:56px;border-radius:16px;background:#FFF1D6;margin:0 auto 6px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#FFB703">☀</div>Pocketsun</div></div></div></body>'''
shots=[("1-home",f'<body>{home(["#FFE8B3","#FFC999"],"💛",msg,t("Varm","Warm"))}</body>'),
("2-varsel",notif()),("3-widget",widget()),
("4-innstillinger",f'<body>{settings()}</body>'),
("5-mine",f'<body>{mine()}</body>'),
("6-humor",f'<body>{home(["#E3EEFC","#C8D9F8"],"🌿",msg2,t("Liten handling","Small action"),True)}</body>')]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":360,"height":640},device_scale_factor=3)
    for n,h in shots:
        pg.set_content(f'<html><head><meta charset="utf-8"><style>{css}</style></head>{h}</html>')
        pg.screenshot(path=f"{L}-{n}.png")
    b.close()
