# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-16 01:55 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ondo | 15.70% | $182,161,203 | $0.3678 |
| 2 | xec | 13.44% | $70,680,986 | $0.0000 |
| 3 | ethfi | 11.93% | $54,012,432 | $0.4410 |
| 4 | rif | 10.64% | $12,707,770 | $0.1330 |
| 5 | ldo | 10.60% | $47,468,718 | $0.3620 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -15.11% | $8,463,147 | $0.0574 |
| 2 | hash | -12.17% | $4,163 | $0.0079 |
| 3 | tibbir | -11.27% | $1,360,188 | $0.1068 |
| 4 | dexe | -9.80% | $102,521,944 | $36.4100 |
| 5 | velvet | -8.04% | $10,564,371 | $0.5160 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $45,041,770,083 | $0.9993 |
| 2 | btc | 0.15% | $28,064,992,483 | $64,720.0000 |
| 3 | usdc | 0.00% | $11,851,553,112 | $0.9998 |
| 4 | eth | 2.87% | $11,544,320,605 | $1,922.3700 |
| 5 | sol | -0.44% | $1,991,848,712 | $77.0000 |


<!-- END_DYNAMIC_CONTENT -->

## How to generate the coingecko demo public api key

[coingecko-api-key-docs](https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key)

## Requirements to setup
## 1. Install uv

```bash
brew install uv
✔︎ JSON API cask.jws.json                                                                                                                                                       [Downloaded   15.1MB/ 15.1MB]
✔︎ JSON API formula.jws.json                                                                                                                                                    [Downloaded   32.1MB/ 32.1MB]
# or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 2. Setup Python Environment (uv)

From the project root:

```bash
uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate
```

Install dependencies (locked):
```bash
uv add pandas requests matplotlib python-dotenv
```


---

## 4. Update coingecko demo key in .env ( I have provided in .env.sample)
```bash
cat .env
CGK_API_DEMO_KEY="Your-coingecko-demo-api-key-here"
```

---

## 3. To manually run the script
```bash
python3.12 main.py
```
---
