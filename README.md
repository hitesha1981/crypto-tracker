# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-27 02:32 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | 48.72% | $22,198,846 | $0.7441 |
| 2 | skyai | 20.89% | $19,819,956 | $0.3731 |
| 3 | aave | 18.30% | $562,419,044 | $96.5100 |
| 4 | dydx | 17.52% | $12,854,261 | $0.1620 |
| 5 | beat | 16.33% | $41,859,665 | $2.6100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | data | -21.50% | $86,559,862 | $0.3182 |
| 2 | m | -12.41% | $15,570,639 | $0.7373 |
| 3 | bdx | -10.92% | $12,400,689 | $0.0808 |
| 4 | dexe | -7.13% | $23,675,802 | $21.5900 |
| 5 | awe | -6.27% | $6,910,417 | $0.0642 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $58,444,525,182 | $0.9986 |
| 2 | btc | 2.41% | $37,110,060,627 | $60,155.0000 |
| 3 | usdc | 0.00% | $16,543,726,229 | $0.9998 |
| 4 | eth | 3.14% | $13,305,223,055 | $1,580.9600 |
| 5 | sol | 8.58% | $4,344,263,565 | $71.9900 |


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
