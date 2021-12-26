from bs4 import BeautifulSoup
siniestro="siniestro_587568195.html"
html = open(siniestro).read()
soup = BeautifulSoup(html)
all_ids=soup.find(id='llistadadesWM_')

list_ids=list(all_ids)
num_list=len(list_ids)