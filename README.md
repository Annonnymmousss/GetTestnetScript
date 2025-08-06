# GetTestnet.Script

An automated Python script for claiming Sepolia ETH from faucets on a scheduled basis using Playwright browser automation.

## 🚀 Features

- **Automated Faucet Claims**: Automatically fills wallet address and clicks receive button
- **Scheduled Execution**: Runs at a specified time daily (default: 23:51)
- **Browser Automation**: Uses Playwright for reliable web interaction
- **Error Handling**: Continues running even if individual claims fail
- **Visual Feedback**: Non-headless mode allows you to see the browser in action

## 📋 Prerequisites

- Python 3.7+
- Playwright
- A Sepolia testnet wallet address

## 🔧 Installation

1. **Install required packages:**
   ```bash
   pip install playwright asyncio
   ```

2. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

## ⚙️ Configuration

Before running the script, update the following variables in `FlaucetScript.py`:

```python
FAUCET_URL = "..."  # Replace with actual faucet URL
WALLET_ADDRESS = "0xYourSepoliaWalletAddress"  # Your Sepolia wallet address
TRIGGER_TIME = "23:51"  # Time to run daily (24-hour format)
```

### Configuration Options

- **FAUCET_URL**: The URL of the Sepolia ETH faucet you want to use
- **WALLET_ADDRESS**: Your Ethereum wallet address for receiving test ETH
- **TRIGGER_TIME**: Daily execution time in HH:MM format (24-hour)

## 🏃‍♂️ Usage

1. **Configure the script** with your faucet URL and wallet address
2. **Run the script:**
   ```bash
   python FlaucetScript.py
   ```
3. **The script will:**
   - Calculate wait time until the next trigger time
   - Open the faucet page in a browser
   - Fill in your wallet address
   - Click the receive button
   - Wait 24 hours before the next claim

## 🔄 How It Works

1. **Wait Calculation**: The script calculates how long to wait until the next trigger time
2. **Browser Launch**: Opens Chromium browser (visible by default)
3. **Page Navigation**: Goes to the specified faucet URL
4. **Form Interaction**: 
   - Waits for input field to load
   - Fills wallet address
   - Clicks "Receive" button
5. **Confirmation**: Waits 5 seconds to see results
6. **Loop**: Sleeps for 24 hours and repeats

## ⚠️ Important Notes

- **Testnet Only**: This script is designed for Sepolia testnet faucets only
- **Rate Limits**: Respects faucet rate limits with 24-hour intervals
- **Browser Visibility**: Runs in non-headless mode by default for transparency
- **Error Recovery**: Continues running even if individual claims fail

## 🛠️ Customization

### Change to Headless Mode
```python
browser = await p.chromium.launch(headless=True)
```

### Modify Button Selector
If the faucet uses different button text:
```python
await page.click("button:has-text('Claim')")  # or 'Send', 'Get ETH', etc.
```

### Adjust Wait Times
```python
await page.wait_for_timeout(10000)  # Wait 10 seconds instead of 5
```

## 🐛 Troubleshooting

### Common Issues

- **Selector Not Found**: Update the input or button selectors based on the faucet's HTML
- **Page Load Timeout**: Increase wait times or check internet connection
- **Faucet Changes**: Faucet websites may update their interface

### Debug Mode
Add debugging by enabling verbose logging:
```python
print(f"Current page title: {await page.title()}")
```

## ⚖️ Legal & Ethical Considerations

- Only use with faucets that allow automated access
- Respect rate limits and terms of service
- This tool is for educational and testing purposes only
- Use responsibly on testnets only

## 📝 License

This script is provided as-is for educational purposes. Use at your own risk and ensure compliance with faucet terms of service.

## 🤝 Contributing

Feel free to fork and improve this script. Common improvements could include:
- Support for multiple faucets
- Configuration file support
- Better error handling
- Captcha solving capabilities
- Logging to files
