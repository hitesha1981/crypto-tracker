# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-08 02:24 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | inj | 20.81% | $233,655,584 | $6.6100 |
| 2 | ai | 18.42% | $44,182,033 | $0.2658 |
| 3 | wld | 18.24% | $499,266,426 | $0.4857 |
| 4 | aero | 17.95% | $135,548,511 | $0.6488 |
| 5 | uai | 16.11% | $25,262,546 | $0.7158 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cashcat | -12.31% | $28,112,964 | $0.1983 |
| 2 | zcat | -11.94% | $24,474,524 | $0.1319 |
| 3 | arb | -8.86% | $454,830,199 | $0.1701 |
| 4 | npc | -8.47% | $4,818,377 | $0.0186 |
| 5 | dash | -7.97% | $204,724,351 | $64.2800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $46,914,805,619 | $0.9999 |
| 2 | btc | -0.75% | $22,883,518,133 | $79,329.0000 |
| 3 | usdc | 0.01% | $11,554,391,443 | $0.9999 |
| 4 | eth | -0.19% | $11,156,447,905 | $2,499.3300 |
| 5 | sol | -1.21% | $3,059,646,969 | $104.2400 |


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
