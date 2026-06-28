# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-28 02:45 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | 105.53% | $87,903,892 | $1.5800 |
| 2 | bas | 27.68% | $12,552,159 | $0.0502 |
| 3 | pieverse | 25.30% | $45,275,089 | $0.8395 |
| 4 | slx | 13.98% | $163,160,282 | $0.5120 |
| 5 | eigen | 11.21% | $30,241,358 | $0.2446 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -37.01% | $16,599,787 | $0.0604 |
| 2 | skyai | -33.76% | $33,666,520 | $0.2479 |
| 3 | lab | -11.27% | $41,947,911 | $17.1600 |
| 4 | xcn | -7.87% | $10,441,625 | $0.0038 |
| 5 | wld | -7.79% | $166,385,257 | $0.4341 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $26,840,182,191 | $0.9986 |
| 2 | btc | -0.22% | $15,319,011,703 | $60,058.0000 |
| 3 | eth | -0.80% | $5,908,608,644 | $1,569.0600 |
| 4 | usdc | -0.00% | $5,636,801,147 | $0.9997 |
| 5 | sol | -1.87% | $1,773,871,334 | $70.6500 |


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
