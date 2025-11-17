# Quick Start Guide - Narrative Journey Web App

Get your workshop running in 5 minutes!

## Fastest Path to Launch

### Option 1: Local Testing (Right Now!)

1. **Open the app:**
   ```bash
   # Just open index.html in your browser
   open index.html  # Mac
   start index.html # Windows
   xdg-open index.html # Linux
   ```

2. **Test it yourself:**
   - Click through the journey
   - Try saving reflections
   - View the summary page
   - Test the export function

### Option 2: Deploy Online (5 Minutes)

#### Using Netlify Drop (No Account Needed!)

1. Go to [drop.netlify.com](https://app.netlify.com/drop)
2. Drag the entire `narrative-journey` folder onto the page
3. Get your instant URL (e.g., `fancy-name-123.netlify.app`)
4. Done! Share the link or create a QR code

#### Using GitHub Pages

1. Create a GitHub account (if you don't have one)
2. Create a new repository called `narrative-journey`
3. Upload `index.html` to the repository
4. Go to Settings → Pages → Select main branch → Save
5. Your URL: `https://yourusername.github.io/narrative-journey/`

## Creating a QR Code (3 Methods)

### Method 1: Online (Easiest)

1. Go to [qr-code-generator.com](https://www.qr-code-generator.com/)
2. Paste your URL
3. Click "Create QR Code"
4. Download and print!

### Method 2: Using Our QR Display Page

1. Open `qr-display.html` in your browser
2. Enter your webapp URL
3. Click "Generate QR Code"
4. Click "Print This Page"
5. Done!

### Method 3: Using Python Script (For Tech Users)

```bash
# Install the package
pip install qrcode[pil]

# Generate QR code
python generate-qr.py https://your-url-here.com

# This creates qr-code.png that you can print!
```

## For In-Person Workshops

### Before the Session:

1. ✅ Test the app on your phone
2. ✅ Generate and print the QR code (at least 3x3 inches)
3. ✅ Verify WiFi is working (if using local URL)
4. ✅ Have backup printed materials ready

### During the Session:

1. **Introduction (5 min):**
   - Show the QR code on screen or handout
   - Have participants scan and open the app
   - Do a quick walkthrough of the welcome screen

2. **Individual Exploration (20-30 min):**
   - Let participants work through themes at their own pace
   - Circulate to answer questions
   - Encourage note-taking in the app

3. **Group Discussion (20-30 min):**
   - Use the discussion prompts from each theme
   - Ask volunteers to share insights
   - Connect themes to real workplace scenarios

4. **Closing (10 min):**
   - Have everyone complete the closing reflection
   - Remind them to export their journey
   - Discuss next steps

## For Virtual Workshops

1. **Share the link directly in chat:**
   ```
   Join our Narrative Journey:
   https://your-app-url.com
   ```

2. **Use breakout rooms:**
   - 15 min: Individual reflection
   - 10 min: Small group discussion
   - 10 min: Full group debrief

3. **Screen share option:**
   - Walk through the first theme together
   - Then let participants explore independently

## Common URLs You Might Use

| Scenario | Example URL | When to Use |
|----------|-------------|-------------|
| Local testing | `http://localhost:8000` | Testing on your computer |
| Local network | `http://192.168.1.5:8000` | Workshop in same room with WiFi |
| GitHub Pages | `https://username.github.io/repo/` | Free permanent hosting |
| Netlify | `https://app-name.netlify.app` | Quick deployment |
| Custom domain | `https://workshop.yourcompany.com` | Professional deployment |

## Troubleshooting in 30 Seconds

**QR code won't scan?**
- Make it bigger (print at least 3x3 inches)
- Check lighting (not too dark or too reflective)
- Try a different phone

**App won't load?**
- Check internet connection
- Try opening URL directly in browser
- Clear browser cache

**Reflections not saving?**
- Make sure to click "Save Reflection" button
- Check for green "Saved! ✓" message
- Remind participants to export regularly

**Need to start over?**
- Click "Start New Journey" button
- Or clear browser data
- Or use incognito/private mode

## Quick Tips for Facilitators

💡 **Pre-load the app:** Have participants open it 5 minutes before starting

💡 **Encourage honesty:** Reflections are private and locally stored

💡 **Use the export:** Remind participants to export at the end

💡 **Don't rush:** Let people move at their own pace through themes

💡 **Connect to work:** Keep bringing examples back to real workplace situations

💡 **Facilitate don't lecture:** Use questions to draw out insights

## Data & Privacy

- ✅ All data stored only on participant's device
- ✅ No server uploads or tracking
- ✅ Private reflections stay private
- ✅ Export feature lets participants keep their work
- ⚠️ Clearing browser data will erase reflections (remind them to export!)

## Need Help?

- Check the full `README.md` for detailed instructions
- All files are in one folder for easy sharing
- No installation or dependencies required
- Works on any modern browser

---

**Ready to start?** Open `index.html` and begin exploring! 🚀

Remember: *You can't always control your positional authority—but you can always control your narrative.*
