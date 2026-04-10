# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-10 01:53 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | 239.25% | $159,197,635 | $1.0570 |
| 2 | siren | 23.38% | $58,425,231 | $0.6811 |
| 3 | vvv | 19.75% | $31,244,471 | $8.0100 |
| 4 | cfg | 19.32% | $28,791,122 | $0.2106 |
| 5 | zec | 17.82% | $677,616,330 | $370.9800 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sn64 | -13.11% | $3,821,762 | $23.8200 |
| 2 | tao | -9.22% | $1,448,964,196 | $293.2200 |
| 3 | lux | -6.90% | $1,351,117 | $0.0013 |
| 4 | crclon | -6.06% | $14,164,766 | $87.0700 |
| 5 | river | -5.76% | $25,095,719 | $10.6200 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $63,728,606,153 | $1.0000 |
| 2 | btc | 2.16% | $40,114,266,616 | $72,294.0000 |
| 3 | eth | 1.20% | $17,412,256,673 | $2,200.7500 |
| 4 | usdc | -0.02% | $13,769,824,879 | $0.9999 |
| 5 | sol | 1.87% | $3,511,457,213 | $83.4900 |


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
