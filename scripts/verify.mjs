import { chromium } from '@playwright/test';
const browser=await chromium.launch({headless:true});
const page=await browser.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
for(const width of [1920,768,390]){
 await page.setViewportSize({width,height:1080});await page.goto(process.env.BASE_URL || 'http://127.0.0.1:3000');await page.evaluate(()=>document.fonts.ready);
 const info=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,images:[...document.images].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0,width:i.getBoundingClientRect().width,height:i.getBoundingClientRect().height})),sections:document.querySelectorAll('main > section').length}));
 if(info.overflow||info.images.some(i=>!i.loaded)||info.sections!==6)throw Error(JSON.stringify(info));console.log(width,JSON.stringify(info));
 if(!await page.locator('.projects-carousel .swiper-initialized').count())throw Error('Swiper did not initialize');
 if(await page.locator('.projects-carousel .swiper-slide').count()===1 && !await page.getByRole('button',{name:'Proyecto siguiente',exact:true}).isDisabled())throw Error('Single project navigation should be disabled');
 if(await page.locator('[data-technology]').count()===0)throw Error('Technology entries missing');
 await page.screenshot({path:`/private/tmp/portfolio-${width}.png`,fullPage:true});
 if(width<1100){await page.getByRole('button',{name:'Abrir menú',exact:true}).click();await page.getByRole('navigation').getByRole('link',{name:'Contacto',exact:true}).click();if(await page.getByRole('button',{name:'Abrir menú',exact:true}).getAttribute('aria-expanded')!=='false')throw Error('Menu failed to close');}
 if(await page.getByRole('link',{name:'Email',exact:true}).getAttribute('href')!=='mailto:francisco_e3@hotmail.com')throw Error('Incorrect email');
}
if(errors.length)throw Error(errors.join('\n'));await browser.close();console.log('All browser checks passed');
