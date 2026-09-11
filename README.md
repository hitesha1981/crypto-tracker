# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-11 02:21 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | 牛来 | 47.65% | $124,937,428 | $0.1156 |
| 2 | stonk | 40.79% | $105,287,356 | $0.2625 |
| 3 | ray | 28.01% | $233,723,018 | $1.5500 |
| 4 | prl | 14.90% | $1,138,342 | $0.4696 |
| 5 | hash | 14.42% | $52,713 | $0.0085 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | laptop | -49.10% | $15,145,464 | $0.3756 |
| 2 | uai | -21.15% | $11,431,588 | $0.5962 |
| 3 | zec | -11.70% | $1,439,237,249 | $1,077.5800 |
| 4 | bch | -9.47% | $349,629,135 | $226.3000 |
| 5 | pump | -8.84% | $196,966,045 | $0.0037 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $56,560,425,890 | $0.9997 |
| 2 | btc | -1.49% | $29,553,817,312 | $76,866.0000 |
| 3 | usdc | 0.02% | $16,640,401,908 | $1.0000 |
| 4 | eth | -0.49% | $15,289,158,711 | $2,450.1600 |
| 5 | sol | -1.88% | $3,000,369,799 | $99.2200 |


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
