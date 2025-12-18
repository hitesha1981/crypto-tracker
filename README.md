# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-18 01:05 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 29.16% | $62,185,295 | $0.3977 |
| 2 | tomi | 12.28% | $49,066 | $0.0000 |
| 3 | cc | 8.99% | $15,182,546 | $0.0777 |
| 4 | syrup | 4.42% | $60,083,438 | $0.2784 |
| 5 | hash | 4.36% | $140,802 | $0.0310 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | leo | -18.47% | $4,836,761 | $7.4600 |
| 2 | fartcoin | -13.28% | $109,502,325 | $0.3076 |
| 3 | ultima | -12.47% | $14,669,063 | $4,943.0900 |
| 4 | pump | -10.91% | $107,521,559 | $0.0021 |
| 5 | spx | -10.76% | $20,010,595 | $0.4822 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $80,393,916,989 | $0.9998 |
| 2 | btc | -1.84% | $49,300,764,320 | $86,042.0000 |
| 3 | eth | -4.26% | $27,021,810,457 | $2,829.3000 |
| 4 | usdc | 0.00% | $13,302,550,552 | $1.0000 |
| 5 | sol | -4.20% | $6,002,240,280 | $123.4900 |


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
