# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-15 01:42 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pepe | 26.90% | $980,535,702 | $0.0000 |
| 2 | pippin | 24.07% | $63,408,501 | $0.7440 |
| 3 | hnt | 18.92% | $21,426,769 | $1.1100 |
| 4 | zec | 16.73% | $667,284,500 | $321.9700 |
| 5 | pi | 16.54% | $49,461,320 | $0.1789 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | myx | -23.88% | $24,795,941 | $2.1700 |
| 2 | river | -23.60% | $36,670,721 | $13.7700 |
| 3 | h | -13.20% | $62,855,356 | $0.1969 |
| 4 | kite | -12.52% | $140,700,699 | $0.1967 |
| 5 | kau | -10.41% | $5,659 | $153.5000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $64,566,758,360 | $0.9997 |
| 2 | btc | 0.89% | $37,697,579,514 | $69,590.0000 |
| 3 | eth | 0.36% | $16,596,315,971 | $2,062.0300 |
| 4 | usdc | -0.01% | $3,085,800,597 | $0.9999 |
| 5 | sol | 3.42% | $3,083,178,075 | $87.7800 |


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
