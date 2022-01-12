i=0
while(True):
    id='llistadades_'+ str(i) + '_3'
    try:
        element = driver.find_element_by_id(str(id))
        i= i+1
    except: 
        break
