# Apuração da Urna — 2º turno 2026

Apuração ao vivo do 2º turno (25/10/2026): presidente (Brasil, 27 UFs e exterior) e governador (AC, AM, DF, ES, RJ, RN, TO), com mapa 3D.

- Os dados são lidos pelo navegador do visitante direto do servidor oficial do TSE (`resultados.tse.jus.br`), a cada 30 s (Brasil) e a cada minuto (estados e governadores). Os percentuais exibidos são os do próprio arquivo do TSE, sem cálculo próprio.
- Antes das 17h (Brasília) o site mostra a contagem regressiva e o mapa do 1º turno.

## Monetização
No arquivo `src/page.html`, bloco `MONETIZACAO`:
- `adsenseClient`: seu ID do AdSense (`ca-pub-...`) e os IDs dos blocos em `adsenseSlots`.
- `pix`: sua chave Pix (mostra o botão de apoio).

Depois rode `python3 build.py` e publique a pasta `site/`.

## Publicar
GitHub Pages: Settings → Pages → Source: GitHub Actions (o workflow em `.github/workflows/pages.yml` publica a pasta `site/`).
