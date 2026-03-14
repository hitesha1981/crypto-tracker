# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-14 01:22 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bananas31 | 45.14% | $96,648,150 | $0.0114 |
| 2 | trump | 29.97% | $1,786,692,053 | $3.8400 |
| 3 | river | 10.87% | $41,547,562 | $20.7000 |
| 4 | dexe | 9.35% | $13,634,335 | $4.6700 |
| 5 | kau | 8.79% | $144,297 | $179.0100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pi | -24.82% | $162,524,023 | $0.2151 |
| 2 | akt | -9.73% | $14,218,920 | $0.4224 |
| 3 | tibbir | -9.12% | $7,655,155 | $0.1509 |
| 4 | kite | -8.32% | $128,594,633 | $0.2290 |
| 5 | pump | -8.16% | $107,508,521 | $0.0020 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $92,478,640,815 | $1.0000 |
| 2 | btc | -1.20% | $58,773,578,952 | $70,768.0000 |
| 3 | eth | -1.64% | $25,282,094,439 | $2,090.7300 |
| 4 | usdc | -0.01% | $13,420,653,790 | $0.9999 |
| 5 | sol | -2.25% | $4,937,176,586 | $88.0500 |


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
