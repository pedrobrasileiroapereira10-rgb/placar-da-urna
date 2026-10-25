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
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
'''
open('site/index.html', 'w', encoding='utf-8').write(head + page + '\n</body>\n</html>\n')
shutil.copy('src/privacidade.html', 'site/privacidade.html')
open('site/.nojekyll', 'w').close()
print('site/index.html', os.path.getsize('site/index.html'), 'bytes')
