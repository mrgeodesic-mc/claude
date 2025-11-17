# Narrative Journey Web App

An interactive web application for exploring Personal Narrative & Career Agency through Adaptive Leadership principles. Participants can scan a QR code to access the app and build their custom leadership journey.

## Features

- **Mobile-First Design**: Optimized for smartphones and tablets accessed via QR code
- **Progressive Journey**: Three themed exploration sections with guided questions
- **Custom Reflections**: Save personal reflections for each theme
- **Local Storage**: Automatically saves progress in the browser
- **Export Functionality**: Download complete journey as a text file
- **Progress Tracking**: Visual progress bar showing completion status
- **Offline-Capable**: Works without internet connection once loaded

## Quick Start

### Option 1: Open Locally

1. Open `index.html` directly in any modern web browser
2. No server or installation required!

### Option 2: Deploy to a Web Server

#### Deploy to GitHub Pages (Free)

1. Create a new GitHub repository
2. Upload `index.html` to the repository
3. Go to Settings → Pages
4. Select your main branch as the source
5. Your app will be available at: `https://yourusername.github.io/repository-name/`

#### Deploy to Netlify (Free)

1. Sign up at [netlify.com](https://netlify.com)
2. Drag and drop the `narrative-journey` folder into Netlify
3. Get your instant URL (e.g., `https://your-app.netlify.app`)

#### Deploy to Vercel (Free)

1. Sign up at [vercel.com](https://vercel.com)
2. Install Vercel CLI: `npm install -g vercel`
3. Run `vercel` in the `narrative-journey` directory
4. Follow the prompts to deploy

## Creating a QR Code

Once you have a URL (either local or deployed), create a QR code:

### Method 1: Online QR Code Generators

Visit any of these free services:
- [QR Code Generator](https://www.qr-code-generator.com/)
- [QR Code Monkey](https://www.qrcode-monkey.com/)
- [QRickit](https://qrickit.com/qrickit_apps/qrickit_qrcode.php)

Steps:
1. Enter your webapp URL
2. Customize the design (optional)
3. Download the QR code image
4. Print or display it for participants to scan

### Method 2: Using Node.js (if you have it installed)

```bash
npm install -g qrcode-terminal
qrcode-terminal "https://your-webapp-url.com"
```

This displays a QR code right in your terminal!

### Method 3: Using Python (if you have it installed)

```bash
pip install qrcode[pil]
python -c "import qrcode; qrcode.make('https://your-webapp-url.com').save('qr-code.png')"
```

## Local Testing with QR Code

If you want to test on mobile before deploying:

1. **Start a local server:**

   Using Python 3:
   ```bash
   cd narrative-journey
   python3 -m http.server 8000
   ```

   Using Python 2:
   ```bash
   cd narrative-journey
   python -m SimpleHTTPServer 8000
   ```

   Using Node.js (if you have `http-server` installed):
   ```bash
   npx http-server narrative-journey -p 8000
   ```

2. **Find your local IP address:**
   - Mac/Linux: Run `ifconfig | grep "inet "` or `ip addr`
   - Windows: Run `ipconfig`
   - Look for something like `192.168.1.X`

3. **Create QR code with your local URL:**
   - Use format: `http://192.168.1.X:8000/index.html`
   - Make sure your phone is on the same WiFi network

4. **Scan with your phone to test!**

## App Structure

### Journey Flow

1. **Welcome Screen**: Introduction to Adaptive Leadership and narrative control
2. **Theme Selection**: Choose from three exploration themes
3. **Theme 1**: Owning Your Narrative
4. **Theme 2**: Sharing Your Story with Colleagues
5. **Theme 3**: Narrative as Career Pathway
6. **Closing Reflection**: Commit to an action step
7. **Journey Summary**: Review all reflections and export

### Key Features

- **Auto-Save**: Reflections automatically save to browser storage
- **Non-Linear Navigation**: Jump between themes as desired
- **Progress Tracking**: See which themes are completed
- **Export**: Download all reflections as a text file
- **Reset**: Start fresh with a new journey

## Customization

The app is contained in a single `index.html` file for easy customization:

### Change Colors

Edit the CSS variables at the top of the `<style>` section:

```css
:root {
    --primary-color: #2C5F7C;      /* Main brand color */
    --secondary-color: #4A90A4;    /* Secondary accents */
    --accent-color: #E8A87C;       /* Highlight color */
}
```

### Modify Content

All content is in the HTML sections:
- Themes are in `<div id="theme1-screen">`, `theme2-screen`, etc.
- Questions are in `<ul class="question-list">`
- Instructions are in `<div class="intro-text">`

### Add Analytics

Add Google Analytics or other tracking before the closing `</body>` tag:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## Browser Support

Works on all modern browsers:
- Chrome/Edge (version 90+)
- Safari (version 14+)
- Firefox (version 88+)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Data Privacy

- All data stored locally in browser's localStorage
- No data sent to any server
- Clearing browser data will reset the journey
- Export feature allows users to save their reflections externally

## Facilitation Tips

### For In-Person Workshops

1. **Display QR Code**: Project on screen or print on handouts
2. **Test Connection**: Verify WiFi/network access before session
3. **Backup Plan**: Have printed versions ready
4. **Group Discussion**: Use after individual reflection time

### For Virtual Workshops

1. **Share Link**: Send direct URL in chat
2. **Share Screen**: Walk through first theme together
3. **Breakout Rooms**: Give time for individual reflection
4. **Reconvene**: Discuss themes as a group

### Discussion Prompts

After each theme, facilitate discussion with:
- "Who would like to share an insight from their reflection?"
- "What patterns are you noticing in your narrative?"
- "How might you apply this in your next team meeting?"

## Troubleshooting

**QR code won't scan:**
- Ensure good lighting
- Try different QR code sizes (larger is often better)
- Test with multiple phones/QR readers

**App not loading:**
- Check internet connection (for remote URLs)
- Verify the URL is correct
- Try opening in incognito/private mode

**Reflections not saving:**
- Click "Save Reflection" button after writing
- Check browser allows localStorage
- Look for "Saved! ✓" confirmation message

**Lost my reflections:**
- Check if you cleared browser data
- Use "Export Journey" regularly to backup
- Reflections are browser-specific (won't sync across devices)

## Technical Details

- **Size**: ~20KB (single file)
- **Dependencies**: None (pure HTML/CSS/JavaScript)
- **Storage**: Browser localStorage (typically 5-10MB limit)
- **Performance**: Instant load, no API calls

## License

Free to use and modify for educational and organizational development purposes.

## Support

For questions or issues, contact your workshop facilitator or system administrator.

---

**Remember**: You can't always control your positional authority—but you can always control your narrative. And your narrative influences how people see your capacity, your readiness, and your trajectory.
