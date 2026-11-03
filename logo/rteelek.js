const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1500,height:3000}});
await p.goto('file://'+__dirname+'/teelek.html');await p.waitForTimeout(800);
for(const id of ['L3','M2']){await (await p.$('#'+id)).screenshot({path:`teelek-${id}.png`});}
await b.close();})();
