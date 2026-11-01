(function(){
var P={slab:{tablet:0,keyboard:0,modem:1,camera:1,homebutton:0,volumebutton:1,powerbutton:1,brightness:1},
qwerty:{tablet:0,keyboard:1,modem:1,camera:1,homebutton:0,volumebutton:1,powerbutton:1,brightness:1},
tablet:{tablet:1,keyboard:0,modem:0,camera:1,homebutton:1,volumebutton:1,powerbutton:1,brightness:1}};
var f,r=document.documentElement,q;
try{q=new URLSearchParams(location.search).get('device')}catch(e){}
if(window.HELP_DEVICE){f=window.HELP_DEVICE;r.dataset.onDevice='1'}
else if(P[q]){f=P[q]}
else{try{f=JSON.parse(localStorage.getItem('help-features'))}catch(e){}
if(!f||typeof f!=='object')f=P[innerWidth>=900?'tablet':'slab']}
window.HELP_PRESETS=P;window.HELP_FEATURES=f;r.dataset.mode=f.tablet?'tablet':'phone'
})();
