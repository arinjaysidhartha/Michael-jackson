from pathlib import Path
import re, html
p=Path('/mnt/data/mj-work')
index=(p/'index.html').read_text()
# Pull artwork URLs from the existing album overview cards so the established art is reused.
entries={}
for block in re.findall(r'<article class="album-entry">.*?</article>', index, re.S):
    num=re.search(r'<div class="album-number">([^<]+)</div>', block)
    title=re.search(r'<h2>(.*?)</h2>', block, re.S)
    img=re.search(r'<img src="([^"]+)" alt="([^"]+)"', block)
    if num and title and img:
        name=re.sub(r'\s+',' ',re.sub(r'<.*?>','',title.group(1))).strip()
        entries[name.lower()]={'year':num.group(1).split('/')[-1].strip(),'src':img.group(1),'alt':img.group(2)}

albums=[
 dict(title='Music & Me',slug='music-and-me',year='1973',label='MOTOWN',date='April 13, 1973',tracks=['With a Child\'s Heart','Up Again','All the Things You Are','Happy','Too Young','Doggin\' Around','Euphoria','Morning Glow','Johnny Raven','Music and Me'],desc='Michael Jackson’s third solo studio album, released by Motown in April 1973. Its gentle pop and soul arrangements capture his voice during his early teenage years.',
      perf='No performance video has been added to this page yet. The performance archive will only include a clip when the song, event, and footage can be matched reliably.'),
 dict(title='Forever, Michael',slug='forever-michael',year='1975',label='MOTOWN',date='January 16, 1975',tracks=["We're Almost There",'Take Me Back','One Day in Your Life','Cinderella Stay Awhile',"We've Got Forever",'Just a Little Bit of You','You Are There','Dapper Dan','Dear Michael',"I'll Come Home to You"],desc='Michael Jackson’s fourth solo studio album and his final Motown solo album before moving to Epic Records. The record leans into smooth soul, pop, and romantic ballads.',perf='No performance video has been added to this page yet. The performance archive will only include a clip when the song, event, and footage can be matched reliably.'),
 dict(title='Off the Wall',slug='off-the-wall',year='1979',label='EPIC',date='August 10, 1979',tracks=['Don’t Stop ’Til You Get Enough','Rock with You','Working Day and Night','Get on the Floor','Off the Wall','Girlfriend','She’s Out of My Life','I Can’t Help It','It’s the Falling in Love','Burn This Disco Out'],desc='Michael Jackson’s breakthrough adult solo album, produced by Quincy Jones. It blends disco, funk, pop, R&B, and soul into an energetic, polished dance record.',perf='No performance video has been added to this page yet. The performance archive will only include a clip when the song, event, and footage can be matched reliably.'),
 dict(title='Thriller',slug='thriller',year='1982',label='EPIC',date='November 30, 1982',tracks=["Wanna Be Startin’ Somethin’",'Baby Be Mine','The Girl Is Mine','Thriller','Beat It','Billie Jean','Human Nature','P.Y.T. (Pretty Young Thing)','The Lady in My Life'],desc='The landmark sixth solo studio album, produced by Quincy Jones. Its mix of pop, rock, funk, and R&B became one of the defining releases in popular music.',perf='No performance video has been added to this page yet. The performance archive will only include a clip when the song, event, and footage can be matched reliably.'),
 dict(title='Bad',slug='bad',year='1987',label='EPIC',date='August 31, 1987',tracks=['Bad','The Way You Make Me Feel','Speed Demon','Liberian Girl','Just Good Friends','Another Part of Me','Man in the Mirror','I Just Can’t Stop Loving You','Dirty Diana','Smooth Criminal','Leave Me Alone'],desc='Michael Jackson’s seventh solo studio album and his third collaboration with Quincy Jones. It moves through dance-pop, rock, R&B, and soul with a sharper, more assertive sound.',perf='No performance video has been added to this page yet. The performance archive will only include a clip when the song, event, and footage can be matched reliably.'),
 dict(title='Dangerous',slug='dangerous',year='1991',label='EPIC',date='November 26, 1991',tracks=['Jam','Why You Wanna Trip on Me','In the Closet','She Drives Me Wild','Remember the Time','Can’t Let Her Get Away','Heal the World','Black or White','Who Is It','Give In to Me','Will You Be There','Keep the Faith','Gone Too Soon','Dangerous'],desc='The eighth solo studio album, featuring a new jack swing direction shaped by producers including Teddy Riley. The record also moves through pop, rock, gospel, and R&B.',perf='No performance video has been added to this page yet. The performance archive will only include a clip when the song, event, and footage can be matched reliably.'),
 dict(title='HIStory: Past, Present and Future, Book I',slug='history',year='1995',label='EPIC • TWO-DISC ALBUM',date='June 20, 1995',tracks=['DISC ONE — HIStory Begins','Billie Jean','The Way You Make Me Feel','Black or White','Rock with You','She’s Out of My Life','Bad','I Just Can’t Stop Loving You','Man in the Mirror','Thriller','Beat It','The Girl Is Mine','Remember the Time','Don’t Stop ’Til You Get Enough','Wanna Be Startin’ Somethin’','Heal the World','DISC TWO — HIStory Continues','Scream','They Don’t Care About Us','Stranger in Moscow','This Time Around','Earth Song','D.S.','Money','Come Together','You Are Not Alone','Childhood','Tabloid Junkie','2 Bad','HIStory','Little Susie','Smile'],desc='A two-disc release pairing a collection of major solo hits with a second disc of new material. The new songs explore public scrutiny, injustice, isolation, and personal reflection.',perf='No performance video has been added to this page yet. The performance archive will only include a clip when the song, event, and footage can be matched reliably.'),
 dict(title='Invincible',slug='invincible',year='2001',label='EPIC',date='October 30, 2001',tracks=['Unbreakable','Heartbreaker','Invincible','Break of Dawn','Heaven Can Wait','You Rock My World','Butterflies','Speechless','2000 Watts','You Are My Life','Privacy','Don’t Walk Away','Cry','The Lost Children','Whatever Happens','Threatened'],desc='Michael Jackson’s tenth and final solo studio album released during his lifetime. It combines contemporary R&B, pop, soul, and electronic production.',perf='No performance video has been added to this page yet. The performance archive will only include a clip when the song, event, and footage can be matched reliably.'),
 dict(title='Blood on the Dance Floor: HIStory in the Mix',slug='blood-on-the-dance-floor',year='1997',label='REMIX ALBUM • EPIC',date='May 20, 1997',tracks=['Blood on the Dance Floor','Morphine','Superfly Sister','Ghosts','Is It Scary','Scream Louder (Flyte Tyme Remix)','Money (Fire Island Radio Edit)','2 Bad (Refugee Camp Mix)','Stranger in Moscow (Tee’s In-House Club Mix)','This Time Around (D.M. Radio Mix)','Earth Song (Hani’s Extended Radio Experience)','You Are Not Alone (Classic Club Mix)','HIStory (Tony Moran’s HIStory Lesson)'],desc='A remix album released during Michael Jackson’s lifetime, combining five new songs with remixes of tracks from HIStory. It belongs in the Remix Albums category, not the posthumous category.',perf='No performance video has been added to this page yet. The performance archive will only include a clip when the song, event, and footage can be matched reliably.'),
 dict(title='Michael',slug='michael',year='2010',label='POSTHUMOUS • EPIC',date='December 10, 2010',tracks=['Hold My Hand (with Akon)','Hollywood Tonight','(I Like) The Way You Love Me','Best of Joy','(I Can’t Make It) Another Day (featuring Lenny Kravitz)','Behind the Mask','Much Too Soon'],desc='Michael Jackson’s first posthumous studio album, assembled from previously unreleased recordings and completed productions. This page follows the original seven-track standard edition listed on the official album page.',perf='This is a posthumous studio collection. No live-performance section is claimed for these studio recordings; any documented earlier performance or archival footage will be identified separately if verified.'),
 dict(title='Xscape',slug='xscape',year='2014',label='POSTHUMOUS • EPIC',date='May 13, 2014',tracks=['Love Never Felt So Good','Chicago','Loving You','A Place with No Name','Slave to the Rhythm','Do You Know Where Your Children Are','Blue Gangsta','Xscape'],desc='Michael Jackson’s second posthumous studio album. The standard edition contains eight previously unreleased recordings, contemporized by a team of producers led by Timbaland.',perf='This is a posthumous studio collection. No live-performance section is claimed for these studio recordings; any documented earlier performance or archival footage will be identified separately if verified.'),
]

# Build all new detail pages in the exact visual system already used by Got to Be There and Ben.
for a in albums:
    key=a['title'].lower()
    src=entries.get(key,{}).get('src')
    if not src:
        # Existing overview image sources are used for all the catalogue cards.
        src=f'https://commons.wikimedia.org/wiki/Special:FilePath/{a["slug"]}.jpg'
    is_history=a['slug']=='history'
    track_html=[]
    for i,t in enumerate(a['tracks']):
        if t.startswith('DISC '):
            track_html.append(f'<li class="track-disc-heading">{html.escape(t)}</li>')
        else:
            track_html.append(f'<li>{html.escape(t)}</li>')
    count='30 TRACKS' if is_history else f'{len(a["tracks"])} TRACKS'
    page=f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(a['title'])} — album details and tracklist by Michael Jackson.">
  <title>{html.escape(a['title'])} | Michael Jackson King of Pop</title>
  <link rel="stylesheet" href="style.css"><link rel="stylesheet" href="albums.css"><link rel="stylesheet" href="real-music.css">
</head>
<body class="albums-page">
  <header class="topbar"><a class="brand" href="index.html">MJ <span>•</span> KING OF POP</a><nav class="topnav"><a href="index.html#legacy">THE LEGACY</a><a href="index.html#mj-radio">MJ RADIO</a><a href="index.html#albums">ALBUMS</a><a href="index.html#real-music">REAL MUSIC</a></nav></header>
  <main class="album-detail-main">
    <a class="back-home" href="index.html#real-music">← BACK TO REAL MUSIC</a>
    <p class="real-music-kicker">MICHAEL JACKSON • {a['year']} • {a['label']}</p>
    <h1 class="album-detail-title"><span>{html.escape(a['title'])}</span></h1>
    <div class="album-detail-hero">
      <img class="album-detail-cover" src="{html.escape(src)}" alt="{html.escape(a['title'])} album cover">
      <div class="album-detail-description">
        <p>{html.escape(a['desc'])}</p>
        <p class="album-meta">{count} <span>•</span> {a['year']} <span>•</span> {a['label']}</p>
      </div>
    </div>
    <section class="track-section">
      <p class="real-music-kicker">THE ALBUM</p><h2>TRACK <span>LIST</span></h2>
      <ol class="album-tracklist">{''.join(track_html)}</ol>
    </section>
    <section class="performances-section">
      <p class="real-music-kicker">ON STAGE &amp; ON SCREEN</p><h2>LIVE <span>PERFORMANCES</span></h2>
      <p class="performance-note">{html.escape(a['perf'])}</p>
    </section>
    <a class="back-home" href="index.html#real-music">← BACK TO REAL MUSIC</a>
  </main>
  <footer>MICHAEL JACKSON • THE KING OF POP</footer>
</body></html>'''
    (p/f"{a['slug']}.html").write_text(page)

# Replace only the Real Music section; all other page content and styling remain untouched.
start=index.index('    <section class="real-music-section"')
end=index.index('    </section>', start)+len('    </section>')
solo=[('Got to Be There','got-to-be-there.html','1972','MOTOWN','https://coverartarchive.org/release/5426c78b-b63f-4db4-9b58-3284a35a3bb1/front-500'),('Ben','ben.html','1972','MOTOWN','https://coverartarchive.org/release/7f59760f-2bc0-4c71-bc9d-03ea2d8a3920/front-500')]
for a in albums:
    if a['slug'] in ['music-and-me','forever-michael','off-the-wall','thriller','bad','dangerous','history','invincible']:
        solo.append((a['title'],a['slug']+'.html',a['year'],a['label'],entries.get(a['title'].lower(),{}).get('src',f'https://commons.wikimedia.org/wiki/Special:FilePath/{a["slug"]}.jpg')))
remix=[(albums[8]['title'],'blood-on-the-dance-floor.html','1997','REMIX ALBUM',entries.get('blood on the dance floor',{}).get('src','https://commons.wikimedia.org/wiki/Special:FilePath/Blood_on_the_Dance_Floor_-_Michael_Jackson.png'))]
post=[(albums[9]['title'],'michael.html','2010','POSTHUMOUS',entries.get('michael',{}).get('src','https://commons.wikimedia.org/wiki/Special:FilePath/Michael_(Michael_Jackson_album).jpg')),(albums[10]['title'],'xscape.html','2014','POSTHUMOUS',entries.get('xscape',{}).get('src','https://commons.wikimedia.org/wiki/Special:FilePath/Xscape_by_Michael_Jackson.png'))]
def cards(items):
    out=[]
    for title,href,year,label,src in items:
        out.append(f'''<a class="real-album-card" href="{href}" aria-label="Open {html.escape(title)} album and tracklist">
          <img src="{html.escape(src)}" alt="{html.escape(title)} album cover">
          <span class="real-album-copy"><small>{year} • {label}</small><strong>{html.escape(title.upper())}</strong><em>OPEN ALBUM &amp; TRACKLIST →</em></span>
        </a>''')
    return '\n'.join(out)
section=f'''    <section class="real-music-section" id="real-music" aria-labelledby="real-music-title">
      <div class="real-music-inner">
        <p class="real-music-kicker">THE RECORDS • THE PERFORMANCES</p>
        <h2 id="real-music-title">REAL <span>MUSIC</span></h2>
        <p class="real-music-intro">Explore Michael Jackson’s solo albums, the remix release, and the posthumous albums. Open an album to see its artwork and tracklist.</p>
        <h3 class="real-category-title">SOLO STUDIO ALBUMS</h3>
        {cards(solo)}
        <h3 class="real-category-title">REMIX ALBUMS</h3>
        {cards(remix)}
        <h3 class="real-category-title">POSTHUMOUS ALBUMS</h3>
        {cards(post)}
      </div>
    </section>'''
index=index[:start]+section+index[end:]
(p/'index.html').write_text(index)
# Minimal category heading styling appended to the existing CSS; existing rules are not changed.
css=p/'real-music.css'
css.write_text(css.read_text()+'''\n.real-category-title{font-family:Cinzel,Georgia,serif;color:#d7b66a;font-size:clamp(19px,3vw,26px);letter-spacing:3px;margin:54px 0 22px;padding-bottom:12px;border-bottom:1px solid #d7b66a55}.real-album-card{margin:0 0 16px}.track-disc-heading{list-style:none!important;margin:18px 0 8px;font-family:Cinzel,Georgia,serif;letter-spacing:1.5px;color:#d7b66a;font-size:13px}.track-disc-heading::marker{content:""}\n''')
# Update README while preserving project instructions and noting the scope of verified performance content.
readme=(p/'README.txt').read_text()
readme+='''\n\nREAL MUSIC CATALOGUE UPDATE\n- Real Music now has separate Solo Studio Albums, Remix Albums, and Posthumous Albums categories.\n- Added dedicated album pages and standard-edition tracklists for Music & Me, Forever, Michael, Off the Wall, Thriller, Bad, Dangerous, HIStory, Invincible, Blood on the Dance Floor: HIStory in the Mix, Michael (2010), and Xscape.\n- Blood on the Dance Floor remains correctly classified as a remix album released during Michael Jackson's lifetime.\n- Michael (2010) and Xscape (2014) are listed as posthumous albums.\n- New pages do not contain guessed live-performance links. Their performance sections clearly state that verified event/video matches have not yet been added. Existing Got to Be There and Ben pages are preserved.\n- Jackson 5 and The Jacksons group albums have not been added to these categories.\n'''
(p/'README.txt').write_text(readme)
