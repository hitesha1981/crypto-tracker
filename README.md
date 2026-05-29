# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-29 02:35 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bat | 17.06% | $78,219,960 | $0.1175 |
| 2 | h | 13.95% | $75,941,299 | $0.2472 |
| 3 | xpl | 13.76% | $107,294,086 | $0.0961 |
| 4 | xlm | 12.36% | $1,742,286,966 | $0.1980 |
| 5 | 9bit | 11.58% | $9,104,511 | $0.0415 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | -16.06% | $33,978,031 | $0.1728 |
| 2 | beat | -13.68% | $21,507,356 | $1.0080 |
| 3 | jto | -12.72% | $63,476,566 | $0.4790 |
| 4 | wld | -11.97% | $262,405,849 | $0.2897 |
| 5 | genius | -10.48% | $148,595,474 | $0.6296 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $66,403,837,611 | $0.9987 |
| 2 | btc | -1.00% | $40,561,430,044 | $73,353.0000 |
| 3 | eth | -0.60% | $17,299,409,797 | $2,002.6000 |
| 4 | usdc | -0.01% | $14,617,199,111 | $0.9996 |
| 5 | sol | -0.34% | $2,778,188,468 | $81.7100 |


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
