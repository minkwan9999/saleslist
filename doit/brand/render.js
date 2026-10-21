// usage: node render.js preview t1,t2,...   |   node render.js full out.mp4
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const dir = __dirname;
const FPS = 30;

(async () => {
  const [mode, arg] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.join(dir, 'brand.html'));
  await page.evaluate(async () => {
    await Promise.all([document.fonts.load('700 100px FR','Do'),document.fonts.load('900 100px GA','가'),document.fonts.load('700 100px GA','가'),document.fonts.load('100px JU','가')]);
    await document.fonts.ready;
  });
  const stage = await page.$('#stage');
  if (mode === 'preview') {
    for (const t of arg.split(',').map(Number)) {
      await page.evaluate(t => render(t), t);
      await stage.screenshot({ path: path.join(dir, 'prev', `p_${t.toFixed(2)}.png`) });
    }
  } else {
    const dur = await page.evaluate(() => DUR);
    const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-r', String(FPS), '-i', '-',
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', path.join(dir, 'silent.mp4')]);
    const n = Math.round(dur * FPS);
    for (let f = 0; f < n; f++) {
      await page.evaluate(t => render(t), f / FPS);
      const buf = await stage.screenshot({ type: 'jpeg', quality: 93 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (f % 60 === 0) console.log('frame', f, '/', n);
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
    fs.writeFileSync(path.join(dir, 'events.json'), JSON.stringify(await page.evaluate(() => __ev)));
  }
  await browser.close();
})();
