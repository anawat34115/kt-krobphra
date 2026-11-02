const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport:{width:1600,height:900}, deviceScaleFactor:1});
  await p.goto('file://' + __dirname + '/logos.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
  for (const id of ['A','B','C']) await (await p.$('#'+id)).screenshot({path:`kt-logo-${id}.png`});
  await b.close();
})();
