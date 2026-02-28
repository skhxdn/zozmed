#!/usr/bin/env python3
"""
SOSMED TOOL - by skhxdn666
20 Features Social Media Toolkit
"""

import os, sys, json, random, time, subprocess, re, math, string
from datetime import datetime

class C:
    RED     = '\033[91m'
    DRED    = '\033[31m'
    PURPLE  = '\033[95m'
    MAG     = '\033[35m'
    WHITE   = '\033[97m'
    GREY    = '\033[90m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    RESET   = '\033[0m'

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    cls()
    print(f"""
{C.DRED}{C.BOLD}
  ██████╗ ██╗███████╗██╗  ██╗██████╗ ██████╗  █████╗ ██╗███╗  ██╗
  ██╔══██╗██║██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██║████╗ ██║
  ██║  ██║██║█████╗   ╚███╔╝ ██████╔╝██████╔╝███████║██║██╔██╗██║
  ██║  ██║██║██╔══╝   ██╔██╗ ██╔══██╗██╔══██╗██╔══██║██║██║╚████║
  ██████╔╝██║███████╗██╔╝╚██╗██████╔╝██║  ██║██║  ██║██║██║ ╚███║
  ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚══╝
{C.RESET}{C.PURPLE}  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{C.RESET}
{C.GREY}     💀  20-Feature Social Media Toolkit  💀{C.RESET}
{C.GREY}        created by {C.PURPLE}skhxdn666{C.RESET}
{C.PURPLE}  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{C.RESET}""")

def menu():
    print(f"""
{C.PURPLE}{C.BOLD}  ☠  MENU  ☠{C.RESET}

  {C.RED}[01]{C.RESET} 💀  Downloader Video/Foto
  {C.RED}[02]{C.RESET} 🩸  Username Checker Multi-Platform
  {C.RED}[03]{C.RESET} 🔮  Caption & Hashtag Generator
  {C.RED}[04]{C.RESET} 📜  Content Manager & Scheduler
  {C.RED}[05]{C.RESET} 👁️   Analisis Bio & Profile
  {C.RED}[06]{C.RESET} 🕷️   Hashtag Toolkit
  {C.RED}[07]{C.RESET} 🩻  Link Shortener & History
  {C.RED}[08]{C.RESET} 🔠  Font Style Generator
  {C.RED}[09]{C.RESET} 📊  Engagement Rate Calculator
  {C.RED}[10]{C.RESET} ⏰  Best Time to Post
  {C.RED}[11]{C.RESET} 💡  Content Idea Generator
  {C.RED}[12]{C.RESET} 🧵  Thread Formatter (Twitter/X)
  {C.RED}[13]{C.RESET} 🤖  Fake Account Analyzer
  {C.RED}[14]{C.RESET} 🎨  Brand Color Palette Generator
  {C.RED}[15]{C.RESET} 📝  Bio Template Generator
  {C.RED}[16]{C.RESET} 🪝  Viral Hook Generator
  {C.RED}[17]{C.RESET} 😈  Emoji Search & Copy
  {C.RED}[18]{C.RESET} 🔑  Password Generator (Akun)
  {C.RED}[19]{C.RESET} 💬  Text Tone Converter
  {C.RED}[20]{C.RESET} 📈  Follower Growth Tracker
  {C.RED}[00]{C.RESET} 🚪  Keluar

{C.PURPLE}  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{C.RESET}""")

def pause():
    input(f"\n  {C.GREY}[ Enter untuk kembali... ]{C.RESET}")

def hdr(title, icon=""):
    print(f"\n{C.RED}{C.BOLD}[ {icon}  {title} ]{C.RESET}\n")

def sep():
    print(f"\n  {C.PURPLE}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{C.RESET}\n")

# ═══════════════════════════════════════════════════════
# 01 - DOWNLOADER
# ═══════════════════════════════════════════════════════
def f01_downloader():
    hdr("VIDEO/FOTO DOWNLOADER","💀")
    print(f"  {C.GREY}YouTube, TikTok, Instagram, Twitter, dll{C.RESET}\n")

    try:
        subprocess.run(['yt-dlp','--version'], capture_output=True, check=True)
    except:
        print(f"  {C.PURPLE}yt-dlp belum ada. Install? (y/n): {C.RESET}", end='')
        if input().lower()=='y': os.system('python -m pip install yt-dlp')
        else: return

    opts = ["Video terbaik","Audio MP3","Video 720p","Thumbnail saja","Playlist penuh"]
    for i,o in enumerate(opts,1): print(f"  {C.RED}[{i}]{C.RESET} {o}")
    fmt = input(f"\n  {C.PURPLE}Format [1-5]: {C.RESET}").strip() or '1'
    url = input(f"  {C.PURPLE}URL: {C.RESET}").strip()
    if not url: print(f"  {C.RED}URL kosong!{C.RESET}"); return

    out = os.path.expanduser('~/Downloads')
    tmpl = f'"{out}/%(title)s.%(ext)s"'
    cmds = {
        '1': f'yt-dlp -o {tmpl} "{url}"',
        '2': f'yt-dlp -x --audio-format mp3 -o {tmpl} "{url}"',
        '3': f'yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" -o {tmpl} "{url}"',
        '4': f'yt-dlp --write-thumbnail --skip-download -o {tmpl} "{url}"',
        '5': f'yt-dlp -o {tmpl} --yes-playlist "{url}"',
    }
    print(f"\n  {C.PURPLE}Downloading...{C.RESET}\n")
    os.system(cmds.get(fmt, cmds['1']))
    print(f"\n  {C.RED}✓ Selesai! -> {out}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 02 - USERNAME CHECKER
# ═══════════════════════════════════════════════════════
def f02_username():
    import urllib.request, urllib.error
    hdr("USERNAME CHECKER","🩸")
    uname = input(f"  {C.PURPLE}Username: {C.RESET}").strip()
    if not uname: print(f"  {C.RED}Kosong!{C.RESET}"); return

    platforms = {
        "GitHub":f"https://github.com/{uname}",
        "Twitter/X":f"https://twitter.com/{uname}",
        "Instagram":f"https://www.instagram.com/{uname}/",
        "TikTok":f"https://www.tiktok.com/@{uname}",
        "YouTube":f"https://www.youtube.com/@{uname}",
        "Reddit":f"https://www.reddit.com/user/{uname}",
        "Pinterest":f"https://www.pinterest.com/{uname}/",
        "Twitch":f"https://www.twitch.tv/{uname}",
        "SoundCloud":f"https://soundcloud.com/{uname}",
        "Linktree":f"https://linktr.ee/{uname}",
        "Spotify":f"https://open.spotify.com/user/{uname}",
        "Snapchat":f"https://www.snapchat.com/add/{uname}",
        "Medium":f"https://medium.com/@{uname}",
        "Tumblr":f"https://{uname}.tumblr.com",
        "DeviantArt":f"https://www.deviantart.com/{uname}",
    }
    print(f"\n  {C.PURPLE}Scanning {C.RED}@{uname}{C.PURPLE} on {len(platforms)} platforms...{C.RESET}\n")
    found=[]
    for p,url in platforms.items():
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
            r=urllib.request.urlopen(req,timeout=5)
            if r.getcode()==200:
                print(f"  {C.RED}[💀 FOUND]{C.RESET}  {C.WHITE}{p:<15}{C.RESET} {C.GREY}{url}{C.RESET}")
                found.append(p)
        except urllib.error.HTTPError as e:
            code=e.code
            print(f"  {C.GREY}[✗ {code}]{'':4}{p}{C.RESET}")
        except: print(f"  {C.PURPLE}[⌛ TMO]{'':4}{C.GREY}{p}{C.RESET}")
        time.sleep(0.15)
    sep()
    print(f"  {C.RED}💀 Found: {len(found)}{C.RESET}  {C.GREY}|  Not found: {len(platforms)-len(found)}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 03 - CAPTION GENERATOR
# ═══════════════════════════════════════════════════════
def f03_caption():
    hdr("CAPTION & HASHTAG GENERATOR","🔮")
    niches = {
        "1":("Lifestyle",["Hidup itu tentang menikmati setiap momen kecil 🌿\nKarena bahagia itu sederhana.","Pagi yang tenang, kopi yang hangat ☕\nItulah resep hari yang sempurna.","Slow living bukan berarti malas 🍃\nTapi sadar bahwa tidak semua hal perlu terburu-buru.","Less is more. Sederhanakan hidupmu 🤍"],"#lifestyle #slowliving #mindfulness #selfcare #dailylife #grateful #blessed"),
        "2":("Motivasi",["Mulai dari mana pun tidak masalah, yang penting mulai 🚀","Setiap hari adalah kesempatan baru untuk jadi lebih baik 💪","Gagal bukan akhir. Itu tanda kamu sedang belajar 🔥","Percaya prosesnya. Hasil tidak akan mengkhianati usaha 🌟"],"#motivasi #semangatpagi #quotes #inspirasi #mindset #nevergiveup"),
        "3":("Travel",["Dunia terlalu luas untuk diam di satu tempat 🌍","Bukan soal destinasi, tapi cerita yang dibawa pulang ✈️","Collect moments, not things 🎒","Every journey begins with a single step 🏔️"],"#travel #wanderlust #explore #backpacker #travelgram #holiday"),
        "4":("Food",["Good food = good mood 🍜","Makanan terbaik dimakan bareng orang yang tepat 🍽️","Life is short, eat the good stuff first 🤤","Resep kebahagiaan: masak sendiri, makan bareng 🧑‍🍳"],"#food #foodie #kuliner #instafood #foodphotography #yummy"),
        "5":("Bisnis",["Mimpi besar dimulai dari langkah kecil 💼","Kualitas bukan janji, tapi komitmen 🏆","Terima kasih sudah mempercayai kami ❤️","Promo spesial hari ini, jangan sampai kelewatan 🎉"],"#bisnis #umkm #entrepreneur #jualan #usaha #produklokal"),
        "6":("Dark/Aesthetic",["Not everyone deserves to know the real you 🖤\nLet them criticize who they think you are.","Some souls are just built different 🌑\nDarkness isn't a flaw — it's depth.","They wanted a storm\nbut I gave them a hurricane 🌪️","Silence is my loudest scream 🕸️\nNot all wounds are visible."],"#dark #aesthetic #darkacademia #shadow #blackcore #grunge"),
        "7":("Gaming",["GG EZ 🎮 Another day another W","Skill issue bukan excuse, itu PR 🔥","In-game or IRL, I don't lose 💀","They called it luck. I call it 1000 hours of practice 🎯"],"#gaming #gamer #esports #fyp #streamer #gamingcommunity"),
        "8":("Fitness",["Pain today, glory tomorrow 💪","The only bad workout is the one that didn't happen 🏋️","Built different. Train different. 🔥","Rest day? Never heard of it 😤"],"#gym #fitness #workout #gains #bodybuilding #fitfam"),
    }

    for k,(name,_,_) in niches.items(): print(f"  {C.RED}[{k}]{C.RESET} {name}")
    c = input(f"\n  {C.PURPLE}Pilih [1-8]: {C.RESET}").strip()
    if c not in niches: print(f"  {C.RED}Tidak valid!{C.RESET}"); return
    name, caps, tags = niches[c]
    custom = input(f"  {C.PURPLE}Info tambahan (Enter skip): {C.RESET}").strip()
    extra = f"\n\n{custom}" if custom else ""
    try: n = min(int(input(f"  {C.PURPLE}Generate berapa? [1-{len(caps)}]: {C.RESET}") or 3), len(caps))
    except: n=3
    sep()
    print(f"  {C.RED}{C.BOLD}HASIL — {name}{C.RESET}\n")
    for i,cap in enumerate(random.sample(caps,n),1):
        print(f"  {C.RED}── {i} ──{C.RESET}\n  {cap}{extra}\n\n  {C.GREY}{tags}{C.RESET}\n")
    if input(f"  {C.PURPLE}Simpan? (y/n): {C.RESET}").lower()=='y':
        fn=f"caption_{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(fn,'w',encoding='utf-8') as f:
            for cap in random.sample(caps,n): f.write(f"{cap}{extra}\n\n{tags}\n\n---\n\n")
        print(f"  {C.RED}✓ {fn}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 04 - CONTENT MANAGER
# ═══════════════════════════════════════════════════════
CF = os.path.expanduser('~/.sosmed_content.json')
def lc():
    if os.path.exists(CF):
        with open(CF,'r',encoding='utf-8') as f: return json.load(f)
    return []
def sc(d):
    with open(CF,'w',encoding='utf-8') as f: json.dump(d,f,ensure_ascii=False,indent=2)

def f04_content():
    hdr("CONTENT MANAGER","📜")
    print(f"  {C.RED}[1]{C.RESET} Tambah  {C.RED}[2]{C.RESET} Lihat  {C.RED}[3]{C.RESET} Posted  {C.RED}[4]{C.RESET} Hapus  {C.RED}[5]{C.RESET} Export TXT")
    ch = input(f"\n  {C.PURPLE}Pilih: {C.RESET}").strip()
    data = lc()

    if ch=='1':
        pls=["Instagram","TikTok","Twitter/X","YouTube","Facebook","Thread","Lainnya"]
        for i,p in enumerate(pls,1): print(f"  {C.RED}[{i}]{C.RESET} {p}")
        pi=input("  Platform: ").strip()
        pl=pls[int(pi)-1] if pi.isdigit() and 1<=int(pi)<=7 else "Lainnya"
        data.append({"id":len(data)+1,"platform":pl,
            "judul":input(f"  {C.PURPLE}Judul/Ide: {C.RESET}").strip(),
            "tanggal":input(f"  {C.PURPLE}Tanggal (YYYY-MM-DD): {C.RESET}").strip() or datetime.now().strftime('%Y-%m-%d'),
            "catatan":input(f"  {C.PURPLE}Catatan: {C.RESET}").strip(),
            "status":"belum","dibuat":datetime.now().strftime('%Y-%m-%d %H:%M')})
        sc(data); print(f"\n  {C.RED}✓ Tersimpan!{C.RESET}")
    elif ch=='2':
        if not data: print(f"\n  {C.GREY}Kosong.{C.RESET}"); return
        total=len(data); posted=sum(1 for x in data if x['status']=='posted')
        print(f"\n  {C.PURPLE}Total: {total}  |  {C.RED}Posted: {posted}  {C.GREY}|  Pending: {total-posted}{C.RESET}\n")
        for c in sorted(data, key=lambda x: x['tanggal']):
            ic="💀" if c['status']=='posted' else "🩸"
            col=C.GREY if c['status']=='posted' else C.RED
            print(f"  {col}[{c['id']:02}] {ic} {c['judul']}{C.RESET}")
            print(f"       {C.PURPLE}{c['platform']}{C.RESET} | 📅 {c['tanggal']}" + (f"\n       {C.GREY}{c['catatan']}{C.RESET}" if c.get('catatan') else ""))
            print()
    elif ch=='3':
        i=input(f"  {C.PURPLE}ID: {C.RESET}").strip()
        for c in data:
            if str(c['id'])==i:
                c['status']='posted'; c['posted_at']=datetime.now().strftime('%Y-%m-%d %H:%M')
                sc(data); print(f"  {C.RED}✓ Marked posted!{C.RESET}"); return
        print(f"  {C.RED}ID tidak ada.{C.RESET}")
    elif ch=='4':
        i=input(f"  {C.PURPLE}ID: {C.RESET}").strip()
        new=[c for c in data if str(c['id'])!=i]
        if len(new)<len(data): sc(new); print(f"  {C.RED}✓ Dihapus.{C.RESET}")
        else: print(f"  {C.RED}ID tidak ada.{C.RESET}")
    elif ch=='5':
        if not data: print(f"\n  {C.GREY}Kosong.{C.RESET}"); return
        fn=f"content_schedule_{datetime.now().strftime('%Y%m%d')}.txt"
        with open(fn,'w',encoding='utf-8') as f:
            f.write("CONTENT SCHEDULE — by skhxdn666\n"+"═"*40+"\n\n")
            for c in sorted(data,key=lambda x:x['tanggal']):
                f.write(f"[{c['id']:02}] {c['judul']}\nPlatform: {c['platform']} | Tanggal: {c['tanggal']} | Status: {c['status']}\n")
                if c.get('catatan'): f.write(f"Catatan: {c['catatan']}\n")
                f.write("\n")
        print(f"  {C.RED}✓ Export: {fn}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 05 - BIO ANALYZER
# ═══════════════════════════════════════════════════════
def f05_bio():
    hdr("ANALISIS BIO & PROFILE","👁️")
    bio=input(f"  {C.PURPLE}Paste bio kamu:\n  > {C.RESET}").strip()
    if not bio: print(f"  {C.RED}Kosong!{C.RESET}"); return
    chars=len(bio); words=bio.split()
    has_emoji=any(ord(c)>127 for c in bio)
    has_link=any(x in bio.lower() for x in ['http','www','.com','linktr','.id'])
    has_cta=any(w in bio.lower() for w in ['dm','contact','hubungi','order','collab','klik','check','wa','whatsapp'])
    has_niche=any(w in bio.lower() for w in ['content','creator','official','traveler','foodie','photographer','artist','designer','writer','gamer','streamer'])
    has_number=bool(re.search(r'\d{8,}', bio))
    sep()
    print(f"  {C.RED}{C.BOLD}HASIL ANALISIS{C.RESET}\n")
    print(f"  {C.WHITE}Karakter:{C.RESET} {C.RED}{chars}{C.RESET}  |  {C.WHITE}Kata:{C.RESET} {C.RED}{len(words)}{C.RESET}")
    clr = C.RED if 30<=chars<=150 else C.PURPLE
    msg = "✓ Panjang ideal" if 30<=chars<=150 else ("⚠ Terlalu panjang (>150)" if chars>150 else "⚠ Terlalu pendek (<30)")
    print(f"  {clr}{msg}{C.RESET}\n")

    checks=[
        (has_emoji,"💀","Emoji","Tidak ada — tambah biar lebih ekspresif"),
        (has_link,"💀","Link/Linktree","Belum ada — tambah link store/portfolio"),
        (has_cta,"💀","Call-to-Action","Belum ada — tambah CTA (DM, Order, dst)"),
        (has_niche,"💀","Niche/Identity","Belum jelas — define siapa kamu"),
        (has_number,"💀","Kontak/WA","Belum ada — tambah no. WA atau kontak"),
    ]
    score=0
    for ok,ic,label,tip in checks:
        if ok: print(f"  {C.RED}{ic}{C.RESET} {label}"); score+=1
        else: print(f"  {C.GREY}✗  {label} — {tip}{C.RESET}")

    pct=int((score/5)*100)
    bar="█"*score+"░"*(5-score)
    grades=["💀 Perlu banyak perbaikan","🩸 Masih kurang","🔮 Lumayan","👁️  Bagus!","☠  Bio sempurna!"]
    print(f"\n  {C.RED}{bar} {pct}% — {grades[score-1] if score>0 else grades[0]}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 06 - HASHTAG TOOLKIT
# ═══════════════════════════════════════════════════════
def f06_hashtag():
    hdr("HASHTAG TOOLKIT","🕷️")
    topic=input(f"  {C.PURPLE}Topik (misal: photography, fashion, gym): {C.RESET}").strip().lower()
    if not topic: print(f"  {C.RED}Kosong!{C.RESET}"); return
    db={
        "photography":["#photography","#photographer","#photooftheday","#portrait","#streetphotography","#lightroom","#goldenhour","#visualsoflife","#shotoniphone","#canon","#nikon","#fujifilm","#photographylovers","#photoedit","#moody","#artofvisuals","#moodygrams","#exploreeverything","#vsco","#filmphotography"],
        "fashion":["#fashion","#style","#ootd","#outfitoftheday","#streetstyle","#fashionista","#lookbook","#styleinspiration","#fashionblogger","#trendy","#aesthetic","#outfitinspo","#model","#editorial","#fashionphotography","#vintage","#thrift","#styling","#menfashion","#womensfashion"],
        "gym":["#gym","#fitness","#workout","#bodybuilding","#fitnessmotivation","#gains","#lifting","#gymlife","#personaltrainer","#physique","#bulking","#cutting","#shredded","#musclebuilding","#trainhard","#nopainnogain","#sweat","#cardio","#fitfam","#gymrat"],
        "food":["#food","#foodphotography","#foodie","#instafood","#kuliner","#foodblogger","#foodstagram","#yummy","#homemade","#recipe","#cooking","#baking","#foodlover","#delicious","#healthyfood","#makan","#enak","#kulinerindonesia","#resep","#foodcontent"],
        "travel":["#travel","#traveling","#travelgram","#wanderlust","#explore","#adventure","#nature","#landscape","#backpacker","#holiday","#vacation","#instatravel","#travelphotography","#trip","#destinations","#outdoor","#hiking","#camping","#wisata","#exploremore"],
        "gaming":["#gaming","#gamer","#game","#streamer","#twitch","#esports","#mobilelegends","#freefire","#valorant","#minecraft","#ps5","#xbox","#pcgaming","#gamingcommunity","#competitive","#casual","#rpg","#fps","#mmo","#gamingnews"],
        "music":["#music","#musician","#producer","#hiphop","#rnb","#beats","#studio","#recording","#songwriter","#musicproducer","#newmusic","#indie","#rap","#lofi","#playlist","#soundcloud","#spotify","#musicvideo","#cover","#original"],
        "design":["#design","#graphicdesign","#ui","#ux","#branding","#logo","#typography","#illustration","#digitalart","#creative","#designer","#adobe","#figma","#photoshop","#visualdesign","#artdirection","#minimalism","#poster","#identity","#colorpalette"],
    }
    match=next((k for k in db if k in topic or topic in k),None)
    tags=db[match] if match else [f"#{topic}",f"#{topic}content",f"#{topic}creator",f"#{topic}life",f"#{topic}id","#contentcreator","#instagram","#reels","#viral","#fyp","#explore","#aesthetic","#creative","#instagood","#content","#creator","#indonesia","#trending","#like","#follow"]
    random.shuffle(tags)
    sep()
    print(f"  {C.RED}{C.BOLD}HASHTAG — #{topic}{C.RESET}\n")
    print(f"  {C.RED}🩸 Niche (7):{C.RESET}\n  {C.WHITE}{' '.join(tags[:7])}{C.RESET}\n")
    print(f"  {C.RED}🩸 Medium (7):{C.RESET}\n  {C.WHITE}{' '.join(tags[7:14])}{C.RESET}\n")
    print(f"  {C.RED}🩸 Full ({len(tags)}):{C.RESET}\n  {C.GREY}{' '.join(tags)}{C.RESET}")
    if input(f"\n  {C.PURPLE}Simpan? (y/n): {C.RESET}").lower()=='y':
        fn=f"hashtag_{topic}_{datetime.now().strftime('%Y%m%d')}.txt"
        with open(fn,'w') as f: f.write(f"#{topic}\n\nSet 1:\n{' '.join(tags[:7])}\n\nSet 2:\n{' '.join(tags[7:14])}\n\nFull:\n{' '.join(tags)}")
        print(f"  {C.RED}✓ {fn}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 07 - LINK SHORTENER
# ═══════════════════════════════════════════════════════
def f07_link():
    import urllib.request, urllib.parse
    hdr("LINK SHORTENER & HISTORY","🩻")
    url=input(f"  {C.PURPLE}URL: {C.RESET}").strip()
    if not url: print(f"  {C.RED}Kosong!{C.RESET}"); return
    if not url.startswith('http'): url='https://'+url
    try:
        print(f"  {C.GREY}Processing...{C.RESET}")
        api=f"http://tinyurl.com/api-create.php?url={urllib.parse.quote(url)}"
        req=urllib.request.Request(api,headers={'User-Agent':'Mozilla/5.0'})
        short=urllib.request.urlopen(req,timeout=10).read().decode()
        sep()
        print(f"  {C.RED}Original :{C.RESET} {C.GREY}{url[:60]}{'...' if len(url)>60 else ''}{C.RESET}")
        print(f"  {C.RED}Short    :{C.RESET} {C.WHITE}{C.BOLD}{short}{C.RESET}")
        hf=os.path.expanduser('~/.link_history.json')
        hist=json.load(open(hf)) if os.path.exists(hf) else []
        hist.append({"url":url,"short":short,"date":datetime.now().strftime('%Y-%m-%d %H:%M')})
        with open(hf,'w') as f: json.dump(hist,f,indent=2)
        print(f"\n  {C.GREY}Saved to history ({len(hist)} total){C.RESET}")
        if len(hist)>1 and input(f"  {C.PURPLE}Lihat history? (y/n): {C.RESET}").lower()=='y':
            print(f"\n  {C.RED}{C.BOLD}HISTORY (last 10):{C.RESET}")
            for i,h in enumerate(hist[-10:],1):
                print(f"\n  {C.RED}[{i:02}]{C.RESET} {C.WHITE}{h['short']}{C.RESET}")
                print(f"       {C.GREY}{h['url'][:55]}...{C.RESET}  {C.PURPLE}{h['date']}{C.RESET}")
    except Exception as e:
        print(f"  {C.RED}Error: {e}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 08 - FONT STYLE GENERATOR
# ═══════════════════════════════════════════════════════
def f08_font():
    hdr("FONT STYLE GENERATOR","🔠")
    print(f"  {C.GREY}Convert teks biasa ke font unicode keren buat bio/caption{C.RESET}\n")
    text=input(f"  {C.PURPLE}Teks: {C.RESET}").strip()
    if not text: print(f"  {C.RED}Kosong!{C.RESET}"); return

    styles={
        "Bold":str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789","𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"),
        "Italic":str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"),
        "Script":str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"),
        "Double":str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789","𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"),
        "Fraktur":str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"),
        "Small Caps":"SMALL",
        "Bubble":str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789","ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ⓪①②③④⑤⑥⑦⑧⑨"),
        "Strikethrough":"STRIKE",
        "Upside Down":str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","∀qƆpƎℲפHIſʞ˥WNOdQɹSʇnΛMX⅄Zɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"),
    }

    sep()
    print(f"  {C.RED}{C.BOLD}HASIL:{C.RESET}\n")
    for name, tbl in styles.items():
        if tbl == "SMALL":
            sc_map=str.maketrans("abcdefghijklmnopqrstuvwxyz","ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘqʀsᴛᴜᴠᴡxʏᴢ")
            converted=text.translate(sc_map)
        elif tbl == "STRIKE":
            converted=''.join(c+'\u0336' for c in text)
        else:
            converted=text.translate(tbl)
        print(f"  {C.RED}{name:<14}{C.RESET} {C.WHITE}{converted}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 09 - ENGAGEMENT RATE CALCULATOR
# ═══════════════════════════════════════════════════════
def f09_engagement():
    hdr("ENGAGEMENT RATE CALCULATOR","📊")
    print(f"  {C.GREY}Hitung ER post atau akun kamu{C.RESET}\n")
    print(f"  {C.RED}[1]{C.RESET} Per post  {C.RED}[2]{C.RESET} Per akun (rata-rata)")
    ch=input(f"\n  {C.PURPLE}Pilih: {C.RESET}").strip()
    try:
        followers=int(input(f"  {C.PURPLE}Jumlah followers: {C.RESET}").replace('.','').replace(',',''))
        if ch=='1':
            likes=int(input(f"  {C.PURPLE}Likes: {C.RESET}").replace('.','').replace(',',''))
            comments=int(input(f"  {C.PURPLE}Comments: {C.RESET}").replace('.','').replace(',',''))
            saves=int(input(f"  {C.PURPLE}Saves (opsional, 0 jika tidak ada): {C.RESET}") or 0)
            total=likes+comments+saves
            er=(total/followers)*100
        else:
            n=int(input(f"  {C.PURPLE}Berapa post yang dihitung? ") or 5)
            totals=[]
            for i in range(1,n+1):
                l=int(input(f"  Post {i} - Likes: ").replace('.','').replace(',',''))
                c=int(input(f"  Post {i} - Comments: ").replace('.','').replace(',',''))
                totals.append(l+c)
            total=sum(totals)//n
            er=(total/followers)*100
        sep()
        if er>=10: grade=f"{C.RED}🔥 Viral / Sangat Tinggi"
        elif er>=5: grade=f"{C.RED}💀 Tinggi"
        elif er>=3: grade=f"{C.PURPLE}🩸 Rata-rata"
        elif er>=1: grade=f"{C.GREY}🕷️  Rendah"
        else: grade=f"{C.GREY}💤 Sangat Rendah"
        print(f"  {C.RED}{C.BOLD}Engagement Rate: {er:.2f}%{C.RESET}")
        print(f"  {grade}{C.RESET}\n")
        print(f"  {C.GREY}Benchmark IG: <1% rendah | 1-3% rata² | 3-6% bagus | >6% excellent{C.RESET}")
    except ValueError: print(f"  {C.RED}Input tidak valid!{C.RESET}")

# ═══════════════════════════════════════════════════════
# 10 - BEST TIME TO POST
# ═══════════════════════════════════════════════════════
def f10_besttime():
    hdr("BEST TIME TO POST","⏰")
    platforms=["Instagram","TikTok","Twitter/X","YouTube","Facebook","LinkedIn"]
    for i,p in enumerate(platforms,1): print(f"  {C.RED}[{i}]{C.RESET} {p}")
    ch=input(f"\n  {C.PURPLE}Platform [1-6]: {C.RESET}").strip()
    niches2=["General/Lifestyle","Bisnis/Brand","Gaming","Food","Fashion","Edukasi"]
    for i,n in enumerate(niches2,1): print(f"  {C.RED}[{i}]{C.RESET} {n}")
    nch=input(f"\n  {C.PURPLE}Niche [1-6]: {C.RESET}").strip()

    data={
        "1":{ # IG
            "1":[("Senin","06:00","08:00","12:00"),("Rabu","11:00","13:00"),("Jumat","10:00","13:00","19:00"),("Minggu","09:00","11:00")],
            "2":[("Selasa","08:00","12:00"),("Rabu","09:00","12:00"),("Kamis","08:00","10:00")],
            "3":[("Jumat","18:00","20:00","22:00"),("Sabtu","14:00","18:00","21:00"),("Minggu","12:00","16:00","20:00")],
            "4":[("Jumat","11:00","13:00","18:00"),("Sabtu","10:00","12:00"),("Minggu","11:00","13:00")],
            "5":[("Senin","07:00","08:00"),("Kamis","12:00","15:00"),("Jumat","08:00","11:00")],
            "6":[("Selasa","07:00","09:00","12:00"),("Rabu","08:00","10:00"),("Kamis","07:00","12:00")],
        },
        "2":{ # TikTok
            "1":[("Selasa","09:00","12:00"),("Jumat","05:00","13:00","15:00"),("Minggu","07:00","08:00","16:00")],
            "2":[("Senin","06:00","10:00"),("Rabu","08:00","11:00"),("Jumat","09:00","12:00")],
            "3":[("Senin","12:00","16:00","21:00"),("Jumat","14:00","18:00","21:00"),("Sabtu","11:00","14:00","21:00")],
            "4":[("Rabu","11:00","14:00"),("Jumat","12:00","15:00"),("Sabtu","11:00","14:00")],
            "5":[("Selasa","10:00","14:00"),("Kamis","09:00","12:00"),("Sabtu","11:00","14:00")],
            "6":[("Senin","07:00","10:00"),("Selasa","08:00","11:00"),("Jumat","07:00","09:00")],
        },
    }
    p_idx=ch if ch in data else "1"
    n_idx=nch if nch in ["1","2","3","4","5","6"] else "1"
    p_name=platforms[int(ch)-1] if ch.isdigit() and 1<=int(ch)<=6 else "Instagram"
    n_name=niches2[int(nch)-1] if nch.isdigit() and 1<=int(nch)<=6 else "General"
    sep()
    print(f"  {C.RED}{C.BOLD}Best Time — {p_name} × {n_name}{C.RESET}\n")
    schedule=data.get(p_idx,data["1"]).get(n_idx,data["1"]["1"])
    for day,*times in schedule:
        print(f"  {C.PURPLE}{day:<10}{C.RESET} {C.RED}{'  '.join(times)}{C.RESET}")
    print(f"\n  {C.GREY}*Berdasarkan riset engagement rata-rata WIB/WITA{C.RESET}")
    print(f"  {C.GREY}*Konsistensi lebih penting dari timing sempurna{C.RESET}")

# ═══════════════════════════════════════════════════════
# 11 - CONTENT IDEA GENERATOR
# ═══════════════════════════════════════════════════════
def f11_idea():
    hdr("CONTENT IDEA GENERATOR","💡")
    niches={
        "1":("Lifestyle",["Morning routine yang bikin produktif","5 hal yang berubah setelah aku konsisten","Day in my life (kerja dari rumah)","Apartment/room tour aesthetic","Apa yang aku beli bulan ini (worth it?)","Self care Sunday routine","Barang yang aku regret beli vs yang worth it","Realistic budget living di kota besar","Slow morning vs rushed morning","6 bulan challenge update"]),
        "2":("Gaming",["Top 5 hero/character underrated","Dari noob ke rank tertinggi — journey","Settings yang aku pake (PC/HP)","Review game yang lagi trending","Moment rage quit compilation","1v5 clutch highlights","Tutorial mechanic lanjut","Tier list update patch terbaru","Gaming setup tour","Respons drama komunitas gaming"]),
        "3":("Food",["Masak makanan dari negara X dengan bahan lokal","Budget meal prep seminggu < 100rb","Restaurant hidden gem di kotamu","Recipe viral yang aku coba","Blind taste test mahal vs murah","3 cara masak ayam yang beda","Street food tour","Mukbang + review jujur","Gagal masak & pelajaran nya","Makanan nostalgia masa kecil"]),
        "4":("Edukasi",["Hal yang sekolah gak pernah ajarkan","5 buku yang ubah hidupku","Belajar X dalam 30 hari — hasilnya","Debunk mitos populer tentang X","Thread tentang topik yang lagi viral","Explain complex topic in 60 seconds","Rekomendasi resource belajar gratis","Journey belajar skill baru dari 0","Q&A — tanya aku soal X","Review kelas/course online"]),
        "5":("Bisnis",["Behind the scene UMKM-ku","Berapa penghasilan content creator pemula","Kesalahan bisnis yang aku pernah buat","Cara dapat client pertama","Modal 500rb bisa usaha apa?","Day in my life sebagai solopreneur","Review tools yang aku pake","Cerita gagal yang jadi pelajaran","Cara nego harga ke supplier","Strategi konten yang works di 2025"]),
        "6":("Fitness",["Workout 20 menit tanpa alat","Transformasi 90 hari — honest review","Diet yang aku coba + hasilnya","Common gym mistake pemula","Home workout vs gym — pros cons","Meal prep tinggi protein budget murah","Form check — latihan yang sering salah","Recovery routine setelah workout keras","Suplemen yang aku rekomendasikan","Progress update bulanan"]),
    }
    for k,(n,_) in niches.items(): print(f"  {C.RED}[{k}]{C.RESET} {n}")
    ch=input(f"\n  {C.PURPLE}Pilih [1-6]: {C.RESET}").strip()
    if ch not in niches: print(f"  {C.RED}Tidak valid!{C.RESET}"); return
    name,ideas=niches[ch]
    try: n=min(int(input(f"  {C.PURPLE}Generate berapa ide? (max 10): {C.RESET}") or 5),10)
    except: n=5
    sep()
    print(f"  {C.RED}{C.BOLD}CONTENT IDEAS — {name}{C.RESET}\n")
    for i,idea in enumerate(random.sample(ideas,min(n,len(ideas))),1):
        print(f"  {C.RED}[{i:02}]{C.RESET} {C.WHITE}{idea}{C.RESET}")
    if input(f"\n  {C.PURPLE}Simpan? (y/n): {C.RESET}").lower()=='y':
        fn=f"ideas_{name}_{datetime.now().strftime('%Y%m%d')}.txt"
        with open(fn,'w',encoding='utf-8') as f:
            f.write(f"CONTENT IDEAS — {name}\nby skhxdn666\n\n")
            for i,idea in enumerate(random.sample(ideas,min(n,len(ideas))),1):
                f.write(f"{i:02}. {idea}\n")
        print(f"  {C.RED}✓ {fn}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 12 - THREAD FORMATTER
# ═══════════════════════════════════════════════════════
def f12_thread():
    hdr("THREAD FORMATTER (Twitter/X)","🧵")
    print(f"  {C.GREY}Format tulisan panjang jadi thread siap posting{C.RESET}\n")
    print(f"  {C.GREY}Paste teks kamu (ketik END di baris baru kalau sudah):{C.RESET}\n")
    lines=[]
    while True:
        l=input("  ")
        if l.strip().upper()=="END": break
        lines.append(l)
    text=" ".join(lines)
    if not text.strip(): print(f"  {C.RED}Kosong!{C.RESET}"); return

    limit=int(input(f"  {C.PURPLE}Batas karakter per tweet (default 280): {C.RESET}") or 280)
    add_num=input(f"  {C.PURPLE}Tambah nomor thread? (y/n): {C.RESET}").lower()=='y'
    add_hook=input(f"  {C.PURPLE}Tambah hook di tweet pertama? (y/n): {C.RESET}").lower()=='y'
    topic=input(f"  {C.PURPLE}Topik thread (untuk hook): {C.RESET}").strip() if add_hook else ""

    words=text.split()
    tweets,current=[],""
    for w in words:
        if len(current)+len(w)+1>limit:
            tweets.append(current.strip())
            current=w+" "
        else:
            current+=w+" "
    if current.strip(): tweets.append(current.strip())

    hooks=[f"🧵 Thread tentang {topic} — bacalah sampai habis:",f"💀 Hal yang harus kamu tahu tentang {topic} (thread):",f"🩸 Ini yang orang jarang tahu soal {topic}:",f"👁️  {topic} — sebuah thread yang akan mengubah perspektifmu:"]
    sep()
    print(f"  {C.RED}{C.BOLD}HASIL THREAD ({len(tweets)} tweets):{C.RESET}\n")
    start=1
    if add_hook and topic:
        hook=random.choice(hooks)
        print(f"  {C.RED}[0/HOOK]{C.RESET}\n  {C.WHITE}{hook}{C.RESET}\n")
    for i,tw in enumerate(tweets,start):
        num=f"{i}/{len(tweets)} " if add_num else ""
        print(f"  {C.RED}[{i}]{C.RESET} {C.GREY}({len(tw)+len(num)} chars){C.RESET}\n  {C.WHITE}{num}{tw}{C.RESET}\n")
    if input(f"  {C.PURPLE}Simpan? (y/n): {C.RESET}").lower()=='y':
        fn=f"thread_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(fn,'w',encoding='utf-8') as f:
            if add_hook and topic: f.write(f"[HOOK]\n{hook}\n\n")
            for i,tw in enumerate(tweets,1): f.write(f"[{i}/{len(tweets)}]\n{tw}\n\n")
        print(f"  {C.RED}✓ {fn}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 13 - FAKE ACCOUNT ANALYZER
# ═══════════════════════════════════════════════════════
def f13_fake():
    hdr("FAKE ACCOUNT ANALYZER","🤖")
    print(f"  {C.GREY}Analisis kemungkinan akun fake berdasarkan rasio & data{C.RESET}\n")
    try:
        followers=int(input(f"  {C.PURPLE}Followers: {C.RESET}").replace('.','').replace(',',''))
        following=int(input(f"  {C.PURPLE}Following: {C.RESET}").replace('.','').replace(',',''))
        posts=int(input(f"  {C.PURPLE}Jumlah post: {C.RESET}"))
        avg_likes=int(input(f"  {C.PURPLE}Rata-rata likes per post: {C.RESET}").replace('.','').replace(',',''))
        avg_comments=int(input(f"  {C.PURPLE}Rata-rata comments per post: {C.RESET}").replace('.','').replace(',',''))
        has_pp=input(f"  {C.PURPLE}Ada foto profil? (y/n): {C.RESET}").lower()=='y'
        has_bio=input(f"  {C.PURPLE}Bio terisi? (y/n): {C.RESET}").lower()=='y'
        old_account=input(f"  {C.PURPLE}Akun sudah > 1 tahun? (y/n): {C.RESET}").lower()=='y'

        score=0; flags=[]
        # Rasio follower/following
        ratio=followers/following if following>0 else followers
        if ratio<0.1: score+=25; flags.append("Rasio following >> followers (sangat mencurigakan)")
        elif ratio<0.5: score+=10; flags.append("Rasio following lebih banyak dari followers")
        # ER
        if followers>0:
            er=((avg_likes+avg_comments)/followers)*100
            if er<0.5 and followers>10000: score+=20; flags.append(f"Engagement rate sangat rendah ({er:.2f}%)")
            elif er<1 and followers>5000: score+=10; flags.append(f"Engagement rate rendah ({er:.2f}%)")
        # Post count
        if posts<5: score+=15; flags.append("Jumlah post sangat sedikit")
        elif posts<10: score+=5; flags.append("Jumlah post minim")
        if not has_pp: score+=20; flags.append("Tidak ada foto profil")
        if not has_bio: score+=10; flags.append("Bio kosong")
        if not old_account: score+=10; flags.append("Akun masih baru")
        if following>5000 and followers<500: score+=15; flags.append("Mass following tanpa difolback")

        score=min(score,100)
        sep()
        bar="█"*int(score/10)+"░"*(10-int(score/10))
        if score>=70: grade=f"{C.RED}💀 KEMUNGKINAN BESAR FAKE/BOT"; 
        elif score>=40: grade=f"{C.PURPLE}🩸 MENCURIGAKAN"
        elif score>=20: grade=f"{C.GREY}🕷️  AGAK MENCURIGAKAN"
        else: grade=f"{C.WHITE}✓ KEMUNGKINAN ASLI"
        print(f"  {C.RED}{C.BOLD}FAKE SCORE: {score}/100{C.RESET}")
        print(f"  {C.RED}{bar}{C.RESET}")
        print(f"  {grade}{C.RESET}\n")
        if flags:
            print(f"  {C.PURPLE}Red flags:{C.RESET}")
            for f_ in flags: print(f"  {C.RED}⚠{C.RESET} {C.GREY}{f_}{C.RESET}")
    except ValueError: print(f"  {C.RED}Input tidak valid!{C.RESET}")

# ═══════════════════════════════════════════════════════
# 14 - BRAND COLOR PALETTE
# ═══════════════════════════════════════════════════════
def f14_color():
    hdr("BRAND COLOR PALETTE GENERATOR","🎨")
    print(f"  {C.GREY}Generate palet warna konsisten buat branding kamu{C.RESET}\n")
    moods={
        "1":("Dark/Mysterious",["#1a0a0a","#2d0d0d","#4a1515","#8b0000","#c41230","#ff3355","#ff6680","#ffcccc"],"Cocok: dark brand, gaming, musik underground, fashion edgy"),
        "2":("Royal Purple",["#0d0019","#1a0033","#2d0066","#4d00b3","#7700ff","#9933ff","#cc99ff","#f0e6ff"],"Cocok: luxury brand, esports, beauty, tech premium"),
        "3":("Minimal Clean",["#0a0a0a","#1c1c1c","#2e2e2e","#5c5c5c","#8c8c8c","#b0b0b0","#d4d4d4","#f5f5f5"],"Cocok: portfolio, arsitektur, lifestyle, fashion minimal"),
        "4":("Warm Earth",["#1a0f00","#3d2200","#6b3e00","#9c5c00","#c97f00","#e8a23c","#f5c878","#ffedc4"],"Cocok: food, coffee, travel, lifestyle hangat"),
        "5":("Ocean Dark",["#000d1a","#001f3f","#003366","#005599","#0077cc","#3399ff","#66b8ff","#cce8ff"],"Cocok: tech, finance, health, corporate modern"),
        "6":("Neon Cyber",["#000000","#0d0d1a","#001100","#003300","#00ff00","#33ff33","#99ff99","#e6ffe6"],"Cocok: cyberpunk, gaming, tech, coding community"),
    }
    for k,(n,_,_) in moods.items(): print(f"  {C.RED}[{k}]{C.RESET} {n}")
    ch=input(f"\n  {C.PURPLE}Pilih [1-6]: {C.RESET}").strip()
    if ch not in moods: print(f"  {C.RED}Tidak valid!{C.RESET}"); return
    name,colors,desc=moods[ch]
    sep()
    print(f"  {C.RED}{C.BOLD}PALETTE — {name}{C.RESET}\n")
    labels=["Background","Surface","Card","Border","Secondary","Primary","Light","Highlight"]
    for i,(hex_,label) in enumerate(zip(colors,labels)):
        print(f"  {C.RED}{label:<12}{C.RESET} {C.WHITE}{hex_}{C.RESET}")
    print(f"\n  {C.GREY}{desc}{C.RESET}")
    print(f"\n  {C.PURPLE}Usage tips:{C.RESET}")
    print(f"  {C.GREY}→ Background  : warna gelap, untuk bg utama")
    print(f"  → Primary     : warna dominan brand kamu")
    print(f"  → Highlight   : aksen untuk CTA, tombol, highlight{C.RESET}")

# ═══════════════════════════════════════════════════════
# 15 - BIO TEMPLATE GENERATOR
# ═══════════════════════════════════════════════════════
def f15_biotemplate():
    hdr("BIO TEMPLATE GENERATOR","📝")
    print(f"  {C.GREY}Generate bio siap pakai sesuai niche{C.RESET}\n")
    name=input(f"  {C.PURPLE}Nama/username kamu: {C.RESET}").strip()
    niche=input(f"  {C.PURPLE}Niche kamu (misal: content creator, photographer, dll): {C.RESET}").strip()
    location=input(f"  {C.PURPLE}Kota (opsional): {C.RESET}").strip()
    cta=input(f"  {C.PURPLE}CTA (misal: DM for collab, link di bawah): {C.RESET}").strip()
    link=input(f"  {C.PURPLE}Link (opsional): {C.RESET}").strip()

    loc_str=f" 📍 {location}" if location else ""
    link_str=f"\n  🔗 {link}" if link else ""
    cta_str=f"\n  👉 {cta}" if cta else ""

    templates=[
        f"  ✦ {niche.title()}{loc_str}\n  Sharing {niche} content daily 💀\n  Life is too short for bad vibes{cta_str}{link_str}",
        f"  {name.upper()} 🩸\n  {niche.title()}{loc_str}\n  I don't follow trends — I set them{cta_str}{link_str}",
        f"  {niche.title()} | {location if location else 'Everywhere'}\n  Creating content that hits different 🔮\n  Not your average creator{cta_str}{link_str}",
        f"  👁️  {niche.title()}\n  Building in silence, posting for impact{loc_str}\n  📩 {cta if cta else 'Open for collab'}{link_str}",
        f"  {name} ☠\n  {niche.title()} based in {location if location else 'the void'}\n  Dark by nature, creative by choice{cta_str}{link_str}",
    ]
    sep()
    print(f"  {C.RED}{C.BOLD}BIO TEMPLATES:{C.RESET}\n")
    for i,t in enumerate(templates,1):
        print(f"  {C.RED}── Template {i} ──{C.RESET}")
        print(f"{C.WHITE}{t}{C.RESET}\n")

# ═══════════════════════════════════════════════════════
# 16 - VIRAL HOOK GENERATOR
# ═══════════════════════════════════════════════════════
def f16_hook():
    hdr("VIRAL HOOK GENERATOR","🪝")
    print(f"  {C.GREY}Generate opening hook yang bikin orang stop scroll{C.RESET}\n")
    topic=input(f"  {C.PURPLE}Topik konten: {C.RESET}").strip()
    style_opts=["Curiosity (bikin penasaran)","Controversy (bikin mikir)","Value (langsung kasih value)","Story (storytelling)","Dark/Edgy"]
    for i,s in enumerate(style_opts,1): print(f"  {C.RED}[{i}]{C.RESET} {s}")
    ch=input(f"\n  {C.PURPLE}Style [1-5]: {C.RESET}").strip() or '1'

    hooks_db={
        "1":[f"Hal tentang {topic} yang ga pernah diajarkan siapapun ke kamu 👇",f"Aku habiskan 3 tahun belajar {topic}. Ini yang aku temukan:",f"Kenapa 90% orang yang belajar {topic} gagal? (dan bagaimana kamu bisa beda)",f"Yang ga ada yang ceritain soal {topic}: sebuah thread 🧵",f"Buka kalau kamu mau tau sisi gelap {topic} 👁️"],
        "2":[f"Pendapat kontroversial: {topic} itu sebenarnya overhyped. Ini alasannya:",f"Aku capek pura-pura {topic} itu mudah. Ini kenyataannya:",f"Orang yang bilang {topic} itu gampang bohong ke kamu 🩸",f"Unpopular opinion tentang {topic} yang akan banyak yang marah dengarnya:",f"Industri {topic} menyembunyikan ini dari kamu:"],
        "3":[f"5 cara {topic} yang bisa kamu coba hari ini (gratis):",f"Copy-paste template {topic} ini — sudah terbukti works:",f"Cara aku dapet hasil dari {topic} dalam 30 hari:",f"Tutorial lengkap {topic} untuk pemula — simpan ini 📌",f"Dari 0 ke {topic} dalam 90 hari — step by step:"],
        "4":[f"Dua tahun lalu aku hampir menyerah dari {topic}. Ini ceritanya:",f"Ini momen yang mengubah caraku memandang {topic} selamanya:",f"Kalau aku bisa kembali ke awal {topic}, aku akan lakukan ini berbeda:",f"Orang itu ketawa waktu aku bilang mau serius di {topic}. Sekarang?",f"Perjalanan {topic}-ku: dari broke ke konsisten dalam 180 hari 💀"],
        "5":[f"Warning: konten {topic} ini mungkin terlalu jujur untuk sebagian orang ☠",f"Semua orang memperindah {topic}. Aku tidak akan. Siap? 🩸",f"Dark truth tentang {topic} yang industry ga mau kamu tahu:",f"{topic.upper()} IS A LIE. Thread 🔮",f"Aku benci bilang ini, tapi {topic} itu jauh lebih gelap dari yang kamu kira:"],
    }
    hooks=hooks_db.get(ch, hooks_db["1"])
    sep()
    print(f"  {C.RED}{C.BOLD}VIRAL HOOKS — {topic}{C.RESET}\n")
    for i,h in enumerate(hooks,1):
        print(f"  {C.RED}[{i}]{C.RESET} {C.WHITE}{h}{C.RESET}\n")

# ═══════════════════════════════════════════════════════
# 17 - EMOJI SEARCH
# ═══════════════════════════════════════════════════════
def f17_emoji():
    hdr("EMOJI SEARCH & COPY","😈")
    db={
        "love":["❤️","🖤","💜","💀","🩸","💔","♥️","🫀","🩷","💗"],
        "fire":["🔥","💥","⚡","✨","💫","🌟","⭐","🌠","☄️","🌋"],
        "dark":["💀","☠️","🩸","👁️","🕷️","🌑","🌚","⬛","🖤","😈"],
        "cool":["😎","🤙","💯","🔥","👑","⚡","🫰","✌️","🤟","🤘"],
        "sad":["😭","💔","😢","🥺","😞","😔","🌧️","⛈️","🩹","💧"],
        "money":["💰","💵","💸","🤑","💎","👑","🏆","📈","💹","🪙"],
        "nature":["🌿","🍃","🌱","🌸","🌺","🍀","🌊","🏔️","🌅","🌿"],
        "food":["🍜","🍕","🍔","🍣","🧋","🍰","🍩","🥗","🌮","🍛"],
        "sport":["💪","🏋️","⚽","🏀","🎯","🥊","🤸","🧘","🏃","🚴"],
        "tech":["💻","📱","⌨️","🖥️","🔌","💾","📡","🤖","🧬","🔬"],
        "aesthetic":["🌙","⭐","🌸","🕯️","🫧","🪞","🦋","🌊","🎭","🖼️"],
        "skull":["💀","☠️","🪦","👻","🫀","🩻","🦴","⚰️","🕸️","🫥"],
    }
    print(f"  {C.GREY}Kategori: {', '.join(db.keys())}{C.RESET}\n")
    q=input(f"  {C.PURPLE}Cari (kategori/keyword): {C.RESET}").strip().lower()
    found=None
    for k,v in db.items():
        if q in k or k in q: found=(k,v); break
    if not found:
        # cari di semua emoji via name
        results=[]
        for k,v in db.items():
            if any(q in k for _ in v): results.extend(v)
        if not results: print(f"  {C.RED}Tidak ditemukan. Coba: {', '.join(db.keys())}{C.RESET}"); return
        found=("hasil pencarian",results)
    cat,emojis=found
    sep()
    print(f"  {C.RED}{C.BOLD}EMOJI — {cat}{C.RESET}\n")
    print(f"  {' '.join(emojis)}\n")
    print(f"  {C.GREY}Copy emoji yang kamu mau dari atas ↑{C.RESET}")
    # Kombinasi
    combos=[random.sample(emojis,min(3,len(emojis))) for _ in range(4)]
    print(f"\n  {C.PURPLE}Kombinasi saran:{C.RESET}")
    for combo in combos:
        print(f"  {C.WHITE}{'  '.join(combo)}{C.RESET}")

# ═══════════════════════════════════════════════════════
# 18 - PASSWORD GENERATOR
# ═══════════════════════════════════════════════════════
def f18_password():
    hdr("PASSWORD GENERATOR (Akun Sosmed)","🔑")
    print(f"  {C.GREY}Generate password kuat buat akun sosmed kamu{C.RESET}\n")
    try:
        length=int(input(f"  {C.PURPLE}Panjang (default 16): {C.RESET}") or 16)
        use_sym=input(f"  {C.PURPLE}Simbol? (y/n, default y): {C.RESET}").lower() or 'y'
        count=int(input(f"  {C.PURPLE}Berapa password? (default 5): {C.RESET}") or 5)
    except: length,use_sym,count=16,'y',5
    chars=string.ascii_letters+string.digits
    if use_sym=='y': chars+="!@#$%^&*()_+-=[]{}|;:,.<>?"
    sep()
    print(f"  {C.RED}{C.BOLD}GENERATED PASSWORDS:{C.RESET}\n")
    for i in range(count):
        pw=''.join(random.choices(chars,k=length))
        strength="WEAK" if length<8 else "MEDIUM" if length<14 else "STRONG"
        sc=C.RED if length>=14 else C.PURPLE if length>=8 else C.GREY
        print(f"  {C.RED}[{i+1}]{C.RESET} {C.WHITE}{pw}{C.RESET}  {sc}[{strength}]{C.RESET}")
    print(f"\n  {C.GREY}Tips: Jangan pakai password yang sama di semua akun!")
    print(f"  Pertimbangkan pakai password manager (Bitwarden, dll){C.RESET}")

# ═══════════════════════════════════════════════════════
# 19 - TEXT TONE CONVERTER
# ═══════════════════════════════════════════════════════
def f19_tone():
    hdr("TEXT TONE CONVERTER","💬")
    print(f"  {C.GREY}Convert tone teks kamu buat berbagai situasi{C.RESET}\n")
    text=input(f"  {C.PURPLE}Teks asli kamu:\n  > {C.RESET}").strip()
    if not text: print(f"  {C.RED}Kosong!{C.RESET}"); return
    sep()
    print(f"  {C.RED}{C.BOLD}HASIL KONVERSI:{C.RESET}\n")

    # Casual
    casual=text.replace("saya","gue").replace("anda","lo").replace("tidak","ga").replace("akan","mau").replace("sangat","banget").replace("dengan","sama").replace("untuk","buat").replace("sudah","udah").replace("belum","blm").replace("bagaimana","gimana").replace("mengapa","kenapa").replace("karena","soalnya")
    # Formal
    formal=text.replace("gue","saya").replace("gw","saya").replace("lo","Anda").replace("lu","Anda").replace("ga","tidak").replace("gak","tidak").replace("nggak","tidak").replace("udah","sudah").replace("lagi","sedang").replace("mau","akan").replace("banget","sangat").replace("buat","untuk")
    # Hype/Energetic
    words=text.split()
    hype=" ".join(w.upper() if random.random()>0.7 else w for w in words)
    hype=hype+"!!! 🔥💀⚡"
    # Dark/Edgy
    dark=text+" 🖤\nNot for the weak."
    # Minimalist
    mini=". ".join(s.strip()[:50] for s in text.split(".") if s.strip())

    tones=[("Casual/Gaul",casual),("Formal",formal),("Hype/Energetic",hype),("Dark/Edgy",dark),("Minimalist",mini)]
    for name,result in tones:
        print(f"  {C.RED}── {name} ──{C.RESET}")
        print(f"  {C.WHITE}{result}{C.RESET}\n")

# ═══════════════════════════════════════════════════════
# 20 - FOLLOWER GROWTH TRACKER
# ═══════════════════════════════════════════════════════
GF=os.path.expanduser('~/.growth_tracker.json')
def f20_growth():
    hdr("FOLLOWER GROWTH TRACKER","📈")
    data=json.load(open(GF)) if os.path.exists(GF) else {}
    print(f"  {C.RED}[1]{C.RESET} Catat data hari ini")
    print(f"  {C.RED}[2]{C.RESET} Lihat progress & statistik")
    print(f"  {C.RED}[3]{C.RESET} Reset data akun")
    ch=input(f"\n  {C.PURPLE}Pilih: {C.RESET}").strip()

    if ch=='1':
        acct=input(f"  {C.PURPLE}Nama akun/platform (misal: ig_skhxdn666): {C.RESET}").strip()
        if not acct: return
        try:
            fl=int(input(f"  {C.PURPLE}Followers sekarang: {C.RESET}").replace('.','').replace(',',''))
            fol=int(input(f"  {C.PURPLE}Following sekarang: {C.RESET}").replace('.','').replace(',',''))
            posts=int(input(f"  {C.PURPLE}Total post: {C.RESET}"))
        except: print(f"  {C.RED}Input tidak valid!{C.RESET}"); return
        if acct not in data: data[acct]=[]
        data[acct].append({"date":datetime.now().strftime('%Y-%m-%d'),"followers":fl,"following":fol,"posts":posts})
        with open(GF,'w') as f: json.dump(data,f,indent=2)
        # Hitung pertumbuhan
        if len(data[acct])>1:
            prev=data[acct][-2]["followers"]
            diff=fl-prev
            pct=(diff/prev*100) if prev>0 else 0
            arrow="📈" if diff>0 else "📉" if diff<0 else "➡️"
            print(f"\n  {arrow} {C.RED}+{diff}{C.RESET} followers dari entri sebelumnya ({C.WHITE}{pct:+.1f}%{C.RESET})")
        else:
            print(f"\n  {C.RED}✓ Data pertama tersimpan! Catat lagi besok untuk lihat progress.{C.RESET}")

    elif ch=='2':
        if not data: print(f"\n  {C.GREY}Belum ada data.{C.RESET}"); return
        acct=input(f"  {C.PURPLE}Nama akun: {C.RESET}").strip()
        if acct not in data: print(f"  {C.RED}Akun tidak ditemukan.{C.RESET}"); return
        entries=data[acct]
        sep()
        print(f"  {C.RED}{C.BOLD}GROWTH REPORT — {acct}{C.RESET}\n")
        for e in entries:
            print(f"  {C.PURPLE}{e['date']}{C.RESET}  {C.RED}{e['followers']:,}{C.RESET} followers  {C.GREY}{e['posts']} posts{C.RESET}")
        if len(entries)>1:
            first,last=entries[0],entries[-1]
            total_growth=last['followers']-first['followers']
            days=(datetime.strptime(last['date'],'%Y-%m-%d')-datetime.strptime(first['date'],'%Y-%m-%d')).days or 1
            daily=total_growth/days
            print(f"\n  {C.WHITE}Total growth  :{C.RESET} {C.RED}{total_growth:+,}{C.RESET}")
            print(f"  {C.WHITE}Periode       :{C.RESET} {days} hari")
            print(f"  {C.WHITE}Rata²/hari    :{C.RESET} {C.RED}{daily:+.1f}{C.RESET}")
            if daily>0:
                to_10k=max(0,(10000-last['followers'])/daily)
                to_100k=max(0,(100000-last['followers'])/daily)
                if last['followers']<10000: print(f"  {C.GREY}Estimasi 10K: {to_10k:.0f} hari lagi{C.RESET}")
                if last['followers']<100000: print(f"  {C.GREY}Estimasi 100K: {to_100k:.0f} hari lagi{C.RESET}")

    elif ch=='3':
        acct=input(f"  {C.PURPLE}Nama akun yang mau direset: {C.RESET}").strip()
        if acct in data:
            del data[acct]
            with open(GF,'w') as f: json.dump(data,f,indent=2)
            print(f"  {C.RED}✓ Data {acct} dihapus.{C.RESET}")
        else: print(f"  {C.RED}Akun tidak ditemukan.{C.RESET}")

# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════
ACTIONS={
    '01':f01_downloader,'1':f01_downloader,
    '02':f02_username,'2':f02_username,
    '03':f03_caption,'3':f03_caption,
    '04':f04_content,'4':f04_content,
    '05':f05_bio,'5':f05_bio,
    '06':f06_hashtag,'6':f06_hashtag,
    '07':f07_link,'7':f07_link,
    '08':f08_font,'8':f08_font,
    '09':f09_engagement,'9':f09_engagement,
    '10':f10_besttime,
    '11':f11_idea,
    '12':f12_thread,
    '13':f13_fake,
    '14':f14_color,
    '15':f15_biotemplate,
    '16':f16_hook,
    '17':f17_emoji,
    '18':f18_password,
    '19':f19_tone,
    '20':f20_growth,
}

def main():
    banner()
    while True:
        menu()
        ch=input(f"  {C.RED}☠  Pilih {C.RESET}[{C.PURPLE}00-20{C.RESET}]: ").strip()
        if ch in ('0','00'):
            print(f"\n  {C.RED}💀 see you in the dark...{C.RESET}\n"); sys.exit(0)
        elif ch in ACTIONS:
            ACTIONS[ch]()
        else:
            print(f"\n  {C.RED}Pilihan tidak valid.{C.RESET}")
        pause()
        banner()

if __name__=='__main__':
    main()
