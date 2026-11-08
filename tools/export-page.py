import sys,os,re
# Turns a canvas page into the standalone page the site serves: local React, images from site/assets.
src,dst,assets=sys.argv[1],sys.argv[2],sys.argv[3]
NEW2OLD={"367414a8c7f264c181ae0cefe21f74a9":"0072284cd42a958df9861a57a6804bf0","bb0aea433bbbcee9c7e640c8d4a3bfc0":"1f1bd631ee9bcfce4029fbe3e059baa0","49ff3364e72a544afbf44a1c342222d4":"34da04980b4c60daefc9f678815bacc2","46910fa495b1d70e7405ff396065639d":"402ef4cb675883c62faac675f1703779","9dbbd40ed40a68ef28f5d0cc381f3b29":"4a9b88a1746b3d047fe516697c53704e","78b68aba02a2fb99e82b54aea2a53edb":"5186ef6da60a3becedfbd2e18878b7ff","9943102285734cad34b529c8a55f912e":"67eb68cba7f8dc710502053c3f85a920","6391c2ef3b2464d9917ad3b33facaf37":"9fcc7d0630886635e93402dad5b7b022","f85db6dc64983f08852d3e0fca98ca11":"c31db3fd457e42732e50a4288da77925","68d7b54bf2dfc8ae746228c423248e99":"d497d5da52a9fbf62bdad6bd124bd428","b0cfd2b364a3245b90a0c9e4e9134491":"d5a84c319e8b46746f3571181b8b8aef","96e153005af0546883796525e2e4b9f3":"d9331cccec8b8d69a08806bedf12dae7","74074b060e1c690e7ae50754f1dfc247":"e1c88b77b227c89a5536417e292eee7c"}
files={f.split('.')[0]:f for f in os.listdir(assets)}
s=open(src).read()
def rep(m):
    i=NEW2OLD.get(m.group(1),m.group(1))
    if i not in files: sys.exit("missing image "+i)
    return "assets/"+files[i]
s=re.sub(r"/_blob/([0-9a-f]{32})",rep,s)
s=s.replace('<script src="./support.js"></script>','<script src="./vendor/react.js"></script>\n<script src="./vendor/react-dom.js"></script>\n<script src="./support.js"></script>',1)
open(dst,'w').write(s)
