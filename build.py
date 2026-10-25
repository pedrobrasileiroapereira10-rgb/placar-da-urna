"""Gera a pasta site/ pronta para publicar (GitHub Pages ou qualquer hospedagem estática)."""
import os, shutil
os.makedirs('site', exist_ok=True)
page = open('src/page.html', encoding='utf-8').read()
page = page.replace('__GEO__', open('src/ufs-min.json', encoding='utf-8').read())
page = page.replace('__T1__', open('src/primeiro-turno.json', encoding='utf-8').read())
head = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Apuração do 2º turno das Eleições 2026 ao vivo: Lula x Flávio Bolsonaro, mapa 3D estado por estado e governadores, com dados oficiais do TSE.">
<meta property="og:title" content="Apuração 2º turno 2026 ao vivo · mapa 3D">
<meta property="og:description" content="Lula x Flávio Bolsonaro estado por estado, atualizado a cada minuto com dados oficiais do TSE.">
<meta property="og:type" content="website">
<meta name="theme-color" content="#080B14">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E%3Cstop offset='0' stop-color='%23FFE7A0'/%3E%3Cstop offset='.45' stop-color='%23F2C14E'/%3E%3Cstop offset='1' stop-color='%23C98A1B'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='64' height='64' rx='16' fill='url(%23g)'/%3E%3Crect x='18' y='10' width='28' height='4' rx='2' fill='%230B0F1A' opacity='.6'/%3E%3Ctext x='32' y='51' text-anchor='middle' font-family='Impact,Arial Black,sans-serif' font-weight='900' font-size='30' fill='%230B0F1A'%3EP10%3C/text%3E%3C/svg%3E">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
'''
open('site/index.html', 'w', encoding='utf-8').write(head + page + '\n</body>\n</html>\n')
shutil.copy('src/privacidade.html', 'site/privacidade.html')
open('site/.nojekyll', 'w').close()
print('site/index.html', os.path.getsize('site/index.html'), 'bytes')
