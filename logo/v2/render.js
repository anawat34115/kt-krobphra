const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1200 }, deviceScaleFactor: +(process.env.DPR || 1) });
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + path.resolve(f));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.screenshot({ path: f.replace('.html', '.png'), omitBackground: f.includes('transparent') });
  }
  await b.close();
})();
