# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-20 00:47 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | trump | 27.20% | $264,319,259 | $1.8000 |
| 2 | cashcat | 21.60% | $26,740,657 | $0.1191 |
| 3 | hype | 19.30% | $1,283,351,750 | $70.7300 |
| 4 | arb | 19.10% | $106,435,825 | $0.0890 |
| 5 | rail | 17.80% | $203,537 | $1.7200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -18.00% | $9,776,482 | $0.0872 |
| 2 | genius | -10.00% | $9,426,000 | $0.3274 |
| 3 | 币安人生 | -9.40% | $12,777,249 | $0.4263 |
| 4 | btw | -9.00% | $146,510,069 | $0.4100 |
| 5 | stable | -4.70% | $13,187,820 | $0.0295 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $76,415,847,016 | $0.9995 |
| 2 | btc | 7.20% | $45,356,832,258 | $69,585.0000 |
| 3 | eth | 17.70% | $28,569,304,363 | $2,268.8500 |
| 4 | usdc | 0.00% | $21,416,389,066 | $0.9997 |
| 5 | sol | 10.80% | $4,441,060,169 | $85.5000 |


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
