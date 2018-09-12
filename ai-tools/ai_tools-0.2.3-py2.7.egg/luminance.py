import cv2


def splitimage(image,n_row,n_col):
    w=image.shape[0]
    h=image.shape[1]
    ws=w/n_col
    hs=h/n_row
    splits=[]
    for i in range(0,w-ws,ws):
        for j in range(0,h-hs,hs):
            tmp=image[j:j+hs,i:i+ws]
            #print tmp.shape,i,j,ws,hs
            tmp1=tmp.reshape((ws*hs))
            splits.append(tmp1)
            
    return splits 
def weights_sum(vallist,weights):
    #weights=[0.1,0.1.0.1,0.1,0.2,0.1,0.1,0.1,0.1]
    c=[]
    i=0
    v=0.0
    ws=0.0
    for iv in vallist:
        
        c.append(iv*weights[i])
        #print c
        v+=c[-1]
        #ws+=weights[i]
        i+=1
    #v=v/ws
    return v 

def analysys_luminance(image_list):
    c=[]
    weights=[0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.1,0.1]
    i=0
    mean_i=[]
    val_i=[]
    min_i=[]
    max_i=[]
    for image in image_list:
        image=image/255.0
        #print image.mean(),image.var(),min(image),max(image)
        mean_i.append(image.mean())
        val_i.append(image.var())
        min_i.append(min(image))
        max_i.append(max(image)) 
        i+=1
    
   
    mean_lumi=weights_sum(mean_i,[0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.1,0.1])
    hori_lumi=weights_sum(mean_i,[1,1,1,0,0,0,-1,-1,-1])
    vert_lumi=weights_sum(mean_i,[1,0,-1,1,0,-1,1,0,-1])
    slop_lumi=weights_sum(mean_i,[0,-1,-1,1,0,-1,1,1,0,0])
    lumi={}
    lumi['mean']=mean_lumi
    lumi['hori']=hori_lumi
    lumi['vert']=vert_lumi
    lumi['slop']=slop_lumi

    return lumi 

def luminance(image):
    xyz=cv2.cvtColor(image,cv2.COLOR_BGR2XYZ)
    #cv2.cvtColor(image,xyz,cv2.COLOR_BGR2GRAY)
    channels=cv2.split(xyz)
    Y=channels[1]
    sp=splitimage(Y,3,3)
    #print len(sp)
    luminance=analysys_luminance(sp)
    print luminance 
    return luminance

if __name__=="__main__":
    image=cv2.imread("roc.jpg")
    luminance(image)
