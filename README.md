# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-16 02:00 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | enj | 54.52% | $714,854,499 | $0.0933 |
| 2 | siren | 18.87% | $30,839,839 | $0.8330 |
| 3 | chz | 14.47% | $144,579,530 | $0.0420 |
| 4 | edge | 12.54% | $16,637,288 | $1.1300 |
| 5 | h | 10.76% | $24,892,099 | $0.1084 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | -42.90% | $295,983,393 | $11.0500 |
| 2 | jst | -17.30% | $49,917,685 | $0.0656 |
| 3 | river | -16.18% | $42,926,225 | $7.4500 |
| 4 | genius | -15.69% | $26,900,286 | $0.5479 |
| 5 | 币安人生 | -8.16% | $293,732,245 | $0.3322 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $63,769,566,043 | $1.0000 |
| 2 | btc | -0.02% | $38,969,800,368 | $74,625.0000 |
| 3 | eth | 0.69% | $16,187,206,994 | $2,351.6400 |
| 4 | usdc | 0.01% | $15,818,637,409 | $0.9999 |
| 5 | sol | 1.09% | $3,618,322,133 | $84.8300 |


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
