import numpy as np, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S=sys.argv[1]; W,H=1920,1080
rng=np.random.default_rng(1)
# 1 degradado: cielo + sol + montañas
y=np.linspace(0,1,H)[:,None]; x=np.linspace(0,1,W)[None,:]
sky=np.stack([40+180*y+0*x, 80+120*y+0*x, 200-80*y+0*x],-1)
d=np.sqrt((x-0.7)**2+((y-0.35)*H/W)**2); sky+= (np.clip(1-d*6,0,1)**2)[...,None]*np.array([255,180,60])
img=Image.fromarray(np.clip(sky,0,255).astype(np.uint8)); dr=ImageDraw.Draw(img)
pts=[(0,H)]+[(i, int(H*0.65-200*np.sin(i/170)-80*np.sin(i/53))) for i in range(0,W+1,20)]+[(W,H)]
dr.polygon(pts,fill=(40,70,50)); img.save(f"{S}/muestras_sint/01_degradado.png")
# 2 texto y cifras
img=Image.new("RGB",(W,H),(20,20,25)); dr=ImageDraw.Draw(img)
try: f=ImageFont.truetype("DejaVuSans-Bold.ttf",140); f2=ImageFont.truetype("DejaVuSans.ttf",60)
except: f=f2=ImageFont.load_default()
dr.text((120,200),"BORDER 262",font=f,fill=(240,240,230)); dr.text((120,450),"4.1 ¢ · 1,716 h · 93.8",font=f2,fill=(255,176,0))
dr.text((120,600),"Small text: Paid with cows? Rumor... correct.",font=f2,fill=(180,200,255))
img.save(f"{S}/muestras_sint/02_texto.png")
# 3 cara (ilustración simple con piel, ojos, sombras)
img=Image.new("RGB",(W,H),(90,120,150)); dr=ImageDraw.Draw(img)
dr.ellipse((660,140,1260,940),fill=(225,175,140)); dr.ellipse((800,420,900,480),fill=(255,255,255)); dr.ellipse((1020,420,1120,480),fill=(255,255,255))
dr.ellipse((830,425,875,475),fill=(60,40,30)); dr.ellipse((1050,425,1095,475),fill=(60,40,30))
dr.arc((850,600,1070,760),20,160,fill=(150,60,60),width=12); dr.polygon([(960,480),(930,620),(990,620)],fill=(205,150,120))
img=img.filter(ImageFilter.GaussianBlur(6)); img.save(f"{S}/muestras_sint/03_cara.png")
# 4 foto-like: textura con ruido y detalle (campo, árboles)
base=np.zeros((H,W,3)); base[...,0]=90+60*y; base[...,1]=130+40*y; base[...,2]=60+20*y
noise=rng.normal(0,25,(H//8,W//8,3)); noise=np.array(Image.fromarray(np.clip(noise+128,0,255).astype(np.uint8)).resize((W,H),Image.BICUBIC),float)-128
img=Image.fromarray(np.clip(base+noise,0,255).astype(np.uint8)); dr=ImageDraw.Draw(img)
for i in range(30):
    cx=int(rng.uniform(0,W)); cy=int(rng.uniform(H*0.3,H*0.7)); r=int(rng.uniform(30,90))
    dr.ellipse((cx-r,cy-r,cx+r,cy+r),fill=(30,int(rng.uniform(70,110)),40))
img.save(f"{S}/muestras_sint/04_foto_textura.png")
# animación: degradado estático + bola que se mueve (24 fotogramas)
bg=Image.open(f"{S}/muestras_sint/01_degradado.png")
for k in range(24):
    im=bg.copy(); ImageDraw.Draw(im).ellipse((200+50*k,700,320+50*k,820),fill=(230,60,40)); im.save(f"{S}/anim/f{k:03d}.png")
